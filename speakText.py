import pyttsx3
import pyttsx
#import pyttsx3
#https://pyttsx.readthedocs.io/en/v1.0/engine.html
#voice options, set with engine.setProperty('voice', voice.id)
# com.apple.speech.synthesis.voice.Alex
# com.apple.speech.synthesis.voice.alice
# com.apple.speech.synthesis.voice.alva
# com.apple.speech.synthesis.voice.amelie
# com.apple.speech.synthesis.voice.anna
# com.apple.speech.synthesis.voice.carmit
# com.apple.speech.synthesis.voice.damayanti
# com.apple.speech.synthesis.voice.daniel
# com.apple.speech.synthesis.voice.diego
# com.apple.speech.synthesis.voice.ellen
# com.apple.speech.synthesis.voice.fiona
# com.apple.speech.synthesis.voice.Fred
# com.apple.speech.synthesis.voice.ioana
# com.apple.speech.synthesis.voice.joana
# com.apple.speech.synthesis.voice.jorge
# com.apple.speech.synthesis.voice.juan
# com.apple.speech.synthesis.voice.kanya
# com.apple.speech.synthesis.voice.karen
# com.apple.speech.synthesis.voice.kyoko
# com.apple.speech.synthesis.voice.laura
# com.apple.speech.synthesis.voice.lekha
# com.apple.speech.synthesis.voice.luca
# com.apple.speech.synthesis.voice.luciana
# com.apple.speech.synthesis.voice.maged
# com.apple.speech.synthesis.voice.mariska
# com.apple.speech.synthesis.voice.mei-jia
# com.apple.speech.synthesis.voice.melina
# com.apple.speech.synthesis.voice.milena
# com.apple.speech.synthesis.voice.moira
# com.apple.speech.synthesis.voice.monica
# com.apple.speech.synthesis.voice.nora
# com.apple.speech.synthesis.voice.paulina
# com.apple.speech.synthesis.voice.samantha
# com.apple.speech.synthesis.voice.sara
# com.apple.speech.synthesis.voice.satu
# com.apple.speech.synthesis.voice.sin-ji
# com.apple.speech.synthesis.voice.tessa
# com.apple.speech.synthesis.voice.thomas
# com.apple.speech.synthesis.voice.ting-ting
# com.apple.speech.synthesis.voice.veena
# com.apple.speech.synthesis.voice.Victoria
# com.apple.speech.synthesis.voice.xander
# com.apple.speech.synthesis.voice.yelda
# com.apple.speech.synthesis.voice.yuna
# com.apple.speech.synthesis.voice.yuri
# com.apple.speech.synthesis.voice.zosia
# com.apple.speech.synthesis.voice.zuzana
import speech_recognition as sr
import sys
import os
#supports:
#WAV: must be in PCM/LPCM format
#AIFF
#AIFF-C
#FLAC: must be native FLAC format; OGG-FLAC is not supported
#recognizer options: bing, google, google_cloud, houndify, ibm, sphinx, wit

def say_hi():
    engine = pyttsx.init()
    engine.say('Good morning')
    engine.runAndWait()
    print("Good Morning")

def speak_text(x):
    engine = pyttsx.init()
    #engine.setProperty('voice', voice.kyoko)
    engine.say(x)
    engine.runAndWait()
    print(x)

def speaker(x):
    newVoice = textToSpeech()
    newVoice.start(x)
    del(newVoice)

class textToSpeech:
    engine = None
    rate = None
    def __init__(self):
        self.engine = pyttsx3.init()


    def start(self,text_):
        self.engine.say(text_)
        self.engine.runAndWait()

def main():
    #terminal method
    thing = sys.argv[1]
    statement = "say '" + thing + "'"
    #os.system("say 'hello world'")
    #os.system(statement)
    speaker(thing)
    #say_hi()
    #speak_text(thing)
main()
