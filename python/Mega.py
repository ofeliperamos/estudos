import random
import pygame
print("ESTAMOS SORTEANDO OS NUMEROS........!!")
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('peao.mp3')
pygame.mixer.music.play()
pygame.event.wait()
input('PRESSIONE ENTER PARA SEGUIR COM O SORTEIO')
num = random.randint(1,60)
num2 = random.randint(1,60)
num3 = random.randint(1,60)
num4 = random.randint(1,60)
num5 = random.randint(1,60)
num6 = random.randint(1,60)




print('NúMEROS DA MEGA SENA DO SORTEIO AUTOMÁTICO !!!')

print(num)
print(num2)
print(num3)
print(num4)
print(num5)
print(num6)

print('QUE PENA, VOCÊ NÃO GANHOU !!! ')
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('tron.mp3')
pygame.mixer.music.play()
pygame.event.wait()

