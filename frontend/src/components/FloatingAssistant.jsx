import React, { useState } from "react";

export default function FloatingAssistant() {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <>
      <div
        onClick={() => setIsOpen(!isOpen)}
        style={{
          position: "fixed",
          bottom: 220,
          right: 20,
          width: 60,
          height: 60,
          background: "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
          borderRadius: "50%",
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          color: "white",
          fontSize: "24px",
          cursor: "pointer",
          boxShadow: "0 4px 12px rgba(0,0,0,0.15)",
          zIndex: 999,
          fontWeight: "bold"
        }}
      >
        ⚡
      </div>
      {isOpen && (
        <div
          style={{
            position: "fixed",
            bottom: 290,
            right: 20,
            width: 300,
            background: "white",
            borderRadius: "10px",
            padding: "15px",
            boxShadow: "0 4px 12px rgba(0,0,0,0.15)",
            zIndex: 998
          }}
        >
          <h3 style={{ margin: "0 0 10px 0" }}>AI Assistant</h3>
          <p style={{ fontSize: "14px", margin: "0", color: "#666" }}>
            Stage 1 Floating Assistant - Coming Soon!
          </p>
        </div>
      )}
    </>
  );
}
