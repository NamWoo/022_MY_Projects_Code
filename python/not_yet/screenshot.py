
# 정의된 폴더에 마지막 파일명을 이용해 마크다운 이미지링크주소 출력
# ![03](img/03-001.png) ...
# '-' 중심으로 03은 앞자리 타이틀 번호, 001은 뒷자리 이미지 번호

import re
from os import listdir
import pyscreenshot as ImageGrab
# https://pypi.org/project/pyscreenshot/
# https://pyscreenshot.readthedocs.io/en/latest/

######### 정의하기 #########
# 마지막 이미지 번호 이어할 것인지 새로 만들 것인지
# option_num = 0  # 0 이나 다른 거면 새로하기
option_num = 1  # 1 이면 이어하기
# option_num = 3  # 3 이면 마지막 번호까지 for문 출력만
new_num_t = 8
new_num_n = 1

# 폴더이름 정의
# nowp = "03_Gaussian Mixture Models and Cluster Validation\\"
nowp = "04_Dimensionality Reduction and PCA\\"
# nowp = "05_Random Projection and ICA\\"
path = "D:\\!NW_Learning\\02 MOOC\\004_DataScientist_Udacity\\04_Unsupervised Learning\\"
############################

path = path + nowp
path_img = path + 'img\\'
img_files = listdir(path_img)

# 마지막 파일의 파일명에서 타이틀번호와 이미지 번호 가져오기
img_files_n = img_files[-1:]
find_numbering = '^([0-9]+)[-]([0-9]+)' # '^(\d+)[-](\d+)'
r = re.compile(find_numbering)
r = r.match(img_files_n[0])

titling = r.group(1)
endi = int(r.group(2))

# def last_t(path):
    

def num_zero(num, plus):
    if num < 10:
        num = '0' + str(num+plus)
    else:
        num = str(num+plus)
    return num


if option_num == 1:
    file_name = str(titling) + "-0" +  num_zero(endi,1) + ".png"
elif option_num == 3:
    for i in range(1, endi+1):
        print("![" + str(titling) + "-0" + num_zero(i,0) + "](img/" + titling + "-0" + num_zero(i,0) + ".png)")
else:
    file_name = num_zero(new_num_t,0) + "-0" +  num_zero(new_num_n,0) + ".png"


if __name__ == '__main__':

    im = ImageGrab.grab(bbox=(0, 176, 1492, 841+176))  # X1,Y1,X2,Y2
    im.save(path_img + file_name)

    # im.show()

    