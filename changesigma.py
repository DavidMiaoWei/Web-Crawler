"""
This program observes the function of sigma
Author: Yunjing LIU
"""
#!/usr/bin/env python
import numpy as np
import threading
import angular as an
import time
#import matlibplot as plt
#set x range and stepsize


t0 = time.clock()



xmin = 0.1
xmax = 1.0
dx = 0.05
#set the number of fireflies 
N = 200
#set different values for sigma 
sigma2 = np.pi/40
sigma3 = np.pi/30 
sigma4 = np.pi/10
#call the class in an 
a = an.Angularfrequency(N)
sigma1 = a.sigma
a.time = 2000
deriva = a.phase(a.kura[a.time,:],a.space[a.time])

#reset sigma value
#a.sigma = sigma2
#reset everything related to sigma 
#a.omega = np.random.normal(a.mu,a.sigma, a.numpoints)
#a.kuramoto()
#get a new derivative 
#deriva2 = a.phase(a.kura[a.time,:],a.space[a.time])
#deriva2 = process(sigma2)


#do it again
"""a.sigma = sigma3
a.omega = np.random.normal(a.mu,a.sigma, a.numpoints)
a.kuramoto()
deriva3 = a.phase(a.kura[a.time,:],a.space[a.time])
"""

#deriva3 = process(sigma3)
#do it again
"""
a.sigma = sigma4
a.omega = np.random.normal(a.mu,a.sigma, a.numpoints)
a.kuramoto()sada
deriva4 = a.phase(a.kura[a.time,:],a.space[a.time])
"""
#deriva4 = process(sigma4)
def process111(sigma_number):
	N = 200
	a = an.Angularfrequency(N)
	a.sigma = sigma_number
	a.omega = np.random.normal(a.mu,a.sigma, a.numpoints)
	a.kuramoto()
	output = a.phase(a.kura[a.time,:],a.space[a.time])
	output=str(output)
	account = 2
	account+=1
	print("deriva%d:"%account,output)

try:
	my_thread2 = threading.Thread(target = process111,args = (sigma2))
	my_thread3 = threading.Thread(target = process111,args = (sigma3))
	my_thread4 = threading.Thread(target = process111,args = (sigma4))
	my_thread2.start()
	my_thread3.start()
	my_thread4.start()
	my_thread2.join()
	my_thread3.join()
	my_thread4.join()
except:
	print "Error: unable to start thread"

elapsed = (time.clock()-t0)
print("Time used:",elapsed)
#print ("deriva1:",deriva)
#print ("deriva2:",deriva2)
#print ("deriva3:",deriva3)
#print ("deriva4:",deriva4)
"""deriva = str(deriva)
deriva2 = str(deriva2)
deriva3=str(deriva3)
deriva4=str(deriva4)
result_file=open("result","wb")
result_file.write("deriva:"+deriva)
result_file.write("deriva2:"+deriva2)
result_file.write("deriva3:"+deriva3)
result_file.write("deriva4:"+deriva4)
result_file.close()"""
# the histogram of the data
"""plt.hist([deriva,deriva2,deriva3,deriva4], bins = np.arange(xmin,xmax,dx), 
         label=['sigma='+str(sigma1)+'','sigma='+str(sigma2)+'',
                'sigma='+str(sigma3)+'','sigma='+str(sigma4)+''])

plt.xlabel('Angular Frequency')
plt.ylabel('Amounts')
plt.title("The distribution of Angular frequency when t ="+str(a.time*0.5)+" ")
plt.axis([xmin, xmax, 0, 150])
plt.grid(True)
plt.legend(loc='upper right')
plt.show()
"""
