from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import aiohttp
import asyncio
import random
import time
import json
from datetime import datetime
from typing import List

# Initialize FastAPI app
app = FastAPI(title="Real-time Dashboard Demo")

# Set up templates and static files
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Keep track of active WebSocket connections
class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

manager = ConnectionManager()

# Mock API endpoints with varying response times
async def fetch_weather_data():
    # Simulate API delay between 0.5 and 1.5 seconds
    await asyncio.sleep(random.uniform(0.5, 1.5))
    
    temperatures = {
        "New York": random.randint(0, 32),
        "London": random.randint(-5, 25),
        "Tokyo": random.randint(5, 35),
        "Sydney": random.randint(10, 40),
        "Berlin": random.randint(-2, 30)
    }
    
    return {
        "data": temperatures,
        "timestamp": datetime.now().strftime("%H:%M:%S"),
        "source": "Weather API",
        "response_time": round(random.uniform(0.5, 1.5), 2)
    }

async def fetch_crypto_prices():
    # Simulate API delay between 0.3 and 2 seconds
    await asyncio.sleep(random.uniform(0.3, 2.0))
    
    prices = {
        "Bitcoin": round(random.uniform(50000, 60000), 2),
        "Ethereum": round(random.uniform(3000, 4000), 2),
        "Cardano": round(random.uniform(1, 3), 2),
        "Solana": round(random.uniform(100, 200), 2),
        "Dogecoin": round(random.uniform(0.1, 0.3), 3)
    }
    
    return {
        "data": prices,
        "timestamp": datetime.now().strftime("%H:%M:%S"),
        "source": "Crypto API",
        "response_time": round(random.uniform(0.3, 2.0), 2)
    }

async def fetch_stock_data():
    # Simulate API delay between 0.7 and 1.2 seconds
    await asyncio.sleep(random.uniform(0.7, 1.2))
    
    stocks = {
        "AAPL": round(random.uniform(150, 180), 2),
        "MSFT": round(random.uniform(280, 310), 2),
        "GOOGL": round(random.uniform(2700, 2900), 2),
        "AMZN": round(random.uniform(3200, 3500), 2),
        "TSLA": round(random.uniform(800, 900), 2)
    }
    
    return {
        "data": stocks,
        "timestamp": datetime.now().strftime("%H:%M:%S"),
        "source": "Stock API",
        "response_time": round(random.uniform(0.7, 1.2), 2)
    }

async def fetch_server_stats():
    # Simulate API delay between 0.2 and 0.8 seconds
    await asyncio.sleep(random.uniform(0.2, 0.8))
    
    servers = {
        "Server 1": random.randint(10, 90),
        "Server 2": random.randint(10, 90),
        "Server 3": random.randint(10, 90),
        "Server 4": random.randint(10, 90)
    }
    
    return {
        "data": servers,
        "timestamp": datetime.now().strftime("%H:%M:%S"),
        "source": "Server API",
        "response_time": round(random.uniform(0.2, 0.8), 2)
    }

# Synchronous vs Asynchronous Endpoints

@app.get("/sync")
def get_sync_data():
    """Demonstrates slow synchronous data fetching"""
    start_time = time.time()
    
    # Simulate sequential API calls
    time.sleep(1.0)  # Weather API
    weather = {"New York": 25, "London": 18, "Tokyo": 30}
    
    time.sleep(1.5)  # Crypto API
    crypto = {"Bitcoin": 55000, "Ethereum": 3500}
    
    time.sleep(0.8)  # Stock API
    stocks = {"AAPL": 165.30, "MSFT": 290.20}
    
    time.sleep(0.5)  # Server API
    servers = {"Server 1": 45, "Server 2": 62}
    
    end_time = time.time()
    
    return {
        "weather": weather,
        "crypto": crypto,
        "stocks": stocks,
        "servers": servers,
        "total_time": round(end_time - start_time, 2)
    }

@app.get("/async")
async def get_async_data():
    """Demonstrates fast asynchronous data fetching"""
    start_time = time.time()
    
    # Fetch data from all sources concurrently
    weather_task = asyncio.create_task(fetch_weather_data())
    crypto_task = asyncio.create_task(fetch_crypto_prices())
    stocks_task = asyncio.create_task(fetch_stock_data())
    servers_task = asyncio.create_task(fetch_server_stats())
    
    # Await all tasks
    weather = await weather_task
    crypto = await crypto_task
    stocks = await stocks_task
    servers = await servers_task
    
    end_time = time.time()
    
    return {
        "weather": weather,
        "crypto": crypto,
        "stocks": stocks,
        "servers": servers,
        "total_time": round(end_time - start_time, 2)
    }

# WebSocket endpoint for real-time updates
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            # Fetch all data concurrently
            weather_task = asyncio.create_task(fetch_weather_data())
            crypto_task = asyncio.create_task(fetch_crypto_prices())
            stocks_task = asyncio.create_task(fetch_stock_data())
            servers_task = asyncio.create_task(fetch_server_stats())
            
            # Await all tasks
            weather = await weather_task
            crypto = await crypto_task
            stocks = await stocks_task
            servers = await servers_task
            
            # Create combined data packet
            data_packet = {
                "weather": weather,
                "crypto": crypto, 
                "stocks": stocks,
                "servers": servers,
                "timestamp": datetime.now().strftime("%H:%M:%S.%f")[:-3]
            }
            
            # Send update to this client
            await manager.send_personal_message(json.dumps(data_packet), websocket)
            
            # Wait before next update
            await asyncio.sleep(2)
            
    except WebSocketDisconnect:
        manager.disconnect(websocket)

# Serve the HTML dashboard
@app.get("/", response_class=HTMLResponse)
async def get_dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})

# Run the server if executed directly
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True) 