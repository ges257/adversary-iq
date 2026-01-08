# AdversaryIQ System Overview
**Version 1.0 | Last Updated: January 7, 2026 - 5:10 PM EST**
**Platform: WSL Ubuntu 24.04 (migrated from Windows)**

---

## Executive Summary

AdversaryIQ is an AI-powered multi-agent crisis simulation system that models how historical political leaders would respond to modern geopolitical scenarios. The system uses evidence-based psychological profiles to generate realistic, personality-driven responses for intelligence analysis and decision support.

**Origin**: AI+ Expo Hackathon, Washington D.C. (June 2025) - OpenAI Track

---

## System Classification

| Classification | Type |
|----------------|------|
| **Primary** | Multi-Agent Simulation System |
| **AI Type** | Generative AI + Predictive Modeling |
| **Architecture** | REST API Backend |
| **Output Modes** | Text (JSON) + Voice (MP3) |

---

## Core Capabilities

### 1. Crisis Analysis
Simulates how three historical leaders would respond to any geopolitical crisis scenario.

**Input**: Text description of crisis
**Output**:
- Public statements from each leader
- Private/behind-the-scenes actions
- Psychological reasoning
- Escalation risk assessment
- Timeline predictions

### 2. Document Analysis
Interprets diplomatic documents through each leader's psychological framework.

**Input**: Document text
**Output**:
- Hidden intentions detection
- Psychological tactics identification
- Authenticity assessment
- Recommended responses

### 3. Voice Synthesis
Converts agent responses to speech using leader-specific voice models.

**Input**: Text + Agent identifier
**Output**: MP3 audio stream

---

## Simulated Leaders

| Leader | Era | Profile Focus |
|--------|-----|---------------|
| **Theodore Roosevelt** | 1901-1909 | Bold action, "Big Stick" diplomacy, strategic delays |
| **Indira Gandhi** | 1966-1984 | Centralized control, crisis management, decisive action |
| **Vladimir Putin** | 2000-present | Escalation ladder, hybrid tactics, maximalist demands |

Each leader has:
- **Dual-layer OCEAN personality scores** (public vs behavioral)
- **Crisis response parameters** (latency, escalation patterns)
- **Contradiction patterns** (say vs do discrepancies)
- **Contextual switching rules** (when to use which persona)
- **Predictive frameworks** (response templates by situation type)

---

## Technical Stack

| Component | Technology | Version |
|-----------|------------|---------|
| Runtime | Node.js | - |
| Framework | Express.js | 5.1.0 |
| LLM | OpenAI GPT-4o-mini | - |
| TTS | ElevenLabs | eleven_multilingual_v2 |
| Data Format | JSON | - |

### Dependencies
```
@elevenlabs/elevenlabs-js: ^2.1.0
cors: ^2.8.5
dotenv: ^16.5.0
express: ^5.1.0
openai: ^5.1.0
```

---

## API Reference

### Health Check
```
GET /api/health
Response: { status, message, timestamp }
```

### Crisis Analysis
```
POST /api/process-crisis
Body: { "crisis": "scenario description" }
Response: {
  scenario,
  timestamp,
  agents: { roosevelt, gandhi, putin },
  overall_risk: "Low|Medium|High",
  key_insights: []
}
```

### Document Analysis
```
POST /api/analyze-document
Body: { "documentText": "...", "filename": "optional" }
Response: {
  document,
  timestamp,
  agents: { roosevelt, gandhi, putin }
}
```

### Voice Synthesis
```
POST /api/synthesize-voice
Body: { "text": "...", "agent": "roosevelt|gandhi|putin" }
Response: audio/mpeg (binary)
```

---

## Directory Structure

```
AdversaryIQ/
├── backend/              # RUNTIME FILES
│   ├── server.js         # Main application (394 lines)
│   ├── .env              # Environment config
│   ├── package.json      # Dependencies
│   ├── node_modules/     # 113 packages
│   └── data/personalities/
│       ├── roosevelt_final_profile.json
│       ├── roosevelt_beliefs.json
│       ├── indira_final_profile.json
│       ├── indira_beliefs.json
│       ├── putin_final_profile.json
│       └── putin_beliefs.json
│
├── docs/                 # DOCUMENTATION
│   ├── architecture/     # System docs (this file)
│   ├── methodology/      # Profile creation guide
│   └── research/         # Leader binders & validation PDFs
│
├── samples/              # TEST DATA
├── copies/               # BACKUPS (deletable)
├── misc/                 # Setup notes
└── README.md
```

---

## Configuration

### Environment Variables (.env)
```
OPENAI_API_KEY=sk-proj-...
PORT=3001
```

