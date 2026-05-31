import pandas as pd

# Load dataset
df = pd.read_csv(r"C:\Users\ASUS\OneDrive\Desktop\data_analyst_task\netflix_titles.csv")

print("Original Shape:", df.shape)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicate rows
duplicates = df.duplicated().sum()
print(f"\nDuplicate rows found: {duplicates}")

df = df.drop_duplicates()

# Fill missing values
df['director'] = df['director'].fillna('Unknown')
df['cast'] = df['cast'].fillna('Unknown')
df['country'] = df['country'].fillna('Unknown')
df['rating'] = df['rating'].fillna('Not Rated')
df['date_added'] = df['date_added'].fillna('Unknown')

# Standardize column names
df.columns = df.columns.str.lower().str.replace(' ', '_')

# Convert date column
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

# Remove leading/trailing spaces from text columns
text_columns = ['type', 'title', 'director', 'country', 'rating']

for col in text_columns:
    df[col] = df[col].astype(str).str.strip()

print("\nFinal Shape:", df.shape)

# Save cleaned dataset
df.to_csv("cleaned_netflix_titles.csv", index=False)

print("\nDataset cleaned successfully!")
print("Saved as: cleaned_netflix_titles.csv")
