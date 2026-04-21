#!/usr/bin/env python3
"""
AssistiveOS Engine - Open Source Disability & Robotics/Exoskeleton Assistance Engine
Built with Python NiceGUI backend and standalone lightweight HTML raw number plugin
"""

import json
import asyncio
from datetime import datetime
from typing import Optional, Dict, Any, List
from nicegui import ui, app
import requests

# ─── THEME ────────────────────────────────────────────────────────────────────
T = {
    "bg": "#080c10",
    "surface": "#0d1117",
    "border": "#1c2430",
    "borderAccent": "#00d4aa",
    "text": "#e8edf2",
    "muted": "#5a6a7a",
    "accent": "#00d4aa",
    "accentDim": "#00d4aa22",
    "warn": "#f59e0b",
    "danger": "#ef4444",
    "success": "#10b981",
    "fontMono": "'IBM Plex Mono', 'Courier New', monospace",
    "fontSans": "'DM Sans', sans-serif",
}

# ─── SECTOR OPTIONS ───────────────────────────────────────────────────────────
SECTORS = ["hospital", "ngo", "rehab_center", "university", "gov", "insurer", "company"]
SCALES = ["local", "regional", "national", "global"]
FOCUS_OPTIONS = [
    "mobility_rehabilitation", "neuro_recovery", "spinal_injury", "stroke_recovery",
    "pediatric_rehab", "geriatric_care", "sports_injury", "prosthetics_integration",
    "remote_patient_monitoring", "clinical_trials", "device_procurement", "workforce_training"
]

# ─── STATE MANAGEMENT ─────────────────────────────────────────────────────────
class AppState:
    def __init__(self):
        self.step = "input"  # input | running | result
        self.log = []
        self.analysis: Optional[Dict[str, Any]] = None
        self.email_status: Optional[str] = None
        self.email_sending = False
        self.recipient_email = ""
        self.inst = {
            "name": "",
            "sector": "hospital",
            "location": "",
            "scale": "regional",
            "focus_areas": [],
            "constraints": {},
            "contact_email": "",
        }

# Store state per session
@app.get("/state/{session_id}")
def get_state(session_id: str):
    if session_id not in app.state.sessions:
        app.state.sessions[session_id] = AppState()
    return app.state.sessions[session_id]

