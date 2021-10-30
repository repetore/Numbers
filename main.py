### find the num game

import random as rand

borders = int(input("Enter max number to play: "))
### checking correct border
if borders >= 2:
  pass
else:
  print("Please enter a num between 2 and infinity!")
  borders = int(input("Enter max number to play: "))


num = rand.randint(1, borders)

test_num = int(input("Press any num to begin"))

while test_num != num:
  test_num = int(input("Try any num!"))
  if test_num == num:
    print("WIN!!!")
    break
  if test_num < num:
    print("Enter smth bigger!")
  if test_num > num:
    print("Enter smth smaller!")


