coutry = input('请问您是哪个国家的： ')
age = input('请问您的年龄是多少： ')
age = int(age)
if coutry == '台湾':
    if age >= 18:
    	print('您可以考驾照')
    else:
    	print('您还不能考驾照！')
if coutry == '美国':
    if age >= 16:
    	print('您可以考驾照')
    else:
    	print('您还不能考驾照！')
else:
	print('您只能输入台湾或美国！')