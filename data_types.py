import numpy as np 		#import numpy library 

#intergers
i=10
print(type(i))		#print out the data type 1

a_i = np.zeros(i,dtype=int)		#declare an array of ints
print(type(a_i))			#will return ndarray
print(type(a_i[0]))			#will return int64

#floats

x = 119.0					#floating point number
print(type(x))				#print out the data type of x

y = 199.0
print(type(y))			#float 199 in scie. notation

z = np.zero(i,dtype=float)
print(type(z))
print(type(z[0]))