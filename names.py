#Тест работы с именами
import random
lines = open('/home/kasrkad/git-repo/munchkin_console/names.txt').read().splitlines()
myline =random.choice(lines)
print(myline)
