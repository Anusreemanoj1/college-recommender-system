# AI-Powered College Admission Recommender System

An intelligent web application that recommends suitable colleges and academic programs to students based on their academic profile, preferences, budget, and domain interest — powered by Python, Flask, and basic AI logic.

## Features

- Personalized college recommendations based on:
  - Class 12th percentage
  - Preferred domain/stream (e.g., AI, Commerce, Law)
  - Budget constraints
  - Preferred location
- AI logic with profile matching
- Optional SWOT analysis for career guidance (AI-generated)
- Simple and responsive UI
- Backend with Flask and data from CSV
- College filters: minimum % criteria, fees, location, ranking

## Tech Stack

| Component  | Technology |
|------------|------------|
| Frontend   | HTML + CSS (with optional Bootstrap) |
| Backend    | Python + Flask |
| AI Logic   | Python + Pandas + basic ML or GPT-4 API (optional) |
| Database   | CSV (can upgrade to SQLite/MySQL) |
| Hosting    | GitHub + (Render / Railway for deployment) |


## Project Structure

college-recommender/ ├── app.py                # Main Flask app ├── models.py             # Logic for filtering or recommendation ├── data/ │   └── colleges.csv      # College dataset ├── templates/ │   ├── index.html        # Form page │   └── results.html      # Output recommendations ├── static/ │   └── styles.css        # Optional styling └── README.md


## Sample College Dataset (colleges.csv)

`csv
College Name,Stream,Location,Fees,Min %,Ranking,Duration,Accreditation,Placement %
ABC Institute of Tech,AI,Bangalore,150000,75,8.5,4 years,NAAC A+,90%
XYZ Commerce College,Commerce,Delhi,50000,65,7.8,3 years,NAAC B,70%
...

git clone https://github.com/Anusreemanoj1/college-recommender-system.git
cd college-recommender-system

python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

pip install flask pandas

python app.py
