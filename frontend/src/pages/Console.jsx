import React from "react";

export default function Console() {
  return (
    <div style={{ padding: "20px" }}>
      <h2>Console</h2>
      <div style={{
        background: "#000",
        color: "#0f0",
        padding: "10px",
        fontFamily: "monospace",
        borderRadius: "5px",
        height: "400px",
        overflowY: "auto"
      }}>
        <p>[CONSOLE] Application started</p>
        <p>[AGENTS] Aelira, Zyra, Xyron, Orryn registered</p>
        <p>[STATUS] Ready for input</p>
      </div>
    </div>
  );
}
