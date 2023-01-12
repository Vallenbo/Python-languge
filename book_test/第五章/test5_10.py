import csv


def writecsv2(csvfilepath):
    headers = ['学号', '姓名', '性别', '班级', '语文', '数学', '英语']
    rows = [{'学号': '100001', '姓名': '宝玉', '性别': '男', '班级': '1 班', '语文': '85', '数学': '60', '英语': '70'},
            {'学号': '100002', '姓名': '黛玉', '性别': '女', '班级': '2 班', '语文': '88', '数学': '65', '英语': '85'}
            ]
    with open(csvfilepath, 'a+', newline='') as f:
        f_csv = csv.DictWriter(f, headers)
        f_csv.writerows(rows)


if __name__ == '__main__':
    writecsv2('d:\\test\\temp\\E05 成绩.csv')
