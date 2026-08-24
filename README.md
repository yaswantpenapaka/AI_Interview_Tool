# 🎯 AI/ML Interview Coach

A comprehensive technical interview preparation tool powered by AI. Conduct realistic 5-question interviews tailored to your target role, company, and experience level, then receive an evidence-based scorecard with detailed feedback.

## 🚀 Features

- **Adaptive Interviews** — Tailored questions based on your profile, experience, and previous answers
- **Evidence-Based Scoring** — Structured evaluation across 5 key criteria with transparent scoring
- **Realistic Scenarios** — Interviews matched to your target role, company, and experience level
- **Streaming Responses** — Real-time AI responses for a natural conversation flow
- **Downloadable Reports** — Get Markdown scorecards with detailed feedback and actionable next steps
- **Smart Error Recovery** — Graceful handling of API failures without losing your progress

## 🏗️ Project Structure

The application is organized into feature-based modules for easy navigation and maintenance:

```
ai_ml_interview_coach/
├── app.py                 # Main entry point with routing
├── config.py              # Configuration and constants
│
├── profile/               # Candidate profile management
│   ├── models.py         # Profile data structures
│   └── view.py           # Setup screen UI
│
├── interview/            # Interview conduct
│   ├── prompts.py        # Interview system prompts
│   ├── service.py        # Question generation logic
│   └── view.py           # Interview UI and interaction
│
├── evaluation/           # Assessment and scoring
│   ├── prompts.py        # Evaluation prompts
│   ├── service.py        # Feedback generation
│   ├── validator.py      # Response validation
│   └── view.py           # Scorecard UI
│
├── reports/              # Report generation
│   └── markdown.py       # Markdown report builder
│
├── ai/                   # LLM integration
│   ├── client.py         # API client setup
│   └── streaming.py      # Streaming response handling
│
├── shared/               # Shared utilities
│   ├── session.py        # Session state management
│   └── styles.py         # UI styling and layout
│
├── .streamlit/
│   └── secrets.toml       # API credentials (not in git)
│
└── requirements.txt       # Python dependencies
```

## 🎓 How It Works

### 1. **Setup Phase**
Provide your candidate profile:
- Name and experience level
- Target position and company
- Relevant experience and technical skills
- The interview structure is customized based on this information

### 2. **Interview Phase**
A 5-question technical interview:
- Real-time questions tailored to your answers
- Progressive difficulty that adapts to your responses
- Up to 1,500 characters per answer
- Professional, neutral interviewer style

### 3. **Evaluation Phase**
Receive an evidence-based scorecard:
- **Overall Score** — Averaged from 5 evaluation criteria
- **Interview Signal** — "Strong signal", "Promising", "Needs more evidence", or "Not ready yet"
- **Detailed Scorecard** — Evidence-backed scoring for:
  - Technical Accuracy
  - Problem Solving
  - Practical Engineering Judgment
  - Communication
  - Role Alignment
- **Actionable Feedback** — Specific strengths, improvements, and next steps
- **Downloadable Report** — Markdown file with your complete scorecard

## 🔧 Technical Stack

