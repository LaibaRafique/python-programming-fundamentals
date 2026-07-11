d={1:{"name":"laiba","roll no":"64","batch":"2022F"},2:{"department":"software engineering","gender":"female"}}
print(d)
print(d[1]["name"])
print(d[2]["department"])
del d[1]["roll no"]
print(d[1])
d[3]={}
d[3]["section"]="B"
d[3]["favorite subject"]="Pfund"
print(d[3])
print(d)