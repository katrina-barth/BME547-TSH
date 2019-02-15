# TSH_Reader
# Katrina Barth , 02/14/19
# Reads in patient data and detects presence of hyper- or hypo- thyroidism


def Read_File():
    """Open and Read Patient Data File

    Opens and reads a file called 'test_data.txt' with patient information
    listed with name, age, sex, and TSH test results, each on their own line.
    The function takes the data and puts it into a list.

    Args:
        none

    Returns:
        list: sorted patient data
    """
    f = open('test_data.txt', 'r')
    data = f.read()
    f.close()
    data_list = data.split()
    return data_list


def FirstName(patients):
    """Extract first names from the patient data

    Extracts the first names of all patients from the list of patient
    information. This is done by extracting every 5th entry in the list.

    Args:
        list: patient data

    Returns:
        list: all patient first names
    """
    FirstName = []
    for i in range(int((len(patients)-1)/5)):
        FirstName.append(patients[i*5])
    return FirstName


def LastName(patients):
    """Extract last names from the patient data

    Extracts the last names of all patients from the list of patient
    information. This is done by extracting every 5th entry in the list.

    Args:
        list: patient data

    Returns:
        list: all patient last names
    """
    LastName = []
    for i in range(int((len(patients)-1)/5)):
        LastName.append(patients[(i*5) + 1])
    return LastName


def Age(patients):
    """Extract ages from the patient data

    Extracts the ages of all patients from the list of patient
    information. This is done by extracting every 5th entry in the list.

    Args:
        list: patient data

    Returns:
        list: all patient ages
    """
    Age = []
    for i in range(int((len(patients)-1)/5)):
        Age.append(patients[(i*5) + 2])
    return Age


def Sex(patients):
    """Extract sexes from the patient data

    Extracts the sexes of all patients from the list of patient
    information. This is done by extracting every 5th entry in the list.

    Args:
        list: patient data

    Returns:
        list: all patient sexes
    """
    Sex = []
    for i in range(int((len(patients)-1)/5)):
        Sex.append(patients[(i*5) + 3])
    return Sex


def TSH(patients):
    """Extract TSH values from the patient data

    Extracts the TSH test results of all patients from the list of patient
    information. This is done by extracting every 5th entry in the list. Each
    entry in this new output list is a string of the test results for
    a given patient.

    Args:
        list: patient data

    Returns:
        list: string of TSH test results
    """
    TSH = []
    for i in range(int((len(patients)-1)/5)):
        TSH.append(patients[(i*5) + 4])
    return TSH


def Split_TSH(TSH, n):  # Function to extract individual patient's TSH data
    """Splits the string of TSH test results into list

    Takes a patient's string of TSH test results and puts it into a list.

    Args:
        list: array of all TSH result strings
        integer: index of patient of interest

    Returns:
        list: the specified patient's TSH results
    """
    TSH_Individual = []
    TSH_Individual = TSH[n].split(",")
    TSH_Individual = TSH_Individual[1:]
    return TSH_Individual


def Diagnose_TSH(TSH_Individual):
    """Searches for TSH values to determine diagnosis

    Takes a patient's array of TSH test results looks for any values above 4.0
    or below 1.0. If above 4.0, the patient is diagnosed as having
    hyperthyroidism, and if below 1.0, the patient is diagnosed as having
    hypothyroidism. Otherwise, the patient is labeled as having normal thyroid
    function.

    Args:
        list: array of the patient's TSH results

    Returns:
        string: diagnosis
    """
    TSH_vals = []
    for x in TSH_Individual:
        TSH_vals.append(float(x))
    if max(TSH_vals) > 4.0:
        Diag = 'hyperthyroidism'
    elif min(TSH_vals) < 1.0:
        Diag = 'hypothyroidism'
    else:
        Diag = 'normal thyroid function'
    return Diag


def Write_Patient_Files():
    """Compiles patient information and diagnosis into files

    Takes a patient's information and diagnosis from the information arrays and
    outputs into a JSON format file.

    Args:
        none

    Returns:
        none
    """
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