- **Frontend** — [Streamlit](https://streamlit.io/) for interactive web interface
- **LLM** — [Groq API](https://groq.com/) via OpenAI-compatible SDK for fast inference
- **Python** — 3.13.1
- **Streaming** — Real-time response streaming for natural conversation flow

## 📋 Requirements

Create a `.streamlit/secrets.toml` file:

```toml
GROQ_API_KEY = "your_groq_api_key_here"
GROQ_MODEL = "openai/gpt-oss-120b"  # Optional, uses default if not set
```

Get your Groq API key from [console.groq.com](https://console.groq.com).

## 🚀 Getting Started

### Installation

```bash
pip install -r requirements.txt
```

### Running the App

```bash
streamlit run app.py
```

The app will open at `http://localhost:8501` by default.

## 📚 Code Organization

### Core Modules

**config.py**
- Interview settings (response limits, token counts)
- Interview options (positions, companies, experience levels)
- Model configuration

**shared/session.py**
- Session state initialization
- Default state values for interview flow

**shared/styles.py**
- UI styling and theming
- Header rendering

**ai/client.py**
- Groq API client initialization
- Cached client for efficient reuse

**ai/streaming.py**
- Streaming response parsing
- Text extraction from LLM responses

### Feature Modules

**profile/** — Candidate setup
- `models.py` — Profile data types
- `view.py` — Setup form and validation

**interview/** — Interview conduct
- `prompts.py` — System prompt for the interviewer
- `service.py` — Question generation and API calls
- `view.py` — Chat interface and interaction logic

**evaluation/** — Assessment
- `prompts.py` — Evaluation system prompt
- `service.py` — Feedback generation and JSON parsing
- `validator.py` — Scorecard validation and correction
- `view.py` — Scorecard display and report download

**reports/** — Output
- `markdown.py` — Markdown scorecard builder

## 🧪 How the Scoring Works

The evaluator uses a 5-criterion rubric:

| Criterion | Description |
|---|---|
| **Technical Accuracy** | Correctness of concepts, terminology, and implementation details |
| **Problem Solving** | Logical reasoning, diagnosis, and ability to break down problems |
| **Engineering Judgment** | Trade-offs in quality, scalability, reliability, and business impact |
| **Communication** | Clarity, organization, and ability to explain decisions |
| **Role Alignment** | Relevance and depth of evidence for the target position |

Each criterion is scored 1–10:
- **1–3** — Major gaps or very little evidence
- **4–6** — Partial understanding or inconsistent evidence
- **7–8** — Strong and relevant evidence
- **9–10** — Exceptional depth and practical judgment

The overall score is the arithmetic average of the five scores.

## 🛡️ Key Features in Depth

### Adaptive Interviews
The system prompt guides the interviewer to:
- Ask one question at a time
- Use previous answers to inform follow-ups
- Adapt difficulty to your experience level
- Probe vague claims with specific questions
- Avoid scoring or coaching during the interview

### Evidence-Based Evaluation
The evaluator is instructed to:
- Evaluate only what was demonstrated
- Explicitly note missing evidence
- Avoid inventing projects, skills, or results
- Ground all scores in specific transcript evidence

### Safety & Reliability
- **Error Recovery** — If an API call fails, your answers aren't lost
- **JSON Validation** — Scorecard validation catches malformed responses
- **Score Consistency** — System corrects any arithmetic inconsistencies
- **Transcript Limits** — Long interviews are safely truncated for evaluation

## 🔐 Security Notes

- API keys are stored in `.streamlit/secrets.toml` (add to `.gitignore`)
- Interview transcripts are sent to Groq for evaluation
- No data is permanently stored on the server
- Treat this tool as practice-only; real interviews require different prep

## 📊 Interview Signal Interpretation

- **Strong signal** — Excellent fit, clear evidence across all criteria
- **Promising** — Good potential, some areas need development
- **Needs more evidence** — Mixed signals, more practice recommended
- **Not ready yet** — Significant gaps, focus on preparation areas

## 🎯 Next Steps After Your Interview

Review the scorecard's recommendations:
1. **Strengths** — Build on what you're doing well
2. **Improvements** — Target specific areas for growth
3. **Next Steps** — Concrete actions for preparation

## 🤝 Contributing

This is a single-user interview coach. Modifications should maintain:
- Feature-based organization
- Separation of prompts, business logic, and UI
- Evidence-based evaluation principles

## 📝 License

This project is provided as-is for technical interview preparation.

## 🙋 FAQ

**Q: How long does the interview take?**  
A: Typically 10–15 minutes, depending on answer length and API response time.

**Q: Can I retake the interview?**  
A: Yes, just click "Start New Interview" after viewing your scorecard.

**Q: What if the API fails mid-interview?**  
A: Your answers are saved. If the interviewer request fails, you can resubmit your answer.

**Q: How accurate is the scoring?**  
A: Scores reflect only evidence from the transcript. The evaluator is instructed to avoid inventing skills or experience. Scores are most useful for identifying patterns, not as definitive measures.

**Q: Can I appeal my score?**  
A: Scores are based on what was demonstrated. Review the evidence section for each criterion to understand the reasoning.

---

Built with ❤️ for AI/ML interview preparation.
