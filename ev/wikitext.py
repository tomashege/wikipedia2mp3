#!/usr/bin/env python3
from gtts import gTTS
import os
print("Starting...")
fileName = "text.txt"
#file = open(fileName,"r")
#print("file open")
#files = file.read()
#file.close()
#print("text file loaded")
#print("mp3 made")
#print("Done")

tts = gTTS(text=files, lang='en')
tts.save("audio.mp3")