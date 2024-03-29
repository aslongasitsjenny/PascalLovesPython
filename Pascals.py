print("Exercise 1")
def fact(n): #this gets the factorial
    fact = 1
    for num in range(2, n + 1): 
        fact *= num
    return fact

for n in range(10, 0,-1):
   print('\n')
   print((-1 * n), end = ' ')
   for k in range(0, 11):
      cn = n + k - 1
      numerator = fact(n+k-1)
      denominator = fact(k) * fact(cn-k) #this gets the denom with the fact function
      result = (numerator/denominator)  #num /denom = stores the result in the result variable
      nsign = pow(-1, k)
      result = result * nsign
      print(f"{result:.0f}",end = ' ') # use f"{result:.0f}" to print numbers to 0f decimal point #print(f"{result:.0f}", end=' ') # example - use 3f instead of 0f to print to 3 numbers after decimal poin
print('\n')
print("Exercise 1 : Part B") 

def fact(n):#this is the factorial code
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact

def convtosuper(n): #this is how to get the supercode ascending[power ascending]
    super=list(map(chr,[8304,185,178,179,8308,8309,8310,8311,8312,8313]))
    supersign = list(map(chr, [8315]))
    st=""
    st+=supersign[int(0)]
    for i in str(n):
        st+=super[int(i)]
    return(st)

for n in range(1, 11): # this is to calculate the final result
   print('\n')
   threesuper = "3" + convtosuper(n)
   print(threesuper, end = ' ')
   for k in range(0, 1000): #the code will run until 0,1000
      cn = n + k - 1
      numerator = fact(n+k-1) 
      denominator = fact(k) * fact(cn-k) #fact = factorial 
      result = (numerator/denominator) #num divided by denom to get the final result
      nsign = pow(-1, k) #the power that ranges from -1 to what K is
      result = result * nsign
      result = result + pow(2, (-n-k))
   print(result, end = ' ')


print('\n')
print("Exercise 2")
preceding_1 = 3                             # first preceding number
preceding_2 = 4                             # second preceding number
sequence_number = 0                         # sequence number

calus_minimum = 100                         # calus minimum
calus_maximum = 1000000                     # calus maximum

line_items = 0                              # number of items to print on each line

# run code while the sequence_number is less than the calus_maximum
while sequence_number < calus_maximum:
    sequence_number = preceding_1 + preceding_2
    preceding_1 = preceding_2
    preceding_2 = sequence_number
    if sequence_number > calus_maximum:
        break

# test if the number of line items required has been reached and sequence_number is greater than the calus_minimum
    if line_items < 5 and preceding_2 >= calus_minimum:
        print(preceding_2, end=(" "))
        line_items +=1
    else:
        if preceding_2 >= calus_minimum:
           print("\n")
           print(preceding_2, end=(" "))
           line_items = 1

print('\n')
print("Exercise 3")

number1 = int(input("Enter the first number:"))
number2 = int(input("Enter the second integer:"))

a = 12
b = 48
n = 0
sumofodd = 0

print("The Odd Common Divisors are:")

for i in range(1, min(number1, number2) + 1):
    if number1 % i == b % i == 0: 
        if (i % 2) == 0: 
            print("{0} is Even".format(i))#if it's even, it prints out "is even"
        else:
            print("{0} is Odd".format(i)) #if it's odd, it prints out "is odd"
            sumofodd = sumofodd + i 
    n += 1

print("The Sum of Odd Common Divisors is:", sumofodd)


print("Exercise 4")
reverse = 0 #reverse number
number = int(input("Please enter an input number:"))

while number > 0: # does the calculation whilst the number is above 0

    quote = (number%10) # quotient of the inputted number
    number = number // 10 #dividing the inputted number by 10
    reverse = (reverse*10+quote) #multiplying the remainder of number by 10 

print("The reversed number is:", reverse)

