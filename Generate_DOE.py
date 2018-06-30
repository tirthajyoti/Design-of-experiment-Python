from DOE_functions import *
from Read_Write_CSV import *

# ====================================================================
# Function to generate the DOE based on user's choice and input file
# ====================================================================

def generate_DOE(doe_choice, infile):
    """
    Generates the output design-of-experiment matrix by calling the appropriate function from the "DOE_function.py file".
    Returns the generated DataFrame (Pandas) and a filename (string) corresponding to the type of the DOE sought by the user. This filename string is used by the CSV writer function to write to the disk i.e. save the generated DataFrame in a CSV format.
    """
    
    dict_vars = read_variables_csv(infile)
    if type(dict_vars)!=int:
        factor_count=len(dict_vars)
    else:
        return (-1,-1)
    
    if doe_choice==1:
        df=build_full_fact(dict_vars)
        filename='Full_factorial_design'
    
    elif doe_choice==2:
        print("For this choice, you will be asked to enter a generator string expression. Please only use small letters e.g. 'a b c bc' for the string. Make sure to put a space in between every variable. Please note that the number of character blocks must be identical to the number of factors you have in your input file.\n")
        gen_string=str(input("Please enter the generator string for the fractional factorial build: "))
        print()
        if len(gen_string.split(' '))!=factor_count:
            print("Length of the generator string does not match the number of factors/variables. Sorry!")
            return (-1,-1)
        df=build_frac_fact(dict_vars,gen_string)
        filename='Fractional_factorial_design'
    
    elif doe_choice==3:
        df=build_plackett_burman(dict_vars)
        filename='Plackett_Burman_design'
    
    elif doe_choice==4:
        num_samples=int(input("Please enter the number of samples: "))
        print()
        df=build_sukharev(dict_vars,num_samples)
        filename='Sukharev_grid_design'
    
    elif doe_choice==5:
        num_center=int(input("Please enter the number of center points to be repeated (if more than one): "))
        print()
        df=build_box_behnken(dict_vars,num_center)
        filename='Box_Behnken_design'
    
    elif doe_choice==6:
        #num_center=int(input("Please enter the number of center points to be repeated (if more than one): "))
        print()
        df=build_central_composite(dict_vars,face='ccf')
        filename='Box_Wilson_face_centered_design'
    
    elif doe_choice==7:
        #num_center=int(input("Please enter the number of center points to be repeated (if more than one): "))
        print()
        df=build_central_composite(dict_vars,face='cci')
        filename='Box_Wilson_face_inscribed_design'
    
    elif doe_choice==8:
        #num_center=int(input("Please enter the number of center points to be repeated (if more than one): "))
        print()
        df=build_central_composite(dict_vars,face='ccc')
        filename='Box_Wilson_face_circumscribed_design'
    
    elif doe_choice==9:
        num_samples=int(input("Please enter the number of random sample points to generate: "))
        print()
        df=build_lhs(dict_vars,num_samples=num_samples)
        filename='Simple_Latin_Hypercube_design'
    
    elif doe_choice==10:
        num_samples=int(input("Please enter the number of random sample points to generate: "))
        print()
        df=build_space_filling_lhs(dict_vars,num_samples=num_samples)
        filename='Space_filling_Latin_Hypercube_design'
    
    elif doe_choice==11:
        num_samples=int(input("Please enter the number of random sample points to generate: "))
        print()
        df=build_random_k_means(dict_vars,num_samples=num_samples)
        filename='Random_k_means_design'
    
    elif doe_choice==12:
        num_samples=int(input("Please enter the number of random sample points to generate: "))
        print()
        df=build_maximin(dict_vars,num_samples=num_samples)
        filename='Maximin_reconstruction_design'
    
    elif doe_choice==13:
        num_samples=int(input("Please enter the number of random sample points to generate: "))
        print()
        df=build_halton(dict_vars,num_samples=num_samples)
        filename='Halton_sequence_design'
    
    elif doe_choice==14:
        num_samples=int(input("Please enter the number of random sample points to generate: "))
        print()
        df=build_uniform_random(dict_vars,num_samples=num_samples)
        filename='Uniform_random_matrix_design'
    
    return (df,filename)