# AdversaryIQ System: Complete Architecture Overview

## System Classification

This is best described as a **"Hybrid AI System"** combining:

- **Generative AI** for personality modeling and response generation
- **Multi-Agent Simulation** for perspective analysis
- **Voice Synthesis AI** for multi-modal output
- **Predictive AI** for crisis response modeling

The system leverages LLMs at two critical phases:

1. **Design-time**: Creating psychological profiles from historical data
2. **Runtime**: Generating contextual responses through those profiles



## System Purpose

AdversaryIQ is an AI-powered intelligence analysis system that simulates how historical political leaders would respond to modern crises using evidence-based psychological profiles. It provides multi-perspective analysis for crisis scenarios, document interpretation, and voice synthesis.

## Complete System Architecture

```
┌─────────────────────────────────────────────────────────┐
│         PROFILE GENERATION (Pre-Runtime Phase)           │
│                                                          │
│  Historical Analysis → Dual-Layer Profiles → JSON Files │
│  (Public vs Behavioral OCEAN, Contradictions, Evidence) │
└────────────────────────┬────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────┐
│              Express.js API Server (Port 3001)           │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  ┌────────────────────────────────────────────────────┐ │
│  │            THREE CORE ANALYSIS ENGINES             │ │
│  ├────────────────────────────────────────────────────┤ │
│  │                                                    │ │
│  │  1. CRISIS ANALYSIS (/api/process-crisis)         │ │
│  │     - Parallel 3-agent simulation                 │ │
│  │     - Risk assessment & insights                  │ │
│  │                                                    │ │
│  │  2. DOCUMENT ANALYSIS (/api/analyze-document)     │ │
│  │     - Hidden intentions detection                 │ │
│  │     - Psychological tactics identification        │ │
│  │     - Authenticity assessment                     │ │
│  │                                                    │ │
│  │  3. VOICE SYNTHESIS (/api/synthesize-voice)       │ │
│  │     - Agent-specific voice selection              │ │
│  │     - Text-to-speech conversion                   │ │
│  │     - Audio stream delivery                       │ │
│  └────────────────────────────────────────────────────┘ │
└────────────────────────┬────────────────────────────────┘
                         │
         ┌───────────────┼───────────────┐
         ▼               ▼               ▼
┌─────────────┐ ┌─────────────┐ ┌─────────────┐
│ Personality │ │   OpenAI    │ │ ElevenLabs  │
│ Profiles    │ │  GPT-4o-mini│ │ Voice API   │
│(JSON Files) │ │             │ │             │
└─────────────┘ └─────────────┘ └─────────────┘

THREE LEADERS:
- Theodore Roosevelt
- Indira Gandhi  
- Vladimir Putin
```

## Implemented Components

### 1. Data Layer - Personality Profiles

Each leader has two JSON files loaded at startup:

**Profile Structure** (`roosevelt_final_profile.json`):

json

```json
{
  "agent_name": "Teddy_Roosevelt_dual_layer_v1",
  "public_ocean_scores": {...},      // What they projected
  "behavioral_ocean_scores": {...},   // How they actually acted
  "behavioral_parameters": {
    "crisis_latency_hours": "24-3000",
    "scapegoat_probability_pct": 60,
    "escalation_ladder": [...],
    "humor_threat_phrases": [...]
  },
  "contradiction_patterns": [...],
  "contextual_switching_rules": [...],
  "predictive_framework": {...}
}
```

**Beliefs Structure** (`roosevelt_beliefs.json`):

json

```json
{
  "beliefs": {
    "domestic_support": 0.75,
    "foreign_threat": 0.50,
    "scapegoat_tendency": 0.60,
    "impulsivity_index": 0.40
  }
}
```

### 2. Crisis Analysis Engine

**Endpoint**: `/api/process-crisis`

**Process**:

javascript

```javascript
// Actual implementation - parallel processing
const [rooseveltResponse, gandhiResponse, putinResponse] = 
  await Promise.all([
    createAgent('roosevelt', crisis),
    createAgent('gandhi', crisis),
    createAgent('putin', crisis)
  ]);

// Aggregated intelligence assessment
const intelligenceAssessment = {
  scenario: crisis,
  timestamp: new Date().toISOString(),
  agents: {
    roosevelt: {...rooseveltResponse, personality_notes},
    gandhi: {...gandhiResponse, personality_notes},
    putin: {...putinResponse, personality_notes}
  },
  overall_risk: calculateOverallRisk([...]),
  key_insights: generateKeyInsights([...])
};
```

**System Prompt Construction** (~500-800 tokens):

- Full psychological profile injection
- Dual OCEAN scores
- Crisis response parameters
- Belief states
- Contradiction patterns
- Contextual switching rules
- Predictive framework

### 3. Document Analysis Engine

**Endpoint**: `/api/analyze-document`

**Purpose**: Analyze diplomatic documents through psychological frameworks

