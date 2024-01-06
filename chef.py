import json
import csv

with open("C:\mock_hack\Student Handout\Input data\level0.json") as json_file:
	data = json.load(json_file)

# now we will open a file for writing
data1 = open("C:\mock_hack\Student Handout\Input data\level0.json", 'w')

csv_writer = csv.writer(data1)
count = 0

for emp in data1:
	if count == 0:
		# Writing headers of CSV file
		header = emp.keys()
		csv_writer.writerow(header)
		count += 1

	# Writing data of CSV file
	csv_writer.writerow(emp.values())

data1.close()
