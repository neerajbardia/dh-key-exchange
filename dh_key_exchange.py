#diffie hellman key exchange
#this is a single file with the sender and the reciever functions, this file can be split into two separate files and made to communicate through socket programming to enable
#transfer of data. Socket programming and diffie hellman key exchange algorithm together can be very helpful to undestand the use of diffie hellman. Also there can be a
#middle-man too who can alter the messages and hence check if the algorithm is actually working or not.


import random
import sys
from math import sqrt
sys.setrecursionlimit(10**6)

prime_no=int(input("Enter the prime no:"))
private_s=47                                                        #input of two private keys s stands for sender, r stands for reciever
private_r=53

def isPrime( n):                                                    #checking if a no is prime or not

	if (n <= 1): 
		return False
	if (n <= 3): 
		return True

	if (n % 2 == 0 or n % 3 == 0): 
		return False
	i = 5
	while(i * i <= n): 
		if (n % i == 0 or n % (i + 2) == 0) : 
			return False
		i = i + 6

	return True

def power( x, y, p):                                          

	res = 1 

	x = x % p

	while (y > 0): 
		if (y & 1): 
			res = (res * x) % p 
		y = y >> 1 
		x = (x * x) % p 

	return res 

def findPrimefactors(s, n) : 

	while (n % 2 == 0) : 
		s.add(2) 
		n = n // 2

	for i in range(3, int(sqrt(n)), 2): 
		
		while (n % i == 0) : 

			s.add(i) 
			n = n // i 
	if (n > 2) : 
		s.add(n) 

def findPrimitive( n) : 
	s = set() 
	if (isPrime(n) == False): 
		return -1
	phi = n - 1
	findPrimefactors(s, phi)
	for r in range(2, phi + 1): 
		flag = False
		for it in s: 

			if (power(r, phi // it, n) == 1): 

				flag = True
				break
			
		if (flag == False): 
			return r 

	return -1

primitive_root= findPrimitive(prime_no)

print("Primitive Root:",primitive_root)

public_r=(primitive_root**private_r)%prime_no
public_s=(primitive_root**private_s)%prime_no

print("Public key of Reciever:",public_r)
print("Public key of Sender:",public_s)

key_s=(public_s**private_r)%prime_no
key_r=(public_r**private_s)%prime_no

if key_r==key_s:
    print("Success! key shared successfully")
    print("Shared Key:",key_r)
else:
    print("Failed")
