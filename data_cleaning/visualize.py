import matplotlib.pyplot as plt
import pandas as pd
import os

def visualization(subject_name, folders):
    file_path = f"./Step-3 T-Test/{subject_name}/Speech/{subject_name}__Speech__{folders[0]}_{folders[1]}.csv"

    if os.path.isfile(file_path):
        df = pd.read_csv(file_path)
        counts = df['Significant Difference'].value_counts()

        plt.bar(counts.index, counts.values, color=['green' if x == 'No' else 'orange' for x in counts.index])
        plt.xlabel('Significant Difference')
        plt.ylabel('Count')
        plt.title(f"{subject_name} {folders[0]} and {folders[1]} data T-test Distribution(Speech)")
        plt.show()

    else:
        print("CSV file not found.")