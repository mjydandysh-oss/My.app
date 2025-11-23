# Docker Image Build Guide

## Agent Docker Image

The `myapp-agent` Docker image has been successfully built and is available in this environment.

### Image Details

- **Image Name:** `myapp-agent`
- **Tag:** `0.1.0`
- **Base Image:** `python:3.12-slim`
- **Size:** ~5.14 GB (uncompressed)
- **Status:** ✅ Built and ready to use

### Building Locally

To build the Docker image on your machine:

```bash
# Clone the repository
git clone https://github.com/mjydandysh-oss/My.app.git
cd My.app

# Build the image
docker build -f Dockerfile.agent -t myapp-agent:0.1.0 .
```

### Running the Agent

#### Using Docker

```bash
# Create an API key (run once)
docker run --rm myapp-agent:0.1.0 myapp-agent create-key

# Start the agent server
docker run -p 9000:9000 \
  -e MYAPP_AGENT_KEYS="<your-api-key>" \
  myapp-agent:0.1.0 myapp-agent serve

# Test the agent
curl -X POST http://localhost:9000/v1/chat \
  -H "X-API-KEY: <your-api-key>" \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello, agent!"}'
```

#### Using Python Package

Alternatively, install and run via pip:

```bash
# Install the wheel from releases
pip install releases/myapp_agent-0.1.0-py3-none-any.whl

# Create an API key
myapp-agent create-key

# Run the server
MYAPP_AGENT_KEYS="<your-api-key>" myapp-agent serve
```

### Exporting the Image

To export the Docker image as a tar file for distribution:

```bash
docker save myapp-agent:0.1.0 -o myapp-agent-image.tar.gz
# Note: The uncompressed tar can be ~5GB; consider compressing with gzip
docker save myapp-agent:0.1.0 | gzip > myapp-agent-image.tar.gz
```

### Loading the Image

To load a saved Docker image:

```bash
docker load -i myapp-agent-image.tar.gz
# or uncompressed
docker load -i myapp-agent-image.tar
```

### API Endpoints

The agent server exposes the following endpoints:

- **POST `/v1/health`** — Health check
  - Response: `{"status": "ok"}`

- **POST `/v1/chat`** — Send a chat message
  - Request: `{"message": "your message"}`
  - Response: `{"response": "agent response"}`

- **POST `/v1/execute`** — Execute a whitelisted command
  - Request: `{"command": "command name", "args": ["arg1", "arg2"]}`
  - Response: `{"output": "command output"}`

### Environment Variables

- `MYAPP_AGENT_KEYS` — Comma-separated list of valid API keys (required for server)
- `MYAPP_AGENT_PORT` — Server port (default: 9000)

### Authentication

All requests must include the `X-API-KEY` header with a valid API key.

Example:
```bash
curl -H "X-API-KEY: your-secret-key" http://localhost:9000/v1/health
```

### Logs

Logs are written to `/app/logs/agent.log` inside the container and to the console.

To view logs:
```bash
docker logs <container-id>
```

## Production Recommendations

1. **Secure API Keys:** Do not hardcode API keys in Dockerfiles or configuration files. Use secrets management systems (e.g., Docker Secrets, HashiCorp Vault).

2. **Container Security:**
   - Run containers as non-root users
   - Use read-only filesystems where possible
   - Implement network policies to restrict egress traffic

3. **Resource Limits:**
   ```bash
   docker run -m 2g --cpus 2 myapp-agent:0.1.0
   ```

4. **Monitoring:**
   - Ship logs to a centralized logging service (ELK, Splunk, etc.)
   - Monitor CPU, memory, and network usage
   - Set up alerts for errors and anomalies

5. **Registry:**
   - Push to a private container registry (Docker Hub, GHCR, ECR, etc.)
   - Use image signing and verification (Notary, Cosign)

---

**Release Version:** v1.0.0  
**Last Updated:** 2024
