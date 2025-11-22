import React, { useState } from "react";

export default function ChatPanel() {
  const [messages, setMessages] = useState([
    { text: "Hello! I'm Aelira", sender: "character", character: "Aelira" }
  ]);
  const [input, setInput] = useState("");

  const handleSend = () => {
    if (input.trim()) {
      setMessages([...messages, { text: input, sender: "user" }]);
      setInput("");
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
      flexDirection: "column"
    }}>
      <div style={{ flex: 1, overflowY: "auto", padding: "10px" }}>
        {messages.map((msg, i) => (
          <div key={i} style={{ marginBottom: "5px" }}>
            <strong>{msg.character || msg.sender}:</strong> {msg.text}
          </div>
        ))}
      </div>
      <div style={{ display: "flex", gap: "5px", padding: "10px" }}>
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyPress={(e) => e.key === "Enter" && handleSend()}
          placeholder="Type message..."
          style={{ flex: 1, padding: "8px", borderRadius: "4px", border: "1px solid #ddd" }}
        />
        <button
          onClick={handleSend}
          style={{
            padding: "8px 15px",
            background: "#007bff",
            color: "white",
            border: "none",
            borderRadius: "4px",
            cursor: "pointer"
          }}
        >
          Send
        </button>
      </div>
    </div>
  );
}
