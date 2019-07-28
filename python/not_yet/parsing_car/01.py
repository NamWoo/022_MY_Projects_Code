from selenium import webdriver
import os

# 준비과정
def prepareWebDriver():
    path = "E:\\chromedriver_win32\\chromedriver"
    options = webdriver.ChromeOptions()
    options.add_argument('headless') # 브라우져 뒤로 띄우고 싶을 때
    br = webdriver.Chrome(executable_path=path, service_log_path=os.path.devnull, chrome_options=options)
    return br

br = prepareWebDriver()

## 브라우져 가져오기
br.get("https://www.kcar.com/car/search/car_search_list.do")

## "https://www.kcar.com/car/info/car_info_detail.do?i_sCarCd=EC60226077"
## 주소 자체에 클레스 car_info로 잘 정리되어있어서 parsing 하기 쉽다.

## 파인드하기
info = br.find_element_by_class_name("car_info").text

print(info)


# ## 연식과 가격정보를 가져올 수 있다.
# result = []
# for i in info:
#     year = i.find_element_by_class_name("md_year").text
#     price = i.find_element_by_class_name("price").text
#     result.append({'year':year, 'price':price})


# print(result)
