products = []

while True:
	name = input ('請使用者輸入名稱: ')
	if name == 'q':
		break
	Price = input ('請輸入商品價格: ')
	P = []
	P.append(name)
	P.append(Price)
	products.append(P) #8910行也可直接寫成products.append([name, Price])	

print (products)
print (products[0][1])

for k in products:
	print (k[0], '的價格為', k[1])


with open ('products.csv', 'w') as f:
	for k in products:
		f.write(k[0] + ',' + k[1] + '\n')  #加入逗點方便CSV檔閱讀，寫入最後一定要用\n做分行