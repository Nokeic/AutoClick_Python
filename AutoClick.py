import keyboard
import mouse
from time import sleep

print("Programa AutoClicker\n By Nokeic\n")

tecla_de_execucao = input("Insira a tecla para o autoclicker funcionar (Terá que mate-la pressionada para o autoclick funcionar): ")
tecla_de_parada = input("Insira a tecla para parar a execução: ") 

while True:
    sleep(0.03) # Caso for usar para "Cheat", e queira legit, mude (0.03) para (0.06)
    if keyboard.is_pressed(tecla_de_execucao):
        mouse.click()
    if keyboard.is_pressed(tecla_de_parada):
        print("O loop foi interrompido.")
        break
input("Aperte enter para sair...")
