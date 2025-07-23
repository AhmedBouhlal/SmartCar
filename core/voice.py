import sounddevice as sd
import vosk
import queue
import sys
import json
import time
import numpy as np
from utils.commands import process_command
from utils.speaker import speak

model = vosk.Model("models/vosk-model-small-en-us-0.15")
q = queue.Queue()

def callback(indata, frames, time, status):
    audio_data = np.frombuffer(indata, dtype=np.int16)
    volume = np.abs(audio_data).mean()
    if volume > 500:  # Adjust threshold (500–1000 is good range)
        q.put(indata)

def recognize_and_respond():
    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                           channels=1, callback=callback):
        print("🎤 Say something:")
        rec = vosk.KaldiRecognizer(model, 16000)
        while True:
            data = q.get()
            if rec.AcceptWaveform(bytes(data)):  # ✅ Convert buffer to bytes
                result = json.loads(rec.Result())
                text = result.get("text", "")
                if text:
                    print(f"[USER] {text}")
                    process_command(text)
                    time.sleep(2)
            else:
                partial = json.loads(rec.PartialResult())
                print(partial.get("partial", ""), end="\r")
