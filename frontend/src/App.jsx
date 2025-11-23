import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import { AppProvider } from './context/AppContext';
import Home from './pages/Home';
import Console from './pages/Console';
import Dashboard from './pages/Dashboard';
import Characters from './components/Characters';
import ChatPanel from './pages/ChatPanel';
import FloatingAssistant from './components/FloatingAssistant';
import Notification from './components/Notification';
import AgentSelector from './components/AgentSelector';
import './App.css';

function App() {
  return (
    <AppProvider>
      <Router>
        <div className="app-container">
          <nav style={{
            background: '#333',
            color: 'white',
            padding: '10px 20px',
            display: 'flex',
            gap: '20px'
          }}>
            <Link to="/" style={{ color: 'white', textDecoration: 'none' }}>Home</Link>
            <Link to="/dashboard" style={{ color: 'white', textDecoration: 'none' }}>Dashboard</Link>
            <Link to="/console" style={{ color: 'white', textDecoration: 'none' }}>Console</Link>
            <Link to="/characters" style={{ color: 'white', textDecoration: 'none' }}>Characters</Link>
          </nav>

          <AgentSelector />

          <div style={{ paddingBottom: '220px' }}>
            <Routes>
              <Route path="/" element={<Home />} />
              <Route path="/dashboard" element={<Dashboard />} />
              <Route path="/console" element={<Console />} />
              <Route path="/characters" element={<Characters />} />
            </Routes>
          </div>

          <Notification />
          <FloatingAssistant />
          <ChatPanel />
        </div>
      </Router>
    </AppProvider>
  );
}

export default App;
