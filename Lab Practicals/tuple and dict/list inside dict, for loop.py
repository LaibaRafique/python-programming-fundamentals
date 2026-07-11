favorite_places={"laiba":["Turkey","Forest","Thailand"],"Dur":["New York","Mountains","Qatar"],"Hamna":["Korea","Muree","Beach"]}
for k,v in favorite_places.items():
    print(k,"likes the following places:")
    for i in v:
        print("-",i)
    print()