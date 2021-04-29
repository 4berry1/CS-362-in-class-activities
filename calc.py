def main():
    x = int(input("enter 1st value: "))
    y = int(input("enter 2nd value: "))
    mode = int(input(" 1 - add \n 2 - sub \n 3 - divide \n 4 - multiply \n :"))
    
    if (mode == 1):
        ans = x + y
        print (ans)
    if (mode == 2):
        ans = x - y
        print (ans)
    if (mode == 3):
        ans = x / y
        print (ans)
    if (mode == 4):
        ans = x * y
        print (ans)

    
main()


