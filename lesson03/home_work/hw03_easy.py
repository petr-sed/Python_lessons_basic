# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
   number = int(number*(10**(ndigits+1)))
   if number%10 >= 5:
       number = number//10+1
   else:
       number = number//10
   number = number/(10**ndigits)
   return(number)


print(my_round(2.1234567, 2))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 13))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
   list_ticket = list(map(int,str(ticket_number)))
   if sum(list_ticket[:3]) - sum(list_ticket[3:]) == 0:
       return("Счастливый билет")
   else:
       return("Попробуйте еще")

print(lucky_ticket(123006))
print(lucky_ticket(123217))
print(lucky_ticket(436751))
