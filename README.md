# AI Study Planner Agent

A beginner-friendly study planning application built using
Python and Streamlit.

The application prioritizes study topics based on their
difficulty and deadline, creates a daily study schedule,
and tracks topic completion.

## Features

- Add subjects and study topics
- Set difficulty and deadline
- Specify estimated study hours
- Generate a prioritized daily study plan
- Adjust the schedule to available daily hours
- Track completed and pending topics
- View overall progress
- Light-mode user interface

## Technology Stack

- Python
- Streamlit
- Rule-based decision-making
- Python session state

## How It Works

The agent calculates a priority score using topic difficulty
and deadline urgency.

It sorts pending topics by priority and allocates study time
without exceeding the user's daily time limit.

When a topic is completed, the user can generate an updated
plan based on the remaining topics.

## Installation

### 1. Install Python

Install Python 3.11 or later.

### 2. Clone or download this repository

Open the project folder in VS Code.

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the environment on Windows

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 6. Run the application

```bash
python -m streamlit run app.py
```

The application will normally open at:

http://localhost:8501

## Privacy and Cost

- No LLM API calls
- No API key required
- No external database required
- No paid service required
- Topics remain in the local application session
- Initial dependency installation requires internet access

## Limitations

- Topic data is not permanently saved
- Priorities are based on predefined rules
- No machine-learning model is trained
- Completion currently records a topic as fully completed

## Future Improvements

- Save and load study plans locally
- Track partial study sessions
- Support weekly schedules
- Add subject-wise progress charts
- Include break recommendations

## Academic Purpose

This project demonstrates basic agent concepts:
input collection, priority-based decision-making,
action selection, progress feedback, and replanning.

It is a rule-based educational agent and does not use
a large language model.

## License

This project is available for educational use.
