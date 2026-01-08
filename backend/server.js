const express = require('express');
const cors = require('cors');
const OpenAI = require('openai');
const { ElevenLabsClient } = require('@elevenlabs/elevenlabs-js');
require('dotenv').config();

const app = express();
const PORT = process.env.PORT || 3001;

// Initialize OpenAI
const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY
});

// Initialize ElevenLabs
const elevenlabs = new ElevenLabsClient({
  apiKey: process.env.ELEVENLABS_API_KEY
});

app.use(cors());
app.use(express.json());

// Load real personality profiles from JSON files
const fs = require('fs');
const path = require('path');

// Load JSON files
const rooseveltProfile = JSON.parse(fs.readFileSync(path.join(__dirname, 'data/personalities/roosevelt_final_profile.json'), 'utf8'));
const rooseveltBeliefs = JSON.parse(fs.readFileSync(path.join(__dirname, 'data/personalities/roosevelt_beliefs.json'), 'utf8'));
const gandhiProfile = JSON.parse(fs.readFileSync(path.join(__dirname, 'data/personalities/indira_final_profile.json'), 'utf8'));
const gandhiBeliefs = JSON.parse(fs.readFileSync(path.join(__dirname, 'data/personalities/indira_beliefs.json'), 'utf8'));
const putinProfile = JSON.parse(fs.readFileSync(path.join(__dirname, 'data/personalities/putin_final_profile.json'), 'utf8'));
const putinBeliefs = JSON.parse(fs.readFileSync(path.join(__dirname, 'data/personalities/putin_beliefs.json'), 'utf8'));

// Analyze documents through agent psychological frameworks
async function analyzeDocumentThroughAgent(leaderName, documentText, filename) {
  let profile, beliefs, name;
  
  // Select the right profile and beliefs
  switch(leaderName) {
    case 'roosevelt':
      profile = rooseveltProfile;
      beliefs = rooseveltBeliefs;
      name = "Theodore Roosevelt";
      break;
    case 'gandhi':
      profile = gandhiProfile;
      beliefs = gandhiBeliefs;
      name = "Indira Gandhi";
      break;
    case 'putin':
      profile = putinProfile;
      beliefs = putinBeliefs;
      name = "Vladimir Putin";
      break;
  }

  const systemPrompt = `You are ${name}. Analyze this diplomatic document through your psychological framework.

DOCUMENT: "${documentText}"

Based on your psychological profile, analyze what this document REALLY means:
- What are the hidden intentions behind the words?
- What psychological tactics do you see being used?
- How would you respond to this document?

Respond with a JSON object:
{
  "document_interpretation": "What this document really means from your perspective",
  "hidden_intentions": "What the author is actually trying to accomplish", 
  "psychological_tactics": "What manipulation or persuasion techniques you identify",
  "your_response": "How you would respond to this document",
  "authenticity_assessment": "Whether you believe this document is genuine or deceptive"
}

Stay completely in character based on your personality profile.`;

  try {
    const response = await openai.chat.completions.create({
      model: "gpt-4o-mini",
      messages: [
        { role: "system", content: systemPrompt },
        { role: "user", content: "Analyze this document through your psychological framework." }
      ],
      temperature: 0.7,
      max_tokens: 600
    });

    // Clean the response content to handle markdown code blocks
    let content = response.choices[0].message.content.trim();
    if (content.startsWith('```json')) {
      content = content.replace(/```json\n?/, '').replace(/\n?```$/, '');
    } else if (content.startsWith('```')) {
      content = content.replace(/```\n?/, '').replace(/\n?```$/, '');
    }

    return {
      name: name,
      ...JSON.parse(content)
    };

  } catch (error) {
    console.error(`Error analyzing document for ${name}:`, error);
    return {
      name: name,
      document_interpretation: "Unable to analyze document",
      hidden_intentions: "Analysis failed",
      psychological_tactics: "Could not identify tactics",
      your_response: "System error prevented analysis",
      authenticity_assessment: "Unable to assess"
    };
  }
}

