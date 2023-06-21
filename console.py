import os

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

def python_path():
    '''
    List the libraries installed with pip.
    '''
    os.system("echo $PYTHONPATH | tr ':' '\n'")

def help():
    '''
    Recieve help on a given topic.
    You can call this function by simply typing 'stellarutil' in the command line.
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
        print("p) Print python paths.")
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
                case 'p':
                    python_path()
                case _:
                    print("\tYou have not chosen a valid option.")
