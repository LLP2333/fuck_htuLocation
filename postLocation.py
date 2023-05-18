import requests


# 请在下面的的headers填写你的cookie
def postLocation(id):
    headers = {
        'Host': 'htu.g8n.cn',
        'Connection': 'keep-alive',
        'Content-Length': '62',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'Origin': 'https://htu.g8n.cn',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 13; Mi 10 Pro Build/TKQ1.221114.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.141 Mobile Safari/537.36 XWEB/5049 MMWEBSDK/20230405 MMWEBID/2177 MicroMessenger/8.0.35.2360(0x28002353) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/wxpic,image/tpg,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'X-Requested-With': 'com.tencent.mm',
        'Referer': 'https://htu.g8n.cn/student/course/31031/punchs',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cookie': '填写你的cookie'}

# lat 为纬度，lng为经度 如'lat': '12.29746',    'lng': '13.06869'，自行修改
    data = {
        'id': id,
        'lat': '',
        'lng': '',
        'acc': '35.0',
        'res': None,
        'gps_addr': None
    }
    url = "https://htu.g8n.cn/student/punchs/course/31031/" + str(id)
    print(url)
    response = requests.post(url=str(url), headers=headers,
                             data=data)
    print(response.text)
