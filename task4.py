#Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
#если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
#3 2 4 -> yes
#3 2 1 -> no

n = int(input('insert the number N:'))
m = int(input('insert the number M:'))
k = int(input('insert the number K:'))

if k % n == 0 or k % m == 0:
    print ('yes')
else :
    print ('no')