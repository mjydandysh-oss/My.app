# 🚀 My.app - The Intelligent Mother System

**Production-Ready Full-Stack Application | Complete Stages 1-10**

A professional, enterprise-grade intelligent agent orchestration system with a modern React frontend, FastAPI backend, Docker support, and automated one-click deployment.

---

## 🎯 Quick Start

### One-Command Installation & Startup

```bash
# Install dependencies (Python + Node, backend + frontend)
bash scripts/install.sh

# Start development servers (backend + frontend simultaneously)
bash scripts/dev.sh

# Stop services
bash scripts/stop.sh
```

Then open:
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs

---

## 📋 Features

- ✅ **4 Intelligent Agents** with unique personalities and memory systems
- ✅ **Real-time Chat Interface** with WebSocket support
- ✅ **Multiple LLM Providers** (OpenAI, HuggingFace, LLaMA, Demo)
- ✅ **Advanced State Management** with React Context + Reducer
- ✅ **Docker & Docker Compose** for easy deployment
- ✅ **Professional Installation Wizard** with validation
- ✅ **Comprehensive Logging** and error handling
- ✅ **Testing Framework** (pytest) with async support
- ✅ **CI/CD Pipeline** (GitHub Actions ready)
- ✅ **Production-Ready Architecture** with best practices

---

## 🏗️ Project Structure

```
My.app/
├── backend/                      # FastAPI Application
│   ├── main.py                  # Application entry point
│   ├── api/                     # API routes
│   │   ├── endpoints/           # Endpoint modules
│   │   │   ├── console.py       # Console status & logs
│   │   │   ├── chat.py          # Chat messaging
│   │   │   └── agents.py        # Agent management
│   │   └── router.py            # Route aggregation
│   ├── agents/                  # Agent orchestration
│   │   ├── parent_controller.py # Main orchestrator
│   │   └── advanced_agent.py    # Agent implementation
│   ├── tools/                   # Utilities
│   │   ├── llm_provider.py      # LLM abstraction
│   │   └── notifier.py          # WebSocket notifications
│   ├── models/                  # Pydantic data models
│   ├── config/                  # Configuration
│   └── utils/                   # Logging, exceptions, database
│
├── frontend/                    # React + Vite Application
│   ├── src/
│   │   ├── App.jsx             # Main app component
│   │   ├── pages/              # Page components
│   │   ├── components/         # UI components
│   │   ├── context/            # React Context
│   │   ├── hooks/              # Custom hooks
│   │   └── services/           # API client
│   ├── vite.config.js
│   └── package.json
│
├── scripts/                     # Utility scripts
│   ├── install.sh              # Installation wizard
│   ├── dev.sh                  # Development server
│   └── stop.sh                 # Service stopper
│
├── docker-compose.yml          # Full stack orchestration
├── Dockerfile.backend          # Backend container
├── Dockerfile.frontend         # Frontend container
├── requirements.txt            # Python dependencies
└── .env.example               # Environment template
```

---

## 🤖 Agent Personalities

| Agent | Title | Emoji | Color | Traits |
|-------|-------|-------|-------|--------|
| **Aelira** | Wisdom Guardian | 🔮 | #667eea | Strategic, Patient, Insightful |
| **Zyra** | Creative Catalyst | ✨ | #764ba2 | Innovative, Bold, Creative |
| **Xyron** | Logic Architect | ⚙️ | #f093fb | Analytical, Precise, Logical |
| **Orryn** | Harmony Keeper | 🌟 | #4facfe | Balanced, Empathetic, Harmonious |

---

## 🔧 Backend Configuration

### Settings (`backend/config/settings.py`)

```python
ENVIRONMENT = "development"  # development, staging, production
LOG_LEVEL = "info"
DATABASE_URL = "sqlite:///./app.db"
LLM_PROVIDER = "demo"  # demo, openai, huggingface, llama
```

### LLM Provider Setup

```bash
# For OpenAI
export OPENAI_API_KEY="your-key"

# For HuggingFace
export HUGGINGFACE_API_KEY="your-key"

# For LLaMA (local)
# Ensure ollama service is running on localhost:11434
```

---

## 🎨 Frontend Configuration

### Vite Config (`frontend/vite.config.js`)

The frontend is configured to:
- Bind to `0.0.0.0:3000` (accessible from host)
- Hot reload on file changes
- Proxy API requests to backend (dev mode)

### Environment Variables

Create `frontend/.env` if needed:

```env
VITE_API_URL=http://localhost:8000
VITE_APP_NAME=My.app
```

---

## 📊 API Endpoints

### Console
- `GET /api/console/status` - System status
- `GET /api/console/logs` - System logs
- `WebSocket /ws/console` - Real-time logs

### Chat
- `POST /api/chat/send` - Send message
- `GET /api/chat/history/{conversation_id}` - Get history
- `DELETE /api/chat/history/{conversation_id}` - Clear history

