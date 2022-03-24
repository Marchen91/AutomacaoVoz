import pyautogui
import time
import keyboard
import speech_recognition as sr    
import winsound


pyautogui.moveTo(x=349, y=18)
#pyautogui.click()

frequency = 500  # Set Frequency To 2500 Hertz
duration = 500  # Set Duration To 1000 ms == 1 second

contador = 0


while (True):
    
    #print("entrou")
    
    
    
    
        #winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
       # print (r.recognize_google(audio, language ="pt-BR"))
    
    try:
    
        r = sr.Recognizer()
        with sr.Microphone() as source:
        #print ("Diga algo!")
        # Play Windows exit sound.
            winsound.Beep(frequency, duration)

            r.adjust_for_ambient_noise(source)

            audio = r.listen(source)
            frase = r.recognize_google(audio, language ="pt-BR")
            
            print(frase)
        
        if "abrir"  in frase:
            
            #print("sim")
            winsound.Beep(frequency, duration)
            winsound.Beep(frequency, duration)
            
            #Sim
            pyautogui.moveTo(x=256, y=1061)
            pyautogui.click()
            #pyautogui.click()
            
            pyautogui.write('excel')
            pyautogui.moveTo(x=149, y=518)
            pyautogui.click()
            #pyautogui.click()
            #time.sleep(2)

            
            #pyautogui.moveTo(x=1352, y=697)
           # pyautogui.click()
            #time.sleep(2)

            pyautogui.moveTo(x=1827, y=958)
            pyautogui.click()

        elif "não" in frase:
            #Não
            winsound.Beep(frequency, duration)
            winsound.Beep(frequency, duration)
            
            
            
            pyautogui.moveTo(x=1885, y=984)
            pyautogui.click()
            #time.sleep(1)

            pyautogui.moveTo(x=1351, y=743)
            pyautogui.click()
            #time.sleep(1)

            pyautogui.moveTo(x=1827, y=958)
            pyautogui.click()

        elif "texto" in frase:
            #Não
            
            winsound.Beep(frequency, duration)
            winsound.Beep(frequency, duration)
            
            pyautogui.moveTo(x=1885, y=984)
            pyautogui.click()
            #time.sleep(1)

            pyautogui.moveTo(x=1757, y=951)
            pyautogui.click()
            #time.sleep(1)

            pyautogui.moveTo(x=706, y=436)
            pyautogui.click()
           # time.sleep(1)

            pyautogui.moveTo(x=1151, y=535)
            pyautogui.click()

        elif "fora" in frase:
            #Não
            
            winsound.Beep(frequency, duration)
            winsound.Beep(frequency, duration)
            
            
            pyautogui.moveTo(x=1885, y=984)
            pyautogui.click()
            #time.sleep(1)

            pyautogui.moveTo(x=1757, y=951)
            pyautogui.click()
            #time.sleep(1)

            pyautogui.moveTo(x=707, y=374)
            pyautogui.click()
            #time.sleep(1)

            pyautogui.moveTo(x=1151, y=535)
            pyautogui.click()
        
        elif "primeiro" in frase:
            #Não
            
            winsound.Beep(frequency, duration)
            winsound.Beep(frequency, duration)
            
            
            pyautogui.moveTo(x=346, y=11)
            pyautogui.click()
            
        elif "segundo" in frase:
            #Não
            
            winsound.Beep(frequency, duration)
            winsound.Beep(frequency, duration)
            
            
            pyautogui.moveTo(x=635, y=10)
            pyautogui.click()
            
        elif "terceiro" in frase:
            #Não
            
            winsound.Beep(frequency, duration)
            winsound.Beep(frequency, duration)
            
            
            pyautogui.moveTo(x=860, y=12)
            pyautogui.click()
        
        elif "quarto" in frase:
            #Não
            
            winsound.Beep(frequency, duration)
            winsound.Beep(frequency, duration)
            
            
            pyautogui.moveTo(x=1054, y=16)
            pyautogui.click()
            
        elif "volta" in frase:
            #Não
            
            winsound.Beep(frequency, duration)
            winsound.Beep(frequency, duration)
            
            
            while (True):
    
                print("entrou")
                time.sleep(2) #espera 5 segundos
                pyautogui.click(x=1433, y=419, clicks = 2)
                pyautogui.write('i')
                pyautogui.hotkey('backspace')
                time.sleep(2)
                pyautogui.click(x=1495, y=356, clicks = 2)
                if keyboard.is_pressed("p"):
                    print('fim')
                    break
            
            
            
            
            
            
            
    except sr.UnknownValueError:
        print(" Nao reconhecido")
        winsound.Beep(frequency, duration)
        winsound.Beep(frequency, duration)
        winsound.Beep(frequency, duration)
    except sr.RequestError as e:
        print ("Erro ao chmar o google speech")
        winsound.Beep(frequency, duration)
        winsound.Beep(frequency, duration)
        winsound.Beep(frequency, duration)
        