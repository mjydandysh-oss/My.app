import React from "react";

export default function Dashboard() {
  return (
    <div style={{ padding: "20px" }}>
      <h2>Dashboard</h2>
      <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "20px" }}>
        <div style={{ border: "1px solid #ddd", padding: "15px", borderRadius: "5px" }}>
          <h3>Agent Status</h3>
          <p>✓ Aelira: idle</p>
          <p>✓ Zyra: idle</p>
          <p>✓ Xyron: idle</p>
          <p>✓ Orryn: idle</p>
        </div>
        <div style={{ border: "1px solid #ddd", padding: "15px", borderRadius: "5px" }}>
          <h3>System Status</h3>
          <p>Controllers: 1</p>
          <p>Agents: 4</p>
          <p>Upgrade Requests: 0</p>
          <p>Status: Active</p>
        </div>
      </div>
    </div>
  );
}
