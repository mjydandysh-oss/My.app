import React, { createContext, useContext, useReducer, useCallback } from 'react';

const AppContext = createContext();

const initialState = {
  notifications: [],
  selectedAgent: null,
  chatHistory: [],
  isLoading: false,
  user: null,
  agents: [
    {
      id: 'aelira',
      name: 'Aelira',
      title: 'Wisdom Guardian',
      color: '#667eea',
      emoji: '🔮',
      personality: 'Strategic, patient, insightful',
      traits: ['strategic', 'patient', 'insightful'],
    },
    {
      id: 'zyra',
      name: 'Zyra',
      title: 'Creative Catalyst',
      color: '#764ba2',
      emoji: '✨',
      personality: 'Innovative, bold, creative',
      traits: ['innovative', 'bold', 'creative'],
    },
    {
      id: 'xyron',
      name: 'Xyron',
      title: 'Logic Architect',
      color: '#f093fb',
      emoji: '⚙️',
      personality: 'Analytical, precise, logical',
      traits: ['analytical', 'precise', 'logical'],
    },
    {
      id: 'orryn',
      name: 'Orryn',
      title: 'Harmony Keeper',
      color: '#4facfe',
      emoji: '🌟',
      personality: 'Balanced, empathetic, harmonious',
      traits: ['balanced', 'empathetic', 'harmonious'],
    },
  ],
};

const appReducer = (state, action) => {
  switch (action.type) {
    case 'ADD_NOTIFICATION':
      return {
        ...state,
        notifications: [
          ...state.notifications,
          {
            id: Date.now(),
            ...action.payload,
          },
        ],
      };

    case 'REMOVE_NOTIFICATION':
      return {
        ...state,
        notifications: state.notifications.filter((n) => n.id !== action.payload),
      };

    case 'SET_SELECTED_AGENT':
      return {
        ...state,
        selectedAgent: action.payload,
      };

    case 'ADD_CHAT_MESSAGE':
      return {
        ...state,
        chatHistory: [
          ...state.chatHistory,
          {
            id: Date.now(),
            ...action.payload,
          },
        ],
      };

    case 'CLEAR_CHAT':
      return {
        ...state,
        chatHistory: [],
      };

    case 'SET_LOADING':
      return {
        ...state,
        isLoading: action.payload,
      };

    case 'SET_USER':
      return {
        ...state,
        user: action.payload,
      };

    default:
      return state;
  }
};

export const AppProvider = ({ children }) => {
  const [state, dispatch] = useReducer(appReducer, initialState);

  const addNotification = useCallback((notification) => {
    dispatch({
      type: 'ADD_NOTIFICATION',
      payload: notification,
    });

    // Auto-dismiss after 4 seconds
    if (notification.duration !== 'persistent') {
      setTimeout(() => {
        removeNotification(notification.id || Date.now());
      }, notification.duration || 4000);
    }
  }, []);

  const removeNotification = useCallback((id) => {
    dispatch({
      type: 'REMOVE_NOTIFICATION',
      payload: id,
    });
  }, []);

  const selectAgent = useCallback((agentId) => {
    const agent = state.agents.find((a) => a.id === agentId);
    dispatch({
      type: 'SET_SELECTED_AGENT',
      payload: agent,
    });
  }, [state.agents]);

  const addMessage = useCallback((message) => {
    dispatch({
      type: 'ADD_CHAT_MESSAGE',
      payload: message,
    });
  }, []);

  const clearChat = useCallback(() => {
    dispatch({
      type: 'CLEAR_CHAT',
    });
  }, []);

  const setLoading = useCallback((loading) => {
    dispatch({
      type: 'SET_LOADING',
      payload: loading,
    });
  }, []);

  const setUser = useCallback((user) => {
    dispatch({
      type: 'SET_USER',
      payload: user,
    });
  }, []);

  const value = {
    ...state,
    addNotification,
    removeNotification,
    selectAgent,
    addMessage,
    clearChat,
    setLoading,
    setUser,
  };

  return <AppContext.Provider value={value}>{children}</AppContext.Provider>;
};

export const useAppContext = () => {
  const context = useContext(AppContext);
  if (!context) {
    throw new Error('useAppContext must be used within AppProvider');
  }
  return context;
};
