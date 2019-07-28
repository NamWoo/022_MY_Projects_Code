# ![](./book/자율주행기능구현을위한차량용SW개발2_페이지_001.jpg)


# pdf 끝 페이지

# def sub_onetwo():


#폴더명
fod = "book/img"

#파일명
fil = "NVIDIA_TX보드를_활용한_딥러닝의_이해_cc_페이지_"

def ini(tt):

    for i in range(1, tt):

        if i < 10:
            print("![" + "00" + str(i) + "](./" + fod + "/" + fil + "00" + str(i) + "_001.jpg)")
            print("![" + "00" + str(i) + "](./" + fod + "/" + fil + "00" + str(i) + "_002.jpg)")
        elif i < 100:
            print("![" + "0" + str(i) + "](./" + fod + "/" + fil + "0" + str(i) + "_001.jpg)")
            print("![" + "0" + str(i) + "](./" + fod + "/" + fil + "0" + str(i) + "_002.jpg)")
        elif i < 1000:
            print("![" + str(i) + "](./" + fod + "/" + fil + str(i) + "_001.jpg)")
            print("![" + str(i) + "](./" + fod + "/" + fil + str(i) + "_002.jpg)")

if __name__ == "__main__":
    ini(300)

