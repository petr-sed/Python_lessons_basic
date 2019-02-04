#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""
import random
class Game:
    def rand_nrs(self):
        list_nrs = []
        while len(list_nrs) < 15:
            i = random.randint(1, 90)
            if i not in list_nrs:
                list_nrs.append(i)
        list_nrs1, list_nrs2, list_nrs3 = Game.list_splitter(list_nrs)
        list_nrs.clear()
        list_nrs1.sort()
        list_nrs2.sort()
        list_nrs3.sort()
        list_nrs = list_nrs1 + list_nrs2 + list_nrs3
        return list_nrs

    def list_splitter(self:list):
        list_nrs1 = self[:5]
        list_nrs2 = self[5:10]
        list_nrs3 = self[10:]
        return list_nrs1, list_nrs2, list_nrs3

    def del_nrs(self, list_nrs, nr):
        if nr in list_nrs:
            ind = list_nrs.index(nr)
            list_nrs.pop(ind)
            list_nrs.insert(ind,'-')
            return 1
        else:
            return 0

    def asker(self):
        answ = input("Do you want to strike number? Y/N")
        return answ

    def formater(self:list):
        output = ''
        out_sum = 23
        for i in range(1, 6):
            i = self[-i]
            ch = int(round(out_sum / 4, 0))
            output = "{}{}".format( ' ' * ch, i) + output
            out_sum = (out_sum - ch) - len(str(i))
        print(output)


    def presenter(self, ticket_1, ticket_2):
        list_nrs1, list_nrs2, list_nrs3 = Game.list_splitter(ticket_1)
        print('-'*6+"Your ticket"+'-'*6)
        Game.formater(list_nrs1)
        Game.formater(list_nrs2)
        Game.formater(list_nrs3)
        list_nrs1, list_nrs2, list_nrs3 = Game.list_splitter(ticket_2)
        print('-' * 4 + "Computer ticket" + '-' * 4)
        Game.formater(list_nrs1)
        Game.formater(list_nrs2)
        Game.formater(list_nrs3)

    def randomer(self):
        count = 0
        while count == 0:
            number = random.randint(1, 90)
            if number in list_kegs:
                list_kegs.remove(number)
                print("New keg: {}".format(number))
                count = 1
                return number

    def deceding(self, ans, res, number):
        if ticket_pers.count('-') != 15 and ticket_comp.count('-') !=15:
            if (ans == "Y" and res == 1) or (ans == "N" and res == 0):
                game.del_nrs(ticket_comp, number)
                number = game.randomer()
                game.presenter(ticket_pers, ticket_comp)
                ans = game.asker()
                res = game.del_nrs(ticket_pers, number)
                game.deceding(ans, res, number)
            else:
                print("You lose")
        elif ticket_pers.count('-') == 15:
            print("You win!")
        elif ticket_comp.count('-') == 15:
            print("Computer wins")

game = Game()
ticket_pers = game.rand_nrs()
ticket_comp = game.rand_nrs()
list_kegs = list(range(1,91))
number = game.randomer()
game.presenter(ticket_pers, ticket_comp)
ans = game.asker()
res = game.del_nrs(ticket_pers, number)
game.deceding(ans, res, number)

