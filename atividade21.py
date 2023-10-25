# Exercício Python 21: Faça um programa que mostre na tela uma contagem regressiva para o estouro de
# fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

fogosdeartifiçio={"1","2","3","4", "5","6", "7", "8","9","10"}
 
from time import sleep
for item in fogosdeartifiçio:
    print(item) 
    sleep(1)