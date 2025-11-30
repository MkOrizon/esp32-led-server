from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Serve the static folder
app.mount("/static", StaticFiles(directory="static"), name="static")

# Homepage (Dashboard)
@app.get("/")
def home():
    return FileResponse("static/index.html")

# LED state (stored on server)
led_state = {"status": "off"}

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
