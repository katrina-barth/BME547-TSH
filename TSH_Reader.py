# TSH_Reader
# Katrina Barth , 02/14/19
# Reads in patient data and detects presence of hyper- or hypo- thyroidism

# Function to read in patient data file
def Read_File():
    f = open('test_data.txt', 'r')
    data = f.read()
    f.close()
    return data

def main():
    data = Read_File()
    print(data)

if __name__ == "__main__":
    main()
