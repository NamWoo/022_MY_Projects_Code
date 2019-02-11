import re
from os import listdir
import pyscreenshot as ImageGrab

######### 정의하기 #########
# 마지막 이미지 번호 이어할 것인지 새로 만들 것인지
continue_num = 0
# continue_num = 1    # 1 이면 이어하기, 0 이면 
new_num_t = 7
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


def num_zero(num, plus):
    if num < 10:
        num = '00' + str(num+plus)
    else:
        num = '0' + str(num+plus)
    return num


if continue_num == 1:
    file_name = str(titling) + "-" +  num_zero(endi,1) + ".png"
else:
    file_name = num_zero(new_num_t,0) + "-" +  num_zero(new_num_n,0) + ".png"


if __name__ == '__main__':

    im = ImageGrab.grab(bbox=(0, 176, 1492, 841+176))  # X1,Y1,X2,Y2
    im.save(path_img + file_name)

    # im.show()

    