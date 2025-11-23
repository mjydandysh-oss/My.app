import { useState, useCallback } from 'react';

export const useAdvancedState = (initialState) => {
  const [state, setState] = useState(initialState);

  const updateState = useCallback((updates) => {
    setState((prev) => ({
      ...prev,
      ...updates,
    }));
  }, []);

  const resetState = useCallback(() => {
    setState(initialState);
  }, [initialState]);

  const getState = useCallback(() => state, [state]);

  return {
    state,
    setState,
    updateState,
    resetState,
    getState,
  };
};
