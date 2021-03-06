#!/usr/bin/python
#
# Ernest Kugel, Oct. 2013.
#
# Project Euler (http://projecteuler.net/), Problem 3

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# New Relic must be imported first:
# https://docs.newrelic.com/docs/agents/python-agent/installation-configuration/python-agent-integratio
import newrelic.agent
import math
from random import randint
import web
import calendar
import time
import datetime
import syslog
import logging

# Define limits for random numbers
world_start = 60085147
world_end = 600851475143
prime_count = 0

logging.basicConfig(filename='log/problem3.log',level=logging.DEBUG)
newrelic.agent.initialize('newrelic.ini')


urls = (
  '/', 'index'
)

# Test a prime number using Trial Division (http://en.wikipedia.org/wiki/Trial_division)
def is_prime_trial_division (n):
	global prime_count
	if n <= 2:
		return False
	max_prime = math.sqrt(n)
	test = 2
	while n % test != 0:
		if test > max_prime:
			prime_count += 1
			return True
		test += 1
	return False

# Find the largest prime below a given number
def get_largest_prime (world):
	largest_prime = int(math.sqrt(world))
	while largest_prime > 2:
		if is_prime_trial_division(largest_prime) and world % largest_prime == 0:
			return largest_prime
		largest_prime -= 1

# index class for web.py
class index:
    def GET(self):
	# Time our performance
	time_start = calendar.timegm(time.gmtime())

	# Let's do our thing!
	ceiling = randint(world_start,world_end)
	result = get_largest_prime(ceiling)

	# Calculate our performance
	time_end = calendar.timegm(time.gmtime())
	runtime = time_end - time_start

	deliver = "Largest prime factor of " + str(ceiling) + " is " + str(result) + ", Runtime was ~" + str(runtime) + " seconds, worked through " + str(prime_count) + " primes."

	# Bail and log on errors
	if result is None:
		syslog.syslog(syslog.LOG_ERR, deliver)
		logging.error(str(datetime.datetime.now()) + " " + deliver)
		raise TypeError('When looking for prime factors, result should not be ' + str(result))
		return "Oops, something went terribly wrong!"
	# Log and deliver!
	else:
		syslog.syslog(deliver)
		logging.info(str(datetime.datetime.now()) + " " + deliver)
		return deliver

if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()
