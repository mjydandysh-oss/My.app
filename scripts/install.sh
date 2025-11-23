#!/bin/bash
set -e

# Color definitions
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
MAGENTA='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Header
echo -e "${CYAN}"
echo "╔════════════════════════════════════════════════════════╗"
echo "║                  My.app Installation                   ║"
echo "║          The Intelligent Mother System v1.0            ║"
echo "╚════════════════════════════════════════════════════════╝"
echo -e "${NC}"

# Get project root
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$PROJECT_ROOT"

# Step 1: Python version check
echo -e "${BLUE}[1/7] Checking Python installation...${NC}"
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}✗ Python 3 not found. Please install Python 3.11+${NC}"
    exit 1
fi

PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
echo -e "${GREEN}✓ Python $PYTHON_VERSION found${NC}"

# Step 2: Virtual environment setup
echo -e "${BLUE}[2/7] Setting up Python virtual environment...${NC}"
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo -e "${GREEN}✓ Virtual environment created${NC}"
else
    echo -e "${YELLOW}! Virtual environment already exists${NC}"
fi

# Activate venv
source venv/bin/activate
echo -e "${GREEN}✓ Virtual environment activated${NC}"

# Step 3: Backend dependencies
echo -e "${BLUE}[3/7] Installing backend dependencies...${NC}"
pip install --upgrade pip setuptools wheel &> /dev/null
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt &> /dev/null
    echo -e "${GREEN}✓ Backend dependencies installed${NC}"
else
    echo -e "${RED}✗ requirements.txt not found${NC}"
    exit 1
fi

# Step 4: Node.js check
echo -e "${BLUE}[4/7] Checking Node.js installation...${NC}"
if ! command -v node &> /dev/null; then
    echo -e "${RED}✗ Node.js not found. Please install Node.js 18+${NC}"
    exit 1
fi

NODE_VERSION=$(node -v)
echo -e "${GREEN}✓ Node.js $NODE_VERSION found${NC}"

# Step 5: Frontend dependencies
echo -e "${BLUE}[5/7] Installing frontend dependencies...${NC}"
cd "$PROJECT_ROOT/frontend"
if [ ! -d "node_modules" ]; then
    npm install &> /dev/null
    echo -e "${GREEN}✓ Frontend dependencies installed${NC}"
else
    echo -e "${YELLOW}! node_modules already exists${NC}"
fi

# Step 6: Environment configuration
echo -e "${BLUE}[6/7] Setting up environment configuration...${NC}"
cd "$PROJECT_ROOT"
if [ ! -f ".env" ] && [ -f ".env.example" ]; then
    cp .env.example .env
    echo -e "${GREEN}✓ .env file created from .env.example${NC}"
elif [ -f ".env" ]; then
    echo -e "${YELLOW}! .env file already exists${NC}"
fi

# Step 7: Script permissions
echo -e "${BLUE}[7/7] Setting up scripts...${NC}"
chmod +x scripts/*.sh
echo -e "${GREEN}✓ Scripts are executable${NC}"

# Final summary
echo -e "${MAGENTA}"
echo "╔════════════════════════════════════════════════════════╗"
echo "║                Installation Complete!                  ║"
echo "╚════════════════════════════════════════════════════════╝"
echo -e "${NC}"

echo -e "${CYAN}Next steps:${NC}"
echo -e "1. Start development servers: ${YELLOW}bash scripts/dev.sh${NC}"
echo -e "2. Backend API docs: ${YELLOW}http://localhost:8000/docs${NC}"
echo -e "3. Frontend: ${YELLOW}http://localhost:3000${NC}"
echo ""
echo -e "${CYAN}Configuration:${NC}"
echo -e "- Backend config: ${YELLOW}backend/config/settings.py${NC}"
echo -e "- Environment vars: ${YELLOW}.env${NC}"
echo -e "- Frontend config: ${YELLOW}frontend/vite.config.js${NC}"
echo ""
