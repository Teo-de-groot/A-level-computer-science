#binary =lambda x: bin(x)[2:]
#print(binary(2))

def intput(x):
    """interger input with error handling"""
    y=0
    while y !=1:
        try:
            return int(input(x))
        except ValueError:
            print("Invalid input. Please enter an integer.")



def binary_sucessive_division(n):
    if n == 0:
        return "0"
    bits = []
    while n > 0:
        bits.append(str(n % 2))
        n //= 2
    bits.reverse()
    return ''.join(bits)
print(binary_sucessive_division(intput("Enter an integer: ")))