print("--------Buffet Menu-----------")
buffet=("1.Biryani","2.Korma","3.Mutton","4.Kabab","5.BBQ")
for i in buffet:
    print(i)
print("-------Updated Buffet Menu--------")
buffet2=list(buffet)
del buffet2[1]
buffet2.insert(1,"2.Cake")
del buffet2[4]
buffet2.insert(4,"5.Ice cream")
buffet3=tuple(buffet2)
for i in buffet3:
    print(i)