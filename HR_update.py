import csv
import os

if os.name == 'nt':  # Windows
    hr_path = r'C:\Users\Wei Shen\OneDrive\Documents\MyPythonStuff\HR.csv'
else:  # Linux sandbox - resolve relative to script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    hr_path = os.path.join(script_dir, '..', 'MyPythonStuff', 'HR.csv')

data_writer = open(hr_path, mode='a', newline='')
csv_writer = csv.writer(data_writer, delimiter=',')
csv_writer.writerow(['0.37', '0.52', '2', '158', '3', '0', '1', '0', 'Wei Shen', 'low'])
data_writer.close()
