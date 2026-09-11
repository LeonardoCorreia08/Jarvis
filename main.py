from Fala_para_texto import Fala_para_texto


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager
from os import getcwd

chrome_options = webdriver.chromeOptions()
chrome_options.add_arguments("--use-fake-ui-for-media-stream")
#chrome_options.add_arguments("--headless=new")


drive = webdriver.Chrome(Service=Service(ChromeDriverManager().install()),options=chrome_options)


website = f"{getcwd()}\\index.html"

drive.get(website)

rec_file = f"{getcwd()}\\input.txt"

def listen():
    try:
        start_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, 'startButton'))
        )
        
        while True:
            output_element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, 'output'))
            )
            current_text = output_element.text.split()
            
            if "Start Listning" in start_button.text and is_second_click:
                if output_text:
                    is_second_click = False
            elif "listning..." in start_button.text:
                is_second_click = False
                if current_text != output_text:
                    output_text = current_text
                    with open(rec_file, "w") as file:
                        file.write(output_text.lower())
                    print("USER : " + output_text)

    except KeyboardInterrupt:
        pass                
    except Exception as e:
        print(f"Erro na função listen: {e}")


listen()


