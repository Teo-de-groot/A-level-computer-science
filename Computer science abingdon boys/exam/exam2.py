def binary(num):
    if num == 0:
        return "0"
    digits = []
    while num > 0:
        digits.append(str(num % 2))
        num = num//2
    digits.reverse()
    return ''.join(digits)
print(binary(int(input("Enter Intiger for  Decimal to binary: "))))


