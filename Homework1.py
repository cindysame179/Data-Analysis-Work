import math
#Cindy Juan 
#CSCI 381 Data Analytics 
#Homework 1

#Problem 14 
def collatzRule(num):
    if num%2 == 0:
        return num//2
    else:
        return 3*num+1

def LongestCollatzChain():
    longestChain = 0
    longestChainNum = 0
    for i in range(1,1000000):
        chainLen = 0
        num = i
        while num != 1:
            chainLen += 1
            num = collatzRule(num)
        if chainLen > longestChain:
            longestChain = chainLen
            longestChainNum = i
    print(f'The Longest Collatz chain has a length of {longestChain} with starting number {longestChainNum}')

#Problem 20
def DigitSumof100Factorial():
    factorial = math.factorial(100)
    sum = 0
    for i in str(factorial):
        sum += int(i)
    print (f'The sum of the digits of 100! is: {sum}')

#problem 17
def NumLetterset(num):
    Keypad = ['',
    'abc',
    'def',
    'ghi',
    'jkl',
    'mno',
    'pqrs',
    'tuv',
    'wxyz']
    PowerSet = []
    for digit in num:
        PowerSet = SetCreate(Keypad, PowerSet, digit)
    print(PowerSet)



def SetCreate(Keypad, Powerset, digit):
    if len(Powerset) == 0:
        return list(Keypad[int(digit)-1])

    temp = []
    for i in Powerset:
        for j in Keypad[int(digit)-1]:
            temp.append(i+j)
    return temp

#problem 11
def WaterTankArea(Heights):
    set = Heights.split(",")
    intSet = [int(num) for num in set]
    r = len(set) - 1
    maxArea = 0
    while r != 0:
        for i in range(r):
            if intSet[i] < intSet[r]:
                height = intSet[i]
                length = r-i
                area = length * height
            else:
                height = intSet[r]
                length = r-i
                area = length * height
            if maxArea < area:
                maxArea = area
        r -= 1
    print(f'The max area for a Water tank from the given set is: {maxArea}')

def main():
    #input for problem 17
    bool = True
    while bool:
        num = input("please input your number (should not contain 1):")
        if not num.isnumeric() or '1' in num:
            print('not a valid number')
        else:
            bool = False
    #input for problem 11
    Heights = input("Please input a set of numbers seperated by , :")

    #Finds longest Collatz chain for a starting number under 1 million
    LongestCollatzChain()
    #Calculates the sum of the digits of 100!
    DigitSumof100Factorial()
    #generates the powerset of letters from the given combination of digits
    NumLetterset(num)
    #finds the largest area of a watertank with the dimensions provided in the set
    WaterTankArea(Heights)

if __name__ == "__main__":
    main()