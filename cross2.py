import astropy.io.ascii as ascii
import gizmo_analysis as gizmo
import matplotlib.pyplot as plt
import os, re, json, numpy as np
# import scipy.integrate


def clear_console():
    '''
    Clear the console.
    '''
    if os.name == 'posix':  # Unix/Linux/MacOS
        os.system('clear')
    else:  # Windows
        os.system('cls')

def list_libraries():
    '''
    List the libraries installed with pip.
    '''
    os.system('pip3 list')

def help():
    '''
    Recieve help on a given topic.
    TODO - maybe put this in a loop and make iot a menu? Make it easy to call from command line?
    TODO - maybe in this function (or another) there can be options to run commands like 'clear', 'list_libraries', execute a file, install a package, etc.
    '''

    def print_menu():
        print("---------------------------------------------------------------------------")
        print("a) What is a halo file!!!")
        print("b) Print a list of fields from the halo file.")
        print("c) Clear this screen.")
        print("d) What is a simulation file?")
        print("e) Print a list of fields from the particle file.")
        print("l) Print the list of libraries installed via pip3.")
        print("m) Print menu.")
        print("q) Quit.")
        print("---------------------------------------------------------------------------")


    print_menu()
    while True:

        prompt = input("\nPress 'm' to see options menu. Enter an option: ").lower()
        print()

        if prompt == 'q' or prompt == "quit":
            break
        else:
            match prompt:
                case 'a':
                    print("\tThe halo file is a summary of the data from the simulation file.")
                    print("\tTo see the names of all relevant fields, enter 'b'")
                case 'b':
                    print("\tID(1) hostHalo(2) Mvir(4) Xc(6) Yc(7)") 
                    print("\tZc(8) VXc(9) VYc(10 VZc(11)")  
                    print("\tRvir(12) Rmax(13) Vmax(17) v_esc(18)")  
                    print("\tn_gas(44) M_gas(45) n_star(64) M_star(65)")
                case 'c':
                    clear_console()
                case 'd':
                    print("\tThe simulation file contains information about all particles in the simulation.")
                    print("\tCATEGORIES: star, gas")
                    print("\tTo see the names of all relevant fields, enter 'e'")
                    print("\tTo use: 'particles['CATEGORY']['FIELD']'")
                case 'e':
                    print("\tStar - position, mass, massfraction, id.child, id.generation, id, form.scalefactor, velocity")  
                    print("\tGas - position, density, electron.fraction, temperature, mass, massfraction, hydrogen.neutral.fraction, id.child, id.generation, id, size, sfr, velocity")  
                case 'l':
                    list_libraries()
                case 'm':
                    print_menu()
                case _:
                    print("\tYou have not chosen a valid option.")

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
    return data

def get_ahf_data(path: str):
    '''
    Get the relevant data from the AHF file.

    Parameters:
    ----------
        path : str 
            the path to the file

    Returns
    -------
        Return a 2D list of the filtered data specified in the AHF file.
    '''
    data = read_ahf_file(path)
    data_filtered = data[(data.field('fMhires(38)') > 0.99)]
    return data_filtered

def dist(x, y, z):
    '''
    Get the magnitude of a vector with three components (x, y, z).

    Parameters:
    ----------
        x : float | int 
            The x component of the vector.
        y : float | int 
            The y component of the vector.
        z : float | int 
            The z component of the vector.

    Returns
    -------
        The magnitude of the vector.
    '''

    result = np.sqrt(np.square(x) + np.square(y) + np.square(z))
    return result



def star_scatter_plot(x, y, z, parts = None, whole = None):
    '''
    Generate a scatter plot by supplying a list of x, y, and z values.

    Parameters:
    ----------
        x : list
            The list of x values.
        y : list
            The list of y values.
        z : list
            The list of z values.
        parts : list
            list of values (like form.scalar factor) associated with each star
        whole : number
            the whole number to compare to each part

    '''

    ax = plt.axes(projection='3d')
    fig = plt.gcf()
    scatter = None

    if parts is not None and whole is not None:
        colors = np.array([part / whole for part in parts])  # Calculate color based on the ratio
        colors = np.where(colors > 0.5, 'green', 'blue')
        # Generate a scatter plot with the specified colors
        # vmin = 0, vmax = 0.5
        scatter = ax.scatter3D(x, y, z, c=colors, cmap='Blues')
    else:
        # Generate a scatter plot without color mapping
        scatter = ax.scatter3D(x, y, z)

    fig.colorbar(scatter)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('3D Scatter Plot')
    ax.grid(False)
    plt.show()

