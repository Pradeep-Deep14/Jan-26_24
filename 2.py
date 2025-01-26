count = 1

def doThis():
    global count


    for i in range(1,5,10):
        count +=10

doThis()
print(count)