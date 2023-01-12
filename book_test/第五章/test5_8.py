import csv

with open('d:\\test\\05\\鸢尾花数据集.csv', 'r') as f:
    reader = csv.reader(f)
    print(type(reader))
    for row in reader:
        print(row)
