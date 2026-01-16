#!/usr/bin/env python3
print("Dwse 2 akeraious arithmous")

flag=1
while(flag):
    a=input("Dwse ton prwto arithmo ")
    b=input("Dwse ton deutero arithmo ")
    if a.lstrip('-').isdigit() and b.lstrip('-').isdigit():
        a = int(a)
        b = int(b)
        print("To apotelesma tou", a," + ", b," einai", a+b)
        flag=0
    else:
        print("Den edwses akeraious ksanaprospathise")
