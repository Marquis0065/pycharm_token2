from multiprocessing.dummy import Pool as ThreadPool
import requests
import time
def getsource(url):
    html = requests.get(url)
urls = []
for i in range(2,50):
    newpage = 'https://sz.lianjia.com/zufang/longgangqu/pg'+str(i)+'rt200600000001l1/#contentList'
    urls.append(newpage)
time1 = time.time()
for i in urls:
    print(i)
    getsource(i)
time2 = time.time()
print('单线程耗时：'+str(time2-time1))
pool = ThreadPool(16)
time3 = time.time()
results = pool.map(getsource,urls)
pool.close()
pool.join()
time4 = time.time()
print('并行耗时'+str(time4-time3))
print('相差'+str(time4-time3-time2+time1))

