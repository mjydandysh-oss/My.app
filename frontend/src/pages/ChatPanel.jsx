import { useState } from "react";
import { useAppContext } from "../context/AppContext";

export default function ChatPanel() {
  const { currentAgent, addNotification } = useAppContext();
  const [messages, setMessages] = useState([
    { text: "Hello! I'm Aelira", sender: "character", character: "Aelira" }
  ]);
  const [input, setInput] = useState("");
  const [isLoading, setIsLoading] = useState(false);

  const handleSend = async () => {
    if (input.trim()) {
      // Add user message
      const userMessage = { text: input, sender: "user", character: "You" };
      setMessages([...messages, userMessage]);
      setInput("");
      setIsLoading(true);

      try {
        // Simulate API call
        await new Promise(resolve => setTimeout(resolve, 500));
        const botMessage = {
          text: `I received: "${input}"`,
          sender: "character",
          character: currentAgent || "Assistant"
        };
        setMessages(prev => [...prev, botMessage]);
      } catch (error) {
        addNotification("Error sending message", "error");
      } finally {
        setIsLoading(false);
      }
    }
  };

  return (
    <div style={{
      position: "fixed",
      bottom: 0,
      width: "100%",
      height: "200px",
      background: "#f5f5f5",
      borderTop: "1px solid #ddd",
      display: "flex",
      flexDirection: "column",
      boxShadow: "0 -2px 8px rgba(0,0,0,0.1)",
      zIndex: 900
    }}>
      <div style={{ 
        padding: "10px 20px", 
        background: "#fff", 
        borderBottom: "1px solid #ddd",
        fontWeight: "bold",
        color: "#333"
      }}>
        Chat with {currentAgent || "Assistant"}
      </div>
      <div style={{ flex: 1, overflowY: "auto", padding: "10px 20px" }}>
        {messages.map((msg, i) => (
          <div 
            key={i} 
            style={{ 
              marginBottom: "8px",
              padding: "8px 12px",
              borderRadius: "4px",
              background: msg.sender === "user" ? "#e3f2fd" : "#f5f5f5",
              textAlign: msg.sender === "user" ? "right" : "left"
            }}
          >
            <strong style={{ color: msg.sender === "user" ? "#1976d2" : "#666" }}>
              {msg.character}:
            </strong> {msg.text}
          </div>
        ))}
        {isLoading && (
          <div style={{ color: "#999", fontSize: "12px" }}>
            {currentAgent} is typing...
          </div>
        )}
      </div>
      <div style={{ display: "flex", gap: "5px", padding: "10px 20px", background: "#fff", borderTop: "1px solid #ddd" }}>
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyPress={(e) => e.key === "Enter" && !isLoading && handleSend()}
          placeholder="Type message..."
          disabled={isLoading}
          style={{ 
            flex: 1, 
            padding: "8px 12px", 
            borderRadius: "4px", 
            border: "1px solid #ddd",
            fontFamily: "inherit"
          }}
        />
        <button
          onClick={handleSend}
          disabled={isLoading}
          style={{
            padding: "8px 15px",
            background: isLoading ? "#ccc" : "#007bff",
            color: "white",
            border: "none",
            borderRadius: "4px",
            cursor: isLoading ? "not-allowed" : "pointer",
            fontWeight: "500"
          }}
        >
          {isLoading ? "..." : "Send"}
        </button>
      </div>
    </div>
  );
}
