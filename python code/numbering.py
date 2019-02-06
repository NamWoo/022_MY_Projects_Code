import sys 
import re
from os import rename, listdir
import shutil

nowt = 5
nown = 2
nowp = "02_Hierarchical and Density Based Clustering\\"
# 출처: https://118k.tistory.com/303 [개발자로 살아남기]

# D:\!NW_Learning\02 MOOC\004_DataScientist_Udacity\04_Unsupervised Learning\02_Hierarchical and Density Based Clustering\img
# ![02](img/03-001.png)

path = "D:\\!NW_Learning\\02 MOOC\\004_DataScientist_Udacity\\04_Unsupervised Learning\\"
path = path + nowp
path_ini = path + 'img_ini'
path_img = path + 'img'

ini_files = listdir(path_ini)
img_files = listdir(path_img)


# 옮겨질 img 폴더의 마지막 파일명 확인 후 앞서 정의한 숫자와 비교.
img_files_n = img_files[-1:]
find_naming = '^.*(?=[-])'
r = re.compile(find_naming)
r = r.match(img_files_n[0])
last_n = int(r.group())

if last_n != nowt:
    pass
else:
    print("img 마지막 파일명: "+ img_files_n, "현재 정의한 목차번호: " + str(nowt))
    exit


# 파일 이름 바꾸며 옮기기
for i in nown:
    
       






for i in ini_files:
    print(i)

    name = str(nowt)+str(nown)


    i.rename(i,)
    print(i)









# print(img_files_n)

# shutil.move(a,b)



# n1 = '04'
# for i in range(1,15):
    
#     if i < 10:
#         n2 = '00' + str(i)
#     elif i < 100:
#         n2 = '0' + str(i)

    
#     # print("![" + n1 + "](img/" + n1 + "-" + n2 + ".png)")
#     print("![" + n1 + "-" + n2 + "](img/" + n1 + "-" + n2 + ".png)")





if __name__ == "__main__":
    pass