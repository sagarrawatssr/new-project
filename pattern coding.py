
a=" "

def main():
    n=int(input("enter the no."))
    b=input("enter the symbol you want to print")
    for i in range(n):
        for j in range(n-i-1):
            print(a,end="")
        for k in range(2*i+1):
            print("*",end="")
        print()
    g=n-1
    for i in range(n-1):
        for j in range(i+1):
            print(a,end="")
        for k in range(2*g-1):
            print("*",end="")
        print()
        g-=1
    ab=input("want to repeat")
    if ab[0]=='y':
         main()
    else:
        print("thanks for using our service")
main()

