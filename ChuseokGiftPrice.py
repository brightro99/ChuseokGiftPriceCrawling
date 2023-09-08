import requests
from bs4 import BeautifulSoup

# 웹페이지의 URL
# https://www.rankingdak.com/product/view?productCd= + product number
urls = [
'https://www.rankingdak.com/product/view?productCd=F000007761',
'https://www.rankingdak.com/product/view?productCd=F000007773',
'https://www.rankingdak.com/product/view?productCd=F000007751',
'https://www.rankingdak.com/product/view?productCd=F000007780',
'https://www.rankingdak.com/product/view?productCd=F000007766',
'https://www.rankingdak.com/product/view?productCd=F000007752',
'https://www.rankingdak.com/product/view?productCd=F000007763',
'https://www.rankingdak.com/product/view?productCd=F000007776',
'https://www.rankingdak.com/product/view?productCd=F000001340',
'https://www.rankingdak.com/product/view?productCd=F000001338',
'https://www.rankingdak.com/product/view?productCd=F000001337',
'https://www.rankingdak.com/product/view?productCd=F000007805',
'https://www.rankingdak.com/product/view?productCd=F000007788',
'https://www.rankingdak.com/product/view?productCd=F000007778',
'https://www.rankingdak.com/product/view?productCd=F000007777',
'https://www.rankingdak.com/product/view?productCd=F000007768',
'https://www.rankingdak.com/product/view?productCd=F000007758',
'https://www.rankingdak.com/product/view?productCd=F000007757',
'https://www.rankingdak.com/product/view?productCd=F000007756',
'https://www.rankingdak.com/product/view?productCd=F000007753',
'https://www.rankingdak.com/product/view?productCd=F000004705',
'https://www.rankingdak.com/product/view?productCd=F000005640',
'https://www.rankingdak.com/product/view?productCd=F000005639',
'https://www.rankingdak.com/product/view?productCd=F000005638',
'https://www.rankingdak.com/product/view?productCd=F000003933',
'https://www.rankingdak.com/product/view?productCd=F000003932',
'https://www.rankingdak.com/product/view?productCd=F000003931',
'https://www.rankingdak.com/product/view?productCd=F000003930',
'https://www.rankingdak.com/product/view?productCd=F000003929',
'https://www.rankingdak.com/product/view?productCd=15827',
'https://www.rankingdak.com/product/view?productCd=15825',
'https://www.rankingdak.com/product/view?productCd=15824',
'https://www.rankingdak.com/product/view?productCd=F000003888',
'https://www.rankingdak.com/product/view?productCd=15779',
'https://www.rankingdak.com/product/view?productCd=15774',
'https://www.rankingdak.com/product/view?productCd=F000003869',
'https://www.rankingdak.com/product/view?productCd=F000003855',
'https://www.rankingdak.com/product/view?productCd=F000003810',
'https://www.rankingdak.com/product/view?productCd=F000003958',
'https://www.rankingdak.com/product/view?productCd=F000003957',
'https://www.rankingdak.com/product/view?productCd=F000003805',
'https://www.rankingdak.com/product/view?productCd=F000003803',
'https://www.rankingdak.com/product/view?productCd=22915',
'https://www.rankingdak.com/product/view?productCd=F000003074',
'https://www.rankingdak.com/product/view?productCd=F000001334',
'https://www.rankingdak.com/product/view?productCd=F000001333',
'https://www.rankingdak.com/product/view?productCd=22811',
'https://www.rankingdak.com/product/view?productCd=22809',
'https://www.rankingdak.com/product/view?productCd=22807',
'https://www.rankingdak.com/product/view?productCd=22806',
'https://www.rankingdak.com/product/view?productCd=22805',
'https://www.rankingdak.com/product/view?productCd=15783',
'https://www.rankingdak.com/product/view?productCd=11839',
'https://www.rankingdak.com/product/view?productCd=4087',
'https://www.rankingdak.com/product/view?productCd=F000007765',
'https://www.rankingdak.com/product/view?productCd=F000007813',
'https://www.rankingdak.com/product/view?productCd=F000007796',
'https://www.rankingdak.com/product/view?productCd=F000002059'
]

for url in urls:
    # 각 URL에서 웹페이지 내용을 가져옵니다.
    response = requests.get(url)
    html_content = response.text

    # BeautifulSoup으로 HTML 파싱
    soup = BeautifulSoup(html_content, 'html.parser')

    # <div class="goods-price"> 안에 있는 <p class="price"> 요소 선택
    price_element = soup.find('div', class_='goods-price').find('p', class_='price')

    # 가격 정보 추출
    if price_element:
        price = price_element.strong.text.strip()  # 텍스트에서 공백 제거
        print(price)
        # print("URL:", url)
        # print("상품 가격:", price)
        # print()
    else:
        print("URL:", url)
        print("가격 정보를 찾을 수 없습니다.")
        # print()
