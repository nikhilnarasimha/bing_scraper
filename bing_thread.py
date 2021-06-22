#Packages
from urllib.parse import urlunparse , urlencode
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import pandas as pd
from multiprocessing.pool import ThreadPool


df = pd.read_csv("indian_companies.csv")

df = df["name"][18000:20000]


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
        #print(url)
        pages = number_of_pages(url)
        urls = []
        for page in pagnation[0:pages]:
            link = url + "&count=50" + page
            urls.append(link)
        return urls
    

#Search('site:"linkedin.com/in" "data analyst" and "ideapoke"')
#urls = Search('site:"linkedin.com/in" "@gmail.com" accenture')
    
def Bing_scapper(company):
    output = []
    print(f'company name--->', company)
    #i += 1
    #print(Query(company))
    try:
        urls = Search(Query(company))
        #print(urls)
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
        return output
            #if i % 50  == 0 :
            #    pd.DataFrame(output).to_csv("proflies.csv")
    except :
        print("No results")
        return output
    

def thread_res(list_companies):
    try:
        answer_list = list()
        print(list_companies)
        if len(list_companies) == 20:
                data_pool = ThreadPool(processes=20)
                th_output_0 = data_pool.apply_async(Bing_scapper, [list_companies[0]])
                th_output_1 = data_pool.apply_async(Bing_scapper, [list_companies[1]])
                th_output_2 = data_pool.apply_async(Bing_scapper, [list_companies[2]])
                th_output_3 = data_pool.apply_async(Bing_scapper, [list_companies[3]])
                th_output_4 = data_pool.apply_async(Bing_scapper, [list_companies[4]])
                th_output_5 = data_pool.apply_async(Bing_scapper, [list_companies[5]])
                th_output_6 = data_pool.apply_async(Bing_scapper, [list_companies[6]])
                th_output_7 = data_pool.apply_async(Bing_scapper, [list_companies[7]])
                th_output_8 = data_pool.apply_async(Bing_scapper, [list_companies[8]])
                th_output_9 = data_pool.apply_async(Bing_scapper, [list_companies[9]])
                th_output_10 = data_pool.apply_async(Bing_scapper, [list_companies[10]])
                th_output_11 = data_pool.apply_async(Bing_scapper, [list_companies[11]])
                th_output_12 = data_pool.apply_async(Bing_scapper, [list_companies[12]])
                th_output_13 = data_pool.apply_async(Bing_scapper, [list_companies[13]])
                th_output_14 = data_pool.apply_async(Bing_scapper, [list_companies[14]])
                th_output_15 = data_pool.apply_async(Bing_scapper, [list_companies[15]])
                th_output_16 = data_pool.apply_async(Bing_scapper, [list_companies[16]])
                th_output_17 = data_pool.apply_async(Bing_scapper, [list_companies[17]])
                th_output_18 = data_pool.apply_async(Bing_scapper, [list_companies[18]])
                th_output_19 = data_pool.apply_async(Bing_scapper, [list_companies[19]])
                
                answer_list.append(th_output_0.get())
                answer_list.append(th_output_1.get())
                answer_list.append(th_output_2.get())
                answer_list.append(th_output_3.get())
                answer_list.append(th_output_4.get())
                answer_list.append(th_output_5.get())
                answer_list.append(th_output_6.get())
                answer_list.append(th_output_7.get())
                answer_list.append(th_output_8.get())
                answer_list.append(th_output_9.get())
                answer_list.append(th_output_10.get())
                answer_list.append(th_output_11.get())
                answer_list.append(th_output_12.get())
                answer_list.append(th_output_13.get())
                answer_list.append(th_output_14.get())
                answer_list.append(th_output_15.get())
                answer_list.append(th_output_16.get())
                answer_list.append(th_output_17.get())
                answer_list.append(th_output_18.get())
                answer_list.append(th_output_19.get())
        #print("ANSWER LIST:",answer_list)
    except Exception as e:
        print('Exception at func thread: ',e)
    return answer_list


s = 0
ouput_dt = list()
for i in range(0,9000,20):
    print(i)
    s += 20
    list_companies = df[i:i+20]
    list_companies = list_companies.tolist()
    res = thread_res(list_companies)
    for lis in res:
        for dic in lis:
            ouput_dt.append(dic)
    if s % 100 == 0:
        pd.DataFrame(ouput_dt).to_csv("proflies-11000-20000.csv")


Bing_scapper("by and large corporate services private ltd")



1816222759:AAEVIOc2b0rGCAcOpSov2cTiklsud1hGg34


