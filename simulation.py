import astropy.io.ascii as ascii
import gizmo_analysis as gizmo
from calculations import dist
import os, json

# import scipy.integrate

def read_ahf_file(path: str):
    '''
    Read the content from the AHF file.
    
    Parameters:
    ----------
        path : str 
            the path to the file

    Returns
    -------
        Return a 2D list of the data specified in the AHF file.
    '''

    data = ascii.read(path)
    data_filtered = data[(data.field('fMhires(38)') > 0.99)]
    return data_filtered

def getField(data, field):
    '''
    Return a list of all items in the field of a dataset

    Parameters:
    ----------
        data : 2d array
            The table of data 
        field : int | string 
            The name of the field.
        elem_range : range
            Range of indices to print (default is all).

    Returns
    -------
        The ist of all items in the field.
    '''
    
    # Get the correct name of the field
    field_name = getFieldName(data, field)
    print(f"{field} changed to {field_name}")
    # Store all the field data in a list called column
    column = data.field(field_name) 
    # Return the column
    return column

def getFieldName(data, name):
    '''
    Return the correct name of a field.

    Parameters:
    ----------
        data : 2d array
            The table of data 
        name : int | string 
            The name of the field.

    Returns
    -------
        The ist of all items in the field.
    '''
    name = str(name).lower()  # Convert field to string if it's an integer
    name = name.replace('_','')
    # Loop through all the field names
    for item in data.dtype.names:
        string = item.lower().replace('_','')
        if name in string:
            return item
            
    return None




# TODO - make the paths more customizable and document
def getH(snapshot_path = '../snapshots'):
    # Open the json file in read mode
    file = open('../settings.json', 'r')
    # Load its contents into a dictionary
    dir = json.load(file)['directory_to_snapshots']
    # Close the file after reading it
    file.close()
    print(f"From JSON: {dir}")
    print(f"From pwd: {os.popen('pwd').read().strip()}") 
    header = gizmo.io.Read.read_header(simulation_directory =dir,snapshot_directory =dir,snapshot_value_kind='index',snapshot_value=600)
    return header['hubble']

# TODO - make the paths/species more customizable and document
def getParticles(species = ['star']):
    # Open the json file in read mode
    file = open('../settings.json', 'r')
    # Load its contents into a dictionary
    dir = json.load(file)['directory']
    # Close the file after reading it
    file.close()
    print(f"From JSON: {dir}")
    print(f"From pwd: {os.popen('pwd').read().strip()}") 
    return gizmo.io.Read.read_snapshots(simulation_directory ='../snapshots',snapshot_directory ='../snapshots',species=species, snapshot_value_kind='index',snapshot_values=600)


        

# This function returns the coordinates, velocity, mass, and age of each star in a galaxy
# Will be cleaned up later
def getGalaxyStarInfo(data, particles, h, index = 0):
    # Get the center of the given galaxy in the simulation
    xc = data.field('Xc(6)')[index] / h
    yc = data.field('Yc(7)')[index] / h
    zc = data.field('Zc(8)')[index] / h

    # Get the center of the given galaxy in the simulation
    vxc = data.field('VXc(9)')[index] / h
    vyc = data.field('VYc(10)')[index] / h
    vzc = data.field('VZc(11)')[index] / h

    # Get the x,y,z positions of each star particle in the simulation, and normalize it with the galaxy center
    x = particles['star']['position'][:,0] - xc
    y = particles['star']['position'][:,1] - yc
    z = particles['star']['position'][:,2] - zc
    # Get the scalefactor (age) of each star in the simulation
    a = particles['star']['form.scalefactor']
    # Get the mass of each star in the simulation
    m = particles['star']['mass']

    # Get the x,y,z velocity of each star particle in the simulation, and normalize it with the velocity center
    vx = particles['star']['velocity'][:,0] - vxc
    vy = particles['star']['velocity'][:,1] - vyc
    vz = particles['star']['velocity'][:,2] - vzc

    # Get the stars in the galaxy
    distances = dist(x,y,z) # Get the distance of each particle from the center galaxy
    rgal = 0.15 * data.field('Rvir(12)')[index] / h # Get the radius of the galaxy that can actually hold stars
    x_gal = x[distances < rgal] # Filter out all stars that are too far away 
    y_gal = y[distances < rgal] # Filter out all stars that are too far away 
    z_gal = z[distances < rgal] # Filter out all stars that are too far away 
    a_gal = a[distances < rgal] # Filter out all stars that are too far away
    m_gal = m[distances < rgal] # Filter out all stars that are too far away

    vx_gal = vx[distances < rgal] # Filter out all stars that are too far away
    vy_gal = vy[distances < rgal] # Filter out all stars that are too far away
    vz_gal = vz[distances < rgal] # Filter out all stars that are too far away
    v_gal = dist(vx_gal, vy_gal, vz_gal)

    return (x_gal, y_gal, z_gal, a_gal, m_gal, v_gal)
