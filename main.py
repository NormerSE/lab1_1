def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    x = int(input("Введите первое число: "))
    y = int(input("Введите второе число: "))
    print("НОД =", gcd(x, y))
    input()
