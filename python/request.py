import requests

# print(response.text)

class Request():
    
    def get(self, url: str, verbose=1):
        response = requests.get(url=url)
        if verbose == 1:
            print(f"Request URL - {url} ({response.status_code})")
        return response
    
if __name__ == "__main__":
    response = requests.get("https://www.naver.com") # URL 접속