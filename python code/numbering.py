
# 정의한 번호의 시작과 끝을 이용해 마크다운 이미지링크주소 출력
# ![03](img/03-001.png) ...
# '-' 중심으로 03은 앞자리 타이틀 번호, 001은 뒷자리 이미지 번호

######### 정의하기 #########
# 앞자리 타이틀 번호 시작과 끝 정의
nowt = 5
endt = 22

# 뒷자리 이미지 번호 끝 정의
endi = 15
############################

def ini(tt):

    # 1,2,3 int -> 01,02,03 str 으로 바꾸기
    if tt < 10:
        titling = '0' + str(tt)
    else:
        titling = str(tt)

    # 출력
    for i in range(1, endi):
        if i < 10:
            print("![" + titling + "-00" + str(i) + "](img/" + titling + "-00" + str(i) + ".png)")
        elif i < 100:
            print("![" + titling + "-0" + str(i) + "](img/" + titling + "-0" + str(i) + ".png)")


if __name__ == "__main__":

    for i in range(nowt, endt):
        ini(i)



    