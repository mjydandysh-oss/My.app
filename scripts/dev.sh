#!/bin/bash
set -e

# Color definitions
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m'

# Cleanup on exit
cleanup() {
    echo -e "${YELLOW}Stopping services...${NC}"
    kill %1 2>/dev/null || true
    kill %2 2>/dev/null || true
    wait 2>/dev/null || true
    echo -e "${GREEN}Services stopped.${NC}"
}
trap cleanup EXIT

# Get project root
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$PROJECT_ROOT"

# Header
echo -e "${CYAN}"
echo "╔════════════════════════════════════════════════════════╗"
echo "║          Development Server (Backend + Frontend)       ║"
echo "╚════════════════════════════════════════════════════════╝"
echo -e "${NC}"

# Check virtual environment
if [ ! -d "venv" ]; then
    echo -e "${RED}Virtual environment not found. Run: bash scripts/install.sh${NC}"
    exit 1
fi

# Activate venv
source venv/bin/activate

# Check ports
echo -e "${BLUE}Checking port availability...${NC}"
if lsof -Pi :8000 -sTCP:LISTEN -t >/dev/null 2>&1; then
    echo -e "${YELLOW}Port 8000 is already in use${NC}"
fi

if lsof -Pi :3000 -sTCP:LISTEN -t >/dev/null 2>&1; then
    echo -e "${YELLOW}Port 3000 is already in use${NC}"
fi

# Create logs directory
mkdir -p logs

# Start backend
echo -e "${BLUE}Starting Backend (FastAPI)...${NC}"
cd "$PROJECT_ROOT/backend"
uvicorn main:app --reload --host 0.0.0.0 --port 8000 > "$PROJECT_ROOT/logs/backend.log" 2>&1 &
BACKEND_PID=$!
echo -e "${GREEN}✓ Backend PID: $BACKEND_PID${NC}"

# Start frontend
echo -e "${BLUE}Starting Frontend (React + Vite)...${NC}"
cd "$PROJECT_ROOT/frontend"
npm run dev > "$PROJECT_ROOT/logs/frontend.log" 2>&1 &
FRONTEND_PID=$!
echo -e "${GREEN}✓ Frontend PID: $FRONTEND_PID${NC}"

# Wait for services to start
sleep 3

# Check if processes are running
if ! kill -0 $BACKEND_PID 2>/dev/null; then
    echo -e "${RED}Backend failed to start. Check logs: tail logs/backend.log${NC}"
    exit 1
fi

if ! kill -0 $FRONTEND_PID 2>/dev/null; then
    echo -e "${RED}Frontend failed to start. Check logs: tail logs/frontend.log${NC}"
    exit 1
fi

# Display status
echo -e "${CYAN}"
echo "╔════════════════════════════════════════════════════════╗"
echo "║                 Services Running                       ║"
echo "╠════════════════════════════════════════════════════════╣"
echo "║ Backend:  ${BLUE}http://localhost:8000${NC}${CYAN}              │"
echo "║ API Docs: ${BLUE}http://localhost:8000/docs${NC}${CYAN}         │"
echo "║ Frontend: ${BLUE}http://localhost:3000${NC}${CYAN}              │"
echo "╠════════════════════════════════════════════════════════╣"
echo "║ Logs: ${YELLOW}logs/backend.log${NC}${CYAN} and ${YELLOW}logs/frontend.log${NC}${CYAN}   │"
echo "║ Stop: ${YELLOW}Ctrl+C${NC}${CYAN}                                       │"
echo "╚════════════════════════════════════════════════════════╝"
echo -e "${NC}"

# Keep running
wait $BACKEND_PID $FRONTEND_PID
