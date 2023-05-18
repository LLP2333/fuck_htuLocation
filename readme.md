## fuck_htuLocation
自动获取移动学工考勤列表，并进行打卡(仅适用于GPS考勤)

### 学院设置
默认软件学院，可在移动学工公众号-学生中心-复制网站链接 查看，
如 https://htu.g8n.cn/student/punchs/course/数字/ 不同的学院的数字不一样
到代码中替换一下数字即可
### 抓网站cookie
手机微信浏览学生中心页面的时候，使用电脑软件fiddler everywhere抓取请求中的cookie，填写到代码指定位置
### 修改经纬度
可以在酷安下载白马地图，利用工具箱的坐标拾取选择地址来获取经纬度，填写到代码指定位置
### 如何启动？
```bash
pip install requests #安装requests(仅首次启动需要)
python start.py #启动脚本的命令
```
### 如何定时运行？
可以使用Linux的cron设置定时任务，或者使用阿里云函数。
