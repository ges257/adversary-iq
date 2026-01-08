# AdversaryIQ System Visualization
**Last Updated: January 7, 2026 - 5:10 PM EST**

---

## High-Level System Architecture

```
                                    ADVERSARYIQ SYSTEM
    ============================================================================

                              +---------------------------+
                              |      CLIENT REQUEST       |
                              |  (Crisis / Document / TTS)|
                              +-------------+-------------+
                                            |
                                            v
    +===========================================================================+
    |                     EXPRESS.JS API SERVER (Port 3001)                      |
    |                                                                            |
    |   +--------------------------------------------------------------------+  |
    |   |                        REQUEST ROUTING                              |  |
    |   +--------------------------------------------------------------------+  |
    |        |                      |                         |                  |
    |        v                      v                         v                  |
    |   +---------+          +------------+           +-------------+            |
    |   | /health |          | /process-  |           | /analyze-   |            |
    |   |         |          |   crisis   |           |  document   |            |
    |   +---------+          +-----+------+           +------+------+            |
    |                              |                         |                   |
    |                              v                         v                   |
    |                    +------------------+      +------------------+           |
    |                    |  PARALLEL AGENT  |      |  PARALLEL AGENT  |          |
    |                    |   PROCESSING     |      |   PROCESSING     |          |
    |                    +------------------+      +------------------+           |
    |                              |                         |                   |
    +===========================================================================+
                                   |                         |
            +----------------------+-------------------------+
            |                      |                         |
            v                      v                         v
    +---------------+      +---------------+         +---------------+
    |   ROOSEVELT   |      |    GANDHI     |         |     PUTIN     |
    |    AGENT      |      |    AGENT      |         |    AGENT      |
    +-------+-------+      +-------+-------+         +-------+-------+
            |                      |                         |
            +----------------------+-------------------------+
                                   |
                                   v
                    +-----------------------------+
                    |      EXTERNAL SERVICES      |
                    +-----------------------------+
                    |  OpenAI GPT-4o-mini (LLM)   |
                    |  ElevenLabs (Voice TTS)     |
                    +-----------------------------+
```

---

## Directory Structure (Post-Reorganization)

```
AdversaryIQ/
|
+-- backend/                          [RUNTIME - Required to run system]
|   |-- .env                          Environment variables (PORT, API keys)
|   |-- server.js                     Main Express application (394 lines)
|   |-- package.json                  Dependencies declaration
|   |-- package-lock.json             Locked dependency versions
|   |-- node_modules/                 113 npm packages installed
|   +-- data/
|       +-- personalities/
|           |-- roosevelt_final_profile.json    (3.0 KB)
|           |-- roosevelt_beliefs.json          (265 bytes)
|           |-- indira_final_profile.json       (4.0 KB)
|           |-- indira_beliefs.json             (263 bytes)
|           |-- putin_final_profile.json        (2.9 KB)
|           +-- putin_beliefs.json              (260 bytes)
|
+-- docs/                             [DOCUMENTATION]
|   +-- architecture/                 System architecture docs
|   +-- methodology/                  Personality extraction guide
|   +-- research/                     Binder & validation PDFs
|   +-- cv_language.md                Portfolio/CV content
|
+-- samples/                          [TEST DATA]
|   |-- CONFIDENTIAL DIPLOMATIC COMMUNICATION.txt
|   |-- OFFICIAL INCIDENT REPORT.txt
|   +-- prompt.txt
|
+-- copies/                           [DUPLICATES - Safe to delete]
|   +-- pers/                         Backup personality JSONs
|   +-- audio_tests/                  Test MP3 files
|   +-- (various backups & zips)
|
+-- misc/                             [OTHER]
|   |-- how.to.turn.on.advasary.IQ.system.to.us.txt
|   +-- AdversaryIQ AI Beyond Defense OpenAI Challenge
|
+-- README.md                         Project overview
```

---

## API Endpoint Flow

```
+============================================================================+
|                           API ENDPOINTS                                     |
+============================================================================+

1. HEALTH CHECK
   GET /api/health
   +------------------+     +------------------+
   |     Request      | --> |     Response     |
   +------------------+     +------------------+
                            | status: "operational"
                            | message: "AdversaryIQ..."
                            | timestamp: ISO string
                            +------------------+

2. CRISIS ANALYSIS
   POST /api/process-crisis
   +------------------+     +------------------------------------------+
   |  Request Body    |     |              Response                    |
   +------------------+     +------------------------------------------+
   | { crisis: "..." }| --> | { scenario, timestamp,                   |
   +------------------+     |   agents: {                              |
                            |     roosevelt: {response...},            |
                            |     gandhi: {response...},               |
                            |     putin: {response...}                 |
                            |   },                                     |
                            |   overall_risk: "Low|Medium|High",       |
                            |   key_insights: [...]                    |
                            | }                                        |
                            +------------------------------------------+

3. DOCUMENT ANALYSIS
   POST /api/analyze-document
   +----------------------+     +------------------------------------------+
   |    Request Body      |     |              Response                    |
   +----------------------+     +------------------------------------------+
   | { documentText: "...",| --> | { document, timestamp,                  |
   |   filename: "..." }  |     |   agents: {                              |
   +----------------------+     |     roosevelt: {analysis...},            |
                                |     gandhi: {analysis...},               |
                                |     putin: {analysis...}                 |
                                |   }                                      |
                                | }                                        |
                                +------------------------------------------+

4. VOICE SYNTHESIS
   POST /api/synthesize-voice
   +----------------------+     +------------------+
   |    Request Body      |     |    Response      |
   +----------------------+     +------------------+
   | { text: "...",       | --> | audio/mpeg       |
   |   agent: "roosevelt" |     | (binary stream)  |
   |        | "gandhi"    |     +------------------+
   |        | "putin" }   |
   +----------------------+
```

