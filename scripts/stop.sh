#!/bin/bash

# Color definitions
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m'

echo -e "${CYAN}Stopping development services...${NC}"

# Kill processes on ports 8000 and 3000
lsof -ti:8000 | xargs kill -9 2>/dev/null || true
lsof -ti:3000 | xargs kill -9 2>/dev/null || true

# Alternative method using pkill
pkill -f "uvicorn" 2>/dev/null || true
pkill -f "vite" 2>/dev/null || true

echo -e "${GREEN}✓ Services stopped${NC}"
