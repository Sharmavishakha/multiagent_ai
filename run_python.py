import pandas as pd

# Load your CSV (replace with the correct path)
df = pd.read_csv(r"C:/Users/hp/OneDrive/Desktop/ollama/Dataset/[Usecase 4] AI for Elderly Care and Support\daily_reminder.csv")

# Step 1: Convert Scheduled Time to datetime
df['Scheduled Time'] = pd.to_datetime(df['Scheduled Time'], errors='coerce')

# Step 2: Fill missing values
df['Acknowledged (Yes/No)'] = df['Acknowledged (Yes/No)'].fillna('No')
df['Reminder Sent (Yes/No)'] = df['Reminder Sent (Yes/No)'].fillna('No')

# (Optional) See how many were fixed
print("Null values after cleaning:\n", df.isnull().sum())

# Save cleaned file
df.to_csv("cleaned_daily_reminders.csv", index=False)
