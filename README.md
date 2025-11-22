<p align="center"> CampusWell Agent</p>
<p align="center">
  <img src="assets/campuswelll.png" width="180" alt="CampusWell Logo"/>
</p>

<p align="center">A multi-agent welfare assistant for college students, built with Google’s Agent Development Kit (ADK)</p>  </p> <p align="center"> <img src="https://img.shields.io/badge/Python-3.10-blue" /> <img src="https://img.shields.io/badge/Google-ADK-green" /> <img src="https://img.shields.io/badge/Status-Prototype-yellow" /> <img src="https://img.shields.io/badge/License-MIT-lightgrey" /> </p>
📘 Project Overview

CampusWell Agent is a multi-agent system designed to improve the academic and personal well-being of college students. Built with Google’s Agent Development Kit (ADK), it brings together specialized agents that streamline academic planning, reduce stress, guide financial decisions, and help students easily navigate campus resources.

This project demonstrates multi-agent coordination, looping agents with validation, custom tools, memory usage, context engineering, and observability — all aligned with the Kaggle x Google Agents Intensive Capstone requirements.

🎯 Problem Statement

College students face a wide range of challenges:

Overwhelming academic workload

Difficulty managing schedules and deadlines

Limited clarity on financial processes (fees, forms, scholarships)

Stress, burnout, and lack of structured wellness practices

Confusion when navigating resources like labs, libraries, counseling, or placement offices

Most institutions lack a unified assistant capable of helping students manage academics + wellness + administrative tasks in one place.
This leads to inefficiency, stress, and reduced academic consistency.

💡 Solution Statement

CampusWell Agent provides a central AI companion that supports students across multiple domains.
Instead of juggling dozens of portals or searching for help manually, students receive:

Personalized study schedules

Verified task breakdowns

Wellness routines

Campus service guidance

Financial process assistance

Formal email/message drafting

All handled by a coordinated ecosystem of specialized agents for higher reliability and clarity.

🏛️ Architecture

At the center of the system is the CampusLife Orchestrator, which coordinates an ecosystem of sub-agents. It manages:

Session state

Long-term memory (MemoryBank)

Agent delegation

Parallel and sequential workflows

Context engineering

Observability hooks

🤖 Sub-Agents
1. Academic Planner Agent

A LoopAgent that:

Creates weekly or daily study schedules

Breaks large tasks into manageable steps

Validates plans with ScheduleValidationChecker

Retries automatically until a conflict-free schedule is produced

2. Mental-Wellbeing Agent

Acts as a personal wellness coach, offering:

Short breathing routines

Stress-reduction tips

Study break plans

Recommendations based on historical stress patterns

3. Financial Guidance Agent

Helps students understand:

Scholarship options

Fee structures

Deadlines

Application steps

Includes lookups via a custom campus financial directory tool.

4. Campus Resource Navigator Agent

Quickly locates:

Library timings

Counselor information

Lab access hours

Placement office details

Academic department contacts

Uses a custom search tool + optional external search integrations.

5. Message Writer Agent

Drafts:

Formal emails to professors

Extension requests

Club participation messages

Simple resumes for college activities

🧰 Tools & Utilities
Schedule Generator Tool

Builds conflict-free study plans based on class timings and task lists.

Campus Info Lookup Tool

Searches through a structured dataset of campus resources.

Student Profile Memory Tool

Stores personalized long-term student details:

Courses

Preferred study style

Stress patterns

Academic goals

Validation Checkers

ScheduleValidationChecker

RoutineValidationChecker

Both ensure agent output quality using LoopAgent retry mechanics.

🔍 Features Demonstrated 

✔ Multi-agent system with both sequential and parallel flows
✔ LoopAgents with custom validation
✔ Multiple custom tools
✔ Session management & MemoryBank
✔ Context compaction
✔ Observability (logs, trace IDs, metrics stubs)
✔ Evaluation using synthetic student cases
✔ Deployable structure with modular agents

🚀 How to Run
1. Install dependencies
pip install -r requirements.txt

2. Run the sample orchestrator
python main.py

3. Try the demo notebook

Open:

notebooks/demo.ipynb


It includes:

Example conversations

Outputs from each sub-agent

Sample student profile inputs

Visual workflow descriptions


📄 License

This project is released under the MIT License.
Feel free to use, modify, and extend it.

🙌 Acknowledgments

Special thanks to the Google ADK team, Kaggle, and the community examples which inspired this project’s architecture and modular organization.

