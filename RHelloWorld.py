print("Hello World!") 
print("I am very excited for this FRC Season!")

z = input("What operation do you want to do? (Types: Multiply, Add, Subtract y - x, Subtract x - y, Divide x by y, Divide y by x, Exponets x ^ y, Exponets y ^ x, Compare x < y, Compare x > y, Compare x = y, Average) ")
if (z == "Average") or z == "average":
    numinput = int(input("How many numbers are you using? "))
    def calcAvg(numinput):
        sum = 0
        count = 0
        while count < numinput:
            num = int(input("Please enter a number: "))
            sum = sum + num
            count = count + 1
        average = sum / numinput
        print(average)
if (z == "Average") or z == "average":
    x = 0
    y = 0
else:
    x = int(input("What is your first number? (x) "))
    y = int(input("What is your second number? (y) "))
ansadd = x + y 
anssub = x - y
anssubtwo = y - x
ansmult = x * y
ansdiv = x / y
ansdivtwo = y / x
anscomp = x > y
anscomptwo = x < y
anscompthree = x == y
ansexpo = x ** y
ansexpotwo = y ** x
if (z == "Multiply") or z == "multiply":
    print(ansmult)
elif (z == "Add") or z == "add":
    print(ansadd)
elif (z == "Subtract y - x") or z == "subtract y - x":
    print(anssubtwo)
elif (z == "Subtract x - y") or z == "subtract x - y":
    print(anssub)
elif (z == "Divide x by y") or z == "divide x by y":
    print(ansdiv)
elif (z == "Divide y by x") or z == "divide y by x":
    print(ansdivtwo)
elif (z == "Compare x < y") or z == "compare x < y":
    print(anscomptwo)
elif (z == "Compare x > y") or z == "compare x > y":
    print(anscomp)
elif (z == "Compare x = y") or z == "compare x == y":
    print(anscompthree)
elif (z == "Exponets x ^ y") or z == "exponets x ^ y":
    print(ansexpo)
elif (z == "Exponets y ^ x") or z == "exponets y ^ x":
    print(ansexpotwo)