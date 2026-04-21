# AssistiveOS Engine

**Open Source Disability & Robotics/Exoskeleton Assistance Engine**

Built with Python NiceGUI backend and standalone lightweight HTML raw number plugin.

## 🚀 Quick Start

```bash
# Install dependencies
pip install nicegui requests

# Run the engine
python assistive_os_engine.py
```

The application will be available at:
- **Main UI**: http://localhost:8080
- **Raw Numbers Plugin**: http://localhost:8080/plugin/raw-numbers

## 📋 Features

### Main Application (`/`)
- **Institution Dispatch Engine**: Ingest institution data and get automated gap analysis
- **Gap Profile Analysis**: 6-dimensional capacity assessment
  - Mobility Care Capacity
  - Neuro Rehab Capacity  
  - Device Integration Level
  - Funding Strength
  - Tech Readiness
  - Unmet Need Score
- **Deployment Package Generation**: Automated system configuration
  - Core modules selection
  - Integration points
  - Device layer support
  - Data layer streams
  - Onboarding path
- **Next Actions Prioritization**: Actionable recommendations with urgency levels
- **Automated Outreach Email**: Professional email draft ready to send
- **Export Bundle**: Download complete analysis as text bundle

### Raw Numbers Plugin (`/plugin/raw-numbers`)
Standalone lightweight widget for embedding key metrics:
- Unmet Need % 
- Priority Score %
- Tech Readiness %
- Funding Strength %

Perfect for embedding in existing dashboards or websites via iframe.

## 🏗️ Architecture

```
assistive_os_engine.py
├── Gap Analysis Engine (simulated LLM-based analysis)
├── Main UI (NiceGUI web interface)
│   ├── Input Form (institution data)
│   ├── Running View (progress logs)
│   └── Result View (analysis dashboard)
└── Raw Numbers Plugin (standalone widget)
```

## 🔧 Configuration

The engine uses a deterministic algorithm based on institution name hash to generate realistic analysis data. In production, you can integrate with:

- **Anthropic Claude API** for AI-powered analysis
- **Gmail MCP** for automated email sending
- Custom data sources for real-time metrics

## 📊 Sectors Supported

- Hospitals
- NGOs
- Rehabilitation Centers
- Universities
- Government Agencies
- Insurance Companies
- Private Companies

## 🎯 Focus Areas

- Mobility Rehabilitation
- Neuro Recovery
- Spinal Injury
- Stroke Recovery
- Pediatric Rehab
- Geriatric Care
- Sports Injury
- Prosthetics Integration
- Remote Patient Monitoring
- Clinical Trials
- Device Procurement
- Workforce Training

## 🌐 Deployment Models

- **Edge**: Local deployment for clinics
- **Cloud**: Centralized SaaS model
- **Hybrid**: Combined edge + cloud architecture
- **Clinic Edge + Cloud Hybrid**: Optimized for healthcare settings

## 📦 Export Bundle Contents

When you export an analysis, you receive:
- `README.md` - Summary document
- `gap_profile.json` - Detailed gap analysis
- `deployment_package.json` - System configuration
- `next_actions.json` - Prioritized action items
- `outreach_email.md` - Professional email draft
- `full_analysis.json` - Complete analysis data

## 🎨 Theme

Dark theme optimized for professional environments:
- Background: `#080c10`
- Surface: `#0d1117`
- Accent: `#00d4aa` (teal)
- Warning: `#f59e0b` (amber)
- Danger: `#ef4444` (red)
- Success: `#10b981` (green)

## 🔌 Embedding the Plugin

Use an iframe to embed the raw numbers plugin:

```html
<iframe 
  src="http://localhost:8080/plugin/raw-numbers" 
  width="420" 
  height="600"
  style="border: none; border-radius: 8px;"
></iframe>
```

## 📝 License

Open Source - Built for the assistive technology community

---

**NextAura × Qvrm** | AssistiveOS Global Dispatch Engine v1.0