### Voice IDs (Hardcoded)
| Agent | ElevenLabs Voice ID |
|-------|---------------------|
| Roosevelt | zkXpoOeAWrFgfuIRi0yD |
| Gandhi | XB0fDUnXU5powFXDhCwa |
| Putin | pNInz6obpgDQGcFmaJgB |

---

## How It Works

### 1. Profile Loading (Startup)
Six JSON files loaded into memory containing psychological profiles and belief states.

### 2. Request Processing
1. Receive crisis/document via API
2. Dispatch to all three agents in parallel (Promise.all)
3. Each agent:
   - Loads its profile + beliefs
   - Constructs system prompt (~600 tokens)
   - Calls GPT-4o-mini
   - Parses JSON response
4. Aggregate responses
5. Calculate overall risk
6. Generate insights
7. Return assessment

### 3. Parallel Processing
All three agents process simultaneously, reducing latency from 3x to 1x.

---

## Psychological Framework

### OCEAN Model (Big Five)
Each leader has two sets of scores:
- **Public OCEAN**: What they project to the world
- **Behavioral OCEAN**: How they actually act in private

| Trait | Description |
|-------|-------------|
| Openness | Creativity, curiosity, willingness to try new things |
| Conscientiousness | Organization, dependability, discipline |
| Extraversion | Sociability, assertiveness, positive emotions |
| Agreeableness | Cooperation, trust, helpfulness |
| Neuroticism | Emotional instability, anxiety, moodiness |

### Behavioral Parameters
- **Crisis Latency**: How long before they respond (hours)
- **Escalation Ladder**: Sequence of response intensification
- **Scapegoat Probability**: Likelihood of blaming others
- **Follow-through Decay**: Commitment deterioration over time

---

## Risk Assessment Logic

```
IF (High risk count >= 2) → Overall: HIGH
ELSE IF (High >= 1 OR Medium >= 2) → Overall: MEDIUM
ELSE → Overall: LOW
```

---

## Known Limitations

| Issue | Status | Notes |
|-------|--------|-------|
| API keys hardcoded in server.js | Active | Should use .env exclusively |
| No authentication | Active | API is open to any caller |
| CORS fully open | Active | Allows all origins |
| No rate limiting | Active | Could be abused |
| File-based storage | Active | Not scalable for production |

---

## Running the System

### Prerequisites
- Node.js installed
- Valid OpenAI API key
- Valid ElevenLabs API key

### Commands
```bash
# Navigate to backend
cd /home/schwartzlabs.ai/02_projects/AdversaryIQ/backend

# Install dependencies
npm install

# Start server
node server.js

# Expected output:
# 🧠 AdversaryIQ Intelligence Engine running on port 3001
# 🎯 Ready for crisis analysis
# 🔊 Voice synthesis enabled with authentic Roosevelt voice
```

### Testing
```bash
# Health check
curl http://localhost:3001/api/health

# Crisis analysis
curl -X POST http://localhost:3001/api/process-crisis \
  -H "Content-Type: application/json" \
  -d '{"crisis": "Russia cuts gas supplies to Europe during winter"}'
```

---

## Sample Crisis Scenarios

From setup notes:
- "Russia threatens to cut energy exports to all of Europe"
- "China launches surprise attack on Taiwan"
- "US bans all semiconductor exports to China"

---

## File Metrics

| Metric | Value |
|--------|-------|
| Main server code | 394 lines |
| API endpoints | 4 |
| Personality profiles | 6 files |
| NPM packages | 113 |
| Total personality data | ~10.5 KB |

---

## Migration Notes (Windows → WSL)

**Original Location**: `D:\Adv_IQ` (Windows)
**Current Location**: `/home/schwartzlabs.ai/02_projects/AdversaryIQ` (WSL Ubuntu 24.04)

**Changes Made**:
1. Reorganized directory structure
2. Renamed `adversary-iq-backend` to `backend`
3. Moved duplicates to `copies/` directory
4. Organized documentation into `docs/`
5. Created `samples/` for test data

**Pending**:
- May need to run `npm install` to rebuild node_modules for Linux
- Update any Windows-specific paths in code (none found)

---

## Document History

| Date | Version | Changes |
|------|---------|---------|
| 2026-01-07 | 1.0 | Initial post-migration documentation |

---

*Generated: January 7, 2026 - 5:10 PM EST*
*System Path: /home/schwartzlabs.ai/02_projects/AdversaryIQ/*
*WSL Path: \\wsl.localhost\Ubuntu-24.04\home\schwartzlabs.ai\02_projects\AdversaryIQ*
