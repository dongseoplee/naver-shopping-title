from selenium import webdriver
from bs4 import BeautifulSoup
titleList = []
visitedSet = set()
# queryString = input('검색어를 입력하세요: ')
queryString = '바나나'
driver = webdriver.Chrome('/Users/leedongseop/Documents/chromedriver')
driver.implicitly_wait(3)

#네이버 쇼핑 키워드 주소와 함께 접속
url = 'https://search.shopping.naver.com/search/all?query=' + queryString
driver.get(url)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
driver.implicitly_wait(3)
# driver.find_element()
html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')
titles = soup.select('.basicList_link__JLQJf')
ad_Y = soup.select('.ad_ad_stk__pBe5A')

titleSets = set()
for title in titles:
    titleList.append(title.text.strip())

for i in range(3, len(titleList)): #제목 갯수 45개
    # print(i + 1, ': ', end=' ')
    tempList = titleList[i].split() #제목 1개를 단어 별로 잘라서 리스트에 담는다.
    wordCnt = 0
    for j in range(len(tempList)): #단어 갯수
        if tempList[j] not in titleSets: #단어가 titleSets에 없다면
            print(tempList[j], end = ' ') #출력
            wordCnt += 1
        # if tempList[j] in titleSets:
        #     for k in range(len(tempList[j])):
        #         print('*', end = ' ')
    if wordCnt == 0:
        continue
    else:
        print()
    titleSets.update(titleList[i].split()) #titleSets 업데이트
