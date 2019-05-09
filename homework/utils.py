import os
import csv

def get_root_path():
    #获取项目绝对路径
    root_path = os.path.dirname(os.path.abspath(__file__))
    #print(root_path)
    return root_path
# get_root_path()

def get_csv_data(file_path):
    file_path = os.path.join(get_root_path(),file_path)
    #print(file_path)
    with open(file_path,'r',encoding = 'utf8' ) as f:
        all_data = csv.reader(f)
        #迭代第一行
        next(all_data)
        data = []
        for d in all_data:
            #元祖化插入到list中成为pytest参数化有效数据
            data.append(tuple(d))
        #print(data)
        return data

def get_csv_loginname(file_path):
    file_path = os.path.join(get_root_path(),file_path)
    with open(file_path,'r',encoding = 'utf8' ) as f:
        all_data = csv.reader(f)
        next(all_data)
        print(all_data)
        data = []
        for d in all_data:
            data.append(d)
        print(data)
        return data

#get_csv_data('cases\create.csv')
# get_csv_loginname('cases/firstcomment.csv')