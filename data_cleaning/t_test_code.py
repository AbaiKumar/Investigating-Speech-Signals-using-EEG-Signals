import os
import pandas as pd
from scipy.stats import ttest_ind

list_of_folders = ["Doctor", "Pain", "No", "Move", "Water", "Yes", "Toilet", "Silent"]


def perform_T_Test(subject_name, cleaned_folder_path):
    print("------------- T-Test -------------")

    speech_output_path = f'./Step-3 T-test/{subject_name}/Speech'

    # Create the output folder if it doesn't exist
    if not os.path.exists(speech_output_path):
        os.makedirs(speech_output_path, exist_ok=True)

    for i, folder1 in enumerate(list_of_folders):
        for j, folder2 in enumerate(list_of_folders):
            if j > i:
                for inner_folder in os.listdir(os.path.join(cleaned_folder_path, folder1)):
                    group1 = os.path.join(os.path.join(
                        cleaned_folder_path, folder1,), inner_folder)
                    group2 = os.path.join(os.path.join(
                        cleaned_folder_path, folder2,), inner_folder)

                    # Significance level (alpha)
                    alpha = 0.05

                    result_matrix = []

                    for group1_data, group2_data in zip(os.listdir(group1), os.listdir(group2)):
                        group1_file_path = os.path.join(group1, group1_data) #Water
                        group2_file_path = os.path.join(group2, group2_data) #Silent
                        print(group1_file_path)
                        print(group2_file_path)

                        df_group1 = pd.read_csv(group1_file_path)
                        df_group2 = pd.read_csv(group2_file_path)

                        numeric_columns_silent = df_group1.columns[1:]
                        numeric_columns_pain = df_group2.columns[1:]

                        for col_group1, col_group2 in zip(numeric_columns_silent, numeric_columns_pain):
                            stat, p_value = ttest_ind(
                                df_group1[col_group1], df_group2[col_group2], nan_policy='omit')

                            col1 = folder1 + "_Group_1"
                            col2 = folder2 + "_Group_2"
                            col3 = f"Column {folder1}_Group_1"
                            col4 = f"Column {folder2}_Group_2"
                            col5 = "T-Statistic"
                            col6 = "P-Value"
                            col7 = "Significant Difference"

                            result_dict = {
                                col1: group1_data,
                                col2: group2_data,
                                col3: col_group1,
                                col4: col_group2,
                                col5: stat,
                                col6: p_value,
                                col7: "Yes" if p_value < alpha else "No"
                            } # Header for csv

                            result_matrix.append(result_dict)

                    result_df = pd.DataFrame(result_matrix, columns=[
                                             col1, col2, col3, col4, col5, col6, col7])
                    
                    cycle_length = 20
                    result_df["S.No"] = list(range(1, len(result_df) + 1))
                    result_df["S.No"] = (result_df["S.No"] - 1) % cycle_length + 1

                    result_df = result_df[["S.No"] + list(result_df.columns[:-1])]

                    result_csv_path = os.path.join((speech_output_path if inner_folder == "Speech" else "img"), f"{subject_name}__{inner_folder}__{folder1}_{folder2}.csv")
                    result_df.to_csv(result_csv_path, index=False)