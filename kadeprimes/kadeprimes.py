'''
My partner Kaden likes primes that add to ten. This script finds all of them up
to a number of your choosing. 

To make this work, download ten pages of prime numbers from this site:

https://t5k.org/lists/small/millions/

or generate your own, as the site advises.

Created by: Benjamin Metha
Last Updated: Apr 24, 2023
'''

import numpy as np

def digit_sum(n):
	"""Returns the sum of the digits of n."""
	return sum(int(digit) for digit in str(n))

def gen_primes_to(N):
	'''
	Generate primes using a simple sieve technique.
	
	Make it fast using numpy and jit.
	
	Parameters
	----------
	
	N: int
		The largest number we generate primes up to.
		
	Returns
	-------
	
	primes: list of intsz
		All prime numbers less than N.
	'''
	N_list = np.arange(2, N)
	primes = []
	while len(N_list) > 0:
		divisor, N_list = N_list[0], N_list[1:]
		N_list = np.delete(N_list, np.where(N_list % divisor == 0))
		primes.append(divisor)
	return primes


# Option 1: make your own primes
#primes = gen_primes_to(10000)

# Option 2: Get them from the internet
# https://t5k.org/lists/small/millions/
# (I looked at 10 million primes. You can download anything from 1 million to 
# 50 million!)
for n in range(1,11):
	with open('primes{}.txt'.format(n), 'r') as f:
		header = True
		for line in f:
			if header:
				header = False
				continue
			# Extract the numbers from the line and add them to the primes list
			primes += [num for num in line.split()]
	
kaden_primes = [p for p in primes if digit_sum(p) == 10]

with open('kadeprimes.txt', 'w') as f:
    for p in kaden_primes:
        f.write(str(p) + '\n')
