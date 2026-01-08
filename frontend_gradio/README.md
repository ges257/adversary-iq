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

# AdversaryIQ - Diplomatic Intelligence Platform

A multi-agent psychological simulation system that models how historical world leaders would respond to modern diplomatic crises.

## Overview

AdversaryIQ leverages psychological profiling and multi-agent orchestration to simulate responses from three distinct leadership archetypes:

- **Theodore Roosevelt** — American pragmatic idealism
- **Indira Gandhi** — Strategic non-alignment and regional power projection
- **Vladimir Putin** — Calculated realpolitik and asymmetric leverage

Each agent processes diplomatic scenarios through evidence-based psychological frameworks, generating both public responses and private strategic calculus.

## Features

### Psychological Analysis Dimensions

| Dimension | Description |
|-----------|-------------|
| **Public Response** | Official statements the leader would release |
| **Private Actions** | Behind-the-scenes strategic moves |
| **Psychological Reasoning** | Big Five + core beliefs driving behavior |
| **Escalation Analysis** | Position on crisis escalation ladder |
| **Belief Impact** | How crisis affects worldview |

### Intelligence Output

- Multi-perspective crisis analysis
- Risk assessment scoring
- Key strategic insights synthesis
- Timeline and decision confidence metrics

## Architecture

```
┌─────────────────────────────────────────┐
│         Gradio Frontend (HF Spaces)     │
│    ┌───────────────────────────────┐    │
│    │  Crisis Input → API Client    │    │
│    └───────────────┬───────────────┘    │
└────────────────────┼────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────┐
│          Backend API Server             │
│  ┌───────────────────────────────────┐  │
│  │    Multi-Agent Orchestrator       │  │
│  │  ┌─────────┐ ┌─────────┐ ┌─────┐  │  │
│  │  │Roosevelt│ │ Gandhi  │ │Putin│  │  │
│  │  └────┬────┘ └────┬────┘ └──┬──┘  │  │
│  │       └───────────┼─────────┘     │  │
│  │                   ▼               │  │
│  │     Psychological Profile Engine  │  │
│  └───────────────────────────────────┘  │
└─────────────────────────────────────────┘
```

## Configuration

Set the `API_URL` environment variable to point to your backend API:

```
API_URL=https://your-backend-api.com
```

## Example Scenarios

Try these crisis scenarios:

1. "Russia announces energy export restrictions following EU semiconductor sanctions"
2. "North Korea tests a new long-range missile system during US-South Korea military exercises"
3. "China establishes a new military base in the South China Sea near disputed waters"
4. "Iran threatens to close the Strait of Hormuz in response to new oil sanctions"

## Design Philosophy

The interface deliberately evokes classified intelligence briefing software:

- **Dark terminal aesthetic** — Professional, serious tone
- **Monospace typography** — Technical credibility
- **Color-coded agents** — Instant visual differentiation
- **BLUF format** — Military intelligence conventions
- **Classification banners** — Immersive context

## License

MIT

---

*Built for portfolio demonstration purposes. The psychological profiles are simplified models for simulation and do not represent actual intelligence assessments.*
