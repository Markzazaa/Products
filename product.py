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