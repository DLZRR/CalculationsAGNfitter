import numpy as np
import matplotlib.pyplot as plt


def correlation(X, Y):

    n = len(X)

    s_x = np.sqrt(1./(n-1) * np.sum((X-np.average(X))**2.))
    s_y = np.sqrt(1./(n-1) * np.sum((Y-np.average(Y))**2.))
    
    R = 1./(n-1.) * np.sum(((X-np.average(X))/s_x) * ((Y-np.average(Y))/s_y))
    
    return R**2.



data = np.loadtxt('ALESScontribution_new.txt', skiprows=1)

name = ['tau', 'age', 'EBVgal', 'Tdust', 'fracPAH', 'Nh', 'EBVbbb', 'GA', 'SB', 'TO', 'BB', 'Mstar', 'SFR_opt', 'LIR(8-1000)', 'Lbb(0.1-1)', 'Lbbdered(0.1-1)', 'Lga(5-15)', 'Ltor(5-15)', 'Lsb(5-15)', 'SFR_IR']

s = 0
t = 0

#print (len(data[0])-6)/3

#print len(data[:,0])

for i in range(1, len(data[0])-5, 3):
    
    t = 0
    
    for j in range(1, len(data[0])-5, 3):
        
        if j>i:
            
            correlation(data[:,i], data[:,j])
            
            #print correlation(data[i,:], data[j,:])
            
            if correlation(data[:,i], data[:,j]) > 0.25:
                
                plt.errorbar(data[:,i], data[:,j], xerr = [data[:,i+1]/2, data[:,i+2]/2], yerr = [data[:,j+1]/2, data[:,j+2]/2], fmt='o')
                plt.xlabel(name[s])
                plt.ylabel(name[t])
                plt.show()
              
        #print t
        t += 1
        
    s += 1
