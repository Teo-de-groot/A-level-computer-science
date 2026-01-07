def intput(a):
    """Returns the intiger version of the input"""
    return int(input(a))
import statistics
store = []
num_digits = intput("number of digits: ")
for i in range(num_digits):
    digit = intput("digit: ")
    store.append(digit)
a = statistics.multimode(store)
if len(a) > 1:
    print("Data was multimodal")
else:
    a=str(a)
    a=a.replace("[","")
    a=a.replace("]","")
    a=int(a)
    print(store.count(a))
    #Question 1 
#x = int(input("Enter an integer greater than 1: ")) 
#Product =1
#Factor = 0
#while Product < x:
 #   Factor = Factor + 1
#    Product = Product * Factor
#if x == Product:
 #   Product = 1
#    for n in range(1,Factor+1):
#        Product = Product * n
#        print(n)
#else:
#    print("no result")
