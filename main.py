from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

led_state = "OFF"

@app.get("/")
def home():
    return {"status": "server running", "led": led_state}

@app.get("/led")
def get_led():
    return led_state

@app.get("/led/on")
def led_on():
    global led_state
    led_state = "ON"
    return "ON"

@app.get("/led/off")
def led_off():
    global led_state
    led_state = "OFF"
    return "OFF"