---

## Agent Processing Pipeline

```
                        MULTI-AGENT PROCESSING FLOW
    =========================================================================

    INPUT: Crisis Scenario / Document Text
                            |
                            v
              +-----------------------------+
              |    PARALLEL DISPATCH        |
              |    (Promise.all)            |
              +-----------------------------+
                   /        |        \
                  /         |         \
                 v          v          v
         +----------+  +----------+  +----------+
         | ROOSEVELT|  |  GANDHI  |  |  PUTIN   |
         |  AGENT   |  |  AGENT   |  |  AGENT   |
         +----------+  +----------+  +----------+
              |             |             |
              v             v             v
    +-------------+ +-------------+ +-------------+
    | Load Profile| | Load Profile| | Load Profile|
    | Load Beliefs| | Load Beliefs| | Load Beliefs|
    +-------------+ +-------------+ +-------------+
              |             |             |
              v             v             v
    +-------------+ +-------------+ +-------------+
    | Build System| | Build System| | Build System|
    |   Prompt    | |   Prompt    | |   Prompt    |
    | (~600 tokens)| (~600 tokens)| (~600 tokens)|
    +-------------+ +-------------+ +-------------+
              |             |             |
              v             v             v
    +-------------+ +-------------+ +-------------+
    |  GPT-4o-mini|  | GPT-4o-mini|  | GPT-4o-mini|
    |  API Call   |  |  API Call  |  |  API Call  |
    +-------------+ +-------------+ +-------------+
              |             |             |
              v             v             v
    +-------------+ +-------------+ +-------------+
    | Parse JSON  | | Parse JSON  | | Parse JSON  |
    |  Response   | |  Response   | |  Response   |
    +-------------+ +-------------+ +-------------+
              \            |            /
               \           |           /
                v          v          v
              +-----------------------------+
              |     AGGREGATE RESPONSES     |
              |  - Calculate overall risk   |
              |  - Generate key insights    |
              +-----------------------------+
                            |
                            v
              +-----------------------------+
              |     RETURN ASSESSMENT       |
              +-----------------------------+
```

---

## Personality Profile Structure

```
    DUAL-LAYER PSYCHOLOGICAL PROFILE
    =========================================================================

    +------------------------------------------------------------------+
    |  AGENT PROFILE (e.g., putin_final_profile.json)                  |
    +------------------------------------------------------------------+
    |                                                                   |
    |  agent_name: "Vladimir_Putin_dual_layer_v1"                      |
    |                                                                   |
    |  +------------------------+    +------------------------+         |
    |  |  PUBLIC OCEAN SCORES   |    | BEHAVIORAL OCEAN SCORES|        |
    |  +------------------------+    +------------------------+         |
    |  | Openness:         3    |    | Openness:         4    |        |
    |  | Conscientiousness: 8   |    | Conscientiousness: 8   |        |
    |  | Extraversion:     4    |    | Extraversion:     3    |        |
    |  | Agreeableness:    2    |    | Agreeableness:    1    |        |
    |  | Neuroticism:      3    |    | Neuroticism:      6    |        |
    |  +------------------------+    +------------------------+         |
    |          ^                              ^                         |
    |          |                              |                         |
    |     What they                      How they                       |
    |     PROJECT                        ACTUALLY ACT                   |
    |                                                                   |
    |  +--------------------------------------------------------------+|
    |  |              BEHAVIORAL PARAMETERS                            ||
    |  +--------------------------------------------------------------+|
    |  | crisis_latency_hours: "20-48 (<=96 outliers)"                 ||
    |  | scapegoat_probability_pct: 70                                 ||
    |  | escalation_ladder: [Denial -> Hybrid/limited -> Ultimatum    ||
    |  |                     -> High-profile threat -> Tactical pause ||
    |  |                     -> Renewed pressure]                      ||
    |  | follow_through_decay_pct_per_30days: 60                       ||
    |  +--------------------------------------------------------------+|
    |                                                                   |
    |  +--------------------------------------------------------------+|
    |  |              CONTRADICTION PATTERNS                           ||
    |  +--------------------------------------------------------------+|
    |  | "'Always open to talks' <-> Maximalist force-backed offers"   ||
    |  | "'Defensive posture' <-> Pre-emptive interventions"           ||
    |  | "Calm affect <-> High private threat-sensitivity"             ||
    |  +--------------------------------------------------------------+|
    |                                                                   |
    |  +--------------------------------------------------------------+|
    |  |              CONTEXTUAL SWITCHING RULES                       ||
    |  +--------------------------------------------------------------+|
    |  | Televised summits => public layer                             ||
    |  | Back-channel bargaining => behavioral layer                   ||
    |  | Domestic elite crisis => behavioral first, public after       ||
    |  +--------------------------------------------------------------+|
    |                                                                   |
    +------------------------------------------------------------------+

    +------------------------------------------------------------------+
    |  BELIEFS FILE (e.g., putin_beliefs.json)                         |
    +------------------------------------------------------------------+
    |                                                                   |
    |  domestic_support:      0.60    [Internal backing confidence]    |
    |  western_threat:        0.80    [Perceived threat level]         |
    |  energy_leverage:       0.70    [Resource weapon confidence]     |
    |  scapegoat_tendency:    0.70    [Blame assignment likelihood]    |
    |  impulsivity_index:     0.50    [Reactive behavior tendency]     |
    |  context_switch_flex:   0.65    [Adaptability score]             |
    |                                                                   |
    +------------------------------------------------------------------+
```

