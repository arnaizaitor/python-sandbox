from collections import Counter

class PrimeFunctionalities():

    ################################################################################
    # arguments: The number n of which we want to know its lesser prime factor 
    #            (different from one)
    # returns: A list containing [firstPrime, quotient]
    ################################################################################
    def firstPrimeFactor(this, n):
        for i in range(2, n+1):
            if(n%i == 0):
                return [i, int(n/i)]


    ################################################################################
    # arguments: L: generic list from which we want to count its elements appearances
    # returns: res: A list made of sublists [element, appearances] in the argument list
    ################################################################################
    def countListAppearances(this, L):
        d = []
        res = []
        for elem in L:
            if elem not in d:
                d.append(elem)
                res.append([elem, L.count(elem)])
        return res


    ################################################################################
    # arguments: n: number to factorize
    # returns: A list made of sublists [element, exponent] of the argument prime factors
    ################################################################################
    def factorize(this, n):
        L = [] #list with the factorization of the argument number made of sublists [prime, exponent]
        i = 0 #number of pairs [prime, exponent] in L
        flag = 0 #stop condition
        
        if(n == 1):
            return [[1, 1]]

        while (flag == 0):
            [primerPrimo, cociente] = this.firstPrimeFactor(n)
            if cociente == 1: flag = 1

            L.append(primerPrimo)
            n = cociente

        return this.countListAppearances(L)


    ################################################################################
    # arguments: n: number to get its divisors
    # returns: A list made of all its divisors, including itself and one
    ################################################################################
    def divisors(this, n):
        divs = []
        for i in range(1,int(n/2)+1):
            if n%i == 0: divs.append(i)             
        divs.append(n)

        return divs


    ################################################################################
    # arguments: L: List of numbers to find its min common multiple
    # returns: res: Minimum common multiple of the numbers in the argument list
    ################################################################################
    def mcm(this, L):
        primes = []
        exponents = []
        res = 1

        for num in L:
            factors = this.factorize(num)
            for duple in factors:
                if (duple[0] not in primes): # if the prime wasnt in the list of primes, we include it in the list
                    primes.append(duple[0])
                    exponents.append(duple[1])
                elif (exponents[primes.index(duple[0])] < duple[1]): #if it was, but with lesser exponent, we change it by the on with the greater
                    exponents[primes.index(duple[0])] = duple[1]

        for i in range(len(primes)):
            res *= primes[i]**exponents[i]

        return res

    ################################################################################
    # arguments: n: Number of which we want to know its prime factors
    # returns: L: listed set of the prime factors of the argument number
    ################################################################################
    def primeFactors(this, n):
        L = set() #listed set of the prime factors of the argument number,  listed as [prime1, prime2, ..., primeN]
        L.add(1)
        L.add(n)

        i = 0 #number of factors in L
        flag = 0 #stop condition
        
        if(n == 1):
            return [1]

        while (flag == 0):
            [primerPrimo, cociente] = this.firstPrimeFactor(n)
            if cociente == 1: flag = 1

            L.add(primerPrimo)
            n = cociente

        return list(L)


    ################################################################################
    # arguments: L: List of numfers of which we want to know their common factors
    # returns: CommonFactors: listof common factors of the numbers in the input list
    ################################################################################
    def commonFactors(this, L):
        CommonFactors = []

        F = []
        for number in L:
            for primeFactor in this.primeFactors(number):
                F.append(primeFactor)

        A = this.countListAppearances(F)

        for factor, apariciones in A:
            if(apariciones == len(L)):
                CommonFactors.append(factor)

        return CommonFactors


    ################################################################################
    # arguments: L: List of numbers to find its max common divisor
    # returns: res: Max common divisor of the numbers in the argument list
    ################################################################################
    def MCD(this, L):
        primes = []
        exponents = []
        res = 1
        CommonFactors = this.commonFactors(L)

        for num in L:
            factors = this.factorize(num)
            for duple in factors:
                if(duple[0] in CommonFactors):
                    if (duple[0] not in primes): # if the prime wasnt in the list of primes, we include it in the list
                        primes.append(duple[0])
                        exponents.append(duple[1])
                    elif (exponents[primes.index(duple[0])] > duple[1]): #if it was, but with greater exponent, we change it by the on with the lesser
                        exponents[primes.index(duple[0])] = duple[1]

        for i in range(len(primes)):
            res *= primes[i]**exponents[i]

        return res