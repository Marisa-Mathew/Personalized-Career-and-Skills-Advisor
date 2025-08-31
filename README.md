# Personalized Career and Skills Advisor


## Overview

**Personalized Career and Skills Advisor** (also known as *Skill Navigator*) is a prototype AI-driven web application designed to guide students through their academic and early career journeys. It analyzes user skills, interests, and job market trends to provide tailored career recommendations, identify skill gaps, and suggest learning resources. This project was developed as part of the Gen AI Exchange Hackathon by Team *The Chosen*, led by Marisa Mathew.

The app leverages simple Python-based logic (with Flask) to simulate core features, making it an accessible starting point for further development into a full AI-powered tool using Google Cloud services.

### Key Objectives
- Empower students with data-driven career insights.
- Bridge skill gaps through personalized recommendations.
- Prepare users for the evolving job market.

## Features

- **Basic Skill Assessment**: Users input hard/soft skills and interests to generate a simple profile.
- **Career Path Recommendations**: Suggests careers with match percentages based on user inputs.
- **Learning Resource Suggestions**: Provides curated resources (e.g., courses) to address skill gaps.
- **Future-Proof Design**: Built with extensibility in mind for real AI integration (e.g., Vertex AI).

*Note*: This is a minimal prototype with hardcoded logic—no real AI or databases yet. Expand it for production use.

## Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML/CSS (with Jinja2 templating)
- **Planned Enhancements**: Google Cloud Platform (Vertex AI, Cloud SQL), NLP libraries (spaCy, Hugging Face), Job APIs (Indeed, LinkedIn)

## Installation

### Prerequisites
- Python 3.8+ installed
- pip (Python package manager)

### Steps
1. Clone the repository:

2. Install dependencies:
pip install flask

3. Ensure the folder structure:
personalized-career-advisor
```bash
├──skill_navigator
├── app.py
└── templates/
      ├── index.html
      └── result.html



4. Open a web browser and navigate to:http://127.0.0.1:5000/
 
5. Fill in your skills and interests in the form to receive recommendations.

Example Input:
- Hard Skills: Python, Data Analysis
- Soft Skills: Communication
- Interests: AI

Output: Skill profile, career suggestions (e.g., Data Scientist - 80% Match), and learning resources.

To stop the server, press `Ctrl+C` in the terminal.





