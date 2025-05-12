# Graz Concert Dashboard

A modern web dashboard for Graz concerts, providing information about events, weather, parking, traffic, and nearby places.

## Features

- Concert information (date, time, venue, available tickets, prices)
- Weather conditions for each concert
- Parking availability and pricing
- Traffic status and delays
- Nearby restaurants, bars, and cafes with ratings and opening hours
- Responsive design for all devices
- Modern UI with interactive elements

## Setup

1. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
uvicorn main:app --reload
```

4. Open your browser and visit:
```
http://localhost:8000
```

## Project Structure

- `main.py` - FastAPI application and routes
- `templates/` - HTML templates
- `static/` - CSS, JavaScript, and other static files
- `requirements.txt` - Python dependencies

## API Endpoints

- `GET /` - Main dashboard page
- `GET /api/concerts` - Get all concerts data
- `GET /api/concert/{concert_id}` - Get specific concert data

## Technologies Used

- FastAPI - Web framework
- Bootstrap 5 - Frontend framework
- Jinja2 - Template engine
- JavaScript - Client-side interactivity 