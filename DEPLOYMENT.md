# Deployment Guide

Instructions for running AdversaryIQ locally and deploying to production.

---

## Prerequisites

- **Node.js** 18+
- **Python** 3.10+
- **OpenAI API Key**
- **ElevenLabs API Key** (optional, for voice synthesis)

---

## Local Development

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/adversary-iq.git
cd adversary-iq
```

### 2. Backend Setup

```bash
cd backend

# Install dependencies
npm install

# Create environment file
cp .env.example .env

# Edit .env with your API keys
# OPENAI_API_KEY=sk-proj-...
# ELEVENLABS_API_KEY=...

# Start server
node server.js
```

Backend runs on `http://localhost:3001`

### 3. Frontend Setup

```bash
cd frontend_gradio

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start frontend with API URL
API_URL=http://localhost:3001 python app.py
```

Frontend runs on `http://localhost:7860`

### 4. Verify Installation

```bash
# Test backend health
curl http://localhost:3001/api/health

# Open frontend in browser
open http://localhost:7860
```

---

## Environment Variables

### Backend (.env)

```env
# Required
OPENAI_API_KEY=sk-proj-your-key-here

# Optional (for voice synthesis)
ELEVENLABS_API_KEY=your-elevenlabs-key

# Server config
PORT=3001
```

### Frontend

```bash
# Pass via command line
API_URL=http://localhost:3001 python app.py

# Or set in environment
export API_URL=http://localhost:3001
python app.py
```

---

## Production Deployment

### Backend: Railway

1. **Create new project** at [railway.app](https://railway.app)
2. **Connect GitHub repo**
3. **Set root directory** to `/backend`
4. **Add environment variables:**
   - `OPENAI_API_KEY`
   - `ELEVENLABS_API_KEY`
   - `PORT=3001`
5. **Deploy**

Railway auto-detects Node.js and runs `npm start`.

### Backend: Render

1. **Create new Web Service** at [render.com](https://render.com)
2. **Connect GitHub repo**
3. **Configure:**
   - Root Directory: `backend`
   - Build Command: `npm install`
   - Start Command: `node server.js`
4. **Add environment variables**
5. **Deploy**

### Frontend: HuggingFace Spaces

1. **Create new Space** at [huggingface.co/spaces](https://huggingface.co/spaces)
2. **Select Gradio SDK**
3. **Upload files:**
   - `app.py`
   - `requirements.txt`
   - `README.md` (with HF metadata)
4. **Add secrets:**
   - `API_URL` = your deployed backend URL
5. **Space auto-builds**

### README.md Header (Required for HF Spaces)

```yaml
---
title: AdversaryIQ
emoji: 🎯
colorFrom: amber
colorTo: cyan
sdk: gradio
sdk_version: 4.0.0
app_file: app.py
pinned: false
license: mit
---
```

---

## Docker Deployment

### Backend Dockerfile

```dockerfile
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY . .
EXPOSE 3001
CMD ["node", "server.js"]
```

### Build and Run

```bash
# Build
docker build -t adversary-iq-backend ./backend

# Run
docker run -p 3001:3001 \
  -e OPENAI_API_KEY=sk-... \
  -e ELEVENLABS_API_KEY=... \
  adversary-iq-backend
```

---

## API Testing

### Health Check

```bash
curl http://localhost:3001/api/health
# {"status":"healthy","timestamp":"2026-01-07T..."}
```

### Crisis Analysis

```bash
curl -X POST http://localhost:3001/api/process-crisis \
  -H "Content-Type: application/json" \
  -d '{"crisis": "China announces military exercises around Taiwan"}'
```

### Document Analysis

```bash
curl -X POST http://localhost:3001/api/analyze-document \
  -H "Content-Type: application/json" \
  -d '{"documentText": "We remain committed to dialogue...", "filename": "statement.txt"}'
```

---

## Troubleshooting

### Backend won't start

```bash
# Check if port is in use
lsof -i :3001

# Kill existing process
pkill -f "node server.js"

# Verify .env exists
cat backend/.env
```

### Frontend can't connect to backend

```bash
# Verify backend is running
curl http://localhost:3001/api/health

# Check API_URL is set
echo $API_URL

# Check for CORS issues in browser console
```

### Gradio CSS warning

```
UserWarning: The parameters have been moved from the Blocks constructor to launch()
```

This is non-breaking. Gradio still works. Optionally move CSS to `launch(css=...)`.

### API rate limits

OpenAI and ElevenLabs have rate limits. For high-traffic deployments:
- Implement request queuing
- Add response caching
- Use rate limit backoff

---

## Monitoring

### Recommended Setup

1. **Logging:** Use PM2 for Node.js process management
   ```bash
   npm install -g pm2
   pm2 start server.js --name adversary-iq
   pm2 logs adversary-iq
   ```

2. **Uptime:** Use UptimeRobot to ping `/api/health`

3. **Error tracking:** Integrate Sentry for production error monitoring

---

## Security Checklist

- [ ] API keys in environment variables, not code
- [ ] `.env` in `.gitignore`
- [ ] CORS configured for production domains only
- [ ] Rate limiting on API endpoints
- [ ] Input sanitization before LLM calls
