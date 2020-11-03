
#Gennadi Ivanov 3.10.20
#1
print('enter value a,')
a = int(input())
print('enter value b,')
b = int(input())
print('enter value c,')
c = int(input())
p = a+b+c
print(p)

#2

d = 36.75
s = d / 100 * (100-40) * 3
print(s)

#3

p = 12.9
o = 10
c = p/100*10
s = p + c /3
print('каждый должен заплатить', round(s,3))


#4
import math
a =int(input('enter value a'))
b =int(input('enter value b'))
print(math.sgrt(a*a +b*b ))

#5

a =int(input('литр топлива'))
b =int(input('пройденные километры'))
result = a/b =100
print(result)

#6
print('enter value')
dec= int(input())
b = bin(dec)
o = oct(dec)
h = hex(dec)
print(f'bin{b}/hex{h}/oct{o}')

#7
k = 29.9/60*24
print('проедит за 24 мин, при средней скорости 29,9км/ч')
print(round(k,2))





