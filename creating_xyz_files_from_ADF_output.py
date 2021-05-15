#!/usr/bin/env python
# coding: utf-8

# In[2]:


##################################### MAKING .XYZ FILES FROM .out FILES #########################################

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

########################### Extract XYZ Coordinates ###########################

new_data = open('optimized_coordinates', 'w+')     ### 'new_data' opens a file that allows for the file to be written. ###
for file in file_names:                            ### This for-loop goes through the specified file(s) denoted in 'file_names'. ###
    molecule_coords_data = open(file, 'r')         ### 'molecule_coords_data' opens and reads specified '.out' files. ###
    data = molecule_coords_data.readlines()        ### 'data' is the data of the read '.out' files. ###
    molecule_coords_data.close()                   ### 'molecule_coords_data.close()' closes the opened files to prevent further reading or editing. ###
    base = os.path.basename(file)                  ### 'base' obtains the name of the file including the '.out' extension. ###
    
    #print(base)
    
    struct_names = os.path.splitext(base)[0]       ### 'struct_names' extracts the name of the file exclusing the '.out' extension. ###
    
    #print(struct_names)

    for linenum, line in enumerate(data):          ### This for-loop goes through each line of the documents being read. ###
        if '>>>> FRAGM' in line:                   ### Looks for '>>>> FRAGM' which occurs once in the '.out' file. ###
            coords_start_linenum = linenum + 3     ### Indicates where to start extracting the data (aka: XYZ coordinates). ###
            
            #print(coords_start_linenum)
            
##################___Work in progress for easier atom numeberinput___##################           
#            atom_num = input('Enter number of atoms in structure:')                  #
#            #print(atom_num)                                                         #
#                                                                                     #
#            coords_end_linenum = coords_start_linenum + float(atom_num)              #
#            #print(coords_end_linenum)                                               #
#######################################################################################

##### MUST EDIT VALUE FOR 'number_of_atoms =' BEFORE RUNNING FOR STRUCTURES WITH DIFFERING NUMBER OF ATOMS. #####
            number_of_atoms = 208                                           ### 'number_of_atoms' is the number of atoms in structure. ###
            coords_end_linenum = coords_start_linenum + number_of_atoms     ### 'coords_end_linenum' indicates where to stop extracting coordinate data. ###
            
            #print(coords_end_linenum)
            
            start_content = data[coords_start_linenum]                      ### 'start_content' is the content of the first coordinates. ###
            
            #print(start_content)
          
    molecule_name = file.split('.')[0]                                      ### 'molecule_name' is the name of the structure / filename used to make the new '.xyz' files. ###
    new_xyz_file = open(molecule_name + '.xyz', 'w')                        ### 'new_xyz_file' makes the new '.xyz' file. ###
    length_of_coords = coords_end_linenum - coords_start_linenum            ### 'length_of_coords' is the entire length of just the coordinates. ###
    
    #print(length_of_coords)
    
## Initial number is the number of atoms in the molecule.
## It MUST be replaced with number of atoms in molecule.
    file_header = str(length_of_coords) + '\n' 'Atom         X           Y           Z   (Angstrom) \n'     ### 'file_header' writes the mandatory first two lines of the '.xyz' file format. ###
                                                                                                            ## '.xyz' will not function properly if formatting is off. ###
    new_xyz_file.write(file_header)                                                                         ### 'new_xyz_file.write(file_header)' writes the new '.xyz' file with the header included. ###
 
    print(file_header)                                                      ### 'print(file_header)' is a good indication of how many '.xyz' files are being written. ###
    
    numbered_atom_and_coords = []                                           ### 'numbered_atom_and_coords' is an array of the coordinates with the atom symbol and atom numbering. ###
    atom_and_coords = []                                                    ### 'atom_and_coords' is an array of jsut the atom symbol and atom coordinates. No atom numbering. ###
        
##### Insert number of atoms in 'range()' function
    for lines in range(int(length_of_coords)):                              ### This for-loop indicates how many lines of coordinates to extract. ###
        coords_contents = data[coords_start_linenum + lines]                ### 'coords_contents' indicates what data to obtain for extraction (coordinates. ###)
        
        #print(coords_contents)
        
        numbered_atom_and_coords.append(coords_contents)                    ### Appends the obtained 'coords_contents' into 'numbered_atom_and_coords' array. ###
        
        #print(numbered_atom_and_coords[-1])
        
        split_numbered_atom_and_coords = numbered_atom_and_coords[-1].split('.')        ### 'split_numbered_atom_and_coords' splits the contents of the 'numbered_atom_and_coords' array by periods (.) and excludes the atom numbering. ###
        
        #print(split_numbered_atom_and_coords)
        
        atom_and_coords.append(split_numbered_atom_and_coords[1:])          ### Appends the newly split coordinates and atom symbols into new 'atom_and_coords' array.
        
        #print(atom_and_coords)

        stringing_atom_and_coords = '.'.join([str(i) for i in atom_and_coords[-1]])     ### 'stringing_atom_and_coords' reconstructs the newly arranged data at the periods / decimal points. ###
        new_xyz_file.write(stringing_atom_and_coords)                                   ### populates the new '.xyz' files with the extracted coordinates. ###
    new_xyz_file.close()                                                                ### Closes the newly amde '.xyz' files to prevent further editing. ###


# In[ ]:




