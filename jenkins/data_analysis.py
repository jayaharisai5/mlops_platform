from load_data import load_data

def data_analysis():
    data = load_data()
    print(data)
    data_types = data.dtypes
    #checking the null values
    data_null_values = data.isnull().sum()
    print(data_null_values)
    print(data_types)
    return data
data_analysis()