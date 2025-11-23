import React from 'react';
import { useAppContext } from '../context/AppContext';
import './AgentSelector.css';

export const AgentSelector = () => {
  const { agents, selectedAgent, selectAgent } = useAppContext();

  return (
    <div className="agent-selector">
      <h3>Select Agent</h3>
      <div className="agent-buttons">
        {agents.map((agent) => (
          <button
            key={agent.id}
            className={`agent-button ${selectedAgent?.id === agent.id ? 'active' : ''}`}
            onClick={() => selectAgent(agent.id)}
            style={{
              borderColor: agent.color,
              backgroundColor: selectedAgent?.id === agent.id ? agent.color : 'transparent',
              color: selectedAgent?.id === agent.id ? 'white' : agent.color,
            }}
            title={agent.personality}
          >
            <span className="agent-emoji">{agent.emoji}</span>
            <span className="agent-name">{agent.name}</span>
          </button>
        ))}
      </div>
      {selectedAgent && (
        <div className="agent-info">
          <h4>{selectedAgent.name}</h4>
          <p className="agent-title">{selectedAgent.title}</p>
          <p className="agent-personality">{selectedAgent.personality}</p>
          <div className="agent-traits">
            {selectedAgent.traits.map((trait) => (
              <span key={trait} className="trait-badge">
                {trait}
              </span>
            ))}
          </div>
        </div>
      )}
    </div>
  );
};

export default AgentSelector;
