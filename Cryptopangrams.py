import string
import math
import copy
from collections import OrderedDict


def Primes(N):
    numbers = []
    for number in range(3, N):
        is_prime = True
        for i in range(2, (number // 2) + 1):
            if (number % i) == 0:
                is_prime = False
                break
        if is_prime:
            numbers.append(number)
    return numbers


alphabet = list(string.ascii_uppercase)
T = int(input("Please enter T: "))
for i in range(T):
    N = int(input("\n\nPlease enter N: "))
    L = int(input("Please enter L: "))
    print("Please enter the Cipher Text: ", end="")
    cipher_text = list(map(int, input().strip().split()))[:L]

    prime_numbers = Primes(N)
    plaintext = []

    first_GCD = math.gcd(cipher_text[0], cipher_text[1])
    next_prime = cipher_text[0]/first_GCD

    for index in range(L):
        plaintext.append(next_prime)
        next_prime = cipher_text[index] / next_prime
    plaintext.append(next_prime)

    plaintext2 = copy.deepcopy(plaintext)
    plaintext2.sort()
    plaintext2 = list(OrderedDict.fromkeys(plaintext2))

    dictionary = {}
    for p in range(26):
        dictionary[plaintext2[p]] = alphabet[p]

    print("Case", T, ": ", end="")
    for m in plaintext:
        print(dictionary[m], end="")
