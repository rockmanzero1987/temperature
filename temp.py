while True:

#使用者輸入
	try:
  		temp = float(input('請輸入體溫︰ '))
	except:
  		print('輸入錯誤')
	else:
	

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
		text = str('你的體溫是攝氏 ' + c + '，華氏 ' + f + ' 度。')
		print(text)


#存檔
		report = open('temperature.txt', 'w')
		report.write(text)

		message = input('請按 Enter 鍵繼續......')