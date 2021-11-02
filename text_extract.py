# ファイル内の日本語をCSVファイルにする
import os
import re
import codecs
import csv

kanjiPattern = re.compile("[一-龥]")
katakanaPattern=re.compile("[ァ-ン]")
hiraganaPattern=re.compile("[ぁ-ん]")

except_file_type = ['.vue','.csv','.xlsx','.json','.json','.h','.sql','.class','.sh','.txt','.jpg','.png','.xls,','.svn-base']
except_file_like = r'test|debug|target|cocos2d|tools|Libraries'
choice_tpye_list = ['.html','.js','.css','.java','.cpp','.mm','.xml']
quationFiles_list = ['.js','.css','.java','.cpp','.mm']
save_path = ''

import time

timestr = time.strftime("%Y%m%d-%H%M%S")

def matchJapanese(str):
    return kanjiPattern.search(str) or katakanaPattern.search(str) or hiraganaPattern.search(str)

def start():
    global choice_tpye_list,save_path
    try:
        # 対象ファイルを設定
        file_name = 'Sample.vue'
        # パスを設定
        paths = './'+file_name
    except Exception:
        paths = ''

    save_path = os.path.join(os.getcwd(),file_name +'_' + timestr +'.csv')

    path_list = paths.split(',')
    for path in path_list:
        checkDIR(path)

def sortcsvfiles(inputfilename, outputfilename):
    with open(inputfilename,'rt') as csvfile1:
        reader = csv.reader(csvfile1)
        headers = next(reader, None) 
        rows = sorted(
            (r for r in reader if len(r) > 1),
            key=lambda r: (int(r[0]), int(r[1])))

    with open(outputfilename,'wt') as csvfile1:
        writer = csv.writer(csvfile1, lineterminator='\n')
        if headers:
            writer.writerow(headers)
        writer.writerows(rows)

def checkDIR(path):
    if os.path.isfile(path):
        a,b = os.path.splitext(path)
        if choice_tpye_list:
            if b in choice_tpye_list:
                replaceFile(path)
        else:
            if b not in except_file_type:
                replaceFile(path)

    elif os.path.isdir(path):
        file_list = os.listdir(path)
        path_list = map(lambda x: os.path.join(path, x), file_list)
        for item in path_list:
            checkDIR(item)
    else:
        print ('---Wrong File---' + path)

def removeComments(string):
    if string.lstrip().lower().startswith(("new","CCAssert","qblogsv","log","cclog","public","cocos2d::log", "return", "void", "@", "*", "throw", ".", "console.log")):
        string = "";

    string = re.sub(re.compile("/\*.*?\*/",re.DOTALL ) ,"" ,string) #/*COMMENT */
    string = re.sub(re.compile("//.*?\n" ) ,"" ,string) # //COMMENT
    string = re.sub(re.compile("(<!--.*?-->)",re.DOTALL ) ,"" ,string)#<!--COMMENT-->)

    for value in ("テスト","<%","実装","クラス", "LOG", "★", "//", "<<"):
        if string.lower().find(value) > 0:
            string = "";
            break

    return string.lstrip()

def getStringFromQua(string):
    quoted = re.compile('"[^"]*"')
    for value in quoted.findall(string):
        if matchJapanese(value):
            return "".join(value)
        else:
            return ""

def getStringFromHtml(raw_html):
    #raw_html = re.sub('<[^>]+>', '', raw_html)
    try:
        raw_html = re.findall(r'>(.*)<', raw_html)[0]
    except IndexError:
        print("")

    return raw_html

def ifHasQuationGetString(strOrgin):
    # quotedDouble = re.compile('"[^"]*"')
    quotedDouble = re.compile('')
    quotedSingle = re.compile("(?<=')[^']+(?=')")

    matchDouble = re.search('"[^"]*"', strOrgin)
    matchSingle = re.search("(?<=')[^']+(?=')", strOrgin)
    string = ""
    if matchDouble:
        for value in quotedDouble.findall(strOrgin):
            if value:
                string = "".join(value)

    if matchSingle:
        for value in quotedSingle.findall(strOrgin):
            if value:
                string = "".join(value)
    return string

def checkIfKeysInString(keys,string):
    return any(s in string for s in keys)

def replaceFile(file):
    num = 1
    all_lis = []
    lis = []
    if any(re.findall(except_file_like, file, re.IGNORECASE)):
        return False
    with open(file, 'r') as f:
        line = f.readline()
        # print('######line', line)
        while line:
            try:
                line = line.decode('utf-8')
                line = removeComments(line)
            except Exception:
                line = removeComments(line)
            content_lis = line.split('#')
            if matchJapanese(content_lis[0]):
                # strOrgin = content_lis[0]
                string  = content_lis[0]

                string = getStringFromHtml(string)
                print('######string', string)

                if ifHasQuationGetString(string) != "":
                    string = ifHasQuationGetString(string)


                if matchJapanese(string):
                    lis = [file, num, len(string.replace('\n', '').replace('\r', '').strip()),string.replace('\n', '').replace('\r', '').strip()]
                    all_lis.append(lis)

            line = f.readline()
            num += 1

    with codecs.open(save_path, 'a', "utf-8") as f:
        if all_lis:
            for itme in all_lis:
                f.write('%s#%s#%s#%s\n' % (itme[0],itme[1],itme[2],itme[3]))


if __name__ == '__main__':
    start()

    print ('Output:%s'%save_path)