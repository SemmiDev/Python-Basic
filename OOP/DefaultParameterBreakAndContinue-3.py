# default parameter
def method(num1=5, num2=3):
    result = num1 + num2
    print(result)


def main():
    method(2, 3)


main()


# break

def method2(num1=1, num2=20, num3=30):
    for x in range(num1, num2 + 1):
        print(x)
        if x == 10:
            continue
            print("continue")
        else:
            print("not continue")

        if  x == 13:
            break

method2()
