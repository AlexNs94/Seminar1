#Задача 1: Найдите сумму цифр трехзначного числа.
#123 -> 6 (1 + 2 + 3)
#100 -> 1 (1 + 0 + 0)



number = int(input("Введите трехзначное число :"))
n1= number % 10
number = number // 10
n2 = number % 10
number = number // 10
print("Сумма цифр числа :",number + n1 + n2)