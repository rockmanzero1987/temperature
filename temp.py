#使用者輸入
temp = float(input('請輸入氣溫︰ '))


#溫度單位
if temp >= 50:
	f = round(temp, 1)
	c = round((temp - 32) / 9 * 5, 1)
else:
	f = round(temp * 9 / 5 + 32, 1)
	c = round(temp, 1)


#列印
f = str(f)
c = str(c)
text = str('現在氣溫是攝氏 ' + c + '，華氏 ' + f + ' 度。')
print(text)


#存檔
report = open('temperature.txt', 'w')
report.write(text)