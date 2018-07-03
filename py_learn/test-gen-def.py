def fib(max):
	n,a,b=0,0,1
	while n<max:
		yield b
		a, b = b, a + b
		n=n+1
	return 'done'
x=input('enter fib(?)(please input 4)')
for i in fib(4):
	print(i)
