import csv
from colorama import init
from colorama import Back

init(autoreset=True)
d = 0
f_before150 = 0
s_after150 = 0
with open('books.csv', "r") as csvfile:
    table = csv.reader(csvfile, delimiter=";")
    for row in table:
        if d > 0:
            if float(row[7] [:-3]) <= 150:
                f_before150 += 1
            else:
                s_after150 += 1
        d += 1
print(f_before150 / (f_before150 + s_after150), s_after150 / (f_before150 + s_after150))
# print(Back.BLACK + '   ')
# print(Back.BLACK + '   ')
# print(Back.BLACK + '   ')
# print(Back.BLACK + '   ')
# print(Back.BLACK + '   ')
# print(Back.BLACK + '   ')
# print(Back.BLACK + '   ')
# print(Back.BLACK + '   ')
# print(Back.BLACK + '   ')
# print(Back.BLACK + '   ')
# print(Back.BLACK + '   ')
# print(Back.BLACK + '   ')
# print(Back.BLACK + '   ')
# print(Back.BLACK + '   ')
# print(Back.BLACK + '   ' + Back.LIGHTWHITE_EX + '    ' + Back.BLACK + '   ')
# print(Back.BLACK + '   ' + Back.LIGHTWHITE_EX + '    ' + Back.BLACK + '   ')
# print(Back.BLACK + '   ' + Back.LIGHTWHITE_EX + '    ' + Back.BLACK + '   ')
# print(Back.BLACK + '   ' + Back.LIGHTWHITE_EX + '    ' + Back.BLACK + '   ')


print(Back.BLACK + '                                         ') #ALL
print(Back.LIGHTWHITE_EX + '                        ') #f_before150
print(Back.RED + '           ') #s_after150
