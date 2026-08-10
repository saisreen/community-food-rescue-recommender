# Community Food Rescue Recommendation System

## Project Overview

The Community Food Rescue Recommendation System is an academic AI and HCI project designed to recommend suitable fictional community food centers for surplus food donations.

Instead of recommending common items such as movies or products, this project explores how recommendation techniques can support community food distribution decisions.

The user provides information about a food donation, and the system evaluates available community centers and returns the top three matches.

## User Inputs

The system considers five factors:

- Food type
- Quantity of food
- Refrigeration requirement
- Distribution urgency
- Preferred community

## Recommendation Method

The application uses a weighted scoring approach.

- Food type match: 30 points
- Refrigeration requirement: 25 points
- Capacity: 20 points
- Distribution urgency: 15 points
- Community preference: 10 points

The maximum possible score is 100.

Each fictional food center is evaluated using these criteria. The centers are sorted according to their scores, and the top three recommendations are displayed.

## HCI Features

The interface was designed to make the recommendation process simple and understandable.

The application provides:

- Simple dropdown selections
- Quantity input
- Top three recommendations
- Match percentage
- Visual progress indicator
- Recommendation confidence level
- Explanation of why each center was recommended

The explanation feature provides transparency instead of presenting the recommendation as an unexplained AI decision.

## Technologies Used

- Python
- Pandas
- Streamlit
- CSV dataset

## Project Files

`app.py` - Streamlit user interface

`recommender.py` - Recommendation and scoring logic

`food_centers.csv` - Fictional food center dataset

`requirements.txt` - Python dependencies

`README.md` - Project documentation

## Running the Application

Install the required packages:

```bash
pip install -r requirements.txt