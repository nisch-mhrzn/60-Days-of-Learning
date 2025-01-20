import speech_recognition as sr
from pyfirmata import Arduino, util
import pyttsx3



board = Arduino('COM9')  #port
led_pin = 13  

recognizer = sr.Recognizer()

def toggle_led(state):
    print(f"Toggling LED to {'on' if state else 'off'}")
    board.digital[led_pin].write(state)
    if state == 1:
        speak("LED turned on.")
    else:
        speak("LED turned off.")

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen_for_command():
    with sr.Microphone() as source:
        print("Listening for command...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print("Command:", command)
        return command
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        speak("Sorry, I didn't catch that.")
        return None
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        speak("Could not request results.")
        return None

while True:
    command = listen_for_command()

    if command == "turn on":
        toggle_led(1)
    elif command == "turn off":
        toggle_led(0)
    elif command == "exit":
        break