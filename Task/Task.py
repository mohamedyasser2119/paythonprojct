import pandas as pd

file_path = 'Taskfileexeecl/Employees.csv'
df = pd.read_csv(file_path)

df = df.drop_duplicates()

df['Age'] = df['Age'].apply(lambda x: int(x))


usd_to_egp_rate = 49
df['Salary(EGP)'] = df['Salary(USD)'] * usd_to_egp_rate


average_age = df['Age'].mean()
median_salary_egp = df['Salary(EGP)'].median()


gender_counts = df['Gender'].value_counts()
male_female_ratio = gender_counts.get('M', 0) / gender_counts.get('F', 1)  # Prevent division by zero


print("Average Age:", average_age)
print("Median Salary (EGP):", median_salary_egp)
print("Male to Female Ratio:", male_female_ratio)


output_file_path = 'Outputfileexexl/Cleaned_Employees.csv'
df.to_csv(output_file_path, index=False)


output_file_path
