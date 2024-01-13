from random import randint
from time import sleep
from train_1 import train
from main_hero import player
from shop import shop
from enemies import enemies
from fight import fight 
name = input('Введи своё имя, путник: ')
player['name'] = name
while player['hp']>0:
    player_choice=input("Хотите тренироваться или в бой или в магазин?1-тренировка;2-бой;3-магазин;:")
    if player_choice=="1":
        train()
    elif player_choice=="2":
        fight()
    elif player_choice=="3":
        shop()

    else:
        print("давай по новой всё не правильно")

print("Game Over")