
hash_arr=[]
for i in range(523):
    hash_arr.append(["", ""])
def hash(en,fr):
    sum = 0 
    key = en 
    for i in range(len(key)):
        sum+= ord(key[i]) * ord(key[i])
    hash = sum%523
    hash_arr[hash][0] =en 
    hash_arr[hash][1] = fr 
def Ha
    french =  hash_arr[hash][1]
hash("PEN", " PLUME")
hash("NOW", "MAINTENANT")