// Create AI agents using real psychological profiles
async function createAgent(leaderName, crisis) {
  let profile, beliefs, name;
  
  // Select the right profile and beliefs
  switch(leaderName) {
    case 'roosevelt':
      profile = rooseveltProfile;
      beliefs = rooseveltBeliefs;
      name = "Theodore Roosevelt";
      break;
    case 'gandhi':
      profile = gandhiProfile;
      beliefs = gandhiBeliefs;
      name = "Indira Gandhi";
      break;
    case 'putin':
      profile = putinProfile;
      beliefs = putinBeliefs;
      name = "Vladimir Putin";
      break;
  }

  const systemPrompt = `You are ${name}.

PSYCHOLOGICAL PROFILE (from historical analysis):
Public OCEAN Scores: Openness=${profile.public_ocean_scores.openness}, Conscientiousness=${profile.public_ocean_scores.conscientiousness}, Extraversion=${profile.public_ocean_scores.extraversion}, Agreeableness=${profile.public_ocean_scores.agreeableness}, Neuroticism=${profile.public_ocean_scores.neuroticism}

Behavioral OCEAN Scores: Openness=${profile.behavioral_ocean_scores.openness}, Conscientiousness=${profile.behavioral_ocean_scores.conscientiousness}, Extraversion=${profile.behavioral_ocean_scores.extraversion}, Agreeableness=${profile.behavioral_ocean_scores.agreeableness}, Neuroticism=${profile.behavioral_ocean_scores.neuroticism}

CRISIS RESPONSE PARAMETERS:
- Crisis latency: ${profile.behavioral_parameters.crisis_latency_hours}
- Escalation ladder: ${profile.behavioral_parameters.escalation_ladder.join(' → ')}
- Scapegoat probability: ${profile.behavioral_parameters.scapegoat_probability_pct}%

CURRENT BELIEF STATE:
${Object.entries(beliefs.beliefs).map(([key, value]) => `- ${key}: ${value}`).join('\n')}

CONTRADICTION PATTERNS:
${profile.contradiction_patterns.join('\n')}

CONTEXTUAL SWITCHING RULES:
${profile.contextual_switching_rules.join('\n')}

PREDICTIVE FRAMEWORK for this type of crisis:
- Public approach: ${profile.predictive_framework.international_negotiation?.public || profile.predictive_framework.economic_pressure?.public}
- Private approach: ${profile.predictive_framework.international_negotiation?.private || profile.predictive_framework.economic_pressure?.private}

CRISIS SCENARIO: ${crisis}

Based on your complete psychological profile, belief state, and historical decision patterns, respond with a JSON object:
{
  "public_response": "Your public statement (using your communication style)",
  "private_actions": "Your behind-the-scenes moves (based on your behavioral patterns)",
  "psychological_reasoning": "Explain your decision process using your personality traits, escalation ladder position, and belief state",
  "escalation_risk": "Low/Medium/High (based on your escalation ladder)",
  "timeline": "When you would act (based on your crisis_latency_hours)",
  "escalation_phase": "Current position on your escalation ladder",
  "belief_impact": "How this crisis affects your belief state"
}

Stay completely true to your psychological profile and historical patterns.`;

  try {
    const response = await openai.chat.completions.create({
      model: "gpt-4o-mini",
      messages: [
        { role: "system", content: systemPrompt },
        { role: "user", content: "Process this crisis through your complete psychological framework and respond accordingly." }
      ],
      temperature: 0.7,
      max_tokens: 800
    });

    // Clean the response content to handle markdown code blocks
    let content = response.choices[0].message.content.trim();
    if (content.startsWith('```json')) {
      content = content.replace(/```json\n?/, '').replace(/\n?```$/, '');
    } else if (content.startsWith('```')) {
      content = content.replace(/```\n?/, '').replace(/\n?```$/, '');
    }

    return JSON.parse(content);
  } catch (error) {
    console.error(`Error creating agent for ${name}:`, error);
    return {
      public_response: "Processing error occurred",
      private_actions: "System unavailable", 
      psychological_reasoning: "Unable to process through personality matrix",
      escalation_risk: "Unknown",
      timeline: "System error",
      escalation_phase: "Error",
      belief_impact: "Unable to calculate"
    };
  }
}

// Main crisis analysis endpoint
app.post('/api/process-crisis', async (req, res) => {
  try {
    const { crisis } = req.body;
    
    if (!crisis) {
      return res.status(400).json({ error: 'Crisis scenario required' });
    }

    console.log('Processing crisis:', crisis);

    // Process crisis through all three agents simultaneously
    const [rooseveltResponse, gandhiResponse, putinResponse] = await Promise.all([
      createAgent('roosevelt', crisis),
      createAgent('gandhi', crisis),
      createAgent('putin', crisis)
    ]);

    // Create intelligence assessment
    const intelligenceAssessment = {
      scenario: crisis,
      timestamp: new Date().toISOString(),
      agents: {
        roosevelt: {
          name: "Theodore Roosevelt",
          ...rooseveltResponse,
          personality_notes: `Extraversion: ${rooseveltProfile.public_ocean_scores.extraversion}/10 → Bold public positioning`
        },
        gandhi: {
          name: "Indira Gandhi", 
          ...gandhiResponse,
          personality_notes: `Crisis latency: ${gandhiProfile.behavioral_parameters.crisis_latency_hours} → Strategic delay`
        },
        putin: {
          name: "Vladimir Putin",
          ...putinResponse,
          personality_notes: `Escalation pattern: ${putinProfile.behavioral_parameters.escalation_ladder[0]} → ${putinProfile.behavioral_parameters.escalation_ladder[1]}`
        }
      },
      overall_risk: calculateOverallRisk([rooseveltResponse, gandhiResponse, putinResponse]),
      key_insights: generateKeyInsights([rooseveltResponse, gandhiResponse, putinResponse]),
      bluf: generateBLUF([rooseveltResponse, gandhiResponse, putinResponse], crisis)
    };

    res.json(intelligenceAssessment);

  } catch (error) {
    console.error('Crisis processing error:', error);
    res.status(500).json({ 
      error: 'Intelligence processing failed',
      details: error.message 
    });
  }
});

