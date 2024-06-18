import speech_recognition as sr
import keyboard

 
recognizer = sr.Recognizer()

print("Press 'Enter' to stop speaking.")
with sr.Microphone() as source:
    while True:
        try:
            print("Listening...")
            audio = recognizer.listen(source)
            if keyboard.is_pressed('enter'):
                print("Alt key pressed. Stopping...")
                break
            text = recognizer.recognize_google(audio)
            print("You said: " + text)

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

print("End of program.")
