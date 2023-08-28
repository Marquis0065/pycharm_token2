import requests
import json

class BaiduTongJi(object):

    def __init__(self, site_id, start_date, end_date, metrics, method, gran):
        """
        初始化方法
        :param site_id: 站点id
        :param start_date: 起始时间
        :param end_date: 截止时间
        :param metrics: 需要查看的字段，如：PV、UV、访问时长等
        :param method: 需要查看的报告如：全部来源、趋势分析等
        :param gran:时间粒度
        """
        self.api_url = 'https://api.baidu.com/json/tongji/v1/ReportService/getData'
        self.api_par = {
            "header": {
                "username": "fzh006591",
                'password': 'fzh0065913',
                "token": 'mLwqTsXdzXyrCuWn0wnXuQpw8rspxNMn',
                "account_type": 1
            },
            "body": {
                "site_id": site_id,
                "start_date": start_date,
                "end_date": end_date,
                "metrics": metrics,
                "method": method,
                "gran": gran
            }
        }
        return

    def send_request(self):
        data = json.dumps(self.api_par)
        request = requests.post(self.api_url, data)
        response = json.loads(request.text)
        self.response = response

        return self.response

    def source_all(self):
        """
        全部来源
        :return:
        """
        response = self.send_request()
        result = response['body']['data'][0]['result']['pageSum'][0]
        ret_pv = result[0]
        ret_uv = result[1]

        print(f"网站的PV是：{ret_pv}\n网站的UV是：{ret_uv}")

        return

    def trend(self):
        """
        趋势分析
        :return:
        """
        response = self.send_request()
        result = response['body']['data'][0]['result']['items']

        ret_data = result[0]
        ret_pv = result[1]


        return ret_data, ret_pv

# bdtj = BaiduTongJi(site_id='你的站点id', start_date=20190901, end_date=20190926,metrics='pv_count,visitor_count',method='source/all/a', gran=None)
# bdtj.source_all()
bdtj = BaiduTongJi(site_id='www.taobao.com', start_date=20190901, end_date=20190926,metrics='pv_count,visitor_count',method='source/all/a', gran=None)
bdtj.source_all()

