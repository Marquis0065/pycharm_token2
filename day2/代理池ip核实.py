# @Time: 2022/12/11 15:57
import random
import urllib.request

import requests

praxies_list = [
    {'http': '183.236.232.160:8080'},
    {'http': '27.42.168.46:55481'},
    {'http': '222.74.73.202:42055'},
    {'http': '210.5.10.87:53281'},
    {'http': '27.42.168.46:55481'},
    {'http': '121.13.252.60:41564'},
    {'http': '120.24.76.81:8123'},
    {'http': '120.24.76.81:8123'},
    {'http': '120.24.76.81:8123'}
]
header = {
    'Accept':' text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    #'Accept-Encoding':' gzip, deflate, br',
    'Accept-Language':' zh-CN,zh;q=0.9',
    'Cache-Control':' max-age=0',
    'Connection':' keep-alive',
    'Cookie': 'PSTM=1670316448; BAIDUID=5C1C13ED838B4E9163EB13447527F898:FG=1; BD_UPN=12314753; BIDUPSID=13BDDFDD4EE50498A13B9E24EA378855; MCITY=-340%3A; BDSFRCVID=xJDOJeC629VsKMnjrJFgUGmKSRN1TM6TH6aoGj5RLCG2dC44-Pl4EG0P8f8g0KubJ2MRogKK3gOTH4PF_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF=JnuqVIKyfID3H48k-4QEbbQH-UnLq5Jx0mOZ04n-ah02bDoJM46KyljX3tJLBhtJ3GTvaC3m3UTdsq76Wh35K5tTQP6rLtJ2t254KKJxbnQ_fM3zDMc-25DIhUJiB5JMBan7_UJIXKohJh7FM4tW3J0ZyxomtfQxtNRJ0DnjtpChbC-xDTKBD5jQepb2KPAHHj733RrJ2n5_ebjYh-u_-P4Dep3HBxRZ5mAqoDQPHRTlqRc4yl5a3f-Dynbt2fbG-2OnaIQqa56SfbnbLJ7455t-DxonKpQ43bRT2UKy5KJvEqC42MQHhP-UyNbMWh37JNRlMKoaMp78jR093JO4y4Ldj4oxJpOJ5JbMonLafD-KMCPGe5AaePDyqx5Ka43tHD7yWCvh5DJcOR59K4nnD5cXLU6BbfTNKaTxWlvRJp5lohI63MOZXMLg5n7Tbb8eBgvZ2UQJKKOzsq0x0bOthR0ihH3u-JkHBCOMahkb5h7xOKbMQlPK5JkgMx6MqpQJQeQ-5KQN3KJmfbL9bT3YjjT3Da-Hq68Htn3e3bbstjr5jbjk-P7qh40_Mfv0etJyaR3ybhTvWJ5TMC_CLCcE3JDqK46lhpQxam3gLRrT0tOcShPC-tPVhb0J0PQOLJ0eMRr--nbG3l02VhRae-t2yU_IDl7C54RMW20e0h7mWIbmsxA45J7cM4IseboJLfT-0bc4KKJxbnLWeIJIjjCKD5QLea0JJjnfb5kXB-5q2RbHjJRYq4bohjPby4O9BtQmJJu8-tOcBRr8qlcDbponhfP904IDLUuqQg-q3R7T2D5C8hOjD4OTj53D0MkJ0x-jLnbhVn0MW-5DOCoE04nJyUnybPnnBT3T3H8HL4nv2JcJbM5m3x6qLTKkQN3T-PKO5bRh_CcJ-J8XMIK6eM5; H_PS_PSSID=37855_36552_37909_37866_37927_37886_37759_37900_26350_22157_37881; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID_BFESS=5C1C13ED838B4E9163EB13447527F898:FG=1; BDSFRCVID_BFESS=xJDOJeC629VsKMnjrJFgUGmKSRN1TM6TH6aoGj5RLCG2dC44-Pl4EG0P8f8g0KubJ2MRogKK3gOTH4PF_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF_BFESS=JnuqVIKyfID3H48k-4QEbbQH-UnLq5Jx0mOZ04n-ah02bDoJM46KyljX3tJLBhtJ3GTvaC3m3UTdsq76Wh35K5tTQP6rLtJ2t254KKJxbnQ_fM3zDMc-25DIhUJiB5JMBan7_UJIXKohJh7FM4tW3J0ZyxomtfQxtNRJ0DnjtpChbC-xDTKBD5jQepb2KPAHHj733RrJ2n5_ebjYh-u_-P4Dep3HBxRZ5mAqoDQPHRTlqRc4yl5a3f-Dynbt2fbG-2OnaIQqa56SfbnbLJ7455t-DxonKpQ43bRT2UKy5KJvEqC42MQHhP-UyNbMWh37JNRlMKoaMp78jR093JO4y4Ldj4oxJpOJ5JbMonLafD-KMCPGe5AaePDyqx5Ka43tHD7yWCvh5DJcOR59K4nnD5cXLU6BbfTNKaTxWlvRJp5lohI63MOZXMLg5n7Tbb8eBgvZ2UQJKKOzsq0x0bOthR0ihH3u-JkHBCOMahkb5h7xOKbMQlPK5JkgMx6MqpQJQeQ-5KQN3KJmfbL9bT3YjjT3Da-Hq68Htn3e3bbstjr5jbjk-P7qh40_Mfv0etJyaR3ybhTvWJ5TMC_CLCcE3JDqK46lhpQxam3gLRrT0tOcShPC-tPVhb0J0PQOLJ0eMRr--nbG3l02VhRae-t2yU_IDl7C54RMW20e0h7mWIbmsxA45J7cM4IseboJLfT-0bc4KKJxbnLWeIJIjjCKD5QLea0JJjnfb5kXB-5q2RbHjJRYq4bohjPby4O9BtQmJJu8-tOcBRr8qlcDbponhfP904IDLUuqQg-q3R7T2D5C8hOjD4OTj53D0MkJ0x-jLnbhVn0MW-5DOCoE04nJyUnybPnnBT3T3H8HL4nv2JcJbM5m3x6qLTKkQN3T-PKO5bRh_CcJ-J8XMIK6eM5; BD_CK_SAM=1; delPer=0; BA_HECTOR=al218h210g84018ha10004gg1hpam9p1h; ZFY=9CdH4D7qNf:AQ5G3tNgV9KroU81IeBFTISk2nCq5efmU:C; COOKIE_SESSION=8912_4_5_9_3_12_0_0_3_5_0_0_8788_20_13_0_1670741017_1670730809_1670741004%7C9%23229_180_1670730803%7C9; ab_sr=1.0.1_YzBhZWIwMjM1OGJmODcxZTBhYzRlNGMyMDlkYjNlNTA5ZTlhNmQ3ZmY4N2YxZjIxOTkyYzFmMWE1MmMzZTU5YmU1MTMwYTAxZTcwNmNkYWMyNjdkOWE2N2FhNWZiZjA1ZTU4YTZjOTRmNDQ0NDAxMGM1YWMwOGMwNDkyYzJlMzRjMDFkNTBhMWU5ZDY3NTBlNDg3YTRiMWU1NmY4OGI0Yw==; PSINO=6; H_PS_645EC=ee76U8QPs0nvA6RFqFJclD%2Fkhe68U8%2FHl6MRpWUSiujawzaXJKrKc7i8muE; baikeVisitId=4f440ee4-2937-44f6-841e-a0c1b1b74984; B64_BOT=1',
    'Host':' www.baidu.com',
    'sec-ch-ua':' "Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile':' ?0',
    'sec-ch-ua-platform':' "Windows"',
    'Sec-Fetch-Dest':' document',
    'Sec-Fetch-Mode':' navigate',
    'Sec-Fetch-Site':' none',
    'Sec-Fetch-User':' ?1',
    'Upgrade-Insecure-Requests':' 1',
    'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}
    # url = https://sz.lianjia.com/zufang/futianqu/pg2rt200600000001l1/#contentList
url_base = 'https://www.baidu.com/s?wd=ip'

from lxml import etree


proxy = random.choice(praxies_list)
print(proxy)
url = url_base
request = urllib.request.Request(url=url, headers=header)
handler = urllib.request.ProxyHandler(proxies=proxy)
opener = urllib.request.build_opener(handler)
response = opener.open(request)
print(response.status)
content = response.read().decode('utf8')
add= etree.HTML(content).xpath('//*[@id="1"]/div[1]/div[1]/div[2]/table/tbody/tr/td/text()')
print(add)




