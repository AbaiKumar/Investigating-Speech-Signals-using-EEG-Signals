from data_cleaning.cleaner import *
from data_cleaning.t_test_code import *
from data_cleaning.visualize import *
import shutil

def execute(**kwargs):
    if kwargs["clean"] == 1:
        csv_cleaner(kwargs["uncleanedfolder"], kwargs["cleanedfolder"], kwargs["subject_name"])
        print()

    if kwargs["t_test"] == 1:
        perform_T_Test(kwargs["subject_name"], kwargs["cleanedfolder"])
        print()

    if kwargs["visualize"] == 1:
        visualization(kwargs["subject_name"], folders)
        print()

def makeSilentFolders():
    for subject_name in os.listdir("./Step-1 Raw Data/"):
        subject_path = f'./Step-1 Raw Data/{subject_name}/Silent'
        d1 = f'./Step-1 Raw Data/{subject_name}/Silent/Speech'
        if os.path.exists(d1):
            return
        os.makedirs(d1, exist_ok=True)

        # Move all CSV files to the destination directory
        for filename in os.listdir(subject_path):
            print(filename)
            if filename.endswith(".csv"):
                source_path = os.path.join(subject_path, filename)
                print(source_path)
                shutil.move(source_path, d1)
        
        for filename in os.listdir(d1):
            if filename.endswith(".csv"):
                source_path = os.path.join(d1, filename)
                destination_path = os.path.join(d2, filename)
                shutil.copy(source_path, destination_path)

folders = ["Doctor", "Silent"]

if __name__ == "__main__":
    makeSilentFolders()
    
    # clean folders
    for each_subject in os.listdir("./Step-1 Raw Data"):
        execute(clean = 0, t_test = 0, visualize = 1, cleanedfolder = f"./Step-2 Cleaned Data/{each_subject}", uncleanedfolder = os.path.join("./Step-1 Raw Data", each_subject), subject_name = each_subject)