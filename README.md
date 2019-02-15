# BME547-TSH
Reads in Patient Data to Analyze for Hypo- or Hyper- thyroidism

The code requires no command line input from the user to function. It pulls in a file 'test_data.txt' containing patient data. This data is sorted into names, ages, sexes, and TSH test results. Each patient's results are searched for any TSH levels which indicate hypothyroidism (TSH < 1) or hyperthyroidism (TSH > 4). The code then outputs a JSON file for each patient with their personal information, TSH levels, and diagnosis. 
