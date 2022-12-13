# @Time: 2022/12/13 16:20
import requests
header = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    #'Accept-Encoding':' gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Cookie': 'PSTM=1670316448; BD_UPN=12314753; BIDUPSID=13BDDFDD4EE50498A13B9E24EA378855; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; MCITY=-340%3A; BAIDUID=51404E947BEC6048FC8A7A68F8516577:FG=1; ab_sr=1.0.1_MTNhZjJiMWExMzA5NWJiYWEwZmQxMTdkNzQ5MDNiZjliOWUyNDEzYWE0MTIzMWNjN2QzNmY5NzAxOTFjNzQ2Y2I1MDQxYzRhMjZjNjJmYzZkMjkxZjY2MzQzMWE4ZTE2YmUyZjYwZThlZDZkNjkxZDQzNzRkZTI0MWU1Y2JhZmI3ZDA4MzMxZjgxMGZjZGQ1YTM2MWYxOGU3YjIzODA4Mw==; BA_HECTOR=8l8525al010ha02g240524ul1hpgbsf1g; BAIDUID_BFESS=51404E947BEC6048FC8A7A68F8516577:FG=1; ZFY=9CdH4D7qNf:AQ5G3tNgV9KroU81IeBFTISk2nCq5efmU:C; Hm_lvt_aec699bb6442ba076c8981c6dc490771=1670327863,1670567188,1670844486,1670918150; COOKIE_SESSION=60806_1_8_9_16_42_0_4_5_8_4_5_60522_0_112_0_1670918140_1670850266_1670918028%7C9%23119424_189_1670850227%7C9; BD_HOME=1; H_PS_PSSID=37857_36555_36920_37906_37871_37795_37934_37759_37904_26350_37788_37881; rsv_jmp_slow=1670919956769; BD_CK_SAM=1; PSINO=6; delPer=0; H_PS_645EC=6ddc1mt0ynk443RtSZtREH%2B2HdnGLz2ABq7ajdidqU8IC4RNfcTSyQDjReE; channel=baidusearch; baikeVisitId=0b5ea9e8-f8a3-4018-96ad-3b7cf914813f; B64_BOT=1',
    'Host':'www.baidu.com',
    'Referer': 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E5%8C%97%E4%BA%AC&fenlei=256&rsv_pq=0xcd0cb59900019c5b&rsv_t=c4b0Hflk9b9ZKhORrRVY2Fxc7Sadya9kx%2BtdHy5%2FSMLDq2%2BacbHiem%2BErBPh&rqlang=en&rsv_dl=tb&rsv_enter=1&rsv_sug3=3&rsv_sug2=0&rsv_btype=i&inputT=1216&rsv_sug4=2633',
    'sec-ch-ua':'"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile':'?0',
    'sec-ch-ua-platform':'"Windows"',
    'Sec-Fetch-Dest':'document',
    'Sec-Fetch-Mode':'navigate',
    'Sec-Fetch-Site':'same-origin',
    'Sec-Fetch-User':'?1',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}

# data={
#     'wd':'北京'
# }
# response = requests.get(url=url,params=data,headers=header)
# response.encoding= 'utf8'
# content = response.text
# print(response.status_code)
# print(content)
url = 'https://sz.lianjia.com/zufang/longgangqu/pg2rt200600000001/#contentList'
response = requests.get(url)
response.encoding= 'utf8'
from lxml import etree
rent = etree.HTML(response.text).xpath('//em/text()')
print(rent)
