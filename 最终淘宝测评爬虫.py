import requests
import re
import csv
import time


def get_one_page(url):
   try:
       headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'}
       response = requests.get(url,headers=headers,timeout=10)
       if response.status_code == 200:
           return response.text
       return None
   except EOFError as e:
       print(e)
       return None


def parse_one_page(html,info):
   info = []
   pattern = re.compile(r'{"auctionPicUrl.*?"rateDate":"(.*?)","rateContent":"(.*?)","fromMall".*?"auctionSku":"(.*?)","anony".*?displayUserNick":"(.*?)","structuredRateList.*?displayUserRateLink":""},',re.S)
   items = re.findall(pattern,html)
   for item in items:
       comments = {}
       comments['Date'] = item[0].strip()
       comments['Comment'] = item[1].strip()
       comments['catagory'] = item[2].strip()
       comments['User'] = item[3].strip().split()
       info.append(comments)
   return info


def write_to_file(info):
    with open('淘宝评论.csv','a',newline='') as f:
       fieldnames = ['Date','Comment','catagory','User']
       writer = csv.DictWriter(f,fieldnames=fieldnames)
       writer.writeheader()
       try:
           writer.writerows(info)
       except:
           pass


def main(start):
    info = {}
    url = 'https://rate.tmall.com/list_detail_rate.htm?itemId=569519492636&spuId=971368677&sellerId=1726473375&order=3&currentPage=' + \
        str(start)
    html = get_one_page(url)
    data = parse_one_page(html,info)
    write_to_file(data)


if __name__ == '__main__':
   for i in range(100):
       main(i)
       j=i+1
       print('第%s页采集完毕。'%j)
       time.sleep(1)
