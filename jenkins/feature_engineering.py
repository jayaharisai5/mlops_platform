from sys import implementation
from data_analysis import data_analysis         #importing the function from the another python file load_data.py

def feature_engineering():
    data = data_analysis()
    print(data.head())
    #finding the duplicate values from the data_frame
    duplicate = data[data.duplicated()]
    #print(duplicate.index)       
    #index values of the diplicates
    #removing the duplicates
    #print(data_frame.shape)             #checking the shape of the data frame before
    for i in duplicate.index:
        print( "index ", i, " is removed and no longer available")
        data.drop(index=[i], inplace = True)
        data.reset_index()                #resetting the index values
    #print(data_frame.shape)             #checking the shape of the dataframe after removing the duplicates
    #feature engineering the GENDER, LUNG_cancer features 
    data.replace({'gender':{'F':0,'M':1}},inplace=True)
    data.replace({'lung_cancer':{'YES':0,'NO':1}},inplace=True)

    #print(data_frame.head())  #here you can see the features are convereted by printing
    print(data.head())
    return data
feature_engineering()