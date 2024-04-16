import numpy as np
import pandas as pd
import os

def isDirectoryExist(path):
    return os.path.isdir(path)

def getPathJoiner(folder_path, folder_name):
    return os.path.join(folder_path, folder_name)

# Data Cleaning function
def csv_cleaner(uncleaned_folder_path, cleaned_folder_path, subject_name):
    for folder_name in os.listdir(uncleaned_folder_path): # Path traverse
        test_list_folder = getPathJoiner(uncleaned_folder_path, folder_name)
        for img_speech_folders in os.listdir(test_list_folder):
            absolute_csv_path = getPathJoiner(test_list_folder, img_speech_folders)

            # Check if the current item is a folder
            if isDirectoryExist(absolute_csv_path):
                print("Folder cleaned :- ", absolute_csv_path)

                output_file_abs = getPathJoiner(cleaned_folder_path, f'{folder_name}/{img_speech_folders}')

                if not os.path.exists(output_file_abs):
                    os.makedirs(output_file_abs)

                for file_name in os.listdir(absolute_csv_path):
                    if file_name.endswith('.csv'):
                        input_file_path = getPathJoiner(
                            absolute_csv_path, file_name)
                        output_file_path = getPathJoiner(
                            output_file_abs, f'cleaned_{file_name}')
                        
                        if file_name.startswith('mindMonitor'):
                            print("Filename change")
                            output_file_path = output_file_path.replace("mindMonitor", subject_name +"_" + img_speech_folders)

                        df = pd.read_csv(input_file_path)

                        # Convert the 'TimeStamp' column to datetime
                        df['TimeStamp'] = pd.to_datetime(df['TimeStamp'])

                        s_time = df['TimeStamp'].iloc[0] + pd.Timedelta(seconds=15)

                        e_time = df['TimeStamp'].iloc[-1] - pd.Timedelta(seconds=15)

                        # Remove rows within the first 15 seconds
                        df = df[df['TimeStamp'] > s_time]

                        # Remove rows within the last 15 seconds
                        df = df[df['TimeStamp'] < e_time]

                        selected_columns = df.iloc[:, :21]
                        selected_columns = selected_columns.dropna()

                        # Replace inf values with NaN
                        selected_columns.replace([np.inf, -np.inf], np.nan, inplace=True)

                        # Drop rows containing NaN values
                        selected_columns.dropna(axis=0, inplace=True)

                        selected_columns.to_csv(output_file_path, index=False)

                        print(f"Data has been cleaned (NaN values removed) and saved to {output_file_path}")
