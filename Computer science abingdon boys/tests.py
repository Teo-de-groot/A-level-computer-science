def euler_phi(n):
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result

def tower_mod(lst, mod):
    
    while len(lst) > 1 and lst[-1] in [0, 1] and not (lst[-1] == 0 and len(lst) >= 2 and lst[-2] == 0):
        lst = (lst[:-2] + [1]) if lst[-1] == 0 else lst[:-1]

    if mod == 1:
        return 0
    if not lst:
        return 1
    
    if len(lst) == 2 and lst[0] == 0 and lst[1] == 0:
        return 1 % mod

    if len(lst) == 1:
        return lst[0] % mod

    ph = euler_phi(mod)
    exp = tower_mod(lst[1:], ph) # This will now call tower_mod([0, 0], ph)

    effective_exp = exp
    if effective_exp == 0:
        effective_exp = ph
    
    base = lst[0]
    if base > 1:
        effective_exp += ph

    return pow(base, effective_exp, mod)

def last_digit(lst):
    if not lst:
        print(4)
        return 1
    if len(lst) == 2 and lst[0] == 0 and lst[1] == 0:
        print(5)
        return 1

    cycles = {
        0: [0], 1: [1], 2: [2,4,8,6], 3: [3,9,7,1],
        4: [4,6], 5: [5], 6: [6], 7: [7,9,3,1],
        8: [8,4,2,6], 9: [9,1]
    }

    base = lst[0] % 10
    cycle = cycles[base]
    length = len(cycle)

    if len(lst) == 1:
        print(6)
        return base

    if length == 1:
        exponent = tower_mod(lst[1:], 1000000000)
        if base == 0 and exponent == 0:
            print(7)
            return 1
        print(8)
        return cycle[0]

    exponent = tower_mod(lst[1:], length)
    if exponent == 0:
        print(9)
        return cycle[-1]
    print(10)
    return cycle[(exponent - 1) % length]
test = last_digit([2,0,2])
print(test)