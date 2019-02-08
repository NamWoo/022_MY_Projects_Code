import sys 
import re
from os import rename, listdir
import shutil

nowt = 1
nown = 2
nowp = "02_Hierarchical and Density Based Clustering\\"

# ![02](img/03-001.png)

path = "D:\\!NW_Learning\\02 MOOC\\004_DataScientist_Udacity\\04_Unsupervised Learning\\"
path = path + nowp
path_ini = path + 'img_ini'
path_img = path + 'img'


def ini():

    ini_files = listdir(path_ini)
    img_files = listdir(path_img)

    # 숫자에 0넣기
    if nowt < 10:
        titling = '0' + str(nowt)
    else:
        titling = str(nowt)

    if nown < 10:
        numbering = '00' + str(nown)
    else:
        numbering = '0' + str(nown)
        

    # 옮겨질 img 폴더의 마지막 파일명 확인 후 앞서 정의한 숫자와 비교.
    img_files_n = img_files[-1:]
    find_naming = '^.*(?=[-])'
    r = re.compile(find_naming)
    r = r.match(img_files_n[0])
    last_n = int(r.group())

    if last_n != nowt:
        pass
    else:
        print("img 마지막 파일명: "+ str(img_files_n[0]), "현재 정의한 목차번호: " + str(nowt))
        exit


    for i in range(1,15):
       # print("![" + n1 + "](img/" + n1 + "-" + n2 + ".png)")
        # print("![" + titling + "-" + numbering + "](img/" + titling + "-" + numbering + ".png)")
        if i < 10:
            print("![" + titling + "-00" + str(i) + "](img/" + titling + "-00" + str(i) + ".png)")
        elif i < 100:
            print("![" + titling + "-0" + str(i) + "](img/" + titling + "-0" + str(i) + ".png)")


# shutil.move(a,b)
# 출처: https://118k.tistory.com/303


if __name__ == "__main__":

    ini()


    