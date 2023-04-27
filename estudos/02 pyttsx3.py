# Introdução e comandos básicos
import pyttsx3

engine = pyttsx3.init()
engine.setProperty("voice", "portuguese")
engine.say("Olá mundo")
engine.runAndWait()