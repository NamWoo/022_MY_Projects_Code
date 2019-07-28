
# 정의된 폴더에 마지막 파일명을 이용해 마크다운 이미지링크주소 출력
# ![03](img/03-001.png) ...
# '-' 중심으로 03은 앞자리 타이틀 번호, 001은 뒷자리 이미지 번호

import re
from os import listdir

######### 정의하기 #########
# 폴더이름 정의
# nowp = "03_Gaussian Mixture Models and Cluster Validation\\"
# nowp = "04_Dimensionality Reduction and PCA\\"
# nowp = "05_Random Projection and ICA\\"
path = "C:\\output\\"



############################

path = path + nowp
path_img = path + 'img'
img_files = listdir(path_img)


def ini_dir():

    # 마지막 파일의 파일명에서 타이틀번호와 이미지 번호 가져오기
    img_files_n = img_files[-1:]
    find_numbering = '^([0-9]+)[-]([0-9]+)' # '^(\d+)[-](\d+)'
    r = re.compile(find_numbering)
    r = r.match(img_files_n[0])

    titling = r.group(1)
    endi = int(r.group(2))

    for i in range(1, endi+1):
        if i < 10:
            print("![" + titling + "-00" + str(i) + "](img/" + titling + "-00" + str(i) + ".png)")
        elif i < 100:
            print("![" + titling + "-0" + str(i) + "](img/" + titling + "-0" + str(i) + ".png)")


if __name__ == "__main__":

    ini_dir()
    