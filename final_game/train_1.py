from time import sleep
from main_hero import player
def train():
    playershois=input("начать тренеровку?(да/нет):")
    while playershois=="да":
        for i in range(5):
            sleep(4)
            print("Идёт тренеровка...")
        player["attack"]+=1
        print(f"текущая атака героя равна={player['attack']}")
        playershois=input("продолжить тренеровку?(да/нет):")