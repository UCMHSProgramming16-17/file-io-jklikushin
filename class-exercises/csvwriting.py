import csv

csvfile = open('examplefile.csv', 'w')

cw = csv.writer(csvfile, delimiter = ',')

cw.writerow(["All","my","cells", "go", "in", "this", "list"])


csvfile.close()