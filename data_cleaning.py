import pandas as pd

file_path=r"D:\Projects\College Student Performance Analytics System\data\student_performance_1000.csv"
def load_data(file_path):
    df = pd.read_csv(file_path)
    return df


def clean_data(df):

    df = df.drop_duplicates()

    df["Gender"] = df["Gender"].map({"Male": 0, "Female": 1})

    df["Final_Result"] = df["Final_Result"].map({
        "Fail": 0,
        "Pass": 1
    })

    return df