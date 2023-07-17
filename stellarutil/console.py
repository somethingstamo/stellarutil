import os, sys

def clear_console():
    '''
    Clear the console.
    '''
    os.system('clear')

def list_libraries():
    '''
    List the libraries installed with pip.
    '''
    os.system('pip3 list')

def python_path():
    '''
    List the libraries installed with pip.
    '''
    os.system("echo $PYTHONPATH | tr ':' '\n'")

def create_directory(name):
    print(f"Creating a directory named {name}.")
    print(f"Put any data files in {name}/data.")
    print(f"Put any code files in {name}/src.")

    os.system(f'mkdir {name}')
    os.system(f'mkdir {name}/src')
    os.system(f'mkdir {name}/data') 
    os.system(f'touch {name}/.gitignore')
    os.system(f'echo "data" >> {name}/.gitignore')
    os.system(f'touch {name}/todo.txt')
    os.system(f'echo "This file is used to keep track of your tasks.\nIt is optional, so delete it if you wish." >> {name}/todo.txt')
    os.system(f'touch {name}/src/main.py')
    os.system(f'echo "from stellarutil.simulation import Simulation\n\n# Sample code - please delete if needed.\n\nsimulation = Simulation()\n\n# Print hubble constant\nprint(simulation.h)" >> {name}/src/main.py')

    


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
        print("o) Create new project directory.")
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

def help():
    '''
    Recieve help on a given topic.
    You can call this function by simply typing 'stellarutil' in the command line.
    '''
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
                clear_console()
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
                list_libraries()
            elif prompt == 'm':
                print_menu()
            elif prompt == 'p':
                python_path()
            elif prompt == 'o':
                name = input("\nWhat do you want to name the directory: ")
                create_directory(name)
            else:
                print("\tYou have not chosen a valid option.")


def entry():
    num_args = len(sys.argv)
    if num_args == 1:
        help()
    elif (num_args == 2 or num_args == 3) and sys.argv[1] == "create":
        create_directory(sys.argv[2] if num_args == 3 else "galaxy_research")
    else:
        print("Invalid Input.\nUsage:")
        print("\tstellarutil\t\t\tSee help menu.")
        print("\tstellarutil create <name>\tCreate a directory to start coding.")
    