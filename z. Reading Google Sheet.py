import pandas as pd 
import matplotlib.pyplot as plt
gsheetId="1Tfsie3jgw-FrZC03vUB4a2jot8oJfHpR3ftF9jnYT2M"
sheet_name="Sheet1"

gsheet_Url="https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}".format(gsheetId,sheet_name)
df=pd.read_csv(gsheet_Url)
print(df)
rows,column=df.shape
print(rows)


def plot_student_comparison(student_name, df):
    # Filter the DataFrame to get the information of the specified student
    student_data = df[df['Student Name'] == student_name]

    if student_data.empty:
        print(f"Student {student_name} not found in the database.")
        return

    # Extract X and XII marks for the specified student
    x_marks = student_data['X Marks'].values[0]
    xii_marks = student_data['XII Marks'].values[0]

    # Plot the comparison
    plt.figure(figsize=(8, 6))

    # Plot the X and XII marks of the specified student
    plt.scatter(x_marks, xii_marks, color='red', label=student_name)

    # Plot the rest of the students
    plt.scatter(df[df['Student Name'] != student_name]['X Marks'],
                df[df['Student Name'] != student_name]['XII Marks'],
                label='Other Students')

    plt.title(f"Comparison of {student_name}'s X and XII Marks")
    plt.xlabel("X Marks")
    plt.ylabel("XII Marks")
    plt.legend()
    plt.grid(True)
    plt.show()

# Example usage:
student_name_input = input("Enter the name of the student for comparison: ").strip().upper()
plot_student_comparison(student_name_input, df)