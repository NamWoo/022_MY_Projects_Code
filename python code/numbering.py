import sys 
import re
from os import rename, listdir

# 출처: https://118k.tistory.com/303 [개발자로 살아남기]

# D:\!NW_Learning\02 MOOC\004_DataScientist_Udacity\04_Unsupervised Learning\02_Hierarchical and Density Based Clustering\img
# ![02](img/03-001.png)

path = "D:\\!NW_Learning\\02 MOOC\\004_DataScientist_Udacity\\04_Unsupervised Learning\\02_Hierarchical and Density Based Clustering\\"
path_ini = path + 'img_ini'
path_img = path + 'img'

ini_files = listdir(path_ini)
img_files = listdir(path_img)

img_files_n = img_files[-1:]



find_naming = '^.*(?=[-])'
r = re.compile(find_naming)
r = r.match(img_files_n[0])




# m = re.search(r'(^[0-9]+)', img_files_n)
# m.group()
print(r)

print(r.group())



# print(img_files_n)





# n1 = '04'
# for i in range(1,15):
    
#     if i < 10:
#         n2 = '00' + str(i)
#     elif i < 100:
#         n2 = '0' + str(i)

    
#     # print("![" + n1 + "](img/" + n1 + "-" + n2 + ".png)")
#     print("![" + n1 + "-" + n2 + "](img/" + n1 + "-" + n2 + ".png)")





