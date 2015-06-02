#!/usr/bin/python
#
# Ernest Kugel, Oct. 2013.
#
# Project Euler (http://projecteuler.net/), Problem 3

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

import math
from random import randint
import web
import calendar
import time
import logging

# Define limits for random numbers
world_start = 60085147
world_end = 600851475143

logging.basicConfig(filename='log/problem3.log',level=logging.DEBUG)

# Test a prime number using Trial Division (http://en.wikipedia.org/wiki/Trial_division)
def is_prime_trial_division (n):
	global primes_list
	if n <= 2:
		return False
	max_prime = math.sqrt(n)
	test = 2
	while n % test != 0:
		if test > max_prime:
			logging.info("Prime number found! - " + str(n))
			return True
		test += 1
	return False

def get_largest_prime (world):
	largest_prime = int(math.sqrt(world))
	while largest_prime > 2:
		if is_prime_trial_division(largest_prime) and world % largest_prime == 0:
			return largest_prime
			break
		largest_prime -= 1

urls = (
  '/', 'index'
)

class index:
    def GET(self):
	time_start = calendar.timegm(time.gmtime())

	ceiling = randint(world_start,world_end)
	logging.info("Ceiling for testing = " + str(ceiling))
	result = get_largest_prime(ceiling)
	logging.info("Found result! - " + str(result))

	time_end = calendar.timegm(time.gmtime())
	runtime = time_end - time_start
	logging.info(str(runtime))
	return "Largest prime below " + str(ceiling) + " is " + str(result) + ".\n" \
		+ "Runtime was ~" + str(runtime) + " seconds.\n" \

if __name__ == "__main__": 
    app = web.application(urls, globals())
    app.run() 
