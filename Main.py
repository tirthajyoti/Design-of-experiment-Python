from Read_Write_CSV import *
from Generate_DOE import *
from User_input import *

import time

# ========================
# Main execution function
# ========================

def execute_main():
    """
    Main function to execute the program.
    Calls "user_input" function to receive the choice of the DOE user wants to build and to read the input CSV file with the ranges of the variables. Thereafter, it calls the "generate_DOE" function to generate the DOE matrix and a suitable filename corresponding to the user's DOE choice. Finally, it calls the "write_CSV" function to write the DOE matrix (a Pandas DataFrame object) into a CSV file on the disk, and prints a message indicating the filename.
    """
    doe_choice, infile = user_input()
    df, filename = generate_DOE(doe_choice,infile)
    if type(df)!=int or type(filename)!=int:
        flag=write_csv(df,filename)
        if flag!=-1:
            print("\nAnalyzing input and building the DOE...",end=' ')
            time.sleep(2)
            print("DONE!!")
            time.sleep(0.5)
            print(f"Output has been written to the file: {filename}.csv")
        else:
            print("\nError in writing the output. \nIf you have a file open with same filename, please close it before running the command again!")


#=====================================================
# Main UX with simple information about the software
#=====================================================
           
print()
print(" "*5+"Design-of-experiment builder by Dr. Tirthajyoti Sarkar, ON Semiconductor"+" "*5)
print(" "*20+"June 2018, Sunnyvale, CA 94086"+" "*20)
print(" "*10+"Uses the following packages: numpy, pandas, pydoe, diversipy"+" "*10)
print()

# Executes the main function
execute_main()