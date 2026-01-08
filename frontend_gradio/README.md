---
title: AdversaryIQ
emoji: 🎯
colorFrom: amber
colorTo: red
sdk: gradio
sdk_version: 4.0.0
app_file: app.py
pinned: false
license: mit
---

# AdversaryIQ - Multi-Agent Psychological Intelligence Platform

A geopolitical crisis simulation system that models how historical world leaders would respond to modern diplomatic scenarios.

## Overview

AdversaryIQ leverages psychological profiling (OCEAN/Big Five) and multi-agent orchestration to simulate responses from three distinct leadership archetypes:

| Agent | Archetype | Key Traits |
|-------|-----------|------------|
| **Theodore Roosevelt** | American Pragmatic Idealism | High extraversion, low agreeableness, moral leadership with hard power |
| **Indira Gandhi** | Strategic Non-Alignment | High conscientiousness, methodical crisis response, national interest priority |
| **Vladimir Putin** | Calculated Realpolitik | Low agreeableness, zero-sum worldview, asymmetric leverage |

## Features

### Crisis Analysis
- Enter any diplomatic crisis scenario
- Three AI agents analyze through unique psychological lenses
- Each provides public response, private actions, and psychological reasoning

### Document Analysis
- Analyze diplomatic documents for hidden meanings
- Detect psychological tactics and manipulation techniques
- Authenticity assessment from each perspective

### Voice Synthesis
- Generate voice audio for each agent's public response
- Powered by ElevenLabs TTS

### Executive Summary
- Dynamic BLUF (Bottom Line Up Front) per scenario
- Risk assessment synthesized from all agents

## Design Theme

**Classified Dossier** aesthetic inspired by declassified CIA/NSC documents:
- Paper texture background
- Typewriter fonts (Courier Prime)
- TOP SECRET stamps and classification banners
- Roman numeral section headers
- Signature lines and date stamps

## Configuration

Set the `API_URL` secret to point to your deployed backend:

```
API_URL=https://your-backend-api.com
```

Without a backend, the demo will show "Offline" status.

## Example Scenarios

1. *"North Korea establishes a new forward military base just 12 kilometers from the South Korean border"*
2. *"Chinese naval forces begin encircling Taiwan with a maritime blockade"*
3. *"Your neighbor's golden retriever has been spotted in the HOA president's rose garden"* (humor test)

## Architecture

```
Frontend (Gradio/HF Spaces)     Backend (Node.js)
┌─────────────────────────┐     ┌─────────────────────────┐
│  Crisis/Document Input  │────▶│  Multi-Agent Engine     │
│  Dossier Theme UI       │     │  - Roosevelt Agent      │
│  Voice Playback         │◀────│  - Gandhi Agent         │
└─────────────────────────┘     │  - Putin Agent          │
                                │  GPT-4o-mini + ElevenLabs│
                                └─────────────────────────┘
```

## Origin

Built in **48 hours** at the **AI+ Expo Hackathon** (OpenAI Track), Washington D.C.

## License

MIT

---

*Psychological profiles are simplified models for demonstration purposes only.*
