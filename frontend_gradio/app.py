"""
AdversaryIQ - Diplomatic Intelligence Platform
Gradio Frontend - Classified Dossier Theme

Inspired by declassified CIA/NSC documents.
"""

import gradio as gr
import requests
import os
import tempfile
import base64
from datetime import datetime

# Configuration
API_URL = os.environ.get("API_URL", "http://localhost:3001")

# Dossier Theme CSS
DOSSIER_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Courier+Prime:wght@400;700&family=Special+Elite&display=swap');

.gradio-container {
    background-color: #f5f2e8 !important;
    background-image:
        repeating-linear-gradient(
            0deg,
            transparent,
            transparent 31px,
            rgba(0,0,0,0.025) 31px,
            rgba(0,0,0,0.025) 32px
        ) !important;
    font-family: 'Courier Prime', 'Courier New', Courier, monospace !important;
}

.contain {
    max-width: 900px !important;
    margin: 0 auto !important;
}

.voice-btn {
    background: #8B4513 !important;
    color: white !important;
    font-size: 11px !important;
    letter-spacing: 1px !important;
}
"""

# Store last response for voice synthesis
last_crisis_response = {}


def format_agent_dossier(agent_key: str, agent_data: dict) -> str:
    """Format agent response as a classified dossier page."""

    agent_info = {
        'roosevelt': {
            'name': 'ROOSEVELT, Theodore',
            'description': 'U.S. Historical Leadership Profile',
            'color': '#8B4513'
        },
        'gandhi': {
            'name': 'GANDHI, Indira',
            'description': 'Indian Strategic Leadership Profile',
            'color': '#2F4F4F'
        },
        'putin': {
            'name': 'PUTIN, Vladimir',
            'description': 'Russian Federation Leadership Profile',
            'color': '#8B0000'
        }
    }

    info = agent_info.get(agent_key, agent_info['roosevelt'])

    if not agent_data:
        return f"""
        <div style="background: #fffefa; border: 1px solid #888; padding: 36px;
                    font-family: 'Courier Prime', monospace; text-align: center; color: #888;">
            No analysis data available for {info['name']}.
        </div>
        """

    public_response = agent_data.get('public_response', 'Awaiting analysis...')
    private_actions = agent_data.get('private_actions', 'Awaiting analysis...')
    psych_reasoning = agent_data.get('psychological_reasoning', 'Awaiting analysis...')

    html = f"""
    <div style="background: #fffefa; border: 1px solid #888; padding: 36px; position: relative;
                font-family: 'Courier Prime', 'Courier New', monospace; box-shadow: 3px 3px 10px rgba(0,0,0,0.08);">

        <!-- Corner fold effect -->
        <div style="position: absolute; bottom: 0; right: 0; width: 40px; height: 40px;
                    background: linear-gradient(135deg, #fffefa 50%, #e8e4d8 50%);
                    box-shadow: -2px -2px 4px rgba(0,0,0,0.05);"></div>

        <!-- Dossier Header -->
        <div style="border-bottom: 1px solid #ccc; padding-bottom: 16px; margin-bottom: 28px;">
            <div style="margin-bottom: 6px;">
                <span style="font-size: 10px; font-weight: bold; letter-spacing: 2px; margin-right: 8px;">SUBJECT:</span>
                <span style="font-size: 13px; text-decoration: underline; text-underline-offset: 3px;">
                    {info['name']} — {info['description']}
                </span>
            </div>
            <div>
                <span style="font-size: 10px; font-weight: bold; letter-spacing: 2px; margin-right: 8px;">STATUS:</span>
                <span style="font-size: 11px; color: #006400; font-weight: bold; letter-spacing: 1px;">PROFILE ACTIVE</span>
            </div>
        </div>

        <!-- Content Blocks -->
        <div style="display: flex; flex-direction: column; gap: 28px;">

            <!-- A. Public Response -->
            <div>
                <h4 style="font-size: 11px; font-weight: bold; letter-spacing: 2px; margin-bottom: 10px;
                           text-decoration: underline; text-underline-offset: 3px;">
                    A. PUBLIC RESPONSE
                </h4>
                <p style="font-size: 13px; line-height: 2; color: #1a1a1a;">
                    {public_response}
                </p>
            </div>

            <!-- B. Private Actions (with redacted hover effect simulation) -->
            <div style="position: relative;">
                <h4 style="font-size: 11px; font-weight: bold; letter-spacing: 2px; margin-bottom: 10px;
                           text-decoration: underline; text-underline-offset: 3px; color: #8b0000;">
                    B. PRIVATE ACTIONS [CLASSIFIED]
                </h4>
                <p style="font-size: 13px; line-height: 2; color: #1a1a1a;">
                    {private_actions}
                </p>
            </div>

            <!-- C. Psychological Assessment -->
            <div>
                <h4 style="font-size: 11px; font-weight: bold; letter-spacing: 2px; margin-bottom: 10px;
                           text-decoration: underline; text-underline-offset: 3px;">
                    C. PSYCHOLOGICAL ASSESSMENT
                </h4>
                <p style="font-size: 13px; line-height: 2; color: #444;">
                    {psych_reasoning}
                </p>
            </div>
        </div>

        <!-- Page Footer -->
        <div style="display: flex; justify-content: space-between; margin-top: 36px; padding-top: 16px;
                    border-top: 1px solid #ccc; font-size: 10px; color: #888; letter-spacing: 1px;">
            <span>Page 1 of 3</span>
            <span>SECRET // NOFORN</span>
        </div>
    </div>
    """
    return html


def format_document_dossier(agent_key: str, agent_data: dict) -> str:
    """Format document analysis as a classified dossier page."""

    agent_info = {
        'roosevelt': {'name': 'ROOSEVELT, Theodore', 'color': '#8B4513'},
        'gandhi': {'name': 'GANDHI, Indira', 'color': '#2F4F4F'},
        'putin': {'name': 'PUTIN, Vladimir', 'color': '#8B0000'}
    }

    info = agent_info.get(agent_key, agent_info['roosevelt'])

    if not agent_data:
        return "<div style='padding: 40px; text-align: center; color: #888;'>No analysis available.</div>"

    html = f"""
    <div style="background: #fffefa; border: 1px solid #888; padding: 36px; position: relative;
                font-family: 'Courier Prime', monospace; box-shadow: 3px 3px 10px rgba(0,0,0,0.08);">

        <div style="position: absolute; bottom: 0; right: 0; width: 40px; height: 40px;
                    background: linear-gradient(135deg, #fffefa 50%, #e8e4d8 50%);"></div>

        <div style="border-bottom: 1px solid #ccc; padding-bottom: 16px; margin-bottom: 28px;">
            <span style="font-size: 10px; font-weight: bold; letter-spacing: 2px;">ANALYST:</span>
            <span style="font-size: 13px; text-decoration: underline; margin-left: 8px;">{info['name']}</span>
        </div>

        <div style="display: flex; flex-direction: column; gap: 24px;">
            <div>
                <h4 style="font-size: 11px; font-weight: bold; letter-spacing: 2px; margin-bottom: 10px;
                           text-decoration: underline;">A. DOCUMENT INTERPRETATION</h4>
                <p style="font-size: 13px; line-height: 2;">{agent_data.get('document_interpretation', 'N/A')}</p>
            </div>

            <div style="background: rgba(139,0,0,0.05); border-left: 3px solid #8b0000; padding: 16px;">
                <h4 style="font-size: 11px; font-weight: bold; letter-spacing: 2px; margin-bottom: 10px;
                           color: #8b0000;">B. HIDDEN INTENTIONS DETECTED</h4>
                <p style="font-size: 13px; line-height: 2;">{agent_data.get('hidden_intentions', 'None detected')}</p>
            </div>

            <div style="background: rgba(139,69,19,0.05); border-left: 3px solid #8B4513; padding: 16px;">
                <h4 style="font-size: 11px; font-weight: bold; letter-spacing: 2px; margin-bottom: 10px;
                           color: #8B4513;">C. PSYCHOLOGICAL TACTICS</h4>
                <p style="font-size: 13px; line-height: 2;">{agent_data.get('psychological_tactics', 'None identified')}</p>
            </div>

            <div>
                <h4 style="font-size: 11px; font-weight: bold; letter-spacing: 2px; margin-bottom: 10px;
                           text-decoration: underline;">D. RECOMMENDED RESPONSE</h4>
                <p style="font-size: 13px; line-height: 2;">{agent_data.get('your_response', 'No response formulated')}</p>
            </div>

            <div style="background: #f5f2e8; padding: 12px; border: 1px dashed #888;">
                <span style="font-size: 10px; font-weight: bold; letter-spacing: 2px; color: #006400;">
                    AUTHENTICITY ASSESSMENT:
                </span>
                <span style="font-size: 12px; margin-left: 8px;">
                    {agent_data.get('authenticity_assessment', 'Unable to assess')}
                </span>
            </div>
        </div>

        <div style="display: flex; justify-content: space-between; margin-top: 36px; padding-top: 16px;
                    border-top: 1px solid #ccc; font-size: 10px; color: #888;">
            <span>DOCUMENT ANALYSIS</span>
            <span>CONFIDENTIAL</span>
        </div>
    </div>
    """
    return html


def format_executive_summary(data: dict) -> str:
    """Format executive summary as classified document."""

    bluf = data.get('bluf', 'Multi-agent psychological analysis reveals divergent national interests.')
    confidence = data.get('overall_risk', 'MEDIUM')
    key_insights = data.get('key_insights', [])
    timestamp = datetime.now().strftime("%d %B %Y")

    insights_html = ""
    for i, insight in enumerate(key_insights, 1):
        insights_html += f'<div style="margin-bottom: 8px;"><span style="font-weight: bold;">{i}.</span> {insight}</div>'

    html = f"""
    <div style="background: #fffefa; border: 2px solid #1a1a1a; padding: 28px;
                font-family: 'Courier Prime', monospace;">

        <!-- BLUF Section -->
        <div style="margin-bottom: 28px;">
            <span style="font-size: 11px; font-weight: bold; letter-spacing: 3px;
                         text-decoration: underline; text-underline-offset: 4px; display: block; margin-bottom: 16px;">
                BOTTOM LINE UP FRONT (BLUF)
            </span>
            <p style="font-size: 13px; line-height: 2;">
                {bluf}
            </p>
        </div>

        <!-- Key Insights -->
        <div style="margin-bottom: 28px; padding: 16px; background: #f5f2e8; border: 1px solid #ccc;">
            <span style="font-size: 10px; font-weight: bold; letter-spacing: 2px; display: block; margin-bottom: 12px;">
                KEY INTELLIGENCE FINDINGS:
            </span>
            <div style="font-size: 12px; line-height: 1.8;">
                {insights_html if insights_html else '<em style="color: #888;">No specific findings recorded.</em>'}
            </div>
        </div>

        <!-- Confidence Assessment -->
        <div style="margin-bottom: 28px; text-align: center; padding: 12px; border: 1px solid #1a1a1a;">
            <span style="font-size: 10px; letter-spacing: 2px; color: #666;">ASSESSMENT CONFIDENCE:</span>
            <span style="font-size: 14px; font-weight: bold; letter-spacing: 2px; margin-left: 12px;
                         color: {'#006400' if confidence == 'Low' else '#8B4513' if confidence == 'Medium' else '#8b0000'};">
                {confidence}
            </span>
        </div>

        <!-- Signature Line -->
        <div style="display: flex; justify-content: space-between; align-items: flex-end;
                    padding-top: 20px; border-top: 1px dashed #ccc;">
            <div style="display: flex; align-items: flex-end; gap: 8px;">
                <span style="font-size: 18px; font-weight: bold;">X</span>
                <div>
                    <div style="border-bottom: 1px solid #1a1a1a; width: 200px; padding-bottom: 6px;"></div>
                    <span style="font-size: 9px; color: #888; letter-spacing: 2px;">ANALYZING OFFICER</span>
                </div>
            </div>
            <div style="text-align: right;">
                <span style="font-size: 9px; color: #888; letter-spacing: 2px; display: block; margin-bottom: 4px;">DATE</span>
                <span style="font-size: 12px; border-bottom: 1px solid #1a1a1a; padding-bottom: 4px;">{timestamp}</span>
            </div>
        </div>
    </div>
    """
    return html


def process_crisis(crisis_text: str, state: dict) -> tuple:
    """Process crisis through backend API."""
    global last_crisis_response

    if not crisis_text or not crisis_text.strip():
        empty = "<div style='padding: 40px; text-align: center; color: #888; font-style: italic;'>Enter a crisis scenario above to begin analysis.</div>"
        return empty, empty, empty, empty, "Awaiting input...", {}

    try:
        response = requests.post(
            f"{API_URL}/api/process-crisis",
            json={"crisis": crisis_text.strip()},
            headers={"Content-Type": "application/json"},
            timeout=120
        )

        if response.status_code != 200:
            error = f"<div style='padding: 20px; border: 2px solid #8b0000; color: #8b0000;'>API Error: {response.status_code}</div>"
            return error, error, error, error, f"Error: {response.status_code}", {}

        data = response.json()
        agents = data.get('agents', {})

        # Store response for voice synthesis
        last_crisis_response = agents

        roosevelt = format_agent_dossier('roosevelt', agents.get('roosevelt'))
        gandhi = format_agent_dossier('gandhi', agents.get('gandhi'))
        putin = format_agent_dossier('putin', agents.get('putin'))
        summary = format_executive_summary(data)

        return roosevelt, gandhi, putin, summary, "Analysis complete", agents

    except requests.exceptions.Timeout:
        error = "<div style='padding: 20px; border: 2px solid #8B4513; color: #8B4513;'>Request timed out. Please try again.</div>"
        return error, error, error, error, "Timeout", {}
    except requests.exceptions.ConnectionError:
        error = f"<div style='padding: 20px; border: 2px solid #8b0000; color: #8b0000;'>Cannot connect to API at {API_URL}</div>"
        return error, error, error, error, "Connection failed", {}
    except Exception as e:
        error = f"<div style='padding: 20px; border: 2px solid #8b0000; color: #8b0000;'>Error: {str(e)}</div>"
        return error, error, error, error, f"Error: {str(e)}", {}


def synthesize_voice(agent: str, state: dict) -> str:
    """Synthesize voice for agent's public response."""

    if not state or agent not in state:
        return None

    agent_data = state.get(agent, {})
    text = agent_data.get('public_response', '')

    if not text or text == 'Awaiting analysis...':
        return None

    try:
        response = requests.post(
            f"{API_URL}/api/synthesize-voice",
            json={"text": text, "agent": agent},
            headers={"Content-Type": "application/json"},
            timeout=60
        )

        if response.status_code != 200:
            return None

        # Save audio to temp file
        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as f:
            f.write(response.content)
            return f.name

    except Exception as e:
        print(f"Voice synthesis error: {e}")
        return None


def analyze_document(document_text: str) -> tuple:
    """Analyze document through backend API."""

    if not document_text or not document_text.strip():
        empty = "<div style='padding: 40px; text-align: center; color: #888; font-style: italic;'>Paste document text above to begin analysis.</div>"
        return empty, empty, empty, "Awaiting document..."

    try:
        response = requests.post(
            f"{API_URL}/api/analyze-document",
            json={"documentText": document_text.strip(), "filename": "document.txt"},
            headers={"Content-Type": "application/json"},
            timeout=120
        )

        if response.status_code != 200:
            error = f"<div style='padding: 20px; border: 2px solid #8b0000; color: #8b0000;'>API Error: {response.status_code}</div>"
            return error, error, error, f"Error: {response.status_code}"

        data = response.json()
        agents = data.get('agents', {})

        roosevelt = format_document_dossier('roosevelt', agents.get('roosevelt'))
        gandhi = format_document_dossier('gandhi', agents.get('gandhi'))
        putin = format_document_dossier('putin', agents.get('putin'))

        return roosevelt, gandhi, putin, "Document analysis complete"

    except Exception as e:
        error = f"<div style='padding: 20px; border: 2px solid #8b0000; color: #8b0000;'>Error: {str(e)}</div>"
        return error, error, error, f"Error: {str(e)}"


def check_api_health() -> str:
    try:
        response = requests.get(f"{API_URL}/api/health", timeout=5)
        if response.status_code == 200:
            return f"System Online | {API_URL}"
        return f"API Error: {response.status_code}"
    except:
        return f"Offline | {API_URL}"


# ============================================================================
# GRADIO INTERFACE
# ============================================================================

with gr.Blocks(title="AdversaryIQ - Intelligence Dossier", css=DOSSIER_CSS) as app:

    # State for storing response data
    response_state = gr.State({})

    # Header with TOP SECRET stamp
    gr.HTML("""
        <div style="display: flex; justify-content: space-between; align-items: flex-start;
                    padding: 24px 0; border-bottom: 2px solid #1a1a1a; background: #faf7f0;
                    font-family: 'Courier Prime', monospace; position: relative; margin-bottom: 20px;">

            <!-- TOP SECRET Stamp -->
            <div style="position: absolute; top: 10px; left: 0; padding: 4px 14px;
                        border: 3px solid #8b0000; color: #8b0000;
                        font-family: 'Special Elite', Impact, sans-serif; font-size: 13px;
                        font-weight: bold; letter-spacing: 3px; background: rgba(255,255,255,0.8);
                        transform: rotate(-12deg);">
                TOP SECRET
            </div>

            <div style="margin-left: 20px; margin-top: 30px;">
                <h1 style="font-size: 32px; font-weight: bold; letter-spacing: 4px; margin: 0;
                           font-family: 'Special Elite', 'Courier New', monospace;">
                    ADVERSARY<span style="color: #8b0000;">IQ</span>
                </h1>
                <p style="font-size: 11px; letter-spacing: 3px; color: #666; margin-top: 4px;">
                    MULTI-AGENT PSYCHOLOGICAL INTELLIGENCE SYSTEM
                </p>
            </div>

            <div style="text-align: right; margin-right: 20px;">
                <div style="margin-bottom: 8px;">
                    <span style="display: block; font-size: 9px; color: #888; letter-spacing: 2px;">SYSTEM ID</span>
                    <span style="font-size: 14px; font-weight: bold; letter-spacing: 2px;">AIQ-DEMO</span>
                </div>
                <div>
                    <span style="display: block; font-size: 9px; color: #888; letter-spacing: 2px;">STATUS</span>
                    <span style="font-size: 14px; font-weight: bold; letter-spacing: 2px; color: #006400;">OPERATIONAL</span>
                </div>
            </div>
        </div>
    """)

    # Classification Banner
    gr.HTML("""
        <div style="background: #8b0000; padding: 10px; text-align: center; margin-bottom: 30px;">
            <span style="color: #fff; font-size: 11px; font-weight: bold; letter-spacing: 6px;
                         font-family: 'Courier Prime', monospace;">
                FOR OFFICIAL USE ONLY — AUTHORIZED PERSONNEL ONLY
            </span>
        </div>
    """)

    # Main Tabs
    with gr.Tabs():

        # ===================== CRISIS ANALYSIS TAB =====================
        with gr.Tab("I. CRISIS ANALYSIS"):

            gr.HTML("""
                <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 20px;
                            padding-bottom: 10px; border-bottom: 1px solid #1a1a1a;
                            font-family: 'Courier Prime', monospace;">
                    <span style="font-size: 14px; font-weight: bold;">I.</span>
                    <span style="font-size: 13px; font-weight: bold; letter-spacing: 3px;">CRISIS SCENARIO INPUT</span>
                </div>
            """)

            crisis_input = gr.Textbox(
                label="",
                placeholder="Enter diplomatic crisis scenario for multi-agent psychological analysis...",
                lines=5,
                elem_classes=["dossier-textarea"]
            )

            gr.HTML("""
                <div style="font-size: 10px; color: #888; letter-spacing: 1px; margin: 8px 0 12px 0;
                            font-family: 'Courier Prime', monospace;">
                    EXAMPLE SCENARIOS (click to load):
                </div>
            """)

            gr.Examples(
                examples=[
                    ["North Korea establishes a new forward military base just 12 kilometers from the South Korean border, deploying artillery systems capable of striking Seoul within minutes."],
                    ["Chinese naval forces begin encircling Taiwan with a maritime blockade, intercepting commercial shipping and declaring a 'special military exercise zone' around the island."],
                    ["Your neighbor's golden retriever has been spotted relieving itself in the HOA president's award-winning rose garden, and security camera footage has gone viral on the community Facebook group."],
                ],
                inputs=crisis_input,
                label=""
            )

            with gr.Row():
                analyze_btn = gr.Button("PROCESS INTELLIGENCE", variant="primary")
                clear_btn = gr.Button("CLEAR FORM")

            status_text = gr.Textbox(label="SYSTEM STATUS", value=check_api_health(), interactive=False)

            # Section II: Agent Analysis
            gr.HTML("""
                <div style="display: flex; align-items: center; gap: 12px; margin: 30px 0 20px 0;
                            padding-bottom: 10px; border-bottom: 1px solid #1a1a1a;
                            font-family: 'Courier Prime', monospace;">
                    <span style="font-size: 14px; font-weight: bold;">II.</span>
                    <span style="font-size: 13px; font-weight: bold; letter-spacing: 3px;">AGENT ANALYSIS</span>
                    <span style="margin-left: auto; padding: 3px 10px; border: 2px solid #8b0000;
                                 color: #8b0000; font-size: 9px; font-weight: bold; letter-spacing: 2px;
                                 transform: rotate(-2deg);">CONFIDENTIAL</span>
                </div>
            """)

            with gr.Tabs():
                with gr.Tab("ROOSEVELT"):
                    crisis_roosevelt = gr.HTML(value="<div style='padding: 40px; text-align: center; color: #888; font-style: italic;'>Enter a crisis scenario above to begin analysis.</div>")
                    with gr.Row():
                        voice_roosevelt_btn = gr.Button("🔊 GENERATE VOICE", size="sm", elem_classes=["voice-btn"])
                    audio_roosevelt = gr.Audio(label="Voice Synthesis", visible=True, interactive=False)

                with gr.Tab("GANDHI"):
                    crisis_gandhi = gr.HTML(value="<div style='padding: 40px; text-align: center; color: #888; font-style: italic;'>Enter a crisis scenario above to begin analysis.</div>")
                    with gr.Row():
                        voice_gandhi_btn = gr.Button("🔊 GENERATE VOICE", size="sm", elem_classes=["voice-btn"])
                    audio_gandhi = gr.Audio(label="Voice Synthesis", visible=True, interactive=False)

                with gr.Tab("PUTIN"):
                    crisis_putin = gr.HTML(value="<div style='padding: 40px; text-align: center; color: #888; font-style: italic;'>Enter a crisis scenario above to begin analysis.</div>")
                    with gr.Row():
                        voice_putin_btn = gr.Button("🔊 GENERATE VOICE", size="sm", elem_classes=["voice-btn"])
                    audio_putin = gr.Audio(label="Voice Synthesis", visible=True, interactive=False)

            # Section III: Executive Summary
            gr.HTML("""
                <div style="display: flex; align-items: center; gap: 12px; margin: 30px 0 20px 0;
                            padding-bottom: 10px; border-bottom: 1px solid #1a1a1a;
                            font-family: 'Courier Prime', monospace;">
                    <span style="font-size: 14px; font-weight: bold;">III.</span>
                    <span style="font-size: 13px; font-weight: bold; letter-spacing: 3px;">EXECUTIVE SUMMARY</span>
                </div>
            """)

            crisis_summary = gr.HTML(value="<div style='padding: 40px; text-align: center; color: #888; font-style: italic;'>Submit a crisis scenario to generate executive intelligence summary.</div>")

        # ===================== DOCUMENT ANALYSIS TAB =====================
        with gr.Tab("II. DOCUMENT ANALYSIS"):

            gr.HTML("""
                <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 20px;
                            padding-bottom: 10px; border-bottom: 1px solid #1a1a1a;
                            font-family: 'Courier Prime', monospace;">
                    <span style="font-size: 14px; font-weight: bold;">I.</span>
                    <span style="font-size: 13px; font-weight: bold; letter-spacing: 3px;">DOCUMENT SUBMISSION</span>
                </div>
            """)

            doc_input = gr.Textbox(
                label="",
                placeholder="Paste diplomatic document, treaty, communique, or proposal text for psychological subtext analysis...",
                lines=8
            )

            gr.HTML("""
                <div style="font-size: 10px; color: #888; letter-spacing: 1px; margin: 8px 0 12px 0;
                            font-family: 'Courier Prime', monospace;">
                    EXAMPLE DOCUMENTS (click to load):
                </div>
            """)

            gr.Examples(
                examples=[
                    ["We remain fully committed to peaceful dialogue and diplomatic resolution of all outstanding issues. However, we must be clear that our nation reserves every right and option to defend our sovereignty and protect our citizens from external threats. We call upon all parties to exercise restraint."],
                    ["The Ministry of Foreign Affairs wishes to express its deep concern regarding recent developments in the region. While we value our longstanding partnership and shared interests, we cannot remain silent when fundamental principles of international law are being challenged."],
                    ["Dear HOA Board Members, I am writing to formally dispute the citation issued on March 15th regarding alleged pet policy violations. My golden retriever, Biscuit, is a certified emotional support animal and therefore exempt from Section 4.2.1 of the community bylaws."],
                ],
                inputs=doc_input,
                label=""
            )

            with gr.Row():
                analyze_doc_btn = gr.Button("ANALYZE DOCUMENT", variant="primary")
                clear_doc_btn = gr.Button("CLEAR")

            doc_status = gr.Textbox(label="SYSTEM STATUS", value=check_api_health(), interactive=False)

            gr.HTML("""
                <div style="display: flex; align-items: center; gap: 12px; margin: 30px 0 20px 0;
                            padding-bottom: 10px; border-bottom: 1px solid #1a1a1a;
                            font-family: 'Courier Prime', monospace;">
                    <span style="font-size: 14px; font-weight: bold;">II.</span>
                    <span style="font-size: 13px; font-weight: bold; letter-spacing: 3px;">PSYCHOLOGICAL SUBTEXT ANALYSIS</span>
                </div>
            """)

            with gr.Tabs():
                with gr.Tab("ROOSEVELT"):
                    doc_roosevelt = gr.HTML(value="<div style='padding: 40px; text-align: center; color: #888; font-style: italic;'>Paste a document above to begin analysis.</div>")
                with gr.Tab("GANDHI"):
                    doc_gandhi = gr.HTML(value="<div style='padding: 40px; text-align: center; color: #888; font-style: italic;'>Paste a document above to begin analysis.</div>")
                with gr.Tab("PUTIN"):
                    doc_putin = gr.HTML(value="<div style='padding: 40px; text-align: center; color: #888; font-style: italic;'>Paste a document above to begin analysis.</div>")

    # Footer
    gr.HTML("""
        <div style="text-align: center; padding: 20px; border-top: 1px solid #ccc; margin-top: 40px;
                    background: #faf7f0; font-family: 'Courier Prime', monospace;">
            <p style="font-size: 9px; letter-spacing: 2px; color: #888;">
                UNAUTHORIZED DISCLOSURE SUBJECT TO ADMINISTRATIVE AND CRIMINAL SANCTIONS
                <br><br>
                AdversaryIQ v1.0 — Psychological profiles are simplified models for demonstration purposes only
            </p>
        </div>
    """)

    # ===================== EVENT HANDLERS =====================

    analyze_btn.click(
        fn=process_crisis,
        inputs=[crisis_input, response_state],
        outputs=[crisis_roosevelt, crisis_gandhi, crisis_putin, crisis_summary, status_text, response_state]
    )

    clear_btn.click(
        fn=lambda: ("",
                    "<div style='padding: 40px; text-align: center; color: #888; font-style: italic;'>Enter a crisis scenario above to begin analysis.</div>",
                    "<div style='padding: 40px; text-align: center; color: #888; font-style: italic;'>Enter a crisis scenario above to begin analysis.</div>",
                    "<div style='padding: 40px; text-align: center; color: #888; font-style: italic;'>Enter a crisis scenario above to begin analysis.</div>",
                    "<div style='padding: 40px; text-align: center; color: #888; font-style: italic;'>Submit a crisis scenario to generate executive intelligence summary.</div>",
                    check_api_health(),
                    {},
                    None, None, None),
        inputs=[],
        outputs=[crisis_input, crisis_roosevelt, crisis_gandhi, crisis_putin, crisis_summary, status_text, response_state, audio_roosevelt, audio_gandhi, audio_putin]
    )

    # Voice synthesis handlers
    voice_roosevelt_btn.click(
        fn=lambda state: synthesize_voice("roosevelt", state),
        inputs=[response_state],
        outputs=[audio_roosevelt]
    )

    voice_gandhi_btn.click(
        fn=lambda state: synthesize_voice("gandhi", state),
        inputs=[response_state],
        outputs=[audio_gandhi]
    )

    voice_putin_btn.click(
        fn=lambda state: synthesize_voice("putin", state),
        inputs=[response_state],
        outputs=[audio_putin]
    )

    analyze_doc_btn.click(
        fn=analyze_document,
        inputs=[doc_input],
        outputs=[doc_roosevelt, doc_gandhi, doc_putin, doc_status]
    )

    clear_doc_btn.click(
        fn=lambda: ("",
                    "<div style='padding: 40px; text-align: center; color: #888; font-style: italic;'>Paste a document above to begin analysis.</div>",
                    "<div style='padding: 40px; text-align: center; color: #888; font-style: italic;'>Paste a document above to begin analysis.</div>",
                    "<div style='padding: 40px; text-align: center; color: #888; font-style: italic;'>Paste a document above to begin analysis.</div>",
                    check_api_health()),
        inputs=[],
        outputs=[doc_input, doc_roosevelt, doc_gandhi, doc_putin, doc_status]
    )


if __name__ == "__main__":
    app.launch(server_name="0.0.0.0", server_port=7860, share=False)
