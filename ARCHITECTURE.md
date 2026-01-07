# AdversaryIQ Architecture

## System Overview

AdversaryIQ is a multi-agent system that automates enterprise threat simulation through coordinated AI agents.

---

## High-Level Flow

```mermaid
flowchart TB
    subgraph S1["1. Intelligence Gathering"]
        A1["MITRE ATT&CK Parser"]
        A2["CVE Aggregator"]
        A3["Environment Profiler"]
    end

    subgraph S2["2. Attack Planning"]
        B1["GPT-4 Strategist"]
        B2["Chain Generator"]
        B3["Feasibility Scorer"]
    end

    subgraph S3["3. Simulation Engine"]
        C1["Safe Executor"]
        C2["Impact Calculator"]
        C3["Evidence Collector"]
    end

    subgraph S4["4. Reporting"]
        D1["Finding Synthesizer"]
        D2["Remediation Engine"]
        D3["Executive Summary"]
    end

    S1 --> S2 --> S3 --> S4

    style S1 fill:#1a1a2e,stroke:#A78BFA,color:#A3B8CC
    style S2 fill:#1a1a2e,stroke:#A78BFA,color:#A3B8CC
    style S3 fill:#1a1a2e,stroke:#A78BFA,color:#A3B8CC
    style S4 fill:#1a1a2e,stroke:#A78BFA,color:#A3B8CC
```

---

## Core Components

### 1. Intelligence Module

| Component | Function |
|-----------|----------|
| **ATT&CK Parser** | Ingests MITRE framework, builds technique graph |
| **CVE Aggregator** | Monitors NVD, correlates with client tech stack |
| **Environment Profiler** | Maps client infrastructure to attack surface |

### 2. Planning Module

| Component | Function |
|-----------|----------|
| **GPT-4 Strategist** | Generates attack hypotheses based on threat model |
| **Chain Generator** | Builds multi-step attack sequences |
| **Feasibility Scorer** | Ranks attacks by likelihood of success |

### 3. Simulation Module

| Component | Function |
|-----------|----------|
| **Safe Executor** | Runs simulations in isolated environment |
| **Impact Calculator** | Estimates business impact of successful attack |
| **Evidence Collector** | Captures proof-of-concept artifacts |

### 4. Reporting Module

| Component | Function |
|-----------|----------|
| **Finding Synthesizer** | Consolidates results into structured findings |
| **Remediation Engine** | Maps findings to actionable fixes |
| **Executive Summary** | Generates C-level briefing documents |

---

## Agent Architecture

```mermaid
graph LR
    subgraph Agents["Multi-Agent Coordination"]
        A["Strategist Agent"]
        B["Executor Agent"]
        C["Analyst Agent"]
    end

    subgraph Tools["Tool Library"]
        T1["ATT&CK Lookup"]
        T2["CVE Search"]
        T3["Impact Estimator"]
        T4["Report Generator"]
    end

    A --> B --> C
    A --> T1
    A --> T2
    B --> T3
    C --> T4

    style Agents fill:#0D1B2A,stroke:#A78BFA,color:#fff
    style Tools fill:#1a1a2e,stroke:#A3B8CC,color:#A3B8CC
```

---

## Security Boundaries

| Boundary | Control |
|----------|---------|
| **Simulation Isolation** | All tests run in sandboxed environment |
| **Credential Handling** | No real credentials stored or transmitted |
| **Data Privacy** | Client data never leaves their infrastructure |
| **Audit Logging** | Complete trace of all agent actions |

---

## Technology Stack

| Layer | Technology |
|-------|------------|
| **Agent Core** | GPT-4 with function calling |
| **Orchestration** | Python, LangChain |
| **Backend** | FastAPI, PostgreSQL |
| **Frontend** | React, TypeScript, TailwindCSS |
| **Infrastructure** | Docker, AWS |

---

*This document describes the architecture without revealing proprietary implementation details.*
