from fractions import Fraction

number = Fraction(input("Enter a number: "))
bits = []
seen = set()

while True:
    number *= 2
    if number >= 1:
        bits.append('1')
        number -= 1
    else:
        bits.append('0')

    if number == 0:
        break

    if number in seen:
        bits.pop(-1)
        bits.append('To infinity and Beyond')
        break

    seen.add(number)

print("0." + "".join(bits))
