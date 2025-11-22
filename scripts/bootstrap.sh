#!/bin/bash

# My.app Bootstrap Script
# Stage 1: Initialize dependencies and environment

echo "🚀 My.app Bootstrap - Stage 1"
echo "================================"

# Backend setup
echo ""
echo "📦 Setting up Backend..."
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
echo "✓ Backend dependencies installed"

# Frontend setup
echo ""
echo "📦 Setting up Frontend..."
cd frontend || exit
npm install
echo "✓ Frontend dependencies installed"
cd ..

echo ""
echo "✅ Stage 1 Bootstrap Complete!"
echo ""
echo "To start development:"
echo "  Backend:  source venv/bin/activate && python backend/main.py"
echo "  Frontend: cd frontend && npm run dev"
echo ""
