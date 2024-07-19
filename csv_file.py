import csv

input_file = 'convertcsv.txt'
output_file = 'converted.csv'

with open(input_file, 'r') as file:
    content = file.readlines()
    lst = content[0].strip().split(',')

with open(output_file, 'w') as csv_files:
    csv_writer = csv.writer(csv_files)

    csv_writer.writerow(lst)
    for line in content[1:]:
        row = line.strip().split()
        csv_writer.writerow(row)

print(f"Data successfully converted to {output_file}")








