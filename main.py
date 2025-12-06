from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Serve static folder
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def home():
    return FileResponse("static/index.html")

# LED state for 4 LEDs
leds = {"led1":"off","led2":"off","led3":"off","led4":"off"}

@app.get("/led/{led_id}")
def get_led_state(led_id: str):
    if led_id not in leds:
        return {"error": "LED not found"}
    return {"id": led_id, "state": leds[led_id]}

@app.get("/led/{led_id}/{state}")
def set_led_state(led_id: str, state: str):
    if led_id not in leds:
        return {"error": "LED not found"}
    if state not in ["on","off"]:
        return {"error": "Invalid state"}
    leds[led_id] = state
    return {"id": led_id, "state": state}

# Servo control state
servo_position = {"position":"center"}

@app.get("/servo/{pos}")
def move_servo(pos: str):
    if pos not in ["left","center","right"]:
        return {"error":"Invalid servo position"}
    servo_position["position"] = pos
    return servo_position

# NEW ENDPOINT: REQUIRED BY ESP32
@app.get("/state_all")
def get_all_states():
    return {
        "led1": leds["led1"],
        "led2": leds["led2"],
        "led3": leds["led3"],
        "led4": leds["led4"],
        "servo": servo_position["position"]
    }