// Document analysis endpoint
app.post('/api/analyze-document', async (req, res) => {
  try {
    const { documentText, filename } = req.body;
    
    if (!documentText) {
      return res.status(400).json({ error: 'Document text required' });
    }

    console.log('Analyzing document:', filename);

    // Process document through all three agents for psychological interpretation
    const [rooseveltAnalysis, gandhiAnalysis, putinAnalysis] = await Promise.all([
      analyzeDocumentThroughAgent('roosevelt', documentText, filename),
      analyzeDocumentThroughAgent('gandhi', documentText, filename),
      analyzeDocumentThroughAgent('putin', documentText, filename)
    ]);

    const documentAnalysis = {
      document: filename,
      timestamp: new Date().toISOString(),
      agents: {
        roosevelt: rooseveltAnalysis,
        gandhi: gandhiAnalysis,
        putin: putinAnalysis
      }
    };

    res.json(documentAnalysis);

  } catch (error) {
    console.error('Document analysis error:', error);
    res.status(500).json({ 
      error: 'Document analysis failed',
      details: error.message 
    });
  }
});

// Voice synthesis endpoint
app.post('/api/synthesize-voice', async (req, res) => {
  try {
    const { text, agent } = req.body;
    
    if (!text || !agent) {
      return res.status(400).json({ error: 'Text and agent required' });
    }

    console.log(`Synthesizing voice for ${agent}:`, text.substring(0, 50) + '...');

    // Voice IDs for authentic historical figures
    let voiceId;
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
      default:
        voiceId = "zkXpoOeAWrFgfuIRi0yD";
    }

    // DEBUG: Log which voice ID is being used
    console.log(`Using voice ID for ${agent}: ${voiceId}`);
    
    const audio = await elevenlabs.textToSpeech.convert(voiceId, {
      text: text,
      model_id: "eleven_multilingual_v2"
    });

    console.log('Audio type:', typeof audio);

    // Convert ReadableStream to Buffer
    const chunks = [];
    const reader = audio.getReader();
    while (true) {
      const { done, value } = await reader.read();
      if (done) break;
      chunks.push(value);
    }
    const audioBuffer = Buffer.concat(chunks);

    res.setHeader('Content-Type', 'audio/mpeg');
    res.send(audioBuffer);

  } catch (error) {
    console.error('Voice synthesis error:', error);
    res.status(500).json({ error: 'Voice synthesis failed', details: error.message });
  }
});

// Helper functions
function calculateOverallRisk(responses) {
  const riskLevels = responses.map(r => r.escalation_risk);
  const highRisk = riskLevels.filter(r => r === 'High').length;
  const mediumRisk = riskLevels.filter(r => r === 'Medium').length;
  
  if (highRisk >= 2) return 'High';
  if (highRisk >= 1 || mediumRisk >= 2) return 'Medium';
  return 'Low';
}

function generateKeyInsights(responses) {
  return [
    `Response timeline variance: ${responses.map(r => r.timeline).join(' vs ')}`,
    `Escalation risk distribution: ${responses.map(r => r.escalation_risk).join(', ')}`,
    `Roosevelt favors ${responses[0].escalation_phase?.toLowerCase() || 'measured'} approach`,
    `Gandhi prioritizes ${responses[1].timeline?.includes('Immediate') ? 'rapid response' : 'deliberate action'}`,
    `Putin calculates ${responses[2].escalation_risk === 'High' ? 'aggressive positioning' : 'strategic patience'}`
  ];
}

function generateBLUF(responses, scenario) {
  const riskLevel = calculateOverallRisk(responses);
  const timelines = responses.map(r => r.timeline);
  const hasImmediateResponse = timelines.some(t => t?.includes('Immediate'));

  let bluf = `Multi-agent psychological analysis of "${scenario.substring(0, 50)}${scenario.length > 50 ? '...' : ''}" reveals `;

  if (riskLevel === 'High') {
    bluf += 'significant escalation potential with divergent national interests. ';
  } else if (riskLevel === 'Medium') {
    bluf += 'moderate tensions with varying strategic approaches across leadership profiles. ';
  } else {
    bluf += 'manageable diplomatic friction with opportunities for de-escalation. ';
  }

  if (hasImmediateResponse) {
    bluf += 'At least one actor is likely to respond within 24 hours, creating pressure for rapid decision-making. ';
  }

  bluf += `Roosevelt emphasizes ${responses[0].public_response?.substring(0, 80) || 'principled engagement'}... `;
  bluf += `Gandhi calculates ${responses[1].public_response?.substring(0, 80) || 'strategic positioning'}... `;
  bluf += `Putin prioritizes ${responses[2].public_response?.substring(0, 80) || 'leverage maximization'}...`;

  return bluf;
}

// Health check endpoint
app.get('/api/health', (req, res) => {
  res.json({ 
    status: 'operational', 
    message: 'AdversaryIQ Intelligence Engine Online',
    timestamp: new Date().toISOString()
  });
});

app.listen(PORT, () => {
  console.log(`🧠 AdversaryIQ Intelligence Engine running on port ${PORT}`);
  console.log(`🎯 Ready for crisis analysis`);
  console.log(`🔊 Voice synthesis enabled with authentic Roosevelt voice`);
});