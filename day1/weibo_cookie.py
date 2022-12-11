import requests
data = {
'Cookie': '_T_WM=65de0c9944f82ef363936d3a34739168; SUB=_2A25OinIUDeRhGeVM7FIS8ijKyTiIHXVqdR5crDV6PUJbktANLU_MkW1NTIY902mfEUbdNJqsWR5UsUvMZku1Doyk; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhbUZ87wBF1xl5dcThxaNSO5NHD95Q0eoM7e0zcSozXWs4DqcjMi--NiK.Xi-2Ri--ciKnRi-zN1gSyqrz0SJpNd5tt; SSOLoginState=1670251077'

}
header = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62'
}
url = 'https://weibo.cn/6436872484'
resp = requests.get(url,headers=header,cookies=data)
print(resp.content)
