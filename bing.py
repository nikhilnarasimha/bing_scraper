#Packages
from urllib.parse import urlunparse , urlencode
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import pandas as pd
from multiprocessing.pool import ThreadPool


df = pd.read_csv("indian_companies.csv")

df = df["name"][0:10]


def Query(company):
    base_query = 'site:"linkedin.com/in" "@gmail.com"'
    query = base_query + " " + company
    return query


def number_of_pages(url):
    custom_user_agent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"
    req = Request(url, headers={"User-Agent": custom_user_agent})
    page = urlopen(req)
    soup = BeautifulSoup(page.read())
    total_results = soup.find('span', {"class" : "sb_count"}).text
    total_results = total_results.replace(",","")
    results = [int(i) for i in total_results.split() if i.isdigit()][0]
    pages = results//50
    pages = round(pages - (pages * 30) /100)
    #print(pages)
    if pages == 0:
        return 1
    elif pages > 25:
        return 25
    return pages

pagnation = ['&first=0&FORM=PERE', '&first=51&FORM=PERE', '&first=101&FORM=PERE', '&first=151&FORM=PERE', '&first=201&FORM=PERE', '&first=251&FORM=PERE', '&first=301&FORM=PERE', '&first=351&FORM=PERE', '&first=401&FORM=PERE', '&first=451&FORM=PERE', '&first=501&FORM=PERE', '&first=551&FORM=PERE', '&first=601&FORM=PERE', '&first=651&FORM=PERE', '&first=701&FORM=PERE', '&first=751&FORM=PERE', '&first=801&FORM=PERE', '&first=851&FORM=PERE', '&first=901&FORM=PERE', '&first=951&FORM=PERE', '&first=1001&FORM=PERE', '&first=1051&FORM=PERE', '&first=1101&FORM=PERE', '&first=1151&FORM=PERE', '&first=1201&FORM=PERE', '&first=1251&FORM=PERE', '&first=1301&FORM=PERE', '&first=1351&FORM=PERE', '&first=1401&FORM=PERE', '&first=1451&FORM=PERE', '&first=1501&FORM=PERE', '&first=1551&FORM=PERE', '&first=1601&FORM=PERE', '&first=1651&FORM=PERE', '&first=1701&FORM=PERE', '&first=1751&FORM=PERE', '&first=1801&FORM=PERE']

def Search(query):
        #query = 'site:"linkedin.com/in" "data analyst" and "ideapoke"'
        url = urlunparse(("https", "www.bing.com", "/search", "", urlencode({"q": query}), ""))
        print(url)
        pages = number_of_pages(url)
        urls = []
        for page in pagnation[0:pages]:
            link = url + "&count=50" + page
            urls.append(link)
        return urls
    

#Search('site:"linkedin.com/in" "data analyst" and "ideapoke"')
#urls = Search('site:"linkedin.com/in" "@gmail.com" accenture')
i = 0
output = []
for company in df:
    print(f'company name--->', company)
    #i += 1
    #print(Query(company))
    try:
        urls = Search(Query(company))
        print(urls)
        for url in urls:
            try:
                custom_user_agent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"
                req = Request(url, headers={"User-Agent": custom_user_agent})
                page = urlopen(req)
                soup = BeautifulSoup(page.read())
                Search_term = soup.find('title').text
                data = soup.find_all('li', {"class":"b_algo"})
                for point in data:
                    d = {}
                    d["company name"] = company
                    d["Search_url"] = url
                    d["Search_term"] = Search_term
                    url_p = point.find("a")
                    #print(f'url----> ', url.get('href'))
                    d["Linkedin_url"] = url_p.get('href')
                    #print(f'title-----> ', point.find("a").text)
                    d["title"] = point.find("a").text
                    #print(f'desc-----> ',point.find("div").text)
                    d["desc"] = point.find("div").text
                    output.append(d)
                    #print(d)
            except Exception as e:
                    print(e)
                    if i % 10  == 0 :
                        pd.DataFrame(output).to_csv("proflies1.csv")
    except Exception as e :
        print(e)
        print("No results")
        pass
    
pd.DataFrame(output).to_csv("proflies.csv")



