import csv

# ==========================================================
# Function for reading a CSV file into a dictionary format
# ==========================================================

def read_variables_csv(csvfile):
    """
    Builds a Python dictionary object from an input CSV file.
    Helper function to read a CSV file on the disk, where user stores the limits/ranges of the process variables.
    """
    dict_key={}
    try:
        with open(csvfile) as f:
            reader = csv.DictReader(f)
            fields = reader.fieldnames
            for field in fields:
                lst=[]
                with open(csvfile) as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        lst.append(float(row[field]))
                dict_key[field]=lst
    
        return dict_key
    except:
        print("Error in reading the specified file from the disk. Please make sure it is in current directory.")
        return -1
        
# ===============================================================
# Function for writing the design matrix into an output CSV file
# ===============================================================

def write_csv(df,filename):
    """
    Writes a CSV file on to the disk from the internal Pandas DataFrame object i.e. the computed design matrix
    """
    try:
        filename=filename+'.csv'
        df.to_csv(filename)
    except:
        return -1