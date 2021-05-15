For both 'ADF_output_final_energies_extraction.py' and 'creating_xyz_files_from_ADF_output.py', the paths should be the paths to the location of the '.out' files.

#**********************************************************************#
#    'path =' should be set to the path of the files.                  #
#    For extracting multiple ADF '.out' files,                         #
#    Denote target files with a wildcard (*)                           #
#    Place all desired '.out' files in one directory for convenience   #
#    Example for WINDOWS OS: 'C:\\filepath\\*.out'                     #
#    Example for mac OS: '/users/filepath/*.out'                       #
#**********************************************************************#
________________________________________________________________________________________________________________
The 'ADF_output_final_energies_extraction.py' scripts requires attention to what kind of ADF '.out' file it is. 
As of now, only '.out' files for geometry optimization and single point are suporrted.

Under line 48 which says: 
	if '>>>> AMETS' in line:

For single point, replace line 49 with:
		overall_energy_linenum = linenum + 3

Or for geometry optimization, replace line 49 with:
		overall_energy_linenum = linenum + 4

________________________________________________________________________________________________________________
For the 'creating_xyz_files_from_ADF_output.py' script, 
the number of atoms in the molecule must be changed for the structure in question in order to extract the correct number of lines of optimized coordinates.

The numerical value in line 63 must be changed.
	number_of_atoms = <insert number of atoms in structure>

Example for CO2:
	number_of_atoms = 3

Optional: the variable 'file header =' may be left blank or writted with anything desired to the user.
Example:
	file_header = str(length_of_coords) + '\n' 'Atom         X           Y           Z   (Angstrom) \n'
May also be:
	file_header = str(length_of_coords) + '\n' '\n'

________________________________________________________________________________________________________________
'ADF_output_final_energies_extraction.py' is for extracting final energies in (kcal/mol).
	
	With the 3 example files given, the outputs should look something like this:

Overall Energy for: SP_au25_cyst_co2_ns_1 is -23130.93 kcal/mol
----------------------------------------------------------------
Overall Energy for: SP_au25_cyst_co2_ns_2 is -23138.87 kcal/mol
----------------------------------------------------------------
Overall Energy for: SP_au25_cyst_co2_ns_3 is -23132.39 kcal/mol
----------------------------------------------------------------

'creating_xyz_files_from_ADF_output.py' is for making new '.xyz' files from ADF '.out' files.
	
	With the 3 example files given, the outputs should look something like this along with newly created '.xyz' files in the same directory as your '.out' files:

208
Atom         X           Y           Z   (Angstrom)

208
Atom         X           Y           Z   (Angstrom)

208
Atom         X           Y           Z   (Angstrom)


