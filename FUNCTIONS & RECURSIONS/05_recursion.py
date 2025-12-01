'''
factorial(0)=1
facrorial(1)= 1
facrorial(2)= 2*1
facrorial(3)= 3*2*1
facrorial(4)= 4*3*2*1
facrorial(5)= 5*4*3*2*1
'''
def factorial(n):
    if(n==1 or n==0):
        return 1
    return n * factorial(n-1)

n = int(input("enter a number: "))
print(f"the factorial of this number is :{factorial(n)}")
    


