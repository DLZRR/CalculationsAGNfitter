import numpy as np
import matplotlib.pyplot as plt
import os
import shutil
import gvar
import os.path



ln_likelihood = []

t = 0
j = 0

#print len(OTHER_BANDS)
#print

folder1 = '/net/pczaal3/data1/OUTPUT_AGNfitter/' 
folder2 = 'ALESS_OUTPUT/'
folder =  ''.join([folder1, folder2])
#print folder

y = 0
z = 0

for i in range(0, 10000, 1): 

        if os.path.isfile(folder + str(float(i)/10.) + '/parameter_outvalues_' + str(float(i)/10.)  + '.txt'):
        #if os.path.isfile(folder + '/parameter_outvalues_' + str(float(i)/10.)  + '.txt'):

            my_data = np.loadtxt(folder + str(float(i)/10.)  + '/parameter_outvalues_' + str(float(i)/10.)  + '.txt', skiprows = 4)
            #my_data = np.loadtxt(folder + '/parameter_outvalues_' + str(float(i)/10.)  + '.txt', skiprows = 4)
            y += 1
        
            if my_data[2][20] > -1000.:
                
                ln_likelihood.append(my_data[2][20])

                z += 1

ln_likelihood = np.asarray(ln_likelihood)

#print np.histogram(ln_likelihood)

print 'Amount under -1000', y-z, ' of', y

#print ln_likelihood

plt.hist(ln_likelihood)
plt.show()


array = np.zeros((z, 3*21+3))