def pie_chart(values, labels):
    '''
    Generate a pie chart by supplying a list of labels and values.

    Parameters:
    ----------
        labels : list
            The list of labels.
        values : list
            The list of values.
    '''
    sizes = [count for count in values if count > 3]
    explode = [0.1 if size == max(sizes) else 0 for size in sizes]
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', explode=explode)
    ax.legend(loc="best")
    plt.show()

def graph(x, y, title = None, x_label = None, y_label = None, windowTitle = "Figure", showLine = True):
    '''
    Generate a 2d graph with given x and y values.

    Parameters:
    ----------
        labels : list
            The list of labels.
        values : list
            The list of values.
    '''
    # Auto generate x_label and y_label with the given title
    if title is not None:
        pattern = r'\s*(vs\.|versus|vs)\s*'
        match = re.search(pattern, title, re.IGNORECASE)
        if match:
            before = title[:match.start()].strip()
            after = title[match.end():].strip()
            x_label = x_label if x_label is not None else after
            y_label = y_label if y_label is not None else before


    # Create a line plot
    if(showLine):
        #find line of best fit
        a, b = np.polyfit(x, y, 1)    
        # 'b.-' - This parameter is a shorthand notation to specify the line color, marker style, and line style of the plot.
        plt.plot(x, y, 'b.-')
    else:
        plt.scatter(x,y)

    # Set the x and y axis labels
    plt.xlabel(x_label if x_label is not None else 'X')
    plt.ylabel(y_label if y_label is not None else 'Y')
    # Set the title of the graph
    plt.title(title if title is not None else 'Y vs X')
    fig = plt.gcf()
    fig.canvas.manager.set_window_title(windowTitle)
    # Display the graph
    plt.show()



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

def getField(data, field, limit = None):
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



def plot_gas_dens(part,data,header,runname,bins=70,ind=0,thick=None,vmin=None,vmax = None):
    """

    """
    import scipy

    ################### LOAD PARTICLE INFO #########################
    h = header['hubble']

    ###########################################

    maincen = np.array([data.field('Xc(6)')[ind]/h,data.field('Yc(7)')[ind]/h,data.field('Zc(8)')[ind]/h])
    mainrvir = data.field('Rvir(12)')[ind]/h

    if thick is None:
        thick = mainrvir

    pos = part['gas']['position'][:]
    pos = pos - maincen
    mass = part['gas']['mass'][:]


    x = pos[:,0] 
    y = pos[:,1] 
    z = pos[:,2] 

    x = x[np.abs(z) < thick]
    y = y[np.abs(z) < thick]
    mass = mass[np.abs(z) < thick]

    mass = mass[((np.abs(x)<=thick)&(np.abs(y)<=thick))]
    xx = x[((np.abs(x)<=thick)&(np.abs(y)<=thick))]
    yy = y[((np.abs(x)<=thick)&(np.abs(y)<=thick))]

    ret = scipy.stats.binned_statistic_2d(xx, yy, mass, statistic='sum', bins=bins)

    # Calc area per bin
    dx = np.diff(ret.x_edge)
    dy = np.diff(ret.y_edge)
    area = dx[:,  None] * dy


    plt.clf()
    fig = plt.figure(1, figsize = (10,10))
    ax1 = fig.add_subplot(1,1,1)
    ax1.patch.set_facecolor('black')

    if vmin is None:
        plt.imshow(np.log10(ret.statistic/area), cmap='seismic', interpolation='gaussian')
    else:
        plt.imshow(np.log10(ret.statistic/area), cmap='seismic', interpolation='gaussian',vmin = vmin,vmax = vmax)

    cbar = plt.colorbar()
    cbar.ax.setylabel(r'$\rm log ,\Sigma ,(M{\odot}/pc^2)$', fontsize = 22)
    plt.savefig("FDensHist%s%i%i.png"%(runname,thick,bins))



