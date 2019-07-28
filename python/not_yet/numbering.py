# ![](./book/자율주행기능구현을위한차량용SW개발2_페이지_001.jpg)

######### 정의하기 #########
# 앞자리 타이틀 번호 시작과 끝 정의
nowt = 5
endt = 22

# pdf 끝 페이지
endi = 300
############################

def ini(tt):




    # 1,2,3 int -> 01,02,03 str 으로 바꾸기
    if tt < 10:
        titling = '0' + str(tt)
    else:
        titling = str(tt)

    # 출력
    for i in range(1, endi):

        print("![" + str(i) + "](./book/자율주행기능구현을위한차량용SW개발2_페이지_" + str(i) + ".jpg)")



if __name__ == "__main__":

    for i in range(nowt, endt):
        ini(i)



    