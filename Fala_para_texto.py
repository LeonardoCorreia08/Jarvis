import speech_recognition as sr
import os
import threading
from mtranslate import translate
from colorama import Fore, Style, init

init(autoreset=True)

def Traducao_portugues_to_ingles(text):
    ingles_text = translate(text, "en-us")
    return ingles_text
    
def Fala_para_texto():
    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_threshold = False
    recognizer.energy_threshold = 340000
    recognizer.dynamic_energy_adjustment_damping = 0.010
    recognizer.dynamic_energy_ratio = 1.0
    recognizer.pause_threshold = 0.3
    recognizer.operation_timeout = None
    recognizer.non_speaking_duration = 0.2
    
    with sr.Microphone() as source:
        print(Fore.YELLOW + "Ajustando para o ruído ambiente...")
        recognizer.adjust_for_ambient_noise(source)
        
        while True:
            print(Fore.GREEN + "Escutando...", end="", flush=True)
            try:
                audio = recognizer.listen(source, timeout=None)
                print("\r" + Fore.LIGHTBLACK_EX + "Reconhecendo...", end="", flush=True)
                recognizer_text = recognizer.recognize_google(audio, language="pt-BR").lower() 
                
                if recognizer_text:
                    trans_text = Traducao_portugues_to_ingles(recognizer_text)
                    print("\r" + Fore.BLUE + "Ark : " + trans_text + " " * 20)
                    return trans_text
                else:
                    return ""
            except sr.UnknownValueError:
                print("\r" + Fore.RED + "Não entendi o áudio. Tente novamente." + " " * 20)
            except Exception as e:
                print(f"\r{Fore.RED}Erro: {e}" + " " * 20)

if __name__ == "__main__":
    # Executa a função diretamente ou via Thread dee forma correta
    stt_thread = threading.Thread(target=Fala_para_texto)
    stt_thread.start()
    stt_thread.join()
