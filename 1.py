#import necessary modules
import csv
with open('D:\barcodes','rt')as f:
  data = csv.reader(f)
  for row in data:
        print(row)
