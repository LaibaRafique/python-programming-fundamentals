d={1:{"name":"laiba","roll no":"64","batch":"2022F"},2:{"name":"dur","roll no":"55","batch":"2022F"}}
for k,v in d.items():
    print("\n-Person",k)
    for i in v:
        print(i+":",v[i])