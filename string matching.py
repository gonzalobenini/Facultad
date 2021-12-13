import math


# Ravin karp

def textoAsciiAListaDeEnteros(string):
    return [ord(char) for char in string]

def ravinKarp(texto,patron):
    texto = textoAsciiAListaDeEnteros(texto) ### si el patron y el texton
    patron = textoAsciiAListaDeEnteros(patron) # son los dos cadenas de caracteres, sino se comentan estas dos lineas y se usan lista de enteros como entrada
    base = 10
    q = 11
    n = len(texto)
    m = len(patron)
    h = pow(base,m-1)
    h = h % q
    p = 0
    t = 0
    matchings = []
    for i in range(m):
        p = ((base*p) + patron[i]) % q
        t = ((base * t) + texto[i]) % q
    for s in range((n-m)+1):
        if p == t:
            if texto[s:s + m] == patron:
                matching.append(s)
        if s < (n-m):
            t = base * (t - (texto[s] * h))
            t += texto[s + m]
            aux = math.floor(t / q)
            t = (t - q * aux)
    return matchings
	
	
# knuth-morris-prat

def computePrefixFunction(patron):
    m = len(patron)
    pi = [0]
    k = 0
    for q in range(1,m):
        while (k>0) and (patron[k] != patron[q]):
            k = pi[k]
        if patron[k] == patron[q]:
            k = k + 1
        pi.append(k)
    return pi

def kmp(texto, patron):
    n = len(texto)
    m = len(patron)
    q = 0
    pi = computePrefixFunction(patron)
    matchings = []
    for i in range(n):
        while q>0 and patron[q]!=texto[i]:
            q = pi[q]
        if patron[q] == texto[i]:
            q = q + 1
        if q == m:
            matchings.append((i-m)+1)
            q = pi[q-1]
    return matchings
	

# automata finito deterministico para reconocer las cadenas del lenguaje
	
	
def obtenerAlfabeto(cadena):
    return str("".join(set(cadena)))

def computeTransitionFunction(patron, alfabeto):
    m = len(patron)
    n = len(alfabeto)
    D = [[] for i in range(m)]
    for q in range(m):
        for char in alfabeto:
            if m+1 < q+2:
                k = m + 1
            else:
                k = q + 2
            noEsSufijo = True
            while noEsSufijo:
                k = k-1
                noEsSufijo = not(patron[0:q] + char).endswith(patron[0:k])
            D[q].append(k)
    D.append([0 for i in range(n)]) # carga final para que no quede un indice fuera de rango
    return D

def automataFinito(texto,patron):
    print("automata")
    m = len(patron)
    n = len(texto)
    alfabeto = obtenerAlfabeto(patron)
    alfabeto = "".join(sorted(alfabeto))  # hace la union con la misma string pero ordenada y en la union se elige el orden del argumento
    funTransicion = computeTransitionFunction(patron,alfabeto)
    q = 0
    matchings = []
    for i in range(n):
        if texto[i] in alfabeto: # agrega complejidad y no es necesario si el si el alfabeto del texto es el mismo que el del patron o si la funcion de transicion de estados envia al estado 0 para los caracteres en la diferencia simetrica de el alfabeto del texto y el del patron
            q = funTransicion[q][alfabeto.index(texto[i])]
        else:
            q = 0
        if q == m:
            matchings.append((i-m)+1)
    return matchings	
	