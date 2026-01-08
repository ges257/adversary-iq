# AdversaryIQ Frontend Rebuild Plan
**Date: January 7, 2026 - 6:30 PM EST**

---

## Current State

### What Exists
- **Backend API**: Running on port 3001 (Node.js/Express)
- **3 Partial React Components**: Found in Downloads folder
  - `updated_index.js` - Main page with tabs
  - `document_upload.js` - File upload component
  - `document_analysis_results.js` - Analysis display
- **Original Project**: Was on Lovable.dev as "adversary-iq-insights-platform" (not recoverable)

### API Endpoints Available
| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/api/health` | GET | Status check |
| `/api/process-crisis` | POST | Crisis analysis → 3 agent responses |
| `/api/analyze-document` | POST | Document psychological analysis |
| `/api/synthesize-voice` | POST | Text-to-speech (ElevenLabs) |

---

## API Response Structure

```python
# Expected response from /api/process-crisis
{
    "scenario": "crisis text",
    "timestamp": "ISO string",
    "agents": {
        "roosevelt": {
            "name": "Theodore Roosevelt",
            "public_response": str,
            "private_actions": str,
            "psychological_reasoning": str,
            "escalation_risk": "Low|Medium|High",
            "timeline": str,
            "escalation_phase": str,
            "belief_impact": str,
            "personality_notes": str
        },
        "gandhi": { ... },
        "putin": { ... }
    },
    "overall_risk": "Low|Medium|High",
    "key_insights": [str, str, str, str]
}

# Expected response from /api/analyze-document
{
    "document": "filename",
    "timestamp": "ISO string",
    "agents": {
        "roosevelt": {
            "name": "Theodore Roosevelt",
            "document_interpretation": str,
            "hidden_intentions": str,
            "psychological_tactics": str,
            "your_response": str,
            "authenticity_assessment": str
        },
        "gandhi": { ... },
        "putin": { ... }
    }
}
```

---

## UI Architecture (From Original Lovable Build)

```
┌─────────────────────────────────────────────────────────┐
│  FOR OFFICIAL USE ONLY (banner)                         │
├─────────────────────────────────────────────────────────┤
│  AdversaryIQ - Diplomatic Intelligence Platform         │
│  Psychological Response Prediction • [timestamp]        │
├─────────────────────────────────────────────────────────┤
│  CRISIS SCENARIO ANALYSIS          ● SECURE TERMINAL    │
│  ┌─────────────────────────────────────────────────┐   │
│  │ [Textarea for crisis input]                      │   │
│  └─────────────────────────────────────────────────┘   │
├─────────────────────────────────────────────────────────┤
│  DOCUMENT INTELLIGENCE ANALYSIS                         │
│  ┌─────────────────────────────────────────────────┐   │
│  │ [File upload zone - drag/drop]                   │   │
│  └─────────────────────────────────────────────────┘   │
├─────────────────────────────────────────────────────────┤
│  [🎙 VOICE BRIEFING]  [PROCESS INTELLIGENCE]           │
├─────────────────────────────────────────────────────────┤
│  ┌──────────┐  ┌──────────┐  ┌──────────┐              │
│  │ROOSEVELT │  │ GANDHI   │  │  PUTIN   │              │
│  │(amber)   │  │(green)   │  │(red)     │              │
│  │          │  │          │  │          │              │
│  │• Public  │  │• Public  │  │• Public  │              │
│  │• Private │  │• Private │  │• Private │              │
│  │• Psych   │  │• Psych   │  │• Psych   │              │
│  │• Escal.  │  │• Escal.  │  │• Escal.  │              │
│  │• Belief  │  │• Belief  │  │• Belief  │              │
│  │• Contrad.│  │• Contrad.│  │• Contrad.│              │
│  └──────────┘  └──────────┘  └──────────┘              │
├─────────────────────────────────────────────────────────┤
│  EXECUTIVE INTELLIGENCE SUMMARY - BLUF                  │
│  [Bottom Line Up Front + Key Objectives + Implications] │
├─────────────────────────────────────────────────────────┤
│  ● Ready for Intelligence Processing                    │
└─────────────────────────────────────────────────────────┘
```

---

## Core Features to Replicate

1. **Crisis Scenario Input** - Text area for geopolitical scenarios
2. **Document Upload** - PDF/DOC/TXT/image support with drag-drop
3. **Process Intelligence Button** - Triggers API call to backend
4. **Three-Agent Dashboard** with per-agent sections:
   - Public Response
   - Private Actions
   - Psychological Reasoning
   - Escalation Analysis (amber border)
   - Belief Impact Assessment (blue border)
   - Contradiction Alert (red border)
   - Confidence Metrics (green border)
5. **Executive Intelligence Summary - BLUF** section at bottom
6. **Voice Synthesis** - Play agent responses as audio

---

## Rebuild Options

### Option 1: Gradio (Python) - RECOMMENDED FOR HF SPACES
**Pros:**
- Native Hugging Face Spaces support
- Python-based (no npm/node needed)
- Quick to build (~150 lines)
- Free hosting on HF Spaces

**Cons:**
- Less customizable than React
- Government aesthetic harder to achieve perfectly
- Limited CSS control

**Files needed:**
- `app.py` (~150 lines)
- `requirements.txt` (~5 lines)
- `README.md`

### Option 2: React + Vite
**Pros:**
- Full control over UI
- Can match original Lovable design exactly
- Professional look

**Cons:**
- Requires Docker for HF Spaces
- More complex deployment
- More files to maintain

**Files needed:**
- Full React project structure
- Dockerfile for HF Spaces
- ~10-15 component files

### Option 3: Static HTML/JS
**Pros:**
- No build step
- Simple deployment
- Can still look professional

**Cons:**
- More verbose code
- Harder to maintain
- No component reuse

---

## Agent Color Scheme

| Agent | Primary Color | Border | Background |
|-------|---------------|--------|------------|
| Roosevelt | Amber/Gold | `#f59e0b` | `rgba(245, 158, 11, 0.1)` |
| Gandhi | Green | `#10b981` | `rgba(16, 185, 129, 0.1)` |
| Putin | Red/Blue | `#3b82f6` | `rgba(59, 130, 246, 0.1)` |

---

## Styling Guidelines

- **Background**: Dark slate (`#0f172a`, `#1e293b`)
- **Text**: Light (`#f1f5f9`, `#cbd5e1`)
- **Accents**: Government blue (`#3b82f6`)
- **Borders**: Subtle (`#334155`)
- **Font**: Monospace for technical elements
- **Aesthetic**: CIA/NSC briefing software look

---

## Next Steps

1. Choose rebuild option (Gradio recommended)
2. Build the frontend
3. Test with running backend
4. Deploy to Hugging Face Spaces
5. Connect GitHub repository

---

## Existing Component Code Location

Downloaded to Windows:
- `C:\Users\grego\Downloads\updated_index.js`
- `C:\Users\grego\Downloads\document_upload.js`
- `C:\Users\grego\Downloads\document_analysis_results.js`

These can be used as reference for the rebuild.
