import speech_recognition as sr
import os
import threading
from mtranslate import translate
from colorama import Fore,Style,init

init(autoreset=True)
def print_loop():
	#while true:
		print(Fore.GREEM + "Escultando...",fim-"",flush=True)
		print(Style.RESET_ALL,end="",flush=True)

print_loop()

def Trandução_portugues_to_ingles(text):
	ingles_text = translate(text,"en-us")
	return ingles_text
	
def Fala_para_texto_ptyhon():
	recognizer = sr.Recognizer()
	recognizer.dynamic_energy_threshold = False
	recognizer.energy_threshold = 340000
	recognizer.dynamic_energy_adjustment_damping = 0.010
	recognizer.dynamic_energy_ratio = 1.0
	recognizer.pause_threshold = 0.3
	recognizer.operation_timeout = None
	recognizer.pause_threshold = 0.2
	recognizer.non_speaking_duration = 0.2
	
	with sr.Microphone() as source:
		recognizer.adjust_for_ambient_noise(source)
		while true:
		   print(Fore.GREEM + "Escultando...",fim-"",flush=True)
		   print(Style.RESET_ALL,end="",flush=True)