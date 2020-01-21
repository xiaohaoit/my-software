# xiaohaoit
使用python进行编写，对接好企业微信机器人的API，然后进行测试先是否可以进行发布。
注意以下几个点：
1.一些目录备注了不能进行修改请勿修改，支持文本和图片进行导出！
2.在编写前注意在config下Config.ini文件进行编辑：
; 邮箱参数（务必填写以下参数）
[Email]
; 邮箱用户名
user = yehao
; 邮箱密码
password = 123456
; 邮箱服务器地址
host = mail.qq.com
; 邮箱服务器端口
port = 110
; 收件人列表, 以 | 分割
MailToList = 56801196@qq.com

; 密钥参数
[Key]
; key 注册地址：https://www.tianapi.com/apiview/26
; 替换26为：20，26，72，87，117，必须要去注册该API接口
Key = f6eb882685060d99ad4e515aa4cce20e

[DailyPaper]
; 画布大小
DefaultWidth = 600
DefaultHeight = 2700

; 最大重试次数
max_retry = 5
; 城市
city_name = 南昌

;不懂得问我，QQ56801196

3.Export文件夹里是代码成功运行后，如果是以图片导出，则会导出到该文件夹下并以当前日期命名。
4.Resource文件夹里是存放字体以及标题图片素材，可自行进行修改，不会的话就默认。
5.Logs文件夹里是存放运行日志、以及错误日志，没啥可动的。
6.pycache文件夹里的存放的是在编译后自动生成的文件，没啥可动。


文件都上传了，自己去打包下载，看说明操作。不懂的问我！QQ56801196
