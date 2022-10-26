def summ(upper, lower):
	return(upper+lower)

def rand(upper, lower, seed=0):
	import random
	if seed:
		random.seed(seed)
	return(random.randrange(upper,lower+1))

def randomprime(upper: int, lower: int, seed=0):
	import random
	import sympy
	if seed:
		random.seed(seed)
	while True:
		num = int(random.randrange(upper,lower))
		if not sympy.isprime(num):
			continue
		return(num)
def allprimes(start,stop):
	import sympy
	primes=[]
	for i in range(start,stop):
		if sympy.isprime(i):
			primes.append(i)
		continue
	return(primes)
def uselesscomp(val,it):
	return([val for i in range(it)])
def easyapp(file: str, content):
	file = file+'.txt'
	try:
		with open(file, 'a') as f:
			f.write(f"{content}\n")
	except(FileNotFoundError):
		with open(file,'w') as f:
			f.write(f"{content}\n")