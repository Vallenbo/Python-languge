import csv

with open('d:\\test\\05\\鸢尾花数据集.csv', 'r') as f:
    reader = csv.reader(f)
    result = list(reader)
    print(result[1])
