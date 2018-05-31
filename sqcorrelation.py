import numpy as np
import matplotlib.pyplot as plt



fluxes = np.loadtxt('ALESS_TRUE_DATA.txt', skiprows=1)

def correlation(X, Y):

    n = len(X)

    s_x = np.sqrt(1./(n-1) * np.sum((X-np.average(X))**2.))
    s_y = np.sqrt(1./(n-1) * np.sum((Y-np.average(Y))**2.))
    
    R = 1./(n-1.) * np.sum(((X-np.average(X))/s_x) * ((Y-np.average(Y))/s_y))
    
    return R**2.



data = np.loadtxt('ALESScontribution_new.txt', skiprows=1)

name = ['tau', 'age', 'EBVgal', 'Tdust', 'fracPAH', 'Nh', 'EBVbbb', 'GA', 'SB', 'TO', 'BB', 'Mstar', 'SFR_opt', 'LIR(8-1000)', 'Lbb(0.1-1)', 'Lbbdered(0.1-1)', 'Lga(5-15)', 'Ltor(5-15)', 'Lsb(5-15)', 'SFR_IR']

print (data[:, 34] - data[:, 34+1])/2.
print (np.log10(data[:, 34]) - np.log10(data[:, 34+1]))/2.

plt.errorbar(np.log10(data[:,34]), data[:,64], xerr = [(np.log10(data[:, 34]) - np.log10(data[:, 34+1]))/2., (np.log10(data[:, 34+2]) - np.log10(data[:, 34]))/2.], yerr = data[:,65], fmt='o')
plt.xlabel('log M$_{*}$')
plt.ylabel('AGN fraction')
plt.savefig('Mvsfrac.pdf')
plt.show()


s = 0

for i in range(1, len(data[0])-5, 3):
    
    t = 0
    
    for j in range(1, len(data[0])-5, 3):
        
        if j>i:
            
            if correlation(data[:,i], data[:,j]) > 0.25:
                
                print correlation(data[:,i], data[:,j])
                plt.errorbar(data[:,i], data[:,j], xerr = [(data[:, i] - data[:, i+1])/2., (data[:, i+2] - data[:, i])/2.], yerr = [(data[:, j] - data[:, j+1])/2., (data[:, j+2] - data[:, j])/2.], fmt='o')
                plt.xlabel(name[s])
                plt.ylabel(name[t])
                plt.title('The squared correlation is ' + str(correlation(data[:,i], data[:,j])))
                #plt.show()
              
        #print t
        t += 1
        
    s += 1


flux = []
cont = []
temp = []
flux_err = []
cont_err = []
temp_err1 = []
temp_err2 = []

for i in range(len(fluxes)):
    
    for j in range(len(data)):
        
        if fluxes[i][0] == data[j][0]:
            
            flux.append(fluxes[i][len(fluxes[0])-2])
            cont.append(data[j][64]) 
            temp.append(data[j][10])
            flux_err.append(fluxes[i][len(fluxes[0])-1]) 
            cont_err.append(data[j][65])
            temp_err1.append((data[j][10] - data[j][11])/2.)
            temp_err2.append((data[j][12] - data[j][10])/2.)

plt.errorbar(np.asarray(flux), np.asarray(cont), xerr=np.asarray(flux_err), yerr=np.asarray(cont_err), fmt='o')
plt.xlabel('S$_{870}$ in Jansky')
plt.ylabel('AGN fraction')
plt.savefig('S870frac.pdf')
#plt.show()

plt.errorbar(np.asarray(flux), np.asarray(temp), xerr=np.asarray(flux_err), yerr=[np.asarray(temp_err1), np.asarray(temp_err2)], fmt='o')
plt.xlabel('S$_{870}$ in Jansky')
plt.ylabel('Temperature in Kelvin')
plt.savefig('S870temp.pdf')
#plt.show()



''' 

#contribution AGN correlations 

'''

'''

s = 0

for i in range(1, len(data[0])-5, 3):
                        
    if correlation(data[:,i], data[:,64]) > 0.25:
        
        print correlation(data[:,i], data[:,64])
                
        plt.errorbar(data[:,i], data[:,64], xerr = [(data[:, i] - data[:, i+1])/2., (data[:, i+2] - data[:, i])/2.], yerr = data[:,65], fmt='o')
        plt.xlabel(name[s])
        plt.ylabel('AGN fraction')
        plt.show()
        
    s += 1
    

'''

'''

Histogram AGN contribution

'''

'''

#plt.hist(data[:, 64], bins=11, weights=data[:, 65])

plt.hist(data[:, 64], bins=11)
plt.xlabel('AGN fraction')
plt.ylabel('Amount of sources')
#data1 = data[:, 64]
#y,binEdges = np.histogram(data1,bins=10)
#bincenters = 0.5*(binEdges[1:]+binEdges[:-1])
#menStd = np.sqrt(y)
##menStd = data[:, 65]
#width = 0.05
#plt.bar(bincenters, y, width=width, color='r', yerr=menStd)
plt.savefig('Histfrac.pdf')
plt.show()



'''

#Histogram of temperature

'''

plt.hist(data[:, 10])
plt.xlabel('Temperature in Kelvin')
plt.ylabel('Amount of sources')
plt.savefig('Histtemp.pdf')
plt.show()

print 'The mean temperature is', np.mean(data[:, 10]), np.std(data[:, 10])

plt.hist(np.log10(data[:, 34]))
plt.xlabel('log M$_{*}$ in solar masses')
plt.ylabel('Amount of sources')
plt.savefig('HistM.pdf')
plt.show()

print 'The mean log M is', np.log10(np.mean(data[:, 34])), np.std(np.log10(data[:, 34]))

plt.hist(np.log10(data[:, 37]))
plt.xlabel('log SFR$_{opt}$ in solar masses per year')
plt.ylabel('Amount of sources')
plt.savefig('HistSFRopt.pdf')
plt.show()

print 'The mean log optical SFR is', np.log10(np.mean(data[:, 37])), np.std(np.log10(data[:, 37]))

plt.hist(np.log10(data[:, 58]))
plt.xlabel('log SFR$_{inf}$ in solar masses per year')
plt.ylabel('Amount of sources')
plt.savefig('HistSFRinf.pdf')
plt.show()

print 'The mean log infrared SFR is', np.log10(np.mean(data[:, 58])), np.std(np.log10(data[:, 58]))

plt.hist(np.log10(data[:, 4]))
plt.xlabel('log age in cm')
plt.ylabel('Amount of sources')
plt.savefig('Histage.pdf')
plt.show()

print 'The mean log age is', np.log10(np.mean(data[:, 4])), np.std(np.log10(data[:, 4]))

'''
