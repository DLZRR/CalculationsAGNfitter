from shutil import copy
import os
import os.path

#folder1 = '/net/vliet/data1/AGNfitter_for_Kirk_GOODS_South/OUTPUT'
#folder1 = '/net/linschoten/data1/OUTPUT_AGNfitter/Kirk125'
folder1 = '/net/raken/data1/OUTPUT_AGNfitter/'
folder2 = 'FLS_ALL_new/'
folder =  ''.join([folder1, folder2])

dst = '/data2/FLS_NEW/'

if not os.path.exists(dst + 'parameter_values/'):
    os.makedirs(dst + 'parameter_values/')

for i in range(0, 10000000, 1): 

        if os.path.isfile(folder + str(float(i)) + '/SED_manyrealizations_' + str(float(i))  + '.pdf'):

            copy(folder + str(float(i)) + '/SED_manyrealizations_' + str(float(i))  + '.pdf', dst)
            copy(folder + str(float(i)) + '/parameter_outvalues_' + str(float(i))  + '.txt', dst + 'parameter_values/')
