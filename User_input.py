# ===========================================================================================
# Function for accepting the user input (choice) for desired DOE and the input CSV file name
# ===========================================================================================

def user_input():
    print("-"*60+"\n"+"Design of Experiments menu\n"+"-"*60+"\n")
    list_doe = ["1) Full factorial",
                "2) 2-level fractional factorial",
                "3) Plackett-Burman",
                "4) Sukharev grid",
                "5) Box-Behnken",
                "6) Box-Wilson (Central-composite) with center-faced option",
               "7) Box-Wilson (Central-composite) with center-inscribed option",
               "8) Box-Wilson (Central-composite) with center-circumscribed option",
                "9) Latin hypercube (simple)",
                "10) Latin hypercube (space-filling)",
                "11) Random k-means cluster",
                "12) Maximin reconstruction",
                "13) Halton sequence based",
                "14) Uniform random matrix"
               ]
    
    for choice in list_doe:
        print(choice)
    print("-"*60)
    
    doe_choice = int(input("Please make a choice for your Deisgn-of-Experiment build: "))
    infile = str(input("Please enter the name of the input csv file (enter only the name without the CSV extension): "))
    print()
    
    if (infile[-3:]!='csv'):
        infile=infile+'.csv'
      
    return (doe_choice,infile)