**Process**:

javascript

```javascript
// Each agent analyzes the document
const [rooseveltAnalysis, gandhiAnalysis, putinAnalysis] = 
  await Promise.all([
    analyzeDocumentThroughAgent('roosevelt', documentText, filename),
    analyzeDocumentThroughAgent('gandhi', documentText, filename),
    analyzeDocumentThroughAgent('putin', documentText, filename)
  ]);
```

**Analysis Output**:

json

```json
{
  "document_interpretation": "What this really means",
  "hidden_intentions": "What they're actually trying to accomplish",
  "psychological_tactics": "Manipulation techniques identified",
  "your_response": "How I would respond",
  "authenticity_assessment": "Genuine or deceptive"
}
```

### 4. Voice Synthesis Service

**Endpoint**: `/api/synthesize-voice`

**Voice Mapping**:

javascript

```javascript
switch(agent) {
  case 'roosevelt':
    voiceId = "zkXpoOeAWrFgfuIRi0yD";
    break;
  case 'gandhi':
    voiceId = "XB0fDUnXU5powFXDhCwa";
    break;
  case 'putin':
    voiceId = "pNInz6obpgDQGcFmaJgB";
    break;
}
```

**Process**:

1. Receive text and agent identifier
2. Select appropriate voice model
3. Call ElevenLabs API
4. Convert stream to buffer
5. Return audio/mpeg response

### 5. Helper Functions

**Risk Assessment**:

javascript

```javascript
function calculateOverallRisk(responses) {
  // Analyzes escalation_risk from all agents
  // Returns: 'High', 'Medium', or 'Low'
}
```

**Insight Generation**:

javascript

```javascript
function generateKeyInsights(responses) {
  // Synthesizes:
  // - Response timeline variance
  // - Escalation risk distribution
  // - Personality-driven patterns
  // - Contradiction impacts
}
```

## Profile Generation Methodology

Based on provided PDFs, profiles were created through:

### Evidence-Based Analysis

- **Public OCEAN Scores**: From speeches, public writings
  - Citations included (e.g., "Strenuous Life" speech, Sorbonne address)
- **Behavioral OCEAN Scores**: From actual decisions
  - Evidence: Panama intervention, coal strike handling, Great White Fleet

### Documented Contradictions

Every contradiction serves strategic purpose:

```
"Square Deal fairness" ↔ "bypasses sovereignty" = dual-audience strategy
"Speak softly" ↔ "Great White Fleet" = bargaining leverage
"Conservation" ↔ "Safari hunting" = multiple constituency management
```

### Behavioral Parameters (Historically Calibrated)

- **Crisis Latency**: From actual response times (e.g., 4.5 months for coal strike)
- **Escalation Ladder**: Pattern from multiple crises
- **Scapegoating**: Targets and frequency from historical record

## Technical Implementation

### API Configuration

- **OpenAI**: GPT-4o-mini, temperature 0.7, 600-800 tokens
- **ElevenLabs**: eleven_multilingual_v2 model
- **Express**: CORS enabled, JSON parsing
- **Error Handling**: Try-catch with fallback responses

### Parallel Processing

- All three agents process simultaneously
- Promise.all reduces latency from 3x to 1x
- Independent failure handling

### JSON Response Handling

javascript

```javascript
// Cleans markdown artifacts from GPT responses
if (content.startsWith('```json')) {
  content = content.replace(/```json\n?/, '').replace(/\n?```$/, '');
}
```

## LLM/GenAI Techniques Applied

1. **Complex Prompt Engineering**
   - 500+ token system prompts
   - Psychological framework embedding
   - Structured output enforcement
2. **Dual-Layer Personality Modeling**
   - Public persona vs behavioral reality
   - Context-dependent switching
   - Contradiction management
3. **Multi-Agent Simulation**
   - Parallel perspective processing
   - Cross-validation of responses
   - Risk aggregation
4. **Evidence-Based Parameters**
   - Every value tied to historical evidence
   - Citations included in profiles
   - Validation against known events
5. **Voice Synthesis Integration**
   - Leader-specific voice models
   - Text-to-speech pipeline
   - Audio stream handling

## System Capabilities Summary

**What It Does**:

- Simulates 3 leader perspectives on any crisis
- Analyzes documents for hidden meanings
- Generates voice responses
- Provides risk assessments
- Creates cross-agent insights

**Current Limitations**:

- Hardcoded API keys (security issue)
- No authentication
- Open CORS
- Synchronous API calls
- File-based storage

## Classification

This is a **Multi-Agent Simulation System** featuring:

- Evidence-based psychological modeling
- Parallel multi-perspective analysis
- Document psychological interpretation
- Multi-modal output (text + voice)
- Structured predictive intelligence

The system combines historical analysis with runtime AI to create a sophisticated behavioral prediction platform for intelligence analysis.