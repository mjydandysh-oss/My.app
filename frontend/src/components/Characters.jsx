import React from "react";

export default function Characters() {
  const characters = [
    {
      name: "Aelira",
      role: "Wisdom Guardian",
      description: "Primary agent for strategic decisions",
      color: "#667eea"
    },
    {
      name: "Zyra",
      role: "Creative Catalyst",
      description: "Drives innovation and new approaches",
      color: "#764ba2"
    },
    {
      name: "Xyron",
      role: "Logic Architect",
      description: "Ensures systematic problem solving",
      color: "#f093fb"
    },
    {
      name: "Orryn",
      role: "Harmony Keeper",
      description: "Balances all perspectives",
      color: "#4facfe"
    }
  ];

  return (
    <div style={{ padding: "20px" }}>
      <h2>Characters</h2>
      <div style={{
        display: "grid",
        gridTemplateColumns: "repeat(auto-fit, minmax(250px, 1fr))",
        gap: "20px"
      }}>
        {characters.map((char) => (
          <div
            key={char.name}
            style={{
              border: `2px solid ${char.color}`,
              padding: "15px",
              borderRadius: "8px",
              background: "#f9f9f9",
              cursor: "pointer",
              transition: "transform 0.2s",
              ":hover": { transform: "translateY(-5px)" }
            }}
            onMouseEnter={(e) => e.currentTarget.style.transform = "translateY(-5px)"}
            onMouseLeave={(e) => e.currentTarget.style.transform = "translateY(0)"}
          >
            <div
              style={{
                width: "50px",
                height: "50px",
                background: char.color,
                borderRadius: "50%",
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
                color: "white",
                fontSize: "24px",
                fontWeight: "bold",
                marginBottom: "10px"
              }}
            >
              {char.name[0]}
            </div>
            <h3 style={{ margin: "10px 0 5px 0" }}>{char.name}</h3>
            <p style={{ margin: "0 0 10px 0", color: "#666", fontSize: "12px" }}>
              {char.role}
            </p>
            <p style={{ margin: "0", fontSize: "13px", color: "#888" }}>
              {char.description}
            </p>
          </div>
        ))}
      </div>
    </div>
  );
}
