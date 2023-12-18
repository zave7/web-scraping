from enum import Enum
from request import Request
from bs4 import BeautifulSoup

class BeautifulSoupUtil():
    
    class Type(Enum):
        HTML = "html.parser"
        HTML5 = "html5lib"
        XML = "lxml"
        
    def _get_object(data, type: "BeautifulSoupUtil.Type", verbose=1) -> BeautifulSoup:
        if verbose == 1:
            print(f"parse -> {type.value}")
        return BeautifulSoup(markup=data, features=type.value)
    
    def parse_html(data, verbose=1) -> BeautifulSoup:
        return BeautifulSoupUtil._get_object(data=data, type=BeautifulSoupUtil.Type.HTML, verbose=verbose)
        

if __name__ == "__main__":
    html_doc = '''
    <html>
    <head>
        <title>웹 페이지 제목</title>
    </head>
    <body>
        <div id="content">
            <h1>웹 페이지 내용</h1>
            <p>스크래핑을 위한 예시 문장입니다.</p>
            <p class="p2" data="kk">스크래핑을 위한 예시 문장입니다.(2)</p>
        </div>
    </body>
    </html>
    '''
    
    request = Request()
    response = request.get(url="https://www.naver.com")
    
    soup = BeautifulSoup(markup=html_doc, features="html.parser")
    
    title = soup.find(name="title") # 가장 먼저 해당하는 element 선택
    p = soup.find(name="p")
    p_all = soup.findAll(name="p")
    print(f"Find - title : {title}")
    print(f"Find - p : {p}")
    for _p in p_all:
        print(f"Find - p : {_p}")
    p_kk = soup.find(attrs={ "data": "kk" })
    print(f"Find - p_kk : {p_kk}")
    
    p_class = soup.select(selector="div > p.p2")
    print(f"Select - p_class : {p_class}")