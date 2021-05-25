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

    #devuelve una lista de sublistas [elemento, exponente] que son los factores primos y sus exponentes del numero argumento
    def factorize(this, n):
        L = [] #lista con la factorizacion del numero, en forma de sublistas [primo, exponente]
        i = 0 #numero de pares [primo, exponente] en L
        flag = 0 #condicion de parada
        
        if(n == 1):
            return [[1, 1]]

        while (flag == 0):
            [primerPrimo, cociente] = this.firstPrimeFactor(n)
            if cociente == 1: flag = 1

            L.append(primerPrimo)
            n = cociente

        return this.countListAppearances(L)

    #minimo comun multiplo de los elementos pasados en la lista argumento
    def mcm(this, L):
        primes = []
        exponents = []
        res = 1

        for num in L:
            factors = this.factorize(num)
            for duple in factors:
                if (duple[0] not in primes): #si el primo no estaba ya en la lista lo metemos en la lista de primos
                    primes.append(duple[0])
                    exponents.append(duple[1])
                elif (exponents[primes.index(duple[0])] < duple[1]): #si estaba, pero con exponente menor, lo modificamos por el mayor
                    exponents[primes.index(duple[0])] = duple[1]

        for i in range(len(primes)):
            res *= primes[i]**exponents[i]

        return res

    #devuelve una lista de factores primos del numero argumento
    def primeFactors(this, n):
        L = set() #lista con la factorizacion del numero, en forma de lista [primo1, primo2, ..., primoN]
        L.add(1)
        L.add(n)

        i = 0 #numero de factores en L
        flag = 0 #condicion de parada
        
        if(n == 1):
            return [1]

        while (flag == 0):
            [primerPrimo, cociente] = this.firstPrimeFactor(n)
            if cociente == 1: flag = 1

            L.add(primerPrimo)
            n = cociente

        return list(L)

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

    #minimo comun multiplo de los elementos pasados en la lista argumento
    def MCD(this, L):
        primes = []
        exponents = []
        res = 1
        CommonFactors = this.commonFactors(L)

        for num in L:
            factors = this.factorize(num)
            for duple in factors:
                if(duple[0] in CommonFactors):
                    if (duple[0] not in primes): #si el primo no estaba ya en la lista lo metemos en la lista de primos
                        primes.append(duple[0])
                        exponents.append(duple[1])
                    elif (exponents[primes.index(duple[0])] > duple[1]): #si estaba, pero con exponente mayor, lo modificamos por el menor
                        exponents[primes.index(duple[0])] = duple[1]

        for i in range(len(primes)):
            res *= primes[i]**exponents[i]

        return res