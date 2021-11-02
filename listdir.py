import os
# 指定フォルダ内のファイルリスト生成

def fileList(folder):
    dirPath = r"./"+folder
    result = next(os.walk(dirPath))[2]
    return result

file_list = list()
files = os.listdir("./")
for f in files:
    path = os.path.join("./"+f)
    if os.path.isfile(path):
        file_list.append('./'+f)
for f in files:
    path = os.path.join("./"+f)
    if os.path.isdir(path):
        files2 = os.listdir('./'+f)
        for f2 in files2:
            file_list.append('./'+f+'/'+f2)



def fileListPrint(list):
    for f in list:
        print(f)

fileListPrint(file_list)
