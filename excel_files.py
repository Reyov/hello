import numpy as np
import pandas as pd
import os

my_values = list()

def get_files(dirName):
    allFiles = list()
    for root, dirs, files in os.walk(dirName):
            for file in files:
                if file.endswith('.xlsm'):
                    fullPath = (os.path.join(root, file))
                    allFiles.append(fullPath)
    return allFiles
               
#excel_file = 'test.xlsx'

#df = pd.read_excel(excel_file, engine='openpyxl')
#print(df) 

#print(df['Job Description'].where['Occupation'] == 'St. John Church')
#print(df['Job Number'].where(df['Job Description'] == 'St. John Church'))

#programmers = df['Job Number'].where(df['Job Description'] == 'St. John Church')
#print(programmers.dropna())

excel_files = ['test.xlsx','test1.xlsx','test2.xlsx']
for individual_file in excel_files:
    df = pd.read_excel(individual_file, engine='openpyxl')
    programmers = df['Job Number'].where(df['Job Description'] == 'St. John Church').dropna()
    print("File Name" +  individual_file)
    print(programmers)


listOfFiles = get_files('c:\Temp')
for e in listOfFiles:
    print(e)
    try:
        df = pd.read_excel(e, engine='openpyxl', sheet_name=0)
        x = df.loc[0][1]
        print(x)
    except:
        print("Error !!")
    

