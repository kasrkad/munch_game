#Манчкин в консоли
import random

class Monster :
    def __init__(self, name):
        self.name=name
    level=random.randrange(1,2)
    gold=random.randrange(100,400)
    run_away_mod=random.randrange(0,2)
    def show_enemy_params(self):
        print ("\n Имя монстра: {0} \n Уровень монстра: {1} \n Золото за победу: {2} \n Модификатор смывки : -{3}".format(self.name, self.level, self.gold, self.run_away_mod))
class Player :
    def __init__(self, name):
        self.name=name
        print ("\n Привет манчкин {0}, здесь начинается твой поход в подземелье".format(self.name))
    level=1
    gold=150
    run_away_mod=3
    def show_params (self):
        print ("\nТвой уровень {0}, \nв твоем кошельке {1} золота, \nа базовый шанс сбежать {2}".format(self.level, self.gold, self.run_away_mod))

def d6_roll():
    return random.randrange(1,6)

def get_monster_name():
    lines = open('/home/kasrkad/git-repo/munchkin_console/names.txt').read().splitlines()
    myline =random.choice(lines)
    return myline

hero = Player(input('Введите имя вашего манчкина: '))
hero.show_params()
if (input("Начнем наше приключение? Да/Нет ").lower()) == "да":
    while hero.level<20:
        print ("Вы встречаете монстра:")
        enemy = Monster(get_monster_name())
        enemy.show_enemy_params()
        if input("Ваши действия?\n 1.Драться \n 2.Сбежать \n") == "1":
            print ("Вы решили драться")
            hero_roll=hero.level+d6_roll()
            enemy_roll=enemy.level+d6_roll()
            print ("Ваш бросок {0}, Бросок монстра {1}".format(hero_roll, enemy_roll))
            if hero_roll>enemy_roll:
                print("Монстр {} побежден! Вы получаете уровень и {} золота ".format(enemy.name,enemy.gold))
                hero.gold+=enemy.gold
                hero.level+=1
            else:
                lose_gold=random.randrange(1,hero.gold)
                print ("Монстр надругался над вами! Вы потеряли {} золота".format(lose_gold))
                hero.gold-=lose_gold
        else:
            print ("Пытаетесь сбежать! ")
            hero_roll=hero.run_away_mod+d6_roll()
            enemy_roll=enemy.run_away_mod+d6_roll()
            if hero_roll>enemy_roll:
                print("Вы успешно сбежали!")
            else:
                lose_gold=random.randrange(1,hero.gold)
                print ("Вы не смогли сбежать и Монстр надругался над вами! Вы потеряли {} золота".format(lose_gold))
                hero.gold-=lose_gold
        if (input("Продолжаем приключение? Да/Нет ").lower()) == "да":
            hero.show_params()
            continue
        else:
            print ("Вы позорно сбежали")
            break
