import numpy as np
import sys		#sys: command line


def expo(x):		##function 
	return np.exp(x)		#return value
	
	
def show_expo(n):		#n: argument 
	for i in range(n):
		print(expo(float(i)))
		
		
#main function
def main():
	n=10		
	
	
	if(len(sys.argv)>1):
		n = int(sys.argv[1])
	
	
	show_expo(n)


if __name__ == "__main__":
	main()