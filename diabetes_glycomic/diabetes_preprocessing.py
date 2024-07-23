import pandas as pd
import csv

def main():

    # Import the data
    df = pd.read_csv('data/HG_FinnRisk.txt', sep="\t", decimal=',')

    # Drop redundant columns and derived traits
    df_filtered = df.drop(columns=["PREVAL_DIAB","INCIDENT_DIAB","DIAB_T2","INCIDENT_DIAB_T2","PREVAL_DIAB_T2","LB","HB","S0","S1","S2","S3","S4","G0","G1","G2","G3","G4"])

    # Add GlyTouCan (https://glytoucan.org/) accessions to glycan peak (GP) headers
    headers = pd.read_csv('mapping_files/gtc_headers.csv', sep=",")
    header_list = df_filtered.columns[:5].to_list()
    header_list += headers['Header'].to_list()
    df_filtered.columns=header_list

    # Move target labels to last column
    df_final = df_filtered.drop(columns="DIABETES")
    df_final["DIABETES"] = df_filtered["DIABETES"]

    # Save dataframe to csv file
    df_final.to_csv("human_proteoform_ml_ready_diabetes_glycomic.csv",sep=",",index=False,quoting=csv.QUOTE_ALL)

if __name__ == '__main__':
    main()