### Agents
- `GET /api/agents/list` - List all agents
- `GET /api/agents/{agent_id}/status` - Agent status
- `POST /api/agents/{agent_id}/execute` - Execute agent
- `POST /api/agents/request-upgrade` - Request capability upgrade

---

## 🐳 Docker Deployment

### Quick Start with Docker

```bash
# Build and start services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

### Build Images Separately

```bash
# Backend
docker build -f Dockerfile.backend -t myapp-backend .
docker run -p 8000:8000 myapp-backend

# Frontend
docker build -f Dockerfile.frontend -t myapp-frontend .
docker run -p 3000:3000 myapp-frontend
```

---

## 🧪 Testing

### Run All Tests

```bash
bash scripts/install.sh  # Ensure dependencies installed
source venv/bin/activate
pytest tests/ -v
```

### Run Specific Test

```bash
pytest tests/test_backend.py::TestParentController -v
```

### With Coverage

```bash
pytest tests/ --cov=backend --cov-report=html
```

---

## 📦 Requirements

### System
- **Python**: 3.11+
- **Node.js**: 18+
- **Docker**: 20+ (optional, for containerization)

### Python Packages
See `requirements.txt`:
- FastAPI 0.121.3
- Uvicorn 0.38.0
- Pydantic 2.12.4
- httpx 0.28.1
- pytest-asyncio 1.3.0

### Node Packages
See `frontend/package.json`:
- React 18+
- Vite 5.4+
- React Router 6+
- Socket.IO Client

---

## 🚀 Deployment

### Production Setup

```bash
# 1. Clone repository
git clone <repo-url>
cd My.app

# 2. Run installation
bash scripts/install.sh

# 3. Configure environment
cp .env.example .env
nano .env  # Edit configuration

# 4. Deploy with Docker
docker-compose -f docker-compose.yml up -d

# 5. Access services
# Frontend: http://your-domain:3000
# API: http://your-domain:8000
# Docs: http://your-domain:8000/docs
```

### Environment Variables

```bash
# Backend
ENVIRONMENT=production
LOG_LEVEL=warning
DATABASE_URL=postgresql://user:pass@host/db
LLM_PROVIDER=openai
OPENAI_API_KEY=your-key

# Frontend
VITE_API_URL=https://api.your-domain.com
```

---

## 🔄 Git Workflow

```bash
# Current status
git status

# Make changes
git add -A
git commit -m "Your message"

# Push to remote
git push origin main

# Create PR
gh pr create --title "Feature name" --body "Description"
```

---

## 📝 Development Workflow

### 1. **Backend Changes**
- Edit files in `backend/`
- Backend auto-reloads on changes (via uvicorn --reload)
- Check logs: `tail -f logs/backend.log`

### 2. **Frontend Changes**
- Edit files in `frontend/src/`
- Frontend hot-reloads instantly (via Vite)
- Check logs: `tail -f logs/frontend.log`

### 3. **New Features**
- Backend: Add endpoint in `backend/api/endpoints/`
- Frontend: Add component in `frontend/src/components/`
- Connect via API client in `frontend/src/services/api.js`

---

## 🛠️ Troubleshooting

### Port Already in Use

```bash
# Kill process on port 8000
lsof -ti:8000 | xargs kill -9

# Kill process on port 3000
lsof -ti:3000 | xargs kill -9

# Or use stop script
bash scripts/stop.sh
```

### Installation Issues

```bash
# Verify Python
python3 --version  # Should be 3.11+

# Verify Node
node --version    # Should be 18+

# Re-run installation
bash scripts/install.sh
```

### Backend Import Errors

```bash
# Ensure venv is activated
source venv/bin/activate

# Re-install dependencies
pip install -r requirements.txt
```

### Frontend Module Not Found

```bash
cd frontend
npm install  # Reinstall dependencies
npm run dev  # Restart dev server
```

---

## 📚 Technology Stack

| Layer | Technologies |
|-------|--------------|
| **Frontend** | React 18, Vite 5, React Router 6, Context API |
| **Backend** | FastAPI, Uvicorn, Pydantic, SQLAlchemy |
| **Database** | SQLite (dev), PostgreSQL (prod) |
| **LLM** | OpenAI, HuggingFace, LLaMA, Demo |
| **DevOps** | Docker, Docker Compose, GitHub Actions |
| **Testing** | Pytest, Pytest-Asyncio |
| **Logging** | Python logging, Uvicorn |

---

## 📄 License

MIT License - See LICENSE file

---

## 🤝 Support

For issues, questions, or feature requests:
1. Check existing issues
2. Create new issue with details
3. Join discussions for questions

---

## 🎓 Learning Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [React Documentation](https://react.dev/)
- [Vite Documentation](https://vitejs.dev/)
- [Docker Documentation](https://docs.docker.com/)
- [WebSocket Guide](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API)

---

**Built with ❤️ for intelligent agent orchestration**
