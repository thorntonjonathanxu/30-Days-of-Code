import sys

def HelloWorld():
    print('Hello World!')

def listTest():
    ar = []
    i = 0
    while(i < len(ar)):
        print (i)
        i += 1
    print ('Count = ' + str(i))

def modTest(n,mod):
    result = mod % n
    print(result)
HelloWorld()
listTest()
modTest(3,6)