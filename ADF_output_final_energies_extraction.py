#!/usr/bin/env python
# coding: utf-8

# In[5]:


##################################### EXTRACTING FINAL ENERGIES (kcal/mol) FROM .out FILES #########################################

## Libraries & Packages ##

import os
import glob

########################### Accessing Files ###########################

#**********************************************************************#
#    'path =' should be set to the path of the files.                  #
#    For extracting multiple ADF '.out' files,                         #
#    Denote target files with a wildcard (*)                           #
#    Place all desired '.out' files in one directory for convenience   #
#    Example for WINDOWS OS: 'C:\\filepath\\*.out'                     #
#    Example for mac OS: '/users/filepath/*.out'                       #
#**********************************************************************#
path = 'E:\\Gold_Research_Files\\Au25_CYST\\All_correct_single_point_calculations\\SP_au25_cyst_co2_nsolv\\SP_au25_cyst_co2_ns_outputs\\*.out'

location_path = os.path.abspath(path)      ### 'location_path' returns absolute path from accessing operating system. ###

#print(location_path)

file_names = glob.glob(location_path)      ### 'file_names' checks the path directory for the '.out' files. ###

#print(multiple_molecules_file_names)


########################### Extract Energies ###########################

for file in file_names:
    outfiles = open(file, 'r')                  ### 'outfiles' is a variable set to open and read ('r') the files in 'file_name' ###
    data = outfiles.readlines()                 ### 'data' reads the lines of the files in 'outfiles'. ###
    outfiles.close()                            ### 'outfiles.close()' closes the files that were opened. Thus no longer making it editable or readable. ###
    base = os.path.basename(file)               ### 'base' obtains the name of the file including its extendtion. In this case '.out'. ###
    cluster_name = os.path.splitext(base)[0]    ### 'cluster_name' takes only the name of the file without the '.out' extension. ###
    
    #print(base)
    #print(cluster_name)
    
    for linenum, line in enumerate(data):           ### This for-loop enumerates through the lines of the 'data' defines previously. ###
        if '>>>> AMETS' in line:                    ### This line looks for the instance, '>>>> AMETS' which occurs only once in the '.out' files ###
            overall_energy_linenum = linenum + 3    ### 'overall_energy_linenum' indicates the line at which the desired final energy in 'kcal/mol' resides. ###
                                                    ## For Single Point '.out' use: linenum + 3 ##
                                                    ## For Geometry Optimization '.out' use: linenum + 4 ##
            
            overall_energy_linenum_content = data[overall_energy_linenum]    ### 'overall_energy_linenum_content' treats the 'overall_energy_linenum' as an array and extracts the contents of 'overall_energy_linenum'  ###
            
            #print(overall_energy_kcal_mol)
            
            energy_split = overall_energy_linenum_content.split()      ### 'energy_split' splits contents of 'overall_energy_linenum_content' by spacings. ###
            energy_kcal_mol = energy_split[-2]                         ### 'energy_kcal_mol' obtains the second to last element of the split 'energy_split' which is the energy value in kcal/mol'. ###
            
            print('Overall Energy for:',cluster_name, 'is', energy_kcal_mol, 'kcal/mol') 
            print('----------------------------------------------------------------') 


# In[ ]:




# CHEM_5630_final_project
