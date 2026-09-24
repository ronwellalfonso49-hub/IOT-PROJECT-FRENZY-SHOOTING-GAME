# FRENZY
IoT-Based Target Shooting Game with Intelligent Player Performance Assessment

## 1. Project Description

FRENZY is an IoT-based target shooting game. A player aims a laser at physical targets. LDR sensors detect hits, an ESP32 processes the signals, and game data is sent over Wi-Fi to a Flask backend. A web dashboard shows live and final results.

The intended hardware and software stack includes:

- ESP32 (planned)
- LDR sensors (planned)
- Servo motors (planned)
- Buzzer (planned)
- Push button (planned)
- Laser (planned)
- Flask backend (implemented)
- Web frontend (implemented)
- Rule-Based Intelligent System (planned)
- SQLite database (planned)

The current codebase is a working web prototype. Game rounds can be started, simulated with mock data, and reviewed in the browser. Hardware, persistent storage, and the intelligent assessment engine are not implemented yet.

## 2. System Architecture

Intended data flow:

```
Player
↓
Laser Shooting
↓
LDR
↓
ESP32
↓
Wi-Fi
↓
Flask Backend
↓
Game Data
↓
Rule-Based Intelligent System
↓
Performance Assessment
↓
Web Dashboard
```

### Already implemented

- Flask backend (`app.py`, page routes, REST API)
- Web dashboard, round results page, and final results page
- In-memory game session (start, mock rounds, reset)
- Game data fields per round (hits, misses, accuracy, reaction time, score)
- Aggregated totals and averages on the Final Results page

### Planned (not implemented)

- Player laser shooting hardware
- LDR hit detection
- ESP32 firmware and target control (servo, buzzer, push button)
- Wi-Fi communication from ESP32 to Flask
- SQLite persistence
- Rule-based Intelligent System and performance classification
- Replacing mock rounds with live hardware data

Until ESP32 integration exists, rounds are created with the **Simulate Next Round (Mock)** button on the dashboard.

## 3. Game Data

Each round is stored with the following fields (already used by the in-memory store and `/api/round`):

| Field | Description |
| --- | --- |
| `round_number` | Round index in the current session |
| `hits` | Number of successful hits |
| `misses` | Number of misses |
| `accuracy` | Hit percentage for the round |
| `reaction_time` | Reaction time in milliseconds |
| `score` | Round score |

A full session currently defaults to **3 rounds**. After all rounds finish, the Final Results page shows totals and averages. Data is held in memory only and is lost when the Flask process stops or the game is reset.

## 4. Intelligent System

The planned Intelligent System is a **rule-based** performance assessment system. It is **not** machine learning.

It will analyze:

- average accuracy
- average reaction time
- total hits
- total misses
- total score
- performance consistency

It will classify performance into:

- Beginner
- Intermediate
- Advanced

and generate performance remarks.

**Status:** not implemented. The Final Results page currently shows placeholders (`TBD - ML module pending` and `TBD - AI remarks pending`). Those labels are leftover UI text; the planned engine remains rule-based, not ML.

## 5. Current Development Status

### Completed

- [x] Flask application entry point (`app.py`)
- [x] Page routes: dashboard, start game, round results, final results, reset
- [x] API routes: status, start, submit round, mock round, list rounds, final results, reset
- [x] In-memory game store with mock round generation
- [x] Web frontend (HTML templates, CSS, dashboard JavaScript)
- [x] Per-round and aggregated score display
- [x] Placeholder slots on Final Results for future assessment output

### In Progress

- [ ] GitHub sharing setup for group collaboration (this repository documentation)
- [ ] Preparing the backend to receive real hardware round payloads (API shape exists; ESP32 is not connected)

### Planned / To Do

- [ ] ESP32 firmware and Wi-Fi integration
- [ ] LDR, servo, buzzer, push button, and laser hardware control
- [ ] Replace mock rounds with live IoT data
- [ ] SQLite database
- [ ] Rule-based Intelligent System (Beginner / Intermediate / Advanced + remarks)
- [ ] Persistent history across server restarts

## 6. Project Structure

```
IOT WEB TARGET FRENZY/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── game/
│   ├── __init__.py
│   └── store.py
├── routes/
│   ├── __init__.py
│   ├── api.py
│   └── pages.py
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── app.js
└── templates/
    ├── base.html
    ├── dashboard.html
    ├── round_results.html
    └── final_results.html
```

## 7. Installation

Commands below are for **Windows** (Command Prompt or PowerShell).

1. Clone the repository:

```bat
git clone <repository-url>
```

2. Enter the project directory:

```bat
cd "IOT WEB TARGET FRENZY"
```

Use the actual folder name after cloning if it differs.

3. Create a Python virtual environment:

```bat
python -m venv venv
```

4. Activate the virtual environment:

```bat
venv\Scripts\activate
```

5. Install dependencies:

```bat
pip install -r requirements.txt
```

6. Run the Flask application:

```bat
python app.py
```

The server listens on `http://0.0.0.0:5000` (debug mode).

7. Open the web application in a browser:

```
http://127.0.0.1:5000
```

or

```
http://localhost:5000
```

## 8. Git Workflow

Before starting work, update your local copy:

```bat
git pull
```

Create a feature branch (do not commit experimental work directly on `main`):

```bat
git checkout -b feature-name
```

After testing:

```bat
git add .
git commit -m "Describe your changes"
git push origin feature-name
```

Open a pull request (or ask a teammate to review) so changes can be merged into `main`.

Avoid pushing unreviewed edits straight to `main`. Coordinate with the group if `main` must be updated.

## How to try the current prototype

1. Open the dashboard.
2. Click **Start Game**.
3. Click **Simulate Next Round (Mock)** until all rounds are complete.
4. Open **Rounds** for the per-round table and **Results** for the session summary.
