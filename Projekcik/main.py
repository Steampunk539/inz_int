print("Elo Word")

print("Elo elo 320")
print("Elo elo 320") #dsfdsfsdgdsfg

x="Nat"
y="Szym"
z = 5
print(x)
print(y,z)

x = str(3)  # x will be '3'
y = int(3)  # y will be 3
z = float(3)  # z will be 3.0

x = 5
y = "John"
print(type(x))
print(type(y))

a, b, c = "Mama", "Ata", "Bubu"
print(a)
print(b)
print(c)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
#
x = "awesome"
print("Python is " + x)
#
x = "awesome"
def myfunc():
    global d
    d = " pupa"
    x = "fantastic"
    print("Python is " + x)
myfunc()
print("Python is " + x + d)
print(len(x))

import random
print(random.randrange(1,11)) #między 1 a 10, lol

a = "Hello, World!"
print(a[1]) #pokazuje litere na pozycji 1 (a zaczyna się 0 liczyć)

for x in "banana":
    print(x)

czy_jest = "The best things in life are free!"
print("free" in czy_jest) #indent - wcięcie . . . można też 'not in' i wychidzi true albo false


b = "Hello, World!"
print(b[2:5])                     #llo
print(b[:3])                      #Hel
print(b[2:])                      #llo, World!
print(b.upper())                  #HELLO, WORLD!
print(b.lower())                  #hello, world!
print(b.replace("H", "J"))        #Jello, World!
print(b.split(","))               #['Hello', ' World!']

age = 22
tekst = "My name is Natuś, and I'm {}"
print(tekst.format(age))

txt = "We are the so-called \"Vikings\" from the north." #żeby w cudzysłowiu dać w stringu
print(txt)
x = 200
print(isinstance(x, int))

thislist = ["apple", "banana", "cherry"]     #jeszcze jest insert
thislist.append("orange")
print(thislist)

tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

thislist.remove("banana")       #usuwa to w nawiasach
print(thislist)

thislist.pop(1)                 #usuwa o konkretnym indeksie, jak dam puste bez id to usunie ostatnie
print(thislist)

del thislist[0]                 #działa jak pop
print(thislist)

del thislist                    #usuwa całą listę

thislist = ["apple", "banana", "cherry"]
thislist.clear()                #czyści listę, ale ona dalej istnieje
print(thislist)
print("--------------------------------------")
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

print("--------------------------------------")

i = 1
while i < len(thislist):
  print(thislist[i])
  i = i + 1

print("--------------------------------------")

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

print("--------------------------------------")

newlist1 = [x for x in fruits if "a" in x]      #to samo co na górze, tylko w 1 linijce     [expression for item in iterable if condition == True]
print(newlist1)