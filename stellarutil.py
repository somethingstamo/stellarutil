import os, gizmo_analysis as gizmo, astropy.io.ascii as ascii, numpy as np

class Star:

    def __init__(self, x = 0, y = 0, z = 0, m = 0, a = 0, vx = 0, vy = 0, vz = 0):
        """
        Initialize a new Star object.

        Parameters:
        ----------
        x : float
            The x position of the star.
        y : float
            The y position of the star.
        z : float
            The z position of the star.
        m : float
            The mass of the star.
        a : float
            The scale factor of the star.
        vx : float
            The x velocity of the star.
        vy : float
            The y velocity of the star.
        vz : float
            The z velocity of the star.

        Attributes:
        -----------
        x : float
            The x position of the star.
        y : float
            The y position of the star.
        z : float
            The z position of the star.
        m : float
            The mass of the star.
        a : float
            The scale factor of the star.
        vx : float
            The x velocity of the star.
        vy : float
            The y velocity of the star.
        vz : float
            The z velocity of the star.
        velocity : float
            The velocity of the star.
        """
        self.x = x
        self.y = y
        self.z = z
        self.m = m
        self.a = a
        self.vx = vx
        self.vy = vy
        self.vz = vz
        self.velocity = self.get_velocity()   
        # ^^^ Should this be a method call or just point to the method? self.velocity was being called below, resulting in an error. 
        # Either the parentheses above or on line 99 (prev 97 before commit) should be removed.
    
    def get_velocity(self):
        """
        Get the velocity of the star by calculating the magnitude of the velocity vector.
        
        Returns
        -------
        The velocity of the star.
        """
        return np.sqrt(np.square(self.vx) + np.square(self.vy)+ np.square(self.vz))
    
    def get_3DR(self):
        """
        Get the 3d radius of the star from the center of the halo.
        
        Returns
        -------
        The radius (r) of the star.
        """
        return np.sqrt(np.square(self.x) + np.square(self.y)+ np.square(self.z))

    def get_2DR(self):
        """
        Get the 2d radius of the star from the center of the halo.
        
        Returns
        -------
        The radius (r) of the star.
        """
        return np.sqrt(np.square(self.x) + np.square(self.y))
    
    def __str__(self):
        """
        The toString method for converting the object to a string.
        
        Returns
        -------
        A stringified version of the object.
        """
        output = f"Star:\n  Position: ({self.x}, {self.y}, {self.z}) [kpc]\n  Mass: {self.m} [unit]\n  Scale Factor (a): {self.a} [unit]\n  Velocity: {self.velocity()} [kpc/s]"
        return output

