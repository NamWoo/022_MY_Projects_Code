*last updated 20190728*


|목표|출력 결과|링크|
|:---:|:---|:---:|
|파일명 바꾸기|`번호 :  29    기존파일명 : 0030.jpg   바꾼파일명:  286.jpg`|[L I N K](#20190728-1)|
|마크다운문법으로 출력|`![299](./book/img/~~~~~~~_299_002.jpg)`|[L I N K](#20190728-2)|


# Python


미정리 잔뜩



## 20190728-1


### 목표

400쪽 되는 책 스켄이미지 파일이 30~50개씩 묶어서 어떤건 홀수 페이지만, 짝수 페이지만, 또 앞에서 부터, 뒤에서 부터 마구마구 섞여있었다. 그래서 400쪽 400번의 작업을 일일이 하느니 파이썬으로 쪽번호랑 파일명으로 폴더마다만 맞추고 몽땅 pdf 로 결합시키고 이미지 파일 내에 글씨 영어, 한글 인식 시키고 최적화 작업으로 용량축소까지.. 원래 매주 하던대로 작업을 했다.

아래 코드는 그 중  파일 관리 하는 파이썬 코드로 정규표현식은 이번엔 필요없어서 제거했다

[L I N K](./python/list.py)


### 과정

이렇게 한땀 한땀... 폴더마다 위치

***결국 for 하고 if 를 어떻게 쓰느냐가 관건***

```python
path_raw = 'C:/Users/NW/Desktop/asdadadadasdasd/'
path1 = path_raw + '001/01/'    # 앞 홀, 1~85
path2 = path_raw + '001/02/'    # 뒤 짝, 86~2
path3 = path_raw + '002/01/'    # 앞 홀, 87~169
path4 = path_raw + '002/02/'    # 앞 짝, 88~170 
path5 = path_raw + '003/01/'    # 앞 홀, 171~269
path6 = path_raw + '003/02/'    # 뒤 짝, 270~172
path7 = path_raw + '004/01/'    # 앞 홀, 271~343
path8 = path_raw + '004/02/'    # 뒤 짝, 344~272

list_path1 = [i for i in range(1,86,2)]              # 001 01
list_path2 = [i for i in range(86,0,-2)]             # 001 02
list_path3 = [i for i in range(87,169+1,2)]          # 002 01
list_path4 = [i for i in range(88,170+1,2)]          # 002 02
list_path5 = [i for i in range(171,269+1,2)]         # 003 01
list_path6 = [i for i in range(270,172-1,-2)]        # 003 02
list_path7 = [i for i in range(271, 343+1,+2)]       # 004 01
list_path8 = [i for i in range(344, 272-1,-2)]       # 004 02
```

### 결과

```

...
...
...
번호 :  29    기존파일명 : 0030.jpg   바꾼파일명:  286.jpg
번호 :  30    기존파일명 : 0031.jpg   바꾼파일명:  284.jpg
번호 :  31    기존파일명 : 0032.jpg   바꾼파일명:  282.jpg
번호 :  32    기존파일명 : 0033.jpg   바꾼파일명:  280.jpg
번호 :  33    기존파일명 : 0034.jpg   바꾼파일명:  278.jpg
번호 :  34    기존파일명 : 0035.jpg   바꾼파일명:  276.jpg
번호 :  35    기존파일명 : 0036.jpg   바꾼파일명:  274.jpg
번호 :  36    기존파일명 : 0037.jpg   바꾼파일명:  272.jpg
well done!
```


### 반성

결국 이것도 폴더 열어서 첫파일 끝파일 어떤 이미지 쪽번호 확인해야했다. 당연하게도 이미지가 무슨 쪽번호를 가지고 있는지는 머신러닝으로 쪽번호 위치 추정해서 숫자인식을 적용하기 전에는 인간레이블 해야겠지만... 어쨌든 조금 더 쉽게 할 수 있는 방법을 생각해봐야겠다.

응용을 하면 폴더 내에 파일명들이 꼬여있고 양도 많고 폴더 마다 또 제 각각 다른 상황이 많아서 자동화 작업을 해야할 때 가져다 쓰면 될 것~

* 폴더 내에 이미지 파일들 파일명 출력하기
* 각각의 파일명 일부를 수정하면서 마크다운 문법 달아서 뽑아내기
* 파일명 원하는 대로 바꾸기
* 파일명 이리저리 옮기기




키워드 : 파이썬, python, 오피스자동화, Industrial Engineer Office Automation





## 20190728-2


### 목표

이미지 파일 2개로 쪼개서 생긴 파일명 마크다운 문법으로 다시 만들기

[L I N K](./python/numbering_pdf.py)


### 결과

```
![295](./book/img/NVIDIA_TX보드를_활용한_딥러닝의_이해_cc_페이지_295_001.jpg)
![295](./book/img/NVIDIA_TX보드를_활용한_딥러닝의_이해_cc_페이지_295_002.jpg)
![296](./book/img/NVIDIA_TX보드를_활용한_딥러닝의_이해_cc_페이지_296_001.jpg)
![296](./book/img/NVIDIA_TX보드를_활용한_딥러닝의_이해_cc_페이지_296_002.jpg)
![297](./book/img/NVIDIA_TX보드를_활용한_딥러닝의_이해_cc_페이지_297_001.jpg)
![297](./book/img/NVIDIA_TX보드를_활용한_딥러닝의_이해_cc_페이지_297_002.jpg)
![298](./book/img/NVIDIA_TX보드를_활용한_딥러닝의_이해_cc_페이지_298_001.jpg)
![298](./book/img/NVIDIA_TX보드를_활용한_딥러닝의_이해_cc_페이지_298_002.jpg)
![299](./book/img/NVIDIA_TX보드를_활용한_딥러닝의_이해_cc_페이지_299_001.jpg)
![299](./book/img/NVIDIA_TX보드를_활용한_딥러닝의_이해_cc_페이지_299_002.jpg)
```



