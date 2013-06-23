# Code by Trinity Allen, 2013/06/22
# Written for Python 2.7.2
# Objective: Find the 10001st prime number to solve Project Euler
#problem 7 using the Sieve of Atkin Algorithm.
import math

def sieveOfAtkins(limit): # Creates a list of primes up to a given number
    primes = [2,3,5] #initialize the list of primes
    sieve = [False]* (limit + 1) #initialize the sieve with all values set to "not-prime"
    testRange = int(math.sqrt(limit)) + 1
    
    # Determine potential Primes
    for x in range(1,testRange):
        for y in range(1,testRange):
          
            n = 4*(x**2) + y**2
            if (n <= limit) and (n % 12 == 1 or n % 12 == 5):
                sieve[n] = not sieve[n]
                
            n2 = 3*(x**2) + y**2
            if (n2 <= limit) and (n2 % 12 == 7):
                sieve[n2] = not sieve[n2]
            
            n3 = 3*(x**2) - y**2
            if (x > y) and (n3 <= limit) and (n3 % 12 == 11):
                sieve[n3] = not sieve[n3]   
    
    # Eliminate Composites
    for i in range(5,testRange):
        if sieve[i]:
            for number in range(i**2, limit, i**2):
                sieve[number] = False
    
    #Create list of primes
    for i in range(7,limit):
        if sieve[i]:
            primes.append(i)
    return primes

def findPrime(number): # Find the nth prime number
    nthPrimeApprox = number * (math.log(number) + math.log(math.log(number)))
    return sieveOfAtkins(nthPrimeApprox)[number - 1]