for i in range(0, 10000, 1): 

    #print OTHER_BANDS[i][0]

    if os.path.isfile(folder + str(float(i)/10.)  + '/parameter_outvalues_' + str(float(i)/10.)  + '.txt'):
    #if os.path.isfile(folder + '/parameter_outvalues_' + str(float(i)/10.)  + '.txt'):

        my_data = np.loadtxt(folder + str(float(i)/10.)  + '/parameter_outvalues_' + str(float(i)/10.)  + '.txt', skiprows = 4)
        #my_data = np.loadtxt(folder + '/parameter_outvalues_' + str(float(i)/10.)  + '.txt', skiprows = 4)

        if my_data[2][20] > -1000.: #np.mean(ln_likelihood) - 1.96*np.std(ln_likelihood):
            
            #print OTHER_BANDS[i][0]
            
            array[t][0] = float(i)/10.
            
            array[t][1] = my_data[2][0]
            array[t][2] = my_data[1][0]
            array[t][3] = my_data[3][0]
            
            array[t][4] = my_data[2][1]
            array[t][5] = my_data[1][1]
            array[t][6] = my_data[3][1]
            
            array[t][7] = my_data[2][2]
            array[t][8] = my_data[1][2]
            array[t][9] = my_data[3][2]
            
            array[t][10] = my_data[2][3]
            array[t][11] = my_data[1][3]
            array[t][12] = my_data[3][3]
            
            array[t][13] = my_data[2][4]
            array[t][14] = my_data[1][4]
            array[t][15] = my_data[3][4]
            
            array[t][16] = my_data[2][5]
            array[t][17] = my_data[1][5]
            array[t][18] = my_data[3][5]
            
            array[t][19] = my_data[2][6]
            array[t][20] = my_data[1][6]
            array[t][21] = my_data[3][6]
            
            array[t][22] = my_data[2][7]
            array[t][23] = my_data[1][7]
            array[t][24] = my_data[3][7]
            
            array[t][25] = my_data[2][8]
            array[t][26] = my_data[1][8]
            array[t][27] = my_data[3][8]
            
            array[t][28] = my_data[2][9]
            array[t][29] = my_data[1][9]
            array[t][30] = my_data[3][9]
            
            array[t][31] = my_data[2][10]
            array[t][32] = my_data[1][10]
            array[t][33] = my_data[3][10]
            
            array[t][34] = 10.**(my_data[2][11])
            array[t][35] = 10.**(my_data[1][11])
            array[t][36] = 10.**(my_data[3][11])
            
            array[t][37] = my_data[2][12]
            array[t][38] = my_data[1][12]
            array[t][39] = my_data[3][12]
            
            array[t][40] = 10.**(my_data[2][13])
            array[t][41] = 10.**(my_data[1][13])
            array[t][42] = 10.**(my_data[3][13])
            
            array[t][43] = 10.**(my_data[2][14])
            array[t][44] = 10.**(my_data[1][14])
            array[t][45] = 10.**(my_data[3][14])
            
            array[t][46] = 10.**(my_data[2][15])
            array[t][47] = 10.**(my_data[1][15])
            array[t][48] = 10.**(my_data[3][15])
            
            array[t][49] = 10.**(my_data[2][16])
            array[t][50] = 10.**(my_data[1][16])
            array[t][51] = 10.**(my_data[3][16])
            
            array[t][52] = 10.**(my_data[2][17])
            array[t][53] = 10.**(my_data[1][17])
            array[t][54] = 10.**(my_data[3][17])
            
            array[t][55] = 10.**(my_data[2][18])
            array[t][56] = 10.**(my_data[1][18])
            array[t][57] = 10.**(my_data[3][18])
            
            array[t][58] = my_data[2][19]
            array[t][59] = my_data[1][19]
            array[t][60] = my_data[3][19]
            
            array[t][61] = my_data[2][20]
            array[t][62] = my_data[1][20]
            array[t][63] = my_data[3][20]
        
            #array[t][5] = 10.**(my_data[2][16])
            #array[t][7] = (10.**(my_data[2][17]) / (10**(my_data[2][18]) + 10**(my_data[2][17]))) * 100.

            #array[t][2] = np.log(10.)* 10.**(my_data[2][17]) * (my_data[3][17] - my_data[1][17]) / 2. # Torus
            #array[t][4] = np.log(10.)* 10.**(my_data[2][18]) * (my_data[3][18] - my_data[1][18]) / 2. # SF Region Dust
            #array[t][6] = np.log(10.)* 10.**(my_data[2][16]) * (my_data[3][16] - my_data[1][16]) / 2. # Galaxy
            #array[t][8] = np.sqrt(array[t][2]**2. * (array[t][3]/(array[t][1] + array[t][3])**2.)**2. + array[t][4] **2. * (array[t][1]/(array[t][1] + array[t][3])**2.)**2.)
            #print array[t][8]

            #print
            #print array[t][1], array[t][2]

            x = gvar.gvar(my_data[2][17], (my_data[3][17] - my_data[1][17]) / 2.)
            y = gvar.gvar(my_data[2][18], (my_data[3][18] - my_data[1][18]) / 2.)

            z = 1. / (1. + 10.**(y - x))

            array[t][64] = z.mean * 100.
            array[t][65] = z.sdev * 100.
            
            print z.sdev/z.mean
            
            #array[t][7] = 10.**(my_data[2][13]) # L_IR
            #array[t][8] = np.log(10.)* 10.**(my_data[2][13]) * (my_data[3][13] - my_data[1][13]) / 2. # STD L_IR
            
            #array[t][9] = my_data[2][19]
            #array[t][10] = (my_data[3][19] - my_data[1][19]) / 2.
            
            #print array[t][8]      
            #print
            #print z.mean * 100.
            #print

            #array[t][9] = OTHER_BANDS[i][25]
            #array[t][10] = OTHER_BANDS[i][26]

            
            t +=1
            
np.savetxt('ALESScontribution_new.txt', array, header='ID tau tau_16 tau_84 age age_16 age_84 EBVgal EBVgal_16 EBVgal_84 Tdust Tdust_16 Tdust_84 fracPAH fracPAH_16 fracPAH_84 Nh Nh_16 Nh_84 EBVbbb EBVbbb_16 EBVbbb_84 GA GA_16 GA_84 SB SB_16 SB_84 TO TO_16 TO_84 BB BB_16 BB_84 Mstar Mstar_16 Mstar_84 SFR_opt SFR_opt_16 SFR_opt_84 LIR(8-1000) LIR(8-1000)_16 LIR(8-1000)_84 Lbb(0.1-1) Lbb(0.1-1)_16 Lbb(0.1-1)_84 Lbbdered(0.1-1) Lbbdered(0.1-1)_16 Lbbdered(0.1-1)_84 Lga(5-15) Lga(5-15)_16 Lga(5-15)_84 Ltor(5-15) Ltor(5-15)_16 Ltor(5-15)_84 Lsb(5-15) Lsb(5-15)_16 Lsb(5-15)_84 SFR_IR SFR_IR_16 SFR_IR_84 -ln_likelihood -ln_likelihood_16 -ln_likelihood_84 AGNfrac AGNfrac_err', comments='')
