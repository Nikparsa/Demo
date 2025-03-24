# Real-time Data Dashboard with FastAPI

A demonstration project showing how FastAPI with asyncio can process data from multiple sources concurrently, providing significant performance benefits over traditional synchronous approaches.

## Project Overview

This project demonstrates:

1. **Asynchronous API Calls** - Using asyncio to fetch data from multiple sources concurrently
2. **Real-time Updates** - WebSocket connections for live dashboard updates
3. **Performance Comparison** - Direct comparison between synchronous and asynchronous approaches
4. **Modern Web Dashboard** - Interactive visualization with Chart.js

## Features

- **Synchronous vs Asynchronous Demo** - Compare the performance directly
- **WebSocket Integration** - Real-time updates without page refresh
- **Multiple Data Visualizations** - Temperature, cryptocurrency, stocks, and server data
- **Response Time Tracking** - See how long each API call takes

## Installation

1. Clone this repository
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

1. Start the FastAPI server:
   ```
   uvicorn main:app --reload
   ```

2. Open your browser and navigate to:
   ```
   http://localhost:8000
   ```

## Project Structure

- `main.py` - FastAPI application with routes and WebSocket support
- `templates/dashboard.html` - Frontend dashboard with visualizations
- `requirements.txt` - Project dependencies

## Demonstration Guide

For your 30-minute seminar, follow this presentation outline:

1. **Introduction (5 min)**
   - Explain the problem of fetching data from multiple sources
   - Introduce asyncio and FastAPI

2. **Live Demo (10 min)**
   - Show the dashboard in action
   - Compare synchronous vs asynchronous performance
   - Demonstrate real-time updates with WebSocket

3. **Code Walkthrough (10 min)**
   - Explain how asyncio works in FastAPI
   - Show the key parts of the code implementation
   - Highlight the WebSocket integration

4. **Q&A and Conclusion (5 min)**
   - Summarize the benefits of async programming
   - Answer questions from the audience

## Key Points to Emphasize

- Asyncio allows multiple I/O operations to proceed concurrently in a single thread
- FastAPI makes it simple to create async endpoints and WebSockets
- The performance difference is especially significant with multiple API calls
- Modern web applications benefit greatly from this approach

## License

This project is available under the MIT License. 