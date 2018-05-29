import numpy as np
import matplotlib.pyplot as plt
import os
import shutil
import gvar
import os.path

OTHER_BANDS = np.loadtxt('FLS_cat_1217131.txt', skiprows = 33)

array = np.zeros((len(OTHER_BANDS), 11))

ln_likelihood = []

t = 0
j = 0

#print len(OTHER_BANDS)
#print

folder1 = '/net/raken/data1/OUTPUT_AGNfitter/'
folder2 = 'FLS_ALL_new/'
folder =  ''.join([folder1, folder2])

for i in range(0, len(OTHER_BANDS), 1): 

    #print OTHER_BANDS[i][0]
        if os.path.isfile(folder + str(OTHER_BANDS[i][0]) + '/parameter_outvalues_' + str(OTHER_BANDS[i][0]) + '.txt'):

            my_data = np.loadtxt(folder + str(OTHER_BANDS[i][0]) + '/parameter_outvalues_' + str(OTHER_BANDS[i][0]) + '.txt', skiprows = 4)
        
            if my_data[2][20] > -1000.:
                
                ln_likelihood.append(my_data[2][20])


ln_likelihood = np.asarray(ln_likelihood)

#print np.histogram(ln_likelihood)

#print 'The amount that had a to low likelihood was: ', j

#print ln_likelihood

plt.hist(ln_likelihood)
plt.show()


for i in range(0, len(OTHER_BANDS), 1): 

    #print OTHER_BANDS[i][0]

    if os.path.isfile(folder + str(OTHER_BANDS[i][0]) + '/parameter_outvalues_' + str(OTHER_BANDS[i][0]) + '.txt'):

        my_data = np.loadtxt(folder + str(OTHER_BANDS[i][0]) + '/parameter_outvalues_' + str(OTHER_BANDS[i][0]) + '.txt', skiprows = 4)

        if my_data[2][20] > -1000.:#np.mean(ln_likelihood) - 1.96*np.std(ln_likelihood):
            
            #print OTHER_BANDS[i][0]
            array[t][0] = OTHER_BANDS[i][0]
            array[t][1] = 10.**(my_data[2][17])
            array[t][3] = 10.**(my_data[2][18])
            array[t][5] = 10.**(my_data[2][16])
            array[t][7] = (10.**(my_data[2][17]) / (10**(my_data[2][18]) + 10**(my_data[2][17]))) * 100.

            array[t][2] = np.log(10.)* 10.**(my_data[2][17]) * (my_data[3][17] - my_data[1][17]) / 2. # Torus
            array[t][4] = np.log(10.)* 10.**(my_data[2][18]) * (my_data[3][18] - my_data[1][18]) / 2. # SF Region Dust
            array[t][6] = np.log(10.)* 10.**(my_data[2][16]) * (my_data[3][16] - my_data[1][16]) / 2. # Galaxy
            #array[t][8] = np.sqrt(array[t][2]**2. * (array[t][3]/(array[t][1] + array[t][3])**2.)**2. + array[t][4] **2. * (array[t][1]/(array[t][1] + array[t][3])**2.)**2.)
            #print array[t][8]

            #print
            #print array[t][1], array[t][2]

            x = gvar.gvar(my_data[2][17], (my_data[3][17] - my_data[1][17]) / 2.)
            y = gvar.gvar(my_data[2][18], (my_data[3][18] - my_data[1][18]) / 2.)

            z = 1. / (1. + 10.**(y - x))

            array[t][8] = z.sdev * 100.

            #print array[t][8]      
            #print
            #print z.mean * 100.
            #print

            array[t][9] = OTHER_BANDS[i][25]
            array[t][10] = OTHER_BANDS[i][26]

            
            t +=1
        '''
        else:

            j += 1
        
            src1 = '/data2/OUTPUT_AGNFitter/OUTLIERS/REDONE/' + str(OTHER_BANDS[i][0]) + '/parameter_outvalues_' + str(OTHER_BANDS[i][0]) + '.txt'
            src2 = '/data2/OUTPUT_AGNFitter/OUTLIERS/REDONE/' + str(OTHER_BANDS[i][0]) + '/SED_manyrealizations_' + str(OTHER_BANDS[i][0]) + '.pdf'
            src3 = '/data2/OUTPUT_AGNFitter/OUTLIERS/REDONE/' + str(OTHER_BANDS[i][0]) + '/MODELSDICT_' + str(OTHER_BANDS[i][0])
            src4 = '/data2/OUTPUT_AGNFitter/OUTLIERS/REDONE/' + str(OTHER_BANDS[i][0]) + '/samples_burn1-2-3.sav'
            src5 = '/data2/OUTPUT_AGNFitter/OUTLIERS/REDONE/' + str(OTHER_BANDS[i][0]) + '/samples_mcmc.sav'
            src6 = '/data2/OUTPUT_AGNFitter/OUTLIERS/REDONE/' + str(OTHER_BANDS[i][0]) + '/traces_mcmc.pdf'
            dst = '/data2/OUTPUT_AGNFitter/OUTLIERS/REDONE/BAD_FITS/' + str(OTHER_BANDS[i][0]) + '/'
            if not os.path.exists(dst):
                os.makedirs(dst)
            shutil.copy2(src1, dst)
            shutil.copy2(src2, dst)
            shutil.copy2(src3, dst)
            shutil.copy2(src4, dst)
            shutil.copy2(src5, dst)
            shutil.copy2(src6, dst)
        '''


np.savetxt('contribution_new.txt', array)
