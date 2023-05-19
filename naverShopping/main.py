import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

queryString = '바나나'
url = 'https://search.shopping.naver.com/search/all?query=' + queryString

print(url)
req = requests.get(url)
html = req.text

# print(html)

soup = BeautifulSoup(html, 'html.parser')

titles = soup.select(
    # 'content > div.style_content__xWg5l > div.list_basis > div > div > div > div > div.basicList_info_area__TWvzp > div.basicList_title__VfX3c > a'
    # '#content > div.style_content__xWg5l > div.list_basis > div > div:nth-child(1) > div > div > div.basicList_info_area__TWvzp > div.basicList_title__VfX3c > a'
    '.basicList_link__JLQJf' # 25 of 25에서 엔터 누르면 26 of 35로 바뀜 페이지네이션? 왜 전체 갯수가 한번에 안나오는지?
    #--> ******동적으로 생성되는 부분이었기 때문******* 셀레니움으로 해야함
    # Selenium은 실제 웹 브라우저가 동작하기 때문에 JS로 렌더링이 완료된 후의 DOM결과물에 접근이 가능하다.
    #https://beomi.github.io/gb-crawling/posts/2017-02-27-HowToMakeWebCrawler-With-Selenium.html
    # '.basicList_title__VfX3c'
)
print(len(titles))
print(titles[4].text)
# print(len(titles))
# for i in range(len(titles)):
#     print(titles[i])
#     print(titles[i].text)


# browser = webdriver.Chrome('/Users/leedongseop/Documents/chromedriver')
#
# queryString = input('검색어를 입력하세요: ')
# print(queryString)
#
# browser.get("https://shopping.naver.com/home")
# browser.find_element(By.CLASS_NAME, "_searchInput_search_text_3CUDs").send_keys(queryString)
# browser.find_element(By.CLASS_NAME, "_searchInput_button_search_1n1aw").click()
#
# titles = browser.find_element(By.CLASS_NAME, "basicList_link__JLQJf")
# print(titles.text)
#
# print('1')
# print('2')
# print(elements.text)

# fruits = driver.find_element(By.ID, "fruits")
# fruit = fruits.find_element(By.CLASS_NAME,"tomatoes")
#