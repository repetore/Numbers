#factorial without Math lib

number = int(input("Enter ur num"))

def fact(x):
    if x == 1:
        return 1
    return x*fact(x-1)
print(fact(number))