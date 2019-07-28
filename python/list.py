import sys
import os

path_raw = 'C:/Users/NW/Desktop/add robot book/파이썬 로보틱스/'
path1 = path_raw + '001/01/'    # 앞 홀, 1~85
path2 = path_raw + '001/02/'    # 뒤 짝, 86~2
path3 = path_raw + '002/01/'    # 앞 홀, 87~169
path4 = path_raw + '002/02/'    # 앞 짝, 88~170 
path5 = path_raw + '003/01/'    # 앞 홀, 171~269
path6 = path_raw + '003/02/'    # 뒤 짝, 270~172
path7 = path_raw + '004/01/'    # 앞 홀, 271~343
path8 = path_raw + '004/02/'    # 뒤 짝, 344~272

# list_path1 = [i for i in range(1,86,2)]              # 001 01
# list_path2 = [i for i in range(86,0,-2)]             # 001 02
# list_path3 = [i for i in range(87,169+1,2)]          # 002 01
# list_path4 = [i for i in range(88,170+1,2)]          # 002 02
# list_path5 = [i for i in range(171,269+1,2)]         # 003 01
# list_path6 = [i for i in range(270,172-1,-2)]        # 003 02
# list_path7 = [i for i in range(271, 343+1,+2)]       # 004 01
list_path8 = [i for i in range(344, 272-1,-2)]       # 004 02


### path1 ~ path8 까지 선택
path_now = path8
list_now = list_path8


if __name__ == "__main__":
    
    file_list = os.listdir(path_now)
    # print('파일리스트 : ', file_list)

    # list_t1 = [i for i in b if i%2 == 1]
    # print(list_t1)

    # print('바꿀리스트 : ', list_path8)

    for i, c in enumerate(list_now):
        try:
            if c < 10:
                list_now[i] = '00' + str(list_now[i]) +'.jpg'
            elif c < 100:
                list_now[i] = '0'+ str(list_now[i]) +'.jpg'
            else:
                list_now[i] = str(list_now[i]) +'.jpg'
            
            print('번호 : ', i,'  ','기존파일명 :', file_list[i], '  '+'바꾼파일명: ', list_now[i])
            os.rename(path_now + file_list[i], path_now + list_now[i])
        except :
            print('뷁!')
            break

    print('well done!')
