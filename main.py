from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Serve the static folder for the dashboard
app.mount("/static", StaticFiles(directory="static"), name="static")

# Homepage (Dashboard)
@app.get("/")
def home():
    return FileResponse("static/index.html")

# LED state stored on the server
led_state = {"status": "off"}

# Existing endpoints for ESP32
@app.get("/led")
def led_status():
    return led_state

@app.get("/led/on")
def led_on():
    led_state["status"] = "on"
    return {"message": "LED turned ON"}

@app.get("/led/off")
def led_off():
    led_state["status"] = "off"
    return {"message": "LED turned OFF"}

# New endpoints for the dashboard
@app.get("/state")
def state():
    return led_state

@app.post("/toggle")
def toggle():
    # Switch LED state
    led_state["status"] = "on" if led_state["status"] == "off" else "off"
    return led_state
