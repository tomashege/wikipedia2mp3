#!/usr/bin/env python3
from gtts import gTTS
import os
files = "for now this string will have to do, but later it will import the wiki"
tts = gTTS(text=files, lang='en')
tts.save("good.mp3")
