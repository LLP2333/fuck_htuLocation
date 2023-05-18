import re
import requests
import postLocation

# 请在下面的getListHeaders中填写你的cookie

getListHeaders = {
    'authority': 'htu.g8n.cn',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    'cookie': '填写你的cookie',
    'dnt': '1',
    'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',

}
resList = requests.get("https://htu.g8n.cn/student/course/31031/punchs", headers=getListHeaders)
# print(resList.content)

# get all提取到的所有数字
pattern = r'punchcard_(\d+)'
matches = re.findall(pattern, resList.text)

for match in matches:
    print(match)
    postLocation.postLocation(match)
    print("考勤成功")
