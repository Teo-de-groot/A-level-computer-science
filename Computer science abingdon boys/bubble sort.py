def intput(inputs):
    a = input(inputs)
    T=1
    while T==1:
        try:
         a=int(a)
         T=0
        except ValueError:
            T=1
    return(a)
def bubble(array):

    length = len(array)
    changes = 1

    while changes == 1:
        changes = 0
        for i in range(length - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                changes = 1
    return array
def test():
    array= []
    Continue = True
    while Continue ==True:
        arr = intput("what number: ")
        array.append(arr)
        continues= input("type no to exit:")
        if continues== "no":
            Continue=False
    array = bubble(array)
    print(array)
test()