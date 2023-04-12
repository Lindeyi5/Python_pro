# 开发时间：2023-03-25 9:35
# 开发人员：林坚洪
# encodeing "UTF-8"
import time

date1='2019-03-29 18:00:00'
# date2='2023-03-24 18:00:00'
# print(time.localtime())
timeArray=time.strptime(date1,"%Y-%m-%d %H:%M:%S")
# print(timeArray)
timestamp=time.mktime(timeArray)
# timeArray2=time.strptime(date2,"%Y-%m-%d %H:%M:%S")
#
# timestamp2=time.mktime(timeArray2)

num=((time.time()-timestamp)/60/60/24/7)
print(num)
print(int(num)+1)