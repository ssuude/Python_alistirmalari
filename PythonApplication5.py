
"""
ax^2+bx+c seklindeki ikinci dereceden bir denklemin koklerini bulan program
"""

from typing import cast


print("a*x^2+b*x+c seklinde bir denklem icin katsayi degerlini giriniz.")
a=int(input())
b=int(input())
c=int(input())

# Delta= b^2-4*a*c
delta=b**2+4*a*c 
# Kokler = (-b+(delta**0.5))//(2*a)
x1=(-b+(delta**0.5))//(2*a)
x2=(-b-(delta**0.5))//(2*a)
if(delta==0):
    print("Kok cift katli koktur.")
elif(delta>0):
    print("Kok vardir ve kokler birbirinden farklidir.")
else:
    print("Gercek kok yoktur.")