---

## Voice Synthesis Flow

```
    ELEVENLABS TEXT-TO-SPEECH PIPELINE
    =========================================================================

    +------------------+
    |  Input Request   |
    | { text, agent }  |
    +--------+---------+
             |
             v
    +------------------+
    |  Voice ID Lookup |
    +------------------+
    |  roosevelt -> zkXpoOeAWrFgfuIRi0yD  |
    |  gandhi    -> XB0fDUnXU5powFXDhCwa  |
    |  putin     -> pNInz6obpgDQGcFmaJgB  |
    +------------------+
             |
             v
    +------------------+
    |  ElevenLabs API  |
    |  textToSpeech.   |
    |  convert()       |
    +------------------+
             |
             v
    +------------------+
    |  ReadableStream  |
    |  -> Buffer       |
    +------------------+
             |
             v
    +------------------+
    |  Response        |
    |  Content-Type:   |
    |  audio/mpeg      |
    +------------------+
```

---

## Technology Stack

```
    +==================================================================+
    |                    TECHNOLOGY STACK                               |
    +==================================================================+

    RUNTIME
    +------------------+     +------------------+     +------------------+
    |     Node.js      |     |    Express 5.1   |     |   CORS enabled   |
    +------------------+     +------------------+     +------------------+

    AI/ML SERVICES
    +------------------+     +------------------+
    |  OpenAI API      |     |  ElevenLabs API  |
    |  GPT-4o-mini     |     |  eleven_multi_v2 |
    |  temp: 0.7       |     |  3 voice models  |
    |  tokens: 600-800 |     |                  |
    +------------------+     +------------------+

    DEPENDENCIES (Key)
    +------------------+     +------------------+     +------------------+
    |  openai ^5.1.0   |     | @elevenlabs      |     |  dotenv ^16.5.0  |
    |                  |     |  /elevenlabs-js  |     |                  |
    |                  |     |  ^2.1.0          |     |                  |
    +------------------+     +------------------+     +------------------+

    DATA STORAGE
    +------------------+
    |  JSON Files      |
    |  (6 personality  |
    |   profiles)      |
    +------------------+
```

---

## Risk Assessment Logic

```
    OVERALL RISK CALCULATION
    =========================================================================

    Input: [roosevelt.escalation_risk, gandhi.escalation_risk, putin.escalation_risk]

                    +-------------------+
                    |  Count Risk Types |
                    +-------------------+
                            |
            +---------------+---------------+
            |               |               |
            v               v               v
    +-------------+  +-------------+  +-------------+
    | High Count  |  |Medium Count |  | Low Count   |
    +-------------+  +-------------+  +-------------+
            |               |               |
            v               v               v
    +-------------------------------------------------------+
    |                   DECISION MATRIX                      |
    +-------------------------------------------------------+
    | IF High >= 2                    --> Return "High"      |
    | ELSE IF High >= 1 OR Medium >= 2 --> Return "Medium"  |
    | ELSE                            --> Return "Low"       |
    +-------------------------------------------------------+
```

---

## Quick Start Commands

```bash
# Navigate to backend
cd /home/schwartzlabs.ai/02_projects/AdversaryIQ/backend

# Install dependencies (if needed)
npm install

# Start server
node server.js

# Test health endpoint
curl http://localhost:3001/api/health

# Test crisis analysis
curl -X POST http://localhost:3001/api/process-crisis \
  -H "Content-Type: application/json" \
  -d '{"crisis": "China threatens Taiwan with military exercises"}'
```

---

*Document generated: January 7, 2026 - 5:10 PM EST*
*System Location: /home/schwartzlabs.ai/02_projects/AdversaryIQ/*
