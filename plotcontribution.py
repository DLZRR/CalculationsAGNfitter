import numpy as np
import matplotlib.pyplot as plt
import os
from shutil import copy
import os.path

array = np.loadtxt('contribution_new.txt', skiprows=0)


folder1 = '/net/raken/data1/OUTPUT_AGNfitter/'
folder2 = 'FLS_ALL_new/'
folder =  ''.join([folder1, folder2])

dst = '/data2/FLS_bad/'

if not os.path.exists(dst + 'parameter_values/'):
    os.makedirs(dst + 'parameter_values/')

means_mine1 = []
mean_hers_calculate = []
mean_hers = []
means_to_calculate = []
std_mine = []
std_hers = []
values = np.arange(-5., 115., 10.).tolist()
#print values
z = 0

for j in range(len(values)-1):

    for i in range(len(array)):

        if array[i][0] == 0.0:
        
            break

        #print array[i][7]
        #print
        
        #print
        if array[i][9] < values[j+1] and array[i][9] >= values[j]:

            #print values[j]
            #print values[j-1]
            means_to_calculate.append(array[i][7])
            mean_hers_calculate.append(array[i][9])
            #print array[i][9]
            
            if abs(array[i][7] - array[i][9]) > 50.:
                
                print array[i][0], abs(array[i][7] - array[i][9]), array[i][8], array[i][10]
                
                if os.path.isfile(folder + str(array[i][0]) + '/SED_manyrealizations_' + str(array[i][0])  + '.pdf'):

                    copy(folder + str(array[i][0]) + '/SED_manyrealizations_' + str(array[i][0])  + '.pdf', dst)
                    copy(folder + str(array[i][0]) + '/parameter_outvalues_' + str(array[i][0])  + '.txt', dst + 'parameter_values/')
                
                z += 1

    
    #mean_hers.append(np.mean(np.asarray(mean_hers_calculate)))
    #std_hers.append(np.std(np.asarray(mean_hers_calculate)))

    #mean_hers_calculate = []
    
    means_hers = np.asarray(mean_hers_calculate)
    
    array_to_save = []
    array_to_save2 = []
    means_mine = np.asarray(means_to_calculate)
    #print means_mine
    
    if means_to_calculate:
        for i in range(1000):
        
            #print np.random.choice(means_mine, size=means_mine.shape, replace=True)
            array_to_save.append(np.mean(np.random.choice(means_mine, size=means_mine.shape, replace=True)))
            array_to_save2.append(np.mean(np.random.choice(means_hers, size=means_hers.shape, replace=True)))

        mean = np.mean(array_to_save)
        se_boot = np.sqrt(np.mean((array_to_save-mean)**2.))

        means_mine1.append(mean)
        std_mine.append(se_boot)
        
        mean = np.mean(array_to_save2)
        se_boot = np.sqrt(np.mean((array_to_save2-mean)**2.))

        #print mean 
        #print
        #print se_boot
        #print

        array_to_save = []

        means_to_calculate = []
        
        mean_hers.append(mean)
        std_hers.append(se_boot)

        mean_hers_calculate = []
        
        

    else:
        
        print values[j], values[j+1]

a = []
b = []
c = []
d = []
        
for i in range(len(array)):
    
    a.append(array[i][9]) 
    b.append(array[i][7]) 
    c.append(array[i][10]) 
    d.append(array[i][8])

    
    
plt.axvspan(xmin = 0., xmax = 30., ymin = 0., ymax = 0.3, facecolor='#2ca02c', alpha=0.3)

plt.axvspan(xmin = 30., xmax = 70., ymin = 0.3, ymax = 0.7, facecolor='#800080', alpha=0.3)

plt.axvspan(xmin = 70., xmax = 100., ymin = 0.7, ymax = 1.0, facecolor='#000000', alpha=0.3)

plt.errorbar(np.asarray(mean_hers), np.asarray(means_mine1), xerr = np.asarray(std_hers), yerr = np.asarray(std_mine), fmt='o', color = 'red')

plt.errorbar(np.asarray(a), np.asarray(b), xerr = np.asarray(c), yerr = np.asarray(d), fmt='o', alpha=0.7, color = 'blue')

print z
#print len(mean_hers)
#print len(means_mine1)




plt.plot(np.linspace(0,100,100), np.linspace(0,100,100))
plt.xlim(0., 100.)
plt.ylim(0., 100.)
plt.xlabel('Contribution article')
plt.ylabel('Contribution AGNfitter')
plt.title('PAHfrac=0.25-6.0')
plt.savefig('special_plot_xFLS_new.pdf')
plt.show()

