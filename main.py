from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse

app = FastAPI()

# Allow ESP32 requests from anywhere
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global LED state
led_state = "OFF"

# Root endpoint (optional)
@app.get("/", response_class=PlainTextResponse)
def home():
    return f"Server running. LED state: {led_state}"

# Get current LED state
@app.get("/led", response_class=PlainTextResponse)
def get_led_state():
    return led_state

# Turn LED ON
@app.get("/led/on", response_class=PlainTextResponse)
def set_led_on():
    global led_state
    led_state = "ON"
    return led_state

# Turn LED OFF
@app.get("/led/off", response_class=PlainTextResponse)
def set_led_off():
    global led_state
    led_state = "OFF"
    return led_state
