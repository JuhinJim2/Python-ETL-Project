import glob 
import pandas as pd 

def extract_from_csv(file_to_process): 
    dataframe = pd.read_csv(file_to_process) 
    return dataframe 

extracted_data = pd.DataFrame(columns=['name','height','weight'])  

for csvfile in glob.glob("*.csv"): 
    extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_csv(csvfile))], ignore_index=True) 

print(extracted_data)