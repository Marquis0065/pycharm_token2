# @Time: 2022/12/10 20:09
import urllib.request
import urllib.parse
url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'
header={
    'Cookie': 'PSTM=1670316448; BAIDUID=5C1C13ED838B4E9163EB13447527F898:FG=1; BIDUPSID=13BDDFDD4EE50498A13B9E24EA378855; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; MCITY=-340:; H_PS_PSSID=37855_36552_37909_37866_37927_37886_37759_37900_26350_22157_37881; BDSFRCVID=Be-OJexroG0rZo7jrbG3UGmKSmKKUdrTDYLEOwXPsp3LGJLVg7-HEG0PtozPcLAbvmD-ogKK3gOTH4PF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tJIOVCDhtKD3H48k-4QEbbQH-UnLq-FHbmOZ04n-ah02qxcvjP6K-tDn3tJLBhJLW23P0Pom3UTdsq76Wh35K5tTQP6rLt-fHmb4KKJxbn70VbOsLt5-hf3DhUJiB5JMBan7_UJIXKohJh7FM4tW3J0ZyxomtfQxtNRJ0DnjtpChbC_Ge5uaDjJLeU5eetjK2CntsJOOaCvT8hvOy4oWK441Dh5z25bB-D63Wf5Talv6Dqvo3tOK3M04X-o9-hvT-54e2p3FBUQJMT6SQft20b0e2R32WUoabDjRsR7jWhk5ep72y5OmQlRX5q79atTMfNTJ-qcH0KQpsIJM5-DWbT8IjHCHt6k8tRCeoCvt-5rDHJTg5DTjhPrMMHOtWMT-MTryKKJ-yJAbj4_zLqQlQPuU0UciBhQb-HnRhlRNB-3iV-OxDUvnyxAZbNtLBUQxtNRJW-cxKhRNH4QzQKcobUPUDUJ9LUkJLgcdot5yBbc8eIna5hjkbfJBQttjQn3hfIkj2CKLtDKWbDDlDTL3-RJH-xQ0KnLXKKOLVbTGLp7ketn4hUt2KlIejU6He6baQmvLaMOEWhvle-o2QhrdQf4WWb3ebTJr32Qr-J05HlnpsIJM5-n00-tTLf5q2x0LaKviaKOjBMb1MMJDBT5h2M4qMxtOLR3pWDTm_q5TtUJMeCnTDMFhe6j0eauDJ6tDfKresJoq2RbhKROvhjRIbDugyxoObtRxtTrzWK3_-JonhU5jhfR6hfPU3fOHLU3kBgT9LMnx--t58h3_XhjJjIunQttjQn3yMHR22pjtbJ6UKJ7TyU45bU47yaOT0q4Hb6b9BJcjfU5MSlcNLTjpQT8r5MDOK5OuJRQ2QJ8BJCK-hCQP; BAIDUID_BFESS=5C1C13ED838B4E9163EB13447527F898:FG=1; BDSFRCVID_BFESS=Be-OJexroG0rZo7jrbG3UGmKSmKKUdrTDYLEOwXPsp3LGJLVg7-HEG0PtozPcLAbvmD-ogKK3gOTH4PF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF_BFESS=tJIOVCDhtKD3H48k-4QEbbQH-UnLq-FHbmOZ04n-ah02qxcvjP6K-tDn3tJLBhJLW23P0Pom3UTdsq76Wh35K5tTQP6rLt-fHmb4KKJxbn70VbOsLt5-hf3DhUJiB5JMBan7_UJIXKohJh7FM4tW3J0ZyxomtfQxtNRJ0DnjtpChbC_Ge5uaDjJLeU5eetjK2CntsJOOaCvT8hvOy4oWK441Dh5z25bB-D63Wf5Talv6Dqvo3tOK3M04X-o9-hvT-54e2p3FBUQJMT6SQft20b0e2R32WUoabDjRsR7jWhk5ep72y5OmQlRX5q79atTMfNTJ-qcH0KQpsIJM5-DWbT8IjHCHt6k8tRCeoCvt-5rDHJTg5DTjhPrMMHOtWMT-MTryKKJ-yJAbj4_zLqQlQPuU0UciBhQb-HnRhlRNB-3iV-OxDUvnyxAZbNtLBUQxtNRJW-cxKhRNH4QzQKcobUPUDUJ9LUkJLgcdot5yBbc8eIna5hjkbfJBQttjQn3hfIkj2CKLtDKWbDDlDTL3-RJH-xQ0KnLXKKOLVbTGLp7ketn4hUt2KlIejU6He6baQmvLaMOEWhvle-o2QhrdQf4WWb3ebTJr32Qr-J05HlnpsIJM5-n00-tTLf5q2x0LaKviaKOjBMb1MMJDBT5h2M4qMxtOLR3pWDTm_q5TtUJMeCnTDMFhe6j0eauDJ6tDfKresJoq2RbhKROvhjRIbDugyxoObtRxtTrzWK3_-JonhU5jhfR6hfPU3fOHLU3kBgT9LMnx--t58h3_XhjJjIunQttjQn3yMHR22pjtbJ6UKJ7TyU45bU47yaOT0q4Hb6b9BJcjfU5MSlcNLTjpQT8r5MDOK5OuJRQ2QJ8BJCK-hCQP; BA_HECTOR=ah8h2l0g8ha10h0k812ka3d21hp8qo21g; ZFY=9CdH4D7qNf:AQ5G3tNgV9KroU81IeBFTISk2nCq5efmU:C; APPGUIDE_10_0_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1669429501,1669699461,1669775517,1670671117; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1670672549; ab_sr=1.0.1_M2YxYzFiODZhYzZhNjUyMzQ1YmIxMWJjN2JhMmE5MmM4ZTlhNjI3MjkxOThiZmEyOWNjYmViMTMyMDc4MzBjMWFkNjNkZDBiMWM4ZDFjN2VlODgyODIwZjliMmQ5MTdiNTUzZWMzMjhhOWVmMTdjMmVjZDc4OTFiNmJkMDcxNDM3NDMxMzZkZjE0Y2FhYWNlZWU3NzUwMmEyNmM0YjcwNg=='
}
data = {
    'from': 'en',
    'to': 'zh',
    'query': 'spider',
    'simple_means_flag': '3',
    'sign': '63766.268839',
    'token': 'f4bfd988c6c11713a2d8aa7ddc440458',
    'domain': 'common'
}
data = urllib.parse.urlencode(data).encode('utf8')
respect = urllib.request.Request(url=url,data=data,headers=header)
response = urllib.request.urlopen(respect)
content= response.read().decode('utf8')
import json
obj = json.loads(content)
print(obj)