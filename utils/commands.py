from utils.speaker import speak
from playsound import playsound

def process_command(command):
    # IGNITION
    if "start" in command or "engine on" in command or "power up" in command:
        speak("Starting the car now.")

    elif "stop" in command or "engine off" in command or "shut down" in command:
        speak("Stopping the car.")
    # GEAR
    elif "zero" in command or "drive mode" in command:
        speak("Switched to Drive mode.")
    elif "one" in command or "neutral mode" in command:
        speak("Switched to Neutral mode.")
    elif "two" in command or "reverse mode" in command:
        speak("Switched to Reverse mode.")

    # TURN SIGNALS
    elif "three" in command or "left signal" in command or "left blink" in command:
        speak("Left indicator on.")
        playsound("assets/clock-tick-101150.mp3")

    # RADIO
    elif "for" in command or "left signal" in command or "left blink" in command:
        speak("Turn radio ON")
        playsound("assets/radio-cuba.mp3")

    # HORN / ALERT
    elif any(kw in command for kw in ["five", "alert", "do tiit", "make beep"]):
        print("[DUO] Playing alert sound.")
        playsound("assets/tiit.wav")
    # SHUTDOWN
    elif "exit" in command or "shutdown" in command:
        speak("Shutting down. Goodbye.")
        exit(0)

    else:
        speak("I did not understand the command.")
