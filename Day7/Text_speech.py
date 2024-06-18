from gtts import gTTS
import os
import requests
response = requests.get("http://www.google.com", timeout=5)
if response.status_code == 200:
    print("Internet connection is active.")
else:
    print("Failed to connect to the internet. Status code:", response.status_code)

mytext = input("Enter a text: ")
language = 'en'

print("Creating gTTS object...")
myobj = gTTS(text=mytext, lang=language, slow=False)

print("Saving the speech to an MP3 file...")
myobj.save("hello.mp3")
print("File saved as hello.mp3")

print("Playing the MP3 file...")
os.system("start hello.mp3")
