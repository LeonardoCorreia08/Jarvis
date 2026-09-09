import speech_recognition as sr
import os
import threading
from mtranslate import translate
from colorama import Fore, Style, init

init(autoreset=True)

def print_loop():
    # while True:
    print(Fore.GREEN + "Escutando...", end="", flush=True)
    print(Style.RESET_ALL, end="", flush=True)

print_loop()

def Traducao_portugues_to_ingles(text):
    ingles_text = translate(text, "en-us")
    return ingles_text
    
def Fala_para_texto_python():
    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_threshold = False
    recognizer.energy_threshold = 340000
    recognizer.dynamic_energy_adjustment_damping = 0.010
    recognizer.dynamic_energy_ratio = 1.0
    recognizer.pause_threshold = 0.3
    recognizer.operation_timeout = None
    recognizer.non_speaking_duration = 0.2
    
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        while True:
            print(Fore.GREEN + "Escutando...", end="", flush=True)
            try:
                audio = recognizer.listen(source, timeout=None)
                print("\r" + Fore.LIGHTBLACK_EX + "Reconhecendo...", end="", flush=True)
                recognizer_text = recognizer.recognize_google(audio).lower() 
                if recognizer_text:
                    trans_text = Traducao_portugues_to_ingles(recognizer_text)
                    print("\r" + Fore.BLUE + "Ark : " + trans_text)
                    return trans_text
                else:
                    return ""
            except sr.UnknownValueError:
                recognizer_text = ""
            finally:
                print("\r", end="", flush=True)
			os.system("cls" if os.name == "nt" else "clean")
		stt_thread = threading.Thread(target=Fala_para_texto_python)
		print_thread = threading.Thread(target=print_loop)
		stt_thread.start()
		print_loop.start()
		stt_thread.join()
		print_loop.join()



