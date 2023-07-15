import astropy.io.ascii as ascii
import gizmo_analysis as gizmo
from stellarutil.calculations import dist, filter_list

#region talk to gizmo stuff

def get_ahf_data(path, filter = True):
    '''
    Read the content from the AHF file.
    
    Parameters:
    ----------
        path : str 
            the path to the file
        filter : boolean
            should the data be filtered to only include rows with: fMhires(38) > 0.99. Default is true.

    Returns
    -------
        Return a 2D list of the data specified in the AHF file.
    '''

    data = ascii.read(path)
    if not filter:
        return data
    else:
        data_filtered = data[(data.field('fMhires(38)') > 0.99)]
        return data_filtered

def get_field(data, field):
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
    field_name = get_field_name(data, field)
    print(f"{field} changed to {field_name}")
    # Store all the field data in a list called column
    column = data.field(field_name) 
    # Return the column
    return column

def get_field_name(data, name):
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

def get_hubble_constant(simulation_directory, snapshot_directory):
    header = gizmo.io.Read.read_header(
        simulation_directory = simulation_directory,
        snapshot_directory = snapshot_directory,
        snapshot_value_kind = 'index',
        snapshot_value = 600
    )
    return header['hubble']

def get_particles(simulation_directory, snapshot_directory, species):
    return gizmo.io.Read.read_snapshots(
        simulation_directory = simulation_directory,
        snapshot_directory = snapshot_directory,
        species=species, 
        snapshot_value_kind='index',
        snapshot_values=600
    )

#endregion


def getGalaxyStarInfo(data, particles, h, index = 0):
    # Get the center of the halo
    xc = data.field('Xc(6)')[index] / h
    yc = data.field('Yc(7)')[index] / h
    zc = data.field('Zc(8)')[index] / h
    # Get the peculiar velocity of halo
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
    from calculations import dist
    distances =  dist(x,y,z) # Get the distance of each particle from the center galaxy
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


class Star:

    def __init__(self, x = 0, y = 0, z = 0, m = 0, a = 0, vx = 0, vy = 0, vz = 0):
        self.x = x
        self.y = y
        self.z = z
        self.m = m
        self.a = a
        self.vx = vx
        self.vy = vy
        self.vz = vz
    
    def velocity(self):
        return dist(self.vx, self.vy, self.vz)
        


class Simulation:

    def __init__(self, simulation_directory = '../data', snapshot_directory = '../data', ahf_path = "../data/snapshot_600.z0.000.AHF_halos"):

        self.h = get_hubble_constant(simulation_directory, snapshot_directory)
        self.particles = get_particles(simulation_directory, snapshot_directory, ['star'])
        self.ahf_data = get_ahf_data(ahf_path)


    def get_stars_in_halo(self, index = 0):
        # Get the center of the halo
        xc = self.ahf_data.field('Xc(6)')[index] / self.h
        yc = self.ahf_data.field('Yc(7)')[index] / self.h
        zc = self.ahf_data.field('Zc(8)')[index] / self.h
        # Get the peculiar velocity of halo
        vxc = self.ahf_data.field('VXc(9)')[index] / self.h
        vyc = self.ahf_data.field('VYc(10)')[index] / self.h
        vzc = self.ahf_data.field('VZc(11)')[index] / self.h
        # Get the x,y,z positions of each star particle in the simulation, and normalize it with the galaxy center
        x = self.particles['star']['position'][:,0] - xc
        y = self.particles['star']['position'][:,1] - yc
        z = self.particles['star']['position'][:,2] - zc
        # Get the scalefactor (age) of each star in the simulation
        a = self.particles['star']['form.scalefactor']
        # Get the mass of each star in the simulation
        m = self.particles['star']['mass']
        # Get the x,y,z velocity of each star particle in the simulation, and normalize it with the velocity center
        vx = self.particles['star']['velocity'][:,0] - vxc
        vy = self.particles['star']['velocity'][:,1] - vyc
        vz = self.particles['star']['velocity'][:,2] - vzc
        # Get the distance of each star from the center galaxy
        distances =  dist(x,y,z) 
        # Get the radius of the galaxy that can actually hold stars
        rgal = 0.15 * self.ahf_data.field('Rvir(12)')[index] / self.h 
        # Filter out all stars that are too far away 
        x_gal = filter_list(x, distances, rgal)
        y_gal = filter_list(y, distances, rgal)
        z_gal = filter_list(z, distances, rgal)
        a_gal = filter_list(a, distances, rgal)
        m_gal = filter_list(m, distances, rgal)
        vx_gal = filter_list(vx, distances, rgal)
        vy_gal = filter_list(vy, distances, rgal)
        vz_gal = filter_list(vz, distances, rgal)
        v_gal = dist(vx_gal, vy_gal, vz_gal)
        
        print(len(x_gal))
        print(len(y_gal))
        print(len(z_gal))
        print(len(a_gal))
        print(len(m_gal))
        print(len(v_gal))

        return (x_gal, y_gal, z_gal, a_gal, m_gal, v_gal)


    def get_field(self, field):
        # Get the correct name of the field
        field_name = get_field_name(self.ahf_data, field)
        # Store all the field data in a list called column
        column = self.ahf_data.field(field_name) 
        # Return the column
        return column