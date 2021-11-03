import time

first_num = 1000
while first_num>=0:
    second = first_num-7
    print(first_num , "- 7 = " , second)
    time.sleep(0.3)
    first_num = second
