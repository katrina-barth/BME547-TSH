# TSH_Reader
# Katrina Barth , 02/14/19
# Reads in patient data and detects presence of hyper- or hypo- thyroidism


def Read_File():  # Function to read in patient data file
    f = open('test_data.txt', 'r')
    data = f.read()
    f.close()
    data_list = data.split()
    return data_list


def FirstName(patients):  # Function to extract patient first names
    FirstName = []
    for i in range(int((len(patients)-1)/5)):
        FirstName.append(patients[i*5])
    return FirstName


def LastName(patients):
    LastName = []
    for i in range(int((len(patients)-1)/5)):
        LastName.append(patients[(i*5) + 1])
    return LastName


def Age(patients):
    Age = []
    for i in range(int((len(patients)-1)/5)):
        Age.append(patients[(i*5) + 2])
    return Age


def Sex(patients):
    Sex = []
    for i in range(int((len(patients)-1)/5)):
        Sex.append(patients[(i*5) + 3])
    return Sex


def TSH(patients):
    TSH = []
    for i in range(int((len(patients)-1)/5)):
        TSH.append(patients[(i*5) + 4])
    return TSH


def Split_TSH(TSH,n):  # Function to extract individual patient's TSH data
    TSH_Individual = []
    TSH_Individual = TSH[n].split(",")
    TSH_Individual = TSH_Individual[1:]
    return TSH_Individual


def main():
    data_list = Read_File()
    FN = FirstName(data_list)
    LN = LastName(data_list)
    A = Age(data_list)
    S = Sex(data_list)
    T = TSH(data_list)
    # print(data_list)
    # print(int((len(data_list)-1)/5))
    # print(FN)
    # print(LN)
    # print(A)
    # print(S)
    # print(T)
    print(Split_TSH(T,2))


if __name__ == "__main__":
    main()
