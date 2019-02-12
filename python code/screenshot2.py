
# 정의된 폴더에 마지막 파일명을 이용해 마크다운 이미지링크주소 출력
# ![03](img/03-001.png) ...
# '-' 중심으로 03은 앞자리 타이틀 번호, 001은 뒷자리 이미지 번호

import re
from os import listdir
import pyscreenshot as ImageGrab
# https://pypi.org/project/pyscreenshot/
# https://pyscreenshot.readthedocs.io/en/latest/

# wxPython 도 있음 https://klonic.tistory.com/18


######### 정의하기 #########
# 마지막 이미지 번호 이어할 것인지 새로 만들 것인지
option_num = 0  # 0 이면 아래 정의한 새번호로 스샷저장
# option_num = 1  # 1 이면 폴더내 마지막 파일명 이어서 스샷저장
# option_num = 2  # 2 이면 마지막 번호까지 for문 출력
new_num_t = 18
new_num_n = 1

# 폴더이름 정의
# nowp = "03_Gaussian Mixture Models and Cluster Validation\\"
# nowp = "04_Dimensionality Reduction and PCA\\"
nowp = "05_Random Projection and ICA\\"
path = "D:\\!NW_Learning\\02 MOOC\\004_DataScientist_Udacity\\04_Unsupervised Learning\\"
############################

path = path + nowp
path_img = path + 'img\\'

# 마지막 파일의 파일명에서 타이틀번호와 이미지 번호 가져오기
def last_t(path):
    global titling, endi
    img_files = listdir(path)
    img_files_n = img_files[-1:]
    find_numbering = '^([0-9]+)[-]([0-9]+)' # '^(\d+)[-](\d+)'
    r = re.compile(find_numbering)
    r = r.match(img_files_n[0])
    titling = r.group(1)
    endi = int(r.group(2))

def num_zero(num, plus):
    if num < 10:
        num = '0' + str(num+plus)
    else:
        num = str(num+plus)
    return num

def screenshot_save(path):
    im = ImageGrab.grab(bbox=(0, 176, 1492, 841+176))  # X1,Y1,X2,Y2
    im.save(path)
    # im.show()


if __name__ == '__main__':

    last_t(path_img)

    if option_num == 0:
        file_name = num_zero(new_num_t,0) + "-0" +  num_zero(new_num_n,0) + ".png"
        screenshot_save(path_img + file_name)
    elif option_num ==1:
        file_name = str(titling) + "-0" +  num_zero(endi,1) + ".png"
        screenshot_save(path_img + file_name)
    elif option_num == 2:
        for i in range(1, endi+1):
            print("![" + str(titling) + "-0" + num_zero(i,0) + "](img/" + titling + "-0" + num_zero(i,0) + ".png)")
    else:
        pass
        