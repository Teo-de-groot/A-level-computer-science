def phi(n):
    if n == 1: return 1
    if n == 2: return 1
    if n == 4: return 2
    return n - 1

def tower_mod(lst, mod):
    if not lst:
        return 1
    if mod == 1:
        return 0
   

    exp_mod = phi(mod)
    
    exp_val = tower_mod(lst[1:], exp_mod)
    

    if exp_val == 0 and len(lst) > 1:
        exp_val = exp_mod
    if len(lst) == 2 and lst[1] == 0 and lst[0] != 0:
        exp_val = 1 

    return pow(lst[0], exp_val, mod)


def last_digit(lst):
    if not lst:
        return 1
    
    if all(x == 0 for x in lst):
        return 1
    
    cycles = {
        0:[0], 1:[1], 2:[2,4,8,6], 3:[3,9,7,1],
        4:[4,6], 5:[5], 6:[6], 7:[7,9,3,1],
        8:[8,4,2,6], 9:[9,1]
    }

    base = lst[0] % 10
    cycle = cycles[base]
    cycle_length = len(cycle)

    if len(lst) == 1:
        return base
   
    if cycle_length == 1:
        return cycle[0]

    exponent_mod_L = tower_mod(lst[1:], cycle_length)
    
    if index == 0:
        index = cycle_length
        
    return cycle[index - 1]