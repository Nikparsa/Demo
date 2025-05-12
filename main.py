from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

# Sample data
concerts = [
    {
        "name": "Graz Symphony Orchestra",
        "date": "2024-04-15",
        "time": "19:30",
        "venue": "Graz Opera House",
        "available_tickets": 150,
        "price_range": "€45-€120",
        "rating": 4.8,
        "weather": {
            "temperature": "18°C",
            "condition": "Partly Cloudy"
        },
        "parking": {
            "spaces": 200,
            "price": "€5/hour"
        },
        "traffic": {
            "status": "Moderate",
            "delay": "10 minutes"
        },
        "nearby_places": [
            {
                "name": "Café Central",
                "type": "Café",
                "opening_hours": "08:00-22:00",
                "rating": 4.5,
                "distance": "0.2 km"
            },
            {
                "name": "Restaurant Schlossberg",
                "type": "Restaurant",
                "opening_hours": "11:00-23:00",
                "rating": 4.7,
                "distance": "0.5 km"
            }
        ]
    },
    {
        "name": "Jazz in the Park",
        "date": "2024-04-20",
        "time": "20:00",
        "venue": "Stadtpark Graz",
        "available_tickets": 300,
        "price_range": "€30-€80",
        "rating": 4.6,
        "weather": {
            "temperature": "20°C",
            "condition": "Sunny"
        },
        "parking": {
            "spaces": 150,
            "price": "€4/hour"
        },
        "traffic": {
            "status": "Light",
            "delay": "5 minutes"
        },
        "nearby_places": [
            {
                "name": "Park Café",
                "type": "Café",
                "opening_hours": "09:00-21:00",
                "rating": 4.3,
                "distance": "0.1 km"
            },
            {
                "name": "Biergarten",
                "type": "Bar",
                "opening_hours": "16:00-01:00",
                "rating": 4.4,
                "distance": "0.3 km"
            }
        ]
    }
]

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "concerts": concerts})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) 