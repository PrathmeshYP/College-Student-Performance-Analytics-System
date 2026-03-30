def create_features(df):

    df["Total_Score"] = (
        df["Internal_Marks"]
        + df["Assignment_Score"]
        + df["Final_Marks"]
    )

    df["Study_Efficiency"] = df["Final_Marks"] / df["Study_Hours"]

    return df


def detect_risk(row):

    if row["Attendance"] < 60:
        return "High Risk"

    elif row["Study_Hours"] < 2:
        return "Medium Risk"

    elif row["Internal_Marks"] < 50:
        return "High Risk"

    else:
        return "Low Risk"


def add_risk_feature(df):

    df["Risk_Level"] = df.apply(detect_risk, axis=1)

    return df