class Halo:

    def __init__(self, simulation, id, stars, xc, yc, zc, vxc, vyc, vzc, hostID, mass, radius, rMax, vMax, vEsc, numGas, gasMass, numStars, starMass):
        """
        Initialize a new Halo object.

        Parameters:
        ----------
        simulation : Simulation
            The simulation the halo comes from.
        id : integer
            The id of the halo.
        stars : Stars list
            The list of stars in the halo.
        xc : float
            The center x position.
        yc : float
            The center y position.
        zc : float
            The center z position.
        hostID : integer
            The id of the parent halo.
        mass : float
            The mass of the halo.
        radius : float
            The radius of the halo.
        rMax : float
            The max radius of the halo.
        vMax : float
            The max velocity of the halo.
        vEsc : float
            The escape velocity of the halo.
        numGas : integer
            The number of gas particles.
        gasMass : float
            The mass of gas particles.
        numStars : integer
            The number of star particles.
        gasMass : float
            The mass of star particles.
        """
        self.simulation = simulation
        self.id = id
        self.stars = stars
        self.xc = xc
        self.yc = yc
        self.zc = zc
        self.vxc = vxc
        self.vyc = vyc
        self.vzc = vzc
        self.hostID = hostID
        self.mass = mass
        self.radius = radius
        self.rMax = rMax
        self.vMax = vMax
        self.vEsc = vEsc
        self.numGas = numGas
        self.gasMass = gasMass
        self.numStars = numStars
        self.starMass = starMass

    def restrict_percentage(self, percentage = 15):
        # Get the radius of the galaxy that can actually hold stars
        # Rhalo, Mhalo, Vhalo <-> Rvir, Mvir, Vvir
        rgal = (percentage / 100.0) * self.simulation.get_field('12')[self.id]
        # Get all the stars and center on the given halo
        x = self.simulation.particles['star']['position'][:,0] - self.xc
        y = self.simulation.particles['star']['position'][:,1] - self.yc
        z = self.simulation.particles['star']['position'][:,2] - self.zc
        a = self.simulation.particles['star']['form.scalefactor']
        m = self.simulation.particles['star']['mass']
        vx = self.simulation.particles['star']['velocity'][:,0] - self.vxc
        vy = self.simulation.particles['star']['velocity'][:,1] - self.vyc
        vz = self.simulation.particles['star']['velocity'][:,2] - self.vzc
        # Get the distance of each star from the center of the indicated dark matter halo
        distances =  np.sqrt(np.square(x) + np.square(y) + np.square(z))
        # Filter out all stars that are too far away 
        x_gal = x[distances < rgal]
        y_gal = y[distances < rgal]
        z_gal = z[distances < rgal]
        a_gal = a[distances < rgal]
        m_gal = m[distances < rgal]
        vx_gal = vx[distances < rgal]
        vy_gal = vy[distances < rgal]
        vz_gal = vz[distances < rgal]
        # Create a new stars list
        new_stars = []
        for i in range(len(x_gal)):
            star = Star(x_gal[i], y_gal[i], z_gal[i], m_gal[i], a_gal[i], vx_gal[i], vy_gal[i], vz_gal[i])
            new_stars.append(star)
        # Update the halos star list
        self.stars = new_stars

    def restrict_slice(self, face = 'xy', proj_distance = 1, thickness = 1):
        x = self.simulation.particles['star']['position'][:,0] - self.xc
        y = self.simulation.particles['star']['position'][:,1] - self.yc
        z = self.simulation.particles['star']['position'][:,2] - self.zc
        a = self.simulation.particles['star']['form.scalefactor']
        m = self.simulation.particles['star']['mass']
        vx = self.simulation.particles['star']['velocity'][:,0] - self.vxc
        vy = self.simulation.particles['star']['velocity'][:,1] - self.vyc
        vz = self.simulation.particles['star']['velocity'][:,2] - self.vzc
        # Get sqrt of the given face
        roots = []
        for i in range(len(x)):
            if face == 'xy' or face == 'yx': roots.append( (x**2 + y**2) ** .5 )
            elif face == 'xz' or face == 'zx': roots.append( (x**2 + z**2) ** .5 )
            elif face == 'yz' or face == 'zy': roots.append( (y**2 + z**2) ** .5 )
        # restrict all stars whose: sqrt(×^2 + y^2) < proj_distance
        x_gal = x[roots < proj_distance]
        y_gal = y[roots < proj_distance]
        z_gal = z[roots < proj_distance]
        a_gal = a[roots < proj_distance]
        m_gal = m[roots < proj_distance]
        vx_gal = vx[roots < proj_distance]
        vy_gal = vy[roots < proj_distance]
        vz_gal = vz[roots < proj_distance]
        # Create a new stars list
        new_stars = []
        for i in range(len(x_gal)):
            star = Star(x_gal[i], y_gal[i], z_gal[i], m_gal[i], a_gal[i], vx_gal[i], vy_gal[i], vz_gal[i])
            # restrict all stars whose |z pos| < thickness
            if face == 'xy' or face == 'yx':
                if abs(z_gal[i]) < thickness: new_stars.append(star)
            elif face == 'xz' or face == 'zx':
                if abs(y_gal[i]) < thickness: new_stars.append(star)
            elif face == 'yz' or face == 'zy':
                if abs(x_gal[i]) < thickness: new_stars.append(star)
        # Update the halos star list
        self.stars = new_stars

    def center_on(self, otherID):
        # Get the center relative to the halo at the given index
        xc = (self.simulation.get_field('Xc(6)')[self.id]) - (self.simulation.get_field('Xc(6)')[otherID])
        yc = (self.simulation.get_field('Yc(7)')[self.id]) - (self.simulation.get_field('Yc(7)')[otherID])
        zc = (self.simulation.get_field('Zc(8)')[self.id]) - (self.simulation.get_field('Zc(8)')[otherID])
        # Recenter each star in the list
        for star in self.stars:
            star.x -= xc
            star.y -= yc
            star.z -= zc

class Simulation:

    def __init__(
            self, 
            simulation_name = None,
            simulation_directory = None, 
            snapshot_directory = 'output',
            ahf_path = None, 
            species = ['star'], 
            snapshot_value_kind='index',
            snapshot_values = 600
        ):
        """
        Initialize a new Simulation object.

        Parameters:
        ----------
        simulation_name : string
            The name of the simulation. 
            By giving the name, it will look for simulation_directory/snapshot_directory/ahf_directory in '../data/{simulation_name}'
        simulation_directory : string
            The path to the .hdf5 file. 
        snapshot_directory : string
            The path to the snapshot_times.txt. 
        ahf_path : string
            The path to the .AHF_halos file.
        species : list
            name[s] of particle species:
                'all' = all species in file
                'dark' = dark matter at highest resolution
                'dark2' = dark matter at lower resolution
                'gas' = gas
                'star' = stars
                'blackhole' = black holes, if snapshot contains them
        snapshot_values : int or float or list
            index[s] or redshift[s] or scale-factor[s] of snapshot[s]

        Attributes:
        -----------
        h : float
            The hubble constant.
        h_fields : list
            List containing the fields that require division by h (Hubble constant)
        particles : float
            The data for all the indicated particles in the simulation.
        ahf_data : float
            The data within the .AHF_halos file.
        """
        # If a simulation name has been given, we can assume the user is using the conventional locations
        if simulation_name is not None:
            simulation_directory = f'../data/{simulation_name}'
            # Look for the file that ends with '.AHF_halos'.
            items = os.listdir(simulation_directory)
            for item in items:
                file_path = os.path.join(simulation_directory, item)
                if not os.path.isdir(file_path) and item.endswith('.AHF_halos'):
                    print(file_path)
                    ahf_path = file_path
            if ahf_path is None:
                print(f'Could not find an ahf_directory in: {simulation_directory}')
                return
        elif simulation_directory is not None and ahf_path is None:
            # Look for the file that ends with '.AHF_halos'.
            items = os.listdir(simulation_directory)
            for item in items:
                file_path = os.path.join(simulation_directory, item)
                if not os.path.isdir(file_path) and item.endswith('.AHF_halos'):
                    ahf_path = file_path
                    print('Found AHF file here: ' + ahf_path)
                    break
            if ahf_path is None:
                print(f'Could not find an ahf_directory in: {simulation_directory}')
                return
        else:
            if simulation_directory is None or ahf_path is None:
                print('Cannot read files. Either:\n')
                print('\t1) Provide a simulation_name while adhering to the proper folder structure.')
                print('\t\tExample:  sim = Simulation("m10r_res250md")')
                print('\t2) Manually specify: simulation_directory and ahf_directory. Also, specify the snapshot directory if it is not output.')
                print('\t\tExample:  sim = Simulation(simulation_directory="path", ahf_path="path")')
                print('\t\tExample:  sim = Simulation(simulation_directory="path", ahf_path="path", snapshot_directory="path")\n')
                if simulation_directory is None:
                    print('Missing simulation directory.') 
                if ahf_path is None:
                    print('Missing ahf_path.') 
                return
            
        # Snpashot value is used to get the hubble constant, it will always be a subset of the snapshot_values
        snapshot_value = snapshot_values[0] if type(snapshot_values) is list else snapshot_values
        # Get the hubble constant from gizmo_analysis
        self.h = gizmo.io.Read.read_header(
            simulation_directory = simulation_directory,
            snapshot_directory = snapshot_directory,
            snapshot_value_kind = snapshot_value_kind,
            snapshot_value = snapshot_value
        )['hubble']
        # Initialize fields that require division by h (Hubble constant)
        self.h_fields = ['xc(6)', 'yc(7)', 'zc(8)', '12', '4', 'rmax(13)', 'mstar(65)', 'ngas(45)']
        # Get the particles from gizmo_analysis
        self.particles = gizmo.io.Read.read_snapshots(
            simulation_directory = simulation_directory,
            snapshot_directory = snapshot_directory,
            species=species, 
            snapshot_value_kind=snapshot_value_kind,
            snapshot_values=snapshot_values
        )
        # Get the AHF data from the halo file
        self.ahf_data = ascii.read(ahf_path)
        # Filter the AHF data
        self.ahf_data = self.ahf_data[(self.ahf_data.field('fMhires(38)') > 0.99)]
    
    def get_halo(self, id = 0):
        """
        Get the indicated dark matter halo.

        Parameters:
        ----------
        id : int
            The index of the dark matter halo. Default is 0.
        
        Returns
        -------
        The indicated dark matter halo in a Halo object.
        """
        # Get the center of the indicated dark matter halo
        xc = self.ahf_data.field('Xc(6)')[id] / self.h
        yc = self.ahf_data.field('Yc(7)')[id] / self.h
        zc = self.ahf_data.field('Zc(8)')[id] / self.h
        # Get the peculiar velocity of the indicated dark matter halo
        vxc = self.ahf_data.field('VXc(9)')[id] / self.h
        vyc = self.ahf_data.field('VYc(10)')[id] / self.h
        vzc = self.ahf_data.field('VZc(11)')[id] / self.h
        # Get the x,y,z positions of each star particle in the simulation
        # And normalize it with the center of the indicated dark matter halo
        x = self.particles['star']['position'][:,0] - xc
        y = self.particles['star']['position'][:,1] - yc
        z = self.particles['star']['position'][:,2] - zc
        # Get the scalefactor (age) of each star in the simulation
        a = self.particles['star']['form.scalefactor']
        # Get the mass of each star in the simulation
        m = self.particles['star']['mass']
        # Get the x,y,z velocity of each star particle in the simulation
        # And normalize it with the peculiar velocity of the indicated dark matter halo
        vx = self.particles['star']['velocity'][:,0] - vxc
        vy = self.particles['star']['velocity'][:,1] - vyc
        vz = self.particles['star']['velocity'][:,2] - vzc
        # Get the distance of each star from the center of the indicated dark matter halo
        distances = np.sqrt(np.square(x) + np.square(y) + np.square(z))
        # Get the radius of the galaxy that can actually hold stars
        # Rhalo, Mhalo, Vhalo <-> Rvir, Mvir, Vvir
        rgal = self.get_field('12')[id]
        # Filter out all stars that are too far away 
        x_gal = x[distances < rgal]
        y_gal = y[distances < rgal]
        z_gal = z[distances < rgal]
        a_gal = a[distances < rgal]
        m_gal = m[distances < rgal]
        vx_gal = vx[distances < rgal]
        vy_gal = vy[distances < rgal]
        vz_gal = vz[distances < rgal]
        # All the lists are the same length
        # Loop through and make a list of stars
        stars = []
        for i in range(len(x_gal)):
            star = Star(x_gal[i], y_gal[i], z_gal[i], m_gal[i], a_gal[i], vx_gal[i], vy_gal[i], vz_gal[i])
            stars.append(star)
        # Grab some more metadata for the halo
        hostID = self.ahf_data.field('hostHalo(2)')[id]
        mass = self.get_field('4')[id]
        rMax = self.ahf_data.field('Rmax(13)')[id] / self.h
        vMax = self.ahf_data.field('Vmax(17)')[id]
        vEsc = self.ahf_data.field('v_esc(18)')[id]
        numGas = self.ahf_data.field('n_gas(44)')[id]
        gasMass = self.ahf_data.field('M_gas(45)')[id]
        numStars = self.ahf_data.field('n_star(64)')[id]
        starMass = self.ahf_data.field('M_star(65)')[id]
        # Return the indicated dark matter halo
        halo = Halo(self, id, stars, xc, yc, zc, vxc, vyc, vzc, hostID, mass, rgal, rMax, vMax, vEsc, numGas, gasMass, numStars, starMass)
        return halo

    def get_field(self, field, divide_h = True):
        """
        Get the values in the column of the specified field from the .AHF_halos file.

        Parameters:
        ----------
        field : string
            The name of the field.

        divide_h : Boolean
            If you would like to divide by h (Hubble Constant).
            Automatically set to True.
        
        Returns
        -------
        The list of values in that field.
        """
        
        # Get the correct name of the field
        field_name = str(field).lower()  # Convert field to string if it's an integer
        field_name = field_name.replace('_','')
        # Loop through all the field names
        for item in self.ahf_data.dtype.names:
            string = item.lower().replace('_','')
            if field_name in string:
                field_name = item
                break 

        if divide_h == True:
            h_query = str(field).lower() # Convert field to string if its an integer
            for h_field in self.h_fields:
                string = h_field.lower().replace('_','')
                if h_query in string:
                    # Desired field is one where we must divide by h before returning
                    # Perform division by h
                    column = self.ahf_data.field(field_name) / self.h
                    return column
                
            # True was passed but the field is one where we do not divide by h
            column = self.ahf_data.field(field_name)
            return column
        else: 
            # Store all the field data in a list called column
            column = self.ahf_data.field(field_name) 
            # Return the column
            return column
    
    def help(self):
        '''
        Recieve help.
        '''
        def print_menu():
            print("---------------------------------------------------------------------------")
            print("a) What is a halo file (.AHF_halos)?")
            print("b) Print a list of fields from the halo file.")
            print("c) Clear this screen.")
            print("d) What is a simulation file (.hdf5)?")
            print("e) Print a list of fields from the particle file.")
            print("l) Print the list of libraries installed via pip3.")
            print("m) Print menu.")
            print("p) Print python paths.")
            print("q) Quit.")
            print("---------------------------------------------------------------------------")

        def print_halo_fields():
            print("\tID(1) - halo ID") 
            print("\thostHalo(2) - ID of host halo, 0 (or -1) if halo itself is not a subhalo") 
            print("\tMvir(4) - mass of halo [Mo/h]") 
            print("\tXc(6) - x position of halo [kpc/h]") 
            print("\tYc(7) - y position of halo [kpc/h]") 
            print("\tZc(8) - z position of halo [kpc/h]") 
            print("\tVXc(9) - x peculiar velocity of halo [km/sec]") 
            print("\tVYc(10) - y peculiar velocity of halo [km/sec]") 
            print("\tVZc(11) - z peculiar velocity of halo [km/sec]") 
            print("\tRvir(12) - virial radius [kpc/h]") 
            print("\tRmax(13) - position of rotation curve maximum [kpc/h]") 
            print("\tVmax(17) - maximum of rotation curve [km/sec]") 
            print("\tv_esc(18) - escape velocity at Rvir [km/sec]") 
            print("\tn_gas(44) - number of gas particles in halo")
            print("\tM_gas(45) - mass of gas particles in halo")
            print("\tn_star(64) - number of star particles in halo")
            print("\tM_star(65) - mass of star particles in halo")

        print_menu()
        while True:
            prompt = input("\nPress 'm' to see options menu. Enter an option: ").lower()
            print()
            if prompt == 'q' or prompt == "quit":
                break
            else:
                if prompt == 'a':
                    print("\tThe halo file is a summary of the data from the simulation file (.hdf5).")
                    print("\tTo see the names of all relevant fields, enter 'b'")
                elif prompt == 'b':
                    print_halo_fields()
                elif prompt == 'c':
                    os.system('clear')
                elif prompt == 'd':
                    print("\tThe simulation file contains information about all particles in the simulation.")
                    print("\tNeed to edit this stuff underneath when structure changes.")
                    print("\tCATEGORIES: star, gas")
                    print("\tTo see the names of all relevant fields, enter 'e'")
                    print("\tTo use: 'particles['CATEGORY']['FIELD']'")
                elif prompt == 'e':
                    print("\tStar - position, mass, massfraction, id.child, id.generation, id, form.scalefactor, velocity")  
                    print("\tGas - position, density, electron.fraction, temperature, mass, massfraction, hydrogen.neutral.fraction, id.child, id.generation, id, size, sfr, velocity")  
                elif prompt == 'l':
                    os.system('pip3 list')
                elif prompt == 'm':
                    print_menu()
                elif prompt == 'p':
                    os.system("echo $PYTHONPATH | tr ':' '\n'")
                else:
                    print("\tYou have not chosen a valid option.")
