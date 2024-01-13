from main_hero import player

def shop():
    print(f"Ваше кол-во денег:{player['money']}")
    magazin = {"Пузырёк опыта":5000,
               "Убийца Драконов":15000,
               "Святая броня":15000,
               "Божественный подгузник":100000,
               "Перчатка бесконечности":25000,
               "Щит тьмы":50000}
    print("Добро пожаловать в наш магазин! У нас есть следующие товары:")
    for key,value in magazin.items():    
        print(f"{key}-{value}")
    chois=input("Какой товар вы хотите купить? Напишите точь в точь:")
    if chois in magazin:
        if magazin[chois]<=player['money']:
            player['money']-=magazin[chois]
            player['inventory'].append(chois)
            del magazin[chois]
            print(f"Ваш инвентарь:{player['inventory']}")
            print(f"Денег осталось:{player['money']}")
        else:
            print("У вас не достаточно денег(")
            return
    else:
        print("Такого товара нет в магазине( Попробуем заново?")
        chois2=input("Введите да/нет:")
        if chois2=="да":
            shop()
        else:
            return
