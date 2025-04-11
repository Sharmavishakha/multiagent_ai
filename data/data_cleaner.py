# import pandas as pd

# # Load original dataset
# df = pd.read_csv(r"C:/Users/hp/OneDrive/Desktop/ollama/Dataset/[Usecase 4] AI for Elderly Care and Support/health_monitoring.csv")

# # Convert Timestamp to datetime
# df["Timestamp"] = pd.to_datetime(df["Timestamp"])

# # Convert Yes/No columns to 1/0
# binary_cols = [
#     "Heart Rate Below/Above Threshold (Yes/No)",
#     "Blood Pressure Below/Above Threshold (Yes/No)",
#     "Glucose Levels Below/Above Threshold (Yes/No)",
#     "SpO₂ Below Threshold (Yes/No)",
#     "Alert Triggered (Yes/No)",
#     "Caregiver Notified (Yes/No)",
# ]
# for col in binary_cols:
#     df[col] = df[col].map({"Yes": 1, "No": 0})

# # Split Blood Pressure into Systolic and Diastolic
# def split_bp(bp_str):
#     if isinstance(bp_str, str) and "/" in bp_str:
#         systolic, diastolic = bp_str.replace(" mmHg", "").split("/")
#         return pd.Series([int(systolic), int(diastolic)])
#     return pd.Series([None, None])

# df[["Systolic BP", "Diastolic BP"]] = df["Blood Pressure"].apply(split_bp)

# # Drop original Blood Pressure column
# df.drop(columns=["Blood Pressure"], inplace=True)

# # Reorder columns
# desired_order = [
#     "Device-ID/User-ID", "Timestamp", "Heart Rate",
#     "Heart Rate Below/Above Threshold (Yes/No)",
#     "Blood Pressure Below/Above Threshold (Yes/No)",
#     "Glucose Levels", "Glucose Levels Below/Above Threshold (Yes/No)",
#     "Oxygen Saturation (SpO₂%)", "SpO₂ Below Threshold (Yes/No)",
#     "Alert Triggered (Yes/No)", "Caregiver Notified (Yes/No)",
#     "Systolic BP", "Diastolic BP"
# ]
# df = df[desired_order]

# # Save the cleaned dataset
# df.to_csv("cleaned_health_vitals.csv", index=False)
# print("Dataset cleaned and saved as 'cleaned_health_vitals.csv'")



# dataset-3---------------------------------------------
# import pandas as pd

# # Load the raw dataset
# df = pd.read_csv(r"C:/Users/hp/OneDrive/Desktop/ollama/Dataset/[Usecase 4] AI for Elderly Care and Support/safety_monitoring.csv")

# # Convert "-" and missing values in 'Impact Force Level' to NaN, then fill with 0 (or any default)
# df["Impact Force Level"] = pd.to_numeric(df["Impact Force Level"], errors="coerce")
# df["Impact Force Level"] = df["Impact Force Level"].fillna(0)

# # Optional: clean other fields too if needed
# df["Fall Detected (Yes/No)"] = df["Fall Detected (Yes/No)"].replace({"Yes": 1, "No": 0})
# df["Alert Triggered (Yes/No)"] = df["Alert Triggered (Yes/No)"].replace({"Yes": 1, "No": 0})
# df["Caregiver Notified (Yes/No)"] = df["Caregiver Notified (Yes/No)"].replace({"Yes": 1, "No": 0})

# # Save the cleaned dataset
# df.to_csv("cleaned_safety_monitoring.csv", index=False)

# import pandas as pd

# def clean_safety_data(file_path):
#     df = pd.read_csv(file_path)

#     # Convert Timestamp to datetime
#     df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce')

#     # Normalize string columns: strip spaces and standardize casing
#     str_cols = ['Movement Activity', 'Location']
#     for col in str_cols:
#         df[col] = df[col].astype(str).str.strip().str.title()

#     # Replace "-" with NaN in numeric columns
#     df['Impact Force Level'] = pd.to_numeric(df['Impact Force Level'].replace('-', None), errors='coerce')
#     df["Impact Force Level"] = df["Impact Force Level"].fillna(0)
#     df['Post-Fall Inactivity Duration (Seconds)'] = pd.to_numeric(df['Post-Fall Inactivity Duration (Seconds)'], errors='coerce')

#     # Convert Yes/No columns to binary
#     yes_no_cols = [
#         'Fall Detected (Yes/No)',
#         'Alert Triggered (Yes/No)',
#         'Caregiver Notified (Yes/No)'
#     ]
#     for col in yes_no_cols:
#         df[col] = df[col].fillna('No').map({'Yes': 1, 'No': 0})

#     # Optional: Print missing values
#     print("Missing values after cleaning:\n", df.isnull().sum())

#     # Save cleaned version
#     df.to_csv("cleaned_safety_monitoring.csv", index=False)
#     return df

# # Example usage
# clean_safety_data(r"C:/Users/hp/OneDrive/Desktop/ollama/Dataset/[Usecase 4] AI for Elderly Care and Support/safety_monitoring.csv")


# reminder data-------------------
import pandas as pd
import numpy as np
def clean_reminder_data(csv_path, save_cleaned_path="cleaned_reminders.csv"):
    df = pd.read_csv(csv_path)

    # Remove trailing empty column
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

    # Replace Yes/No with 1/0
    df.replace({"Yes": 1, "No": 0}, inplace=True)

    # Convert 'Timestamp' to datetime
    df["Timestamp"] = pd.to_datetime(df["Timestamp"], errors="coerce")

    # Create full datetime for Scheduled Time by combining date from Timestamp
    df["Scheduled Time"] = pd.to_datetime(
        df["Timestamp"].dt.date.astype(str) + " " + df["Scheduled Time"],
        errors="coerce"
    )

    # ✅ Save to a new file
    df.to_csv(save_cleaned_path, index=False)

    return df

df = clean_reminder_data(r"C:/Users/hp/OneDrive/Desktop/ollama/Dataset/[Usecase 4] AI for Elderly Care and Support/daily_reminder.csv")  # It will save to cleaned_reminders.csv by default
