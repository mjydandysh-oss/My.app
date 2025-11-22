/**
 * API Service - Frontend API calls to backend
 * Stage 1: Skeleton with placeholder endpoints
 */

const API_BASE = import.meta.env.VITE_API_URL || "http://localhost:8000";

class APIService {
  /**
   * Generic fetch wrapper
   */
  async fetch(endpoint, options = {}) {
    const url = `${API_BASE}${endpoint}`;
    try {
      const response = await fetch(url, {
        headers: {
          "Content-Type": "application/json",
          ...options.headers,
        },
        ...options,
      });
      if (!response.ok) {
        throw new Error(`HTTP ${response.status}`);
      }
      return await response.json();
    } catch (error) {
      console.error(`API Error: ${endpoint}`, error);
      throw error;
    }
  }

  // Console endpoints
  getConsoleStatus() {
    return this.fetch("/console/status");
  }

  getConsoleLogs(limit = 50) {
    return this.fetch(`/console/logs?limit=${limit}`);
  }

  // Chat endpoints
  sendChatMessage(text, character = "aelira") {
    return this.fetch("/chat/send", {
      method: "POST",
      body: JSON.stringify({ text, character }),
    });
  }

  getChatHistory(limit = 50) {
    return this.fetch(`/chat/history?limit=${limit}`);
  }

  // Agent endpoints
  listAgents() {
    return this.fetch("/agents/list");
  }

  getAgentStatus() {
    return this.fetch("/agents/status");
  }

  runAgents(prompt, context = {}, targetAgents = null) {
    return this.fetch("/agents/run", {
      method: "POST",
      body: JSON.stringify({
        prompt,
        context,
        target_agents: targetAgents,
      }),
    });
  }

  submitUpgradeRequest(user, proposal) {
    return this.fetch("/agents/upgrade-request", {
      method: "POST",
      body: JSON.stringify({ user, proposal }),
    });
  }

  getUpgradeRequests() {
    return this.fetch("/agents/upgrade-requests");
  }

  // Health checks
  healthCheck() {
    return this.fetch("/health");
  }

  getConfig() {
    return this.fetch("/config");
  }
}

export default new APIService();