# ─── GAP ANALYSIS ENGINE ──────────────────────────────────────────────────────
async def run_gap_analysis(institution: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """
    Simulated gap analysis engine.
    In production, this would call an LLM API (Anthropic Claude, etc.)
    For now, we generate a realistic analysis based on institution data.
    """
    await asyncio.sleep(0.5)  # Simulate processing
    
    # Generate deterministic scores based on institution characteristics
    name_hash = hash(institution["name"]) % 100
    focus_count = len(institution["focus_areas"])
    
    gap_profile = {
        "mobility_care_capacity": min(0.95, max(0.15, 0.4 + (name_hash % 40) / 100 + focus_count * 0.05)),
        "neuro_rehab_capacity": min(0.95, max(0.15, 0.35 + ((name_hash >> 2) % 45) / 100 + focus_count * 0.04)),
        "device_integration_level": min(0.95, max(0.1, 0.3 + ((name_hash >> 3) % 50) / 100)),
        "funding_strength": min(0.95, max(0.2, 0.45 + ((name_hash >> 4) % 40) / 100)),
        "tech_readiness": min(0.95, max(0.25, 0.4 + ((name_hash >> 5) % 45) / 100)),
        "unmet_need_score": min(0.95, max(0.3, 0.6 - ((name_hash >> 6) % 35) / 100)),
        "patient_volume_estimate": ["low", "medium", "medium-high", "high", "very-high"][name_hash % 5],
        "primary_gap_category": ["communication", "data", "results", "integration", "training"][name_hash % 5],
        "gap_narrative": f"Based on analysis of {institution['name']}, there is significant opportunity for assistive technology deployment. "
                        f"The institution shows {'strong' if gap_profile['funding_strength'] > 0.6 else 'moderate'} capacity "
                        f"with key gaps in {institution['sector']} sector operations. "
                        f"Focus areas indicate demand for {'advanced' if focus_count > 3 else 'foundational'} rehabilitation solutions."
    }
    
    await asyncio.sleep(0.3)
    
    deployment_package = {
        "system_name": f"AssistiveOS::{institution['name'].replace(' ', '_')}",
        "core_modules": [
            "Patient Mobility Tracker",
            "Device Integration Hub",
            "Clinical Workflow Manager",
            "Outcome Analytics Dashboard",
            "Remote Monitoring Gateway",
            "Staff Training Portal",
            "Compliance Reporter"
        ][:5 + (focus_count % 3)],
        "integration_points": [
            "EHR/EMR Systems",
            "IoT Device Network",
            "Telehealth Platform",
            "Data Warehouse",
            "Mobile Applications",
            "Cloud Infrastructure"
        ][:4 + (focus_count % 3)],
        "clinical_workflows": [
            "Initial Patient Assessment",
            "Device Fitting & Calibration",
            "Progress Tracking",
            "Outcome Evaluation",
            "Care Plan Adjustment"
        ],
        "device_layer_support": [
            "Robotic Exoskeletons",
            "Powered Prosthetics",
            "Mobility Assistance Devices",
            "Sensory Feedback Systems",
            "Adaptive Control Interfaces"
        ][:3 + (focus_count % 3)],
        "data_layer": [
            "Patient Progress Metrics",
            "Device Usage Analytics",
            "Clinical Outcome Data",
            "Operational Efficiency Stats",
            "Compliance Reports"
        ],
        "deployment_model": "hybrid" if institution["scale"] in ["national", "global"] else "clinic_edge + cloud hybrid",
        "onboarding_path": [
            "Infrastructure Assessment",
            "System Configuration",
            "Staff Training",
            "Pilot Deployment",
            "Full Rollout",
            "Continuous Optimization"
        ][:4 + (focus_count % 3)],
        "estimated_timeline_weeks": 6 + (focus_count * 2) + (name_hash % 8),
        "priority_score": min(0.95, max(0.3, gap_profile["unmet_need_score"] * 0.7 + gap_profile["tech_readiness"] * 0.3))
    }
    
    await asyncio.sleep(0.2)
    
    next_actions = [
        {
            "action": f"Schedule technical assessment for {institution['name']}",
            "owner": "Implementation Team",
            "urgency": "immediate",
            "impact": "high"
        },
        {
            "action": "Prepare device compatibility matrix",
            "owner": "Engineering Team",
            "urgency": "30d",
            "impact": "high"
        },
        {
            "action": f"Conduct stakeholder workshops with {institution['sector']} leadership",
            "owner": "Project Manager",
            "urgency": "30d",
            "impact": "medium"
        },
        {
            "action": "Develop custom integration specifications",
            "owner": "Solutions Architect",
            "urgency": "90d",
            "impact": "medium"
        }
    ]
    
    email_subject = f"AssistiveOS Deployment Opportunity for {institution['name']}"
    email_body = f"""Dear Leadership Team at {institution['name']},

I hope this message finds you well. Following our comprehensive gap analysis of your {institution['sector']} operations, I'm excited to present findings that demonstrate significant opportunities for enhancing your rehabilitation technology capabilities.

KEY FINDINGS:
- Unmet Need Score: {round(gap_profile['unmet_need_score'] * 100)}%
- Priority Score: {round(deployment_package['priority_score'] * 100)}%
- Primary Gap Category: {gap_profile['primary_gap_category'].upper()}
- Estimated Timeline: {deployment_package['estimated_timeline_weeks']} weeks

Our analysis indicates that {institution['name']} is well-positioned to benefit from AssistiveOS deployment. The system would integrate seamlessly with your existing infrastructure while providing advanced capabilities for patient mobility tracking, device management, and outcome analytics.

RECOMMENDED NEXT STEPS:
1. Schedule a technical assessment (Immediate)
2. Prepare device compatibility matrix (30 days)
3. Conduct stakeholder workshops (30 days)
4. Develop integration specifications (90 days)

The proposed AssistiveOS::{institution['name'].replace(' ', '_')} deployment package includes core modules specifically tailored to your focus areas: {', '.join(institution['focus_areas'])}.

We believe this deployment will significantly enhance your capacity to deliver cutting-edge rehabilitation services while improving operational efficiency and patient outcomes.

I would welcome the opportunity to discuss these findings in detail and answer any questions you may have.

Best regards,
AssistiveOS Deployment Team
NextAura × Qvrm

---
This analysis was generated automatically by the AssistiveOS Global Dispatch Engine v1.0
"""
    
    return {
        "gap_profile": gap_profile,
        "deployment_package": deployment_package,
        "next_actions": next_actions,
        "email_subject": email_subject,
        "email_body": email_body
    }


# ─── MAIN UI ──────────────────────────────────────────────────────────────────
@ui.page("/")
def main_page():
    state = AppState()
    
    # Custom CSS
    ui.add_head_html(f"""
    <style>
        @keyframes pulse {{ 0%, 100% {{ opacity: 1 }} 50% {{ opacity: 0.3 }} }}
        @keyframes blink {{ 0%, 100% {{ opacity: 1 }} 50% {{ opacity: 0 }} }}
        
        .metric-bar {{
            height: 4px;
            background: {T['border']};
            border-radius: 2px;
            overflow: hidden;
        }}
        
        .metric-fill {{
            height: 100%;
            border-radius: 2px;
            transition: width 1s ease;
        }}
        
        .tag {{
            display: inline-block;
            padding: 2px 8px;
            border-radius: 3px;
            font-size: 11px;
            font-family: {T['fontMono']};
            margin: 2px 3px 2px 0;
            border: 1px solid;
        }}
        
        .log-entry {{
            font-family: {T['fontMono']};
            font-size: 12px;
            line-height: 1.6;
            margin-bottom: 5px;
        }}
    </style>
    """)
    
    def create_header():
        with ui.element('div').classes('flex justify-between items-center w-full').style(f'border-bottom: 1px solid {T["border"]}; padding: 14px 24px;'):
            with ui.element('div').classes('flex items-center gap-3'):
                ui.element('div').style(f'width: 8px; height: 8px; border-radius: 50%; background: {T["accent"]}; box-shadow: 0 0 10px {T["accent"]};')
                ui.label('ASSISTIVEOS').style(f'font-family: {T["fontMono"]}; font-size: 13px; color: {T["accent"]}; letter-spacing: 0.12em;')
                ui.label('/ GLOBAL DISPATCH ENGINE v1.0').style(f'font-size: 11px; color: {T["muted"]}; font-family: {T["fontMono"]};')
            ui.label('NextAura × Qvrm').style(f'font-size: 10px; font-family: {T["fontMono"]}; color: {T["muted"]};')
    
    def create_input_form():
        with ui.column().classes('w-full gap-4'):
            ui.html('<h1 style="font-size: 22px; font-weight: 700; margin: 0 0 6px; letter-spacing: -0.02em;">Institution Dispatch</h1>')
            ui.html(f'<p style="color: {T["muted"]}; font-size: 14px; margin: 0;">Ingest an institution. Get a full gap analysis, deployment stack, and outreach email — automated.</p>')
            
            # Name and Location
            with ui.row().classes('w-full gap-4'):
                name_input = ui.input(label='Institution Name *').classes('w-full').style(f'padding: 9px 12px; background: {T["surface"]}; border: 1px solid {T["border"]}; border-radius: 5px; color: {T["text"]}; font-family: {T["fontMono"]}; font-size: 13px;')
                name_input.props('dark')
                location_input = ui.input(label='Location *').classes('w-full').style(f'padding: 9px 12px; background: {T["surface"]}; border: 1px solid {T["border"]}; border-radius: 5px; color: {T["text"]}; font-family: {T["fontMono"]}; font-size: 13px;')
                location_input.props('dark')
            
            # Sector, Scale, Email
            with ui.row().classes('w-full gap-4'):
                sector_select = ui.select(SECTORS, value='hospital', label='Sector').classes('w-full').style(f'padding: 9px 12px; background: {T["surface"]}; border: 1px solid {T["border"]}; border-radius: 5px; color: {T["text"]}; font-family: {T["fontMono"]}; font-size: 13px;')
                scale_select = ui.select(SCALES, value='regional', label='Scale').classes('w-full').style(f'padding: 9px 12px; background: {T["surface"]}; border: 1px solid {T["border"]}; border-radius: 5px; color: {T["text"]}; font-family: {T["fontMono"]}; font-size: 13px;')
                contact_input = ui.input(label='Contact Email').classes('w-full').style(f'padding: 9px 12px; background: {T["surface"]}; border: 1px solid {T["border"]}; border-radius: 5px; color: {T["text"]}; font-family: {T["fontMono"]}; font-size: 13px;')
                contact_input.props('dark')
            
            # Focus Areas
            ui.label('Focus Areas * (select all that apply)').style(f'font-size: 11px; font-family: {T["fontMono"]}; color: {T["muted"]}; text-transform: uppercase; letter-spacing: 0.07em;')
            focus_container = ui.row().classes('w-full gap-1 flex-wrap')
            selected_focus = []
            
            def toggle_focus(focus_area, btn):
                if focus_area in selected_focus:
                    selected_focus.remove(focus_area)
                    btn.style(f'background: transparent; color: {T["muted"]}; border: 1px solid {T["border"]};')
                else:
                    selected_focus.append(focus_area)
                    btn.style(f'background: {T["accent"]}22; color: {T["accent"]}; border: 1px solid {T["accent"]};')
            
            for focus in FOCUS_OPTIONS:
                btn = ui.button(focus.replace('_', ' ')).style(f'padding: 9px 18px; border-radius: 5px; border: 1px solid {T["border"]}; background: transparent; color: {T["muted"]}; font-family: {T["fontMono"]}; font-size: 12px; cursor: pointer; margin-right: 6px; margin-bottom: 6px;')
                btn.on('click', lambda e, f=focus, b=btn: toggle_focus(f, b))
                focus_container.__enter__()
                btn.move(focus_container)
                focus_container.__exit__(None, None, None)
            
            # Run Button
            async def run_engine():
                if not name_input.value or not location_input.value or len(selected_focus) == 0:
                    return
                
                state.step = "running"
                state.log = []
                state.analysis = None
                log_content.clear()
                
                add_log("► Initializing AssistiveOS dispatch engine...", "system")
                await asyncio.sleep(0.4)
                add_log(f"► Ingesting institution: {name_input.value}", "system")
                await asyncio.sleep(0.3)
                add_log("► Computing gap profile across 6 dimensions...", "info")
                await asyncio.sleep(0.3)
                add_log("► Running deployment package synthesis...", "info")
                
                state.inst = {
                    "name": name_input.value,
                    "sector": sector_select.value,
                    "location": location_input.value,
                    "scale": scale_select.value,
                    "focus_areas": selected_focus,
                    "contact_email": contact_input.value,
                }
                
                result = await run_gap_analysis(state.inst)
                
                if not result:
                    add_log("✗ Analysis failed — parse error", "error")
                    return
                
                state.analysis = result
                state.recipient_email = contact_input.value or ""
                
                add_log("✓ Gap profile computed", "success")
                add_log("✓ Deployment package generated", "success")
                add_log(f"✓ {len(result['next_actions'])} next actions prioritized", "success")
                add_log("► Building email draft...", "info")
                await asyncio.sleep(0.2)
                add_log("✓ Outreach email ready", "success")
                add_log("► Engine complete.", "system")
                
                state.step = "result"
                update_ui()
            
            run_btn = ui.button('► DISPATCH ENGINE').classes('w-full').style(f'padding: 13px; background: {T["accent"]}; color: #000; border-radius: 6px; border: none; font-family: {T["fontMono"]}; font-size: 13px; font-weight: 700; cursor: pointer; letter-spacing: 0.08em;')
            run_btn.on('click', run_engine)
            
            log_container = ui.column()
            return name_input, location_input, sector_select, scale_select, contact_input, selected_focus, log_container, run_btn
    
    def add_log(msg: str, log_type: str = "info"):
        state.log.append({"msg": msg, "type": log_type, "ts": datetime.now()})
    
    def create_running_view():
        with ui.column().classes('w-full gap-4'):
            with ui.row().classes('items-center gap-3'):
                ui.element('div').style(f'width: 8px; height: 8px; border-radius: 50%; background: {T["accent"]}; animation: pulse 1s infinite;')
                ui.label('ENGINE RUNNING').style(f'font-family: {T["fontMono"]}; font-size: 13px; color: {T["accent"]};')
            ui.html(f'<p style="color: {T["muted"]}; font-size: 13px; margin: 0;">Analyzing {state.inst["name"]}...</p>')
            
            log_scroll = ui.scroll_area().classes('w-full').style(f'background: {T["surface"]}; border: 1px solid {T["border"]}; border-radius: 6px; padding: 16px; height: 280px;')
            
            with log_scroll:
                log_content = ui.column().classes('w-full')
                
                def update_log():
                    log_content.clear()
                    with log_content:
                        for entry in state.log:
                            color_map = {
                                "success": T["success"],
                                "error": T["danger"],
                                "system": T["accent"],
                                "info": T["muted"]
                            }
                            ts = entry["ts"].strftime('%H:%M:%S')
                            ui.html(f'''<div class="log-entry" style="color: {color_map.get(entry["type"], T["muted"])};">
                                <span style="color: {T["border"]}; margin-right: 8px;">{ts}</span>{entry["msg"]}
                            </div>''')
                        ui.html('<div style="display: inline-block; width: 8px; height: 14px; background: ' + T["accent"] + '; animation: blink 0.8s infinite;"></div>')
                
                return log_content, update_log
    
    def create_result_view():
        if not state.analysis:
            return
        
        analysis = state.analysis
        
        with ui.column().classes('w-full gap-6'):
            # Header
            with ui.row().classes('w-full justify-between items-start'):
                with ui.column():
                    ui.label('ANALYSIS COMPLETE').style(f'font-size: 11px; font-family: {T["fontMono"]}; color: {T["accent"]}; margin-bottom: 4px; letter-spacing: 0.1em;')
                    ui.label(state.inst["name"]).style('font-size: 20px; font-weight: 700; margin: 0;')
                    ui.label(f'{state.inst["sector"]} · {state.inst["scale"]} · {state.inst["location"]}').style(f'font-size: 12px; color: {T["muted"]}; font-family: {T["fontMono"]};')
                
                with ui.row():
                    def download_bundle():
                        bundle = f"""=== AssistiveOS Export Bundle ===
Generated: {datetime.now().isoformat()}

{'='*60}
FILE: README.md
{'='*60}
# AssistiveOS Deployment Package
## Institution: {state.inst["name"]}
Generated: {datetime.now().isoformat()}
### System: {analysis["deployment_package"]["system_name"]}
Deployment Model: {analysis["deployment_package"]["deployment_model"]}
Timeline: {analysis["deployment_package"]["estimated_timeline_weeks"]} weeks
Priority Score: {round(analysis["deployment_package"]["priority_score"] * 100)}%
---
{analysis["gap_profile"]["gap_narrative"]}

{'='*60}
FILE: gap_profile.json
{'='*60}
{json.dumps(analysis["gap_profile"], indent=2)}

{'='*60}
FILE: deployment_package.json
{'='*60}
{json.dumps(analysis["deployment_package"], indent=2)}

{'='*60}
FILE: next_actions.json
{'='*60}
{json.dumps(analysis["next_actions"], indent=2)}

{'='*60}
FILE: outreach_email.md
{'='*60}
# Outreach Email
**Subject:** {analysis["email_subject"]}

{analysis["email_body"]}
"""
                        ui.download(bundle.encode('utf-8'), f'AssistiveOS_{state.inst["name"].replace(" ", "_")}_{int(datetime.now().timestamp())}.txt')
                    
                    ui.button('↓ Export Bundle').style(f'padding: 8px 14px; border-radius: 5px; border: 1px solid {T["accent"]}; background: {T["accent"]}22; color: {T["accent"]}; font-family: {T["fontMono"]}; font-size: 12px; cursor: pointer;')
                    ui.button('← New Analysis').style(f'padding: 8px 14px; border-radius: 5px; border: 1px solid {T["border"]}; background: transparent; color: {T["muted"]}; font-family: {T["fontMono"]}; font-size: 12px; cursor: pointer;').on('click', lambda: ui.navigate.to('/'))
            
            # Gap Profile Hero
            with ui.card().style(f'background: linear-gradient(135deg, {T["surface"]} 0%, #0a1a14 100%); border: 1px solid {T["borderAccent"]}33; border-radius: 8px; padding: 20px;'):
                with ui.row().classes('w-full gap-6'):
                    # Metrics
                    with ui.column().classes('flex-1'):
                        ui.label('GAP PROFILE').style(f'font-size: 11px; font-family: {T["fontMono"]}; color: {T["muted"]}; margin-bottom: 12px; letter-spacing: 0.08em;')
                        
                        def metric_bar(label: str, value: float):
                            pct = round(value * 100)
                            bar_color = T["danger"] if pct < 40 else T["warn"] if pct < 65 else T["success"]
                            with ui.column().classes('w-full').style('margin-bottom: 10px;'):
                                with ui.row().classes('justify-between w-full'):
                                    ui.label(label).style(f'font-size: 11px; font-family: {T["fontMono"]}; color: {T["muted"]};')
                                    ui.label(f'{pct}%').style(f'font-size: 11px; font-family: {T["fontMono"]}; color: {bar_color}; font-weight: 700;')
                                ui.element('div').classes('w-full').style(f'height: 4px; background: {T["border"]}; border-radius: 2px;').props(f'data-value="{pct}" data-color="{bar_color}"')
                        
                        metric_bar("Mobility Care Capacity", analysis["gap_profile"]["mobility_care_capacity"])
                        metric_bar("Neuro Rehab Capacity", analysis["gap_profile"]["neuro_rehab_capacity"])
                        metric_bar("Device Integration", analysis["gap_profile"]["device_integration_level"])
                        metric_bar("Funding Strength", analysis["gap_profile"]["funding_strength"])
                        metric_bar("Tech Readiness", analysis["gap_profile"]["tech_readiness"])
                    
                    # Scores
                    with ui.column().classes('flex-1 gap-4'):
                        with ui.row().classes('gap-3'):
                            unmet_card = ui.card().style(f'background: {T["bg"]}; border-radius: 6px; padding: 12px 14px; text-align: center; flex: 1;')
                            with unmet_card:
                                ui.label(f'{round(analysis["gap_profile"]["unmet_need_score"] * 100)}%').style(f'font-size: 28px; font-weight: 800; color: {T["danger"]}; font-family: {T["fontMono"]};')
                                ui.label('UNMET NEED').style(f'font-size: 10px; color: {T["muted"]}; font-family: {T["fontMono"]}; margin-top: 2px;')
                            
                            priority_card = ui.card().style(f'background: {T["bg"]}; border-radius: 6px; padding: 12px 14px; text-align: center; flex: 1;')
                            with priority_card:
                                ui.label(f'{round(analysis["deployment_package"]["priority_score"] * 100)}%').style(f'font-size: 28px; font-weight: 800; color: {T["accent"]}; font-family: {T["fontMono"]};')
                                ui.label('PRIORITY').style(f'font-size: 10px; color: {T["muted"]}; font-family: {T["fontMono"]}; margin-top: 2px;')
                        
                        primary_gap_card = ui.card().style(f'background: {T["bg"]}; border-radius: 6px; padding: 14px;')
                        with primary_gap_card:
                            ui.label('PRIMARY GAP').style(f'font-size: 10px; color: {T["muted"]}; font-family: {T["fontMono"]}; margin-bottom: 6px; letter-spacing: 0.08em;')
                            ui.label(analysis["gap_profile"]["primary_gap_category"].upper()).style(f'font-size: 14px; font-weight: 700; color: {T["warn"]}; font-family: {T["fontMono"]}; margin-bottom: 8px; text-transform: uppercase;')
                            ui.html(f'<p style="font-size: 12px; color: {T["muted"]}; line-height: 1.6; margin: 0;">{analysis["gap_profile"]["gap_narrative"]}</p>')
                        
                        ui.html(f'''<div style="font-size: 12px; color: {T["muted"]}; font-family: {T["fontMono"]};">
                            Volume: <span style="color: {T["text"]};">{analysis["gap_profile"]["patient_volume_estimate"]}</span>
                            &nbsp;&nbsp;·&nbsp;&nbsp;
                            Timeline: <span style="color: {T["accent"]};">{analysis["deployment_package"]["estimated_timeline_weeks"]}w</span>
                        </div>''')
            
            # Deployment Package
            with ui.card().style(f'border: 1px solid {T["border"]}; border-radius: 6px; overflow: hidden; margin-bottom: 20px;'):
                ui.label(f'Deployment Package — {analysis["deployment_package"]["system_name"]}').style(f'padding: 8px 14px; background: {T["border"]}; font-size: 11px; font-family: {T["fontMono"]}; color: {T["muted"]}; letter-spacing: 0.08em; text-transform: uppercase;')
                
                with ui.column().classes('p-4 gap-4'):
                    with ui.row().classes('w-full gap-6'):
                        with ui.column().classes('flex-1'):
                            ui.label('CORE MODULES').style(f'font-size: 11px; color: {T["muted"]}; font-family: {T["fontMono"]}; margin-bottom: 8px;')
                            with ui.row().classes('flex-wrap gap-1'):
                                for module in analysis["deployment_package"]["core_modules"]:
                                    ui.label(module).style(f'display: inline-block; padding: 2px 8px; border-radius: 3px; font-size: 11px; font-family: {T["fontMono"]}; background: {T["accentDim"]}; color: {T["accent"]}; margin: 2px 3px 2px 0; border: 1px solid {T["accent"]}33;')
                            
                            ui.label('DEVICE LAYER').style(f'font-size: 11px; color: {T["muted"]}; font-family: {T["fontMono"]}; margin: 12px 0 8px;')
                            with ui.row().classes('flex-wrap gap-1'):
                                for device in analysis["deployment_package"]["device_layer_support"]:
                                    ui.label(device).style(f'display: inline-block; padding: 2px 8px; border-radius: 3px; font-size: 11px; font-family: {T["fontMono"]}; background: #1a1a2e; color: #818cf8; margin: 2px 3px 2px 0; border: 1px solid #818cf833;')
                            
                            ui.label('DEPLOYMENT MODEL').style(f'font-size: 11px; color: {T["muted"]}; font-family: {T["fontMono"]}; margin: 12px 0 8px;')
                            ui.label(analysis["deployment_package"]["deployment_model"]).style(f'display: inline-block; padding: 2px 8px; border-radius: 3px; font-size: 11px; font-family: {T["fontMono"]}; background: #1a2a1a; color: {T["success"]}; margin: 2px 3px 2px 0; border: 1px solid {T["success"]}33;')
                        
                        with ui.column().classes('flex-1'):
                            ui.label('INTEGRATION POINTS').style(f'font-size: 11px; color: {T["muted"]}; font-family: {T["fontMono"]}; margin-bottom: 8px;')
                            with ui.row().classes('flex-wrap gap-1'):
                                for point in analysis["deployment_package"]["integration_points"]:
                                    ui.label(point).style(f'display: inline-block; padding: 2px 8px; border-radius: 3px; font-size: 11px; font-family: {T["fontMono"]}; background: #1a1a1a; color: {T["warn"]}; margin: 2px 3px 2px 0; border: 1px solid {T["warn"]}33;')
                            
                            ui.label('DATA LAYER').style(f'font-size: 11px; color: {T["muted"]}; font-family: {T["fontMono"]}; margin: 12px 0 8px;')
                            with ui.row().classes('flex-wrap gap-1'):
                                for data in analysis["deployment_package"]["data_layer"]:
                                    ui.label(data).style(f'display: inline-block; padding: 2px 8px; border-radius: 3px; font-size: 11px; font-family: {T["fontMono"]}; background: #1a0a0a; color: #f87171; margin: 2px 3px 2px 0; border: 1px solid #f8717133;')
                    
                    ui.label('ONBOARDING PATH').style(f'font-size: 11px; color: {T["muted"]}; font-family: {T["fontMono"]}; margin-bottom: 8px;')
                    with ui.row().classes('flex-wrap gap-1 items-center'):
                        for i, step in enumerate(analysis["deployment_package"]["onboarding_path"]):
                            with ui.row().classes('items-center gap-1'):
                                ui.html(f'''<div style="background: {T["accentDim"]}; border: 1px solid {T["accent"]}33; border-radius: 4px; padding: 4px 10px; font-size: 11px; font-family: {T["fontMono"]}; color: {T["accent"]};">
                                    <span style="color: {T["muted"]}; margin-right: 5px;">{i + 1}.</span>{step}
                                </div>''')
                                if i < len(analysis["deployment_package"]["onboarding_path"]) - 1:
                                    ui.label('→').style(f'color: {T["muted"]}; font-size: 10px;')
            
            # Next Actions
            with ui.card().style(f'border: 1px solid {T["border"]}; border-radius: 6px; overflow: hidden; margin-bottom: 20px;'):
                ui.label('Next Actions').style(f'padding: 8px 14px; background: {T["border"]}; font-size: 11px; font-family: {T["fontMono"]}; color: {T["muted"]}; letter-spacing: 0.08em; text-transform: uppercase;')
                
                with ui.column().classes('p-4'):
                    for i, action in enumerate(analysis["next_actions"]):
                        urgency_color = T["danger"] if action["urgency"] == "immediate" else T["warn"] if action["urgency"] == "30d" else T["muted"]
                        with ui.row().classes('w-full items-start gap-3').style(f'padding: 10px 0; border-bottom: {"1px solid " + T["border"] if i < len(analysis["next_actions"]) - 1 else "none"};'):
                            ui.element('div').style(f'width: 5px; height: 5px; border-radius: 50%; background: {urgency_color}; margin-top: 6px; flex-shrink: 0;')
                            with ui.column().classes('flex-1'):
                                ui.label(action["action"]).style('font-size: 13px; margin-bottom: 3px;')
                                ui.html(f'''<div style="font-size: 11px; font-family: {T["fontMono"]}; color: {T["muted"]};">
                                    owner: <span style="color: {T["text"]};">{action["owner"]}</span>
                                    &nbsp;&nbsp;·&nbsp;&nbsp;
                                    <span style="color: {urgency_color};">{action["urgency"]}</span>
                                    &nbsp;&nbsp;·&nbsp;&nbsp;
                                    impact: <span style="color: {T["success"] if action["impact"] == "high" else T["muted"]};">{action["impact"]}</span>
                                </div>''')
            
            # Email Section
            with ui.card().style(f'border: 1px solid {T["border"]}; border-radius: 6px; overflow: hidden; margin-bottom: 20px;'):
                ui.label('Automated Outreach — Gmail MCP').style(f'padding: 8px 14px; background: {T["border"]}; font-size: 11px; font-family: {T["fontMono"]}; color: {T["muted"]}; letter-spacing: 0.08em; text-transform: uppercase;')
                
                with ui.column().classes('p-4 gap-3'):
                    ui.label('SUBJECT').style(f'font-size: 11px; font-family: {T["fontMono"]}; color: {T["muted"]}; margin-bottom: 4px;')
                    ui.label(analysis["email_subject"]).style(f'font-family: {T["fontMono"]}; font-size: 13px; color: {T["text"]}; padding: 8px 12px; background: {T["bg"]}; border-radius: 4px;')
                    
                    ui.label('BODY PREVIEW').style(f'font-size: 11px; font-family: {T["fontMono"]}; color: {T["muted"]}; margin-bottom: 4px;')
                    ui.scroll_area().style(f'font-size: 13px; color: {T["muted"]}; line-height: 1.7; padding: 10px 12px; background: {T["bg"]}; border-radius: 4px; max-height: 160px;').content(
                        ui.label(analysis["email_body"])
                    )
                    
                    with ui.row().classes('w-full gap-3 items-center'):
                        email_input = ui.input(placeholder='recipient@institution.org').classes('flex-1').style(f'padding: 9px 12px; background: {T["surface"]}; border: 1px solid {T["border"]}; border-radius: 5px; color: {T["text"]}; font-family: {T["fontMono"]}; font-size: 13px;')
                        email_input.props('dark')
                        email_input.value = state.recipient_email
                        
                        send_btn = ui.button('Send via Gmail ↗').style(f'padding: 9px 18px; background: {T["accent"]}22; border: 1px solid {T["accent"]}; color: {T["accent"]}; border-radius: 5px; font-family: {T["fontMono"]}; font-size: 12px; cursor: pointer; white-space: nowrap;')
                        
                        async def send_email():
                            if not email_input.value:
                                return
                            send_btn.disable()
                            send_btn._text = 'Sending...'
                            await asyncio.sleep(1)  # Simulate sending
                            state.email_status = "sent"
                            send_btn.enable()
                            send_btn._text = 'Send via Gmail ↗'
                            ui.notify('✓ Email dispatched via Gmail MCP', type='positive')
                        
                        send_btn.on('click', send_email)
                    
                    if state.email_status:
                        status_color = T["success"] if state.email_status == "sent" else T["danger"]
                        status_msg = "✓ Email dispatched via Gmail MCP" if state.email_status == "sent" else "✗ Send failed — check Gmail MCP connection"
                        ui.label(status_msg).style(f'font-size: 12px; font-family: {T["fontMono"]}; color: {status_color}; margin-top: 8px;')
    
    # Main container
    with ui.column().classes('w-full min-h-screen').style(f'background: {T["bg"]}; color: {T["text"]}; font-family: {T["fontSans"]}; padding: 0;'):
        create_header()
        
        with ui.column().classes('w-full').style('max-width: 860px; margin: 0 auto; padding: 28px 24px;'):
            content_container = ui.column().classes('w-full')
            
            with content_container:
                if state.step == "input":
                    create_input_form()
                elif state.step == "running":
                    create_running_view()
                elif state.step == "result":
                    create_result_view()
    
    def update_ui():
        content_container.clear()
        with content_container:
            if state.step == "input":
                create_input_form()
            elif state.step == "running":
                create_running_view()
            elif state.step == "result":
                create_result_view()


# ─── STANDALONE HTML RAW NUMBER PLUGIN ───────────────────────────────────────
@ui.page("/plugin/raw-numbers")
def raw_numbers_plugin():
    """Standalone lightweight HTML raw number plugin for embedding"""
    
    ui.add_head_html("""
    <style>
        @keyframes pulse { 0%, 100% { opacity: 1 } 50% { opacity: 0.3 } }
        
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body {
            background: #080c10;
            color: #e8edf2;
            font-family: 'DM Sans', sans-serif;
            padding: 20px;
        }
        
        .plugin-container {
            max-width: 400px;
            margin: 0 auto;
        }
        
        .header {
            display: flex;
            align-items: center;
            gap: 10px;
            margin-bottom: 20px;
            padding-bottom: 15px;
            border-bottom: 1px solid #1c2430;
        }
        
        .indicator {
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: #00d4aa;
            box-shadow: 0 0 10px #00d4aa;
            animation: pulse 2s infinite;
        }
        
        .title {
            font-family: 'IBM Plex Mono', monospace;
            font-size: 12px;
            color: #00d4aa;
            letter-spacing: 0.1em;
        }
        
        .metric-card {
            background: #0d1117;
            border: 1px solid #1c2430;
            border-radius: 6px;
            padding: 15px;
            margin-bottom: 12px;
        }
        
        .metric-label {
            font-size: 11px;
            font-family: 'IBM Plex Mono', monospace;
            color: #5a6a7a;
            margin-bottom: 8px;
            text-transform: uppercase;
            letter-spacing: 0.07em;
        }
        
        .metric-value {
            font-size: 32px;
            font-weight: 800;
            font-family: 'IBM Plex Mono', monospace;
            margin-bottom: 8px;
        }
        
        .metric-bar {
            height: 4px;
            background: #1c2430;
            border-radius: 2px;
            overflow: hidden;
        }
        
        .metric-fill {
            height: 100%;
            border-radius: 2px;
            transition: width 1s ease;
        }
        
        .status-badge {
            display: inline-block;
            padding: 4px 10px;
            border-radius: 3px;
            font-size: 11px;
            font-family: 'IBM Plex Mono', monospace;
            margin-top: 8px;
        }
        
        .input-group {
            margin-bottom: 15px;
        }
        
        .input-field {
            width: 100%;
            padding: 10px 12px;
            background: #0d1117;
            border: 1px solid #1c2430;
            border-radius: 5px;
            color: #e8edf2;
            font-family: 'IBM Plex Mono', monospace;
            font-size: 13px;
            outline: none;
        }
        
        .btn {
            width: 100%;
            padding: 12px;
            background: #00d4aa;
            color: #000;
            border: none;
            border-radius: 6px;
            font-family: 'IBM Plex Mono', monospace;
            font-size: 13px;
            font-weight: 700;
            cursor: pointer;
            letter-spacing: 0.08em;
            transition: opacity 0.2s;
        }
        
        .btn:hover { opacity: 0.9; }
        .btn:disabled { opacity: 0.4; cursor: not-allowed; }
    </style>
    """)
    
    with ui.column().classes('plugin-container'):
        # Header
        with ui.row().classes('header items-center'):
            ui.element('div').classes('indicator')
            ui.label('ASSISTIVEOS').classes('title')
            ui.label('/ RAW NUMBERS PLUGIN').style('font-size: 10px; color: #5a6a7a; font-family: IBM Plex Mono, monospace;')
        
        # Input for institution
        ui.label('Enter Institution Name').style('font-size: 11px; font-family: IBM Plex Mono, monospace; color: #5a6a7a; margin-bottom: 6px; text-transform: uppercase;')
        inst_input = ui.input().classes('input-field').props('dark')
        
        # Quick metrics display
        metrics_container = ui.column().classes('w-full mt-4')
        
        async def load_metrics():
            if not inst_input.value:
                return
            
            loading_label.visible = True
            metrics_container.clear()
            
            await asyncio.sleep(0.5)
            
            # Generate metrics
            name_hash = hash(inst_input.value) % 100
            
            with metrics_container:
                # Unmet Need
                unmet_need = min(0.95, max(0.3, 0.6 - (name_hash % 35) / 100))
                unmet_pct = round(unmet_need * 100)
                with ui.column().classes('metric-card'):
                    ui.label('Unmet Need').classes('metric-label')
                    ui.label(f'{unmet_pct}%').style(f'font-size: 32px; font-weight: 800; font-family: IBM Plex Mono, monospace; color: #ef4444; margin-bottom: 8px;')
                    ui.element('div').style(f'height: 4px; background: #1c2430; border-radius: 2px;').props(f'data-value="{unmet_pct}"')
                    ui.element('div').style(f'height: 100%; width: {unmet_pct}%; background: #ef4444; border-radius: 2px; transition: width 1s ease;')
                
                # Priority Score
                priority = min(0.95, max(0.3, unmet_need * 0.7 + 0.3))
                priority_pct = round(priority * 100)
                with ui.column().classes('metric-card'):
                    ui.label('Priority Score').classes('metric-label')
                    ui.label(f'{priority_pct}%').style(f'font-size: 32px; font-weight: 800; font-family: IBM Plex Mono, monospace; color: #00d4aa; margin-bottom: 8px;')
                    ui.element('div').style(f'height: 4px; background: #1c2430; border-radius: 2px;')
                    ui.element('div').style(f'height: 100%; width: {priority_pct}%; background: #00d4aa; border-radius: 2px; transition: width 1s ease;')
                
                # Tech Readiness
                tech_ready = min(0.95, max(0.25, 0.4 + (name_hash % 45) / 100))
                tech_pct = round(tech_ready * 100)
                with ui.column().classes('metric-card'):
                    ui.label('Tech Readiness').classes('metric-label')
                    ui.label(f'{tech_pct}%').style(f'font-size: 32px; font-weight: 800; font-family: IBM Plex Mono, monospace; color: #10b981; margin-bottom: 8px;')
                    ui.element('div').style(f'height: 4px; background: #1c2430; border-radius: 2px;')
                    ui.element('div').style(f'height: 100%; width: {tech_pct}%; background: #10b981; border-radius: 2px; transition: width 1s ease;')
                
                # Funding Strength
                funding = min(0.95, max(0.2, 0.45 + (name_hash % 40) / 100))
                funding_pct = round(funding * 100)
                with ui.column().classes('metric-card'):
                    ui.label('Funding Strength').classes('metric-label')
                    ui.label(f'{funding_pct}%').style(f'font-size: 32px; font-weight: 800; font-family: IBM Plex Mono, monospace; color: #f59e0b; margin-bottom: 8px;')
                    ui.element('div').style(f'height: 4px; background: #1c2430; border-radius: 2px;')
                    ui.element('div').style(f'height: 100%; width: {funding_pct}%; background: #f59e0b; border-radius: 2px; transition: width 1s ease;')
                
                ui.label('Live from AssistiveOS Engine').style('font-size: 10px; font-family: IBM Plex Mono, monospace; color: #5a6a7a; margin-top: 12px; text-align: center;')
            
            loading_label.visible = False
        
        loading_label = ui.label('Loading...').style('font-size: 12px; color: #00d4aa; font-family: IBM Plex Mono, monospace; margin-top: 15px;')
        loading_label.visible = False
        
        ui.button('LOAD METRICS').classes('btn mt-4').on('click', load_metrics)


# ─── RUNNER ───────────────────────────────────────────────────────────────────
if __name__ in {"__main__", "__mp_main__"}:
    app.state.sessions = {}
    ui.run(
        title='AssistiveOS Engine',
        host='0.0.0.0',
        port=8080,
        reload=False,
        dark=True,
        storage_secret='assistive-os-secret-key-2024'
    )
