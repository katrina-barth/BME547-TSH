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


def Split_TSH(TSH, n):  # Function to extract individual patient's TSH data
    TSH_Individual = []
    TSH_Individual = TSH[n].split(",")
    TSH_Individual = TSH_Individual[1:]
    return TSH_Individual


def Diagnose_TSH(TSH_Individual):
    TSH_vals = []
    for x in TSH_Individual:
        TSH_vals.append(float(x))
    if max(TSH_vals) > 4.0:
        Diag = "hyperthyroidism"
    elif min(TSH_vals) < 1.0:
        Diag = 'hypothyroidism'
    else:
        Diag = 'normal thyroid function'
    return Diag

def Write_Patient_Files():
    data_list = Read_File()
    FN = FirstName(data_list)
    LN = LastName(data_list)
    A = Age(data_list)
    S = Sex(data_list)
    T = TSH(data_list)
    import json
    for i in range(len(FN)):
        patient_result = {
                    "Name": FN[i] + LN[i],
                    "Age": A[i],
                    "Sex": S[i],
                    "Diagnosis": Diagnose_TSH(Split_TSH(T, i)),
                    "TSH Results": Split_TSH(T, i),
                    }
        filename = str(FN[i]) + "-" + str(LN[i])
        out_file = open(filename + ".json", "w")
        json.dump(patient_result, out_file)
        out_file.close()


def main():
    Write_Patient_Files()


if __name__ == "__main__":
    main()
