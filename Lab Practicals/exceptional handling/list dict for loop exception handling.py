instagram = [{'Photos': 6, 'disLikes': 22, 'Comments': 3},
             {'disLikes': 13, 'Comments': 1, 'Shares': 6},
             {'Photos': 6, 'disLikes': 33, 'Comments': 9, 'Shares': 4},
             {'Comments': 5, 'Shares': 1},
             {'Photos': 5, 'Comments': 4, 'Shares': 2},
             {'Photos': 3, 'disLikes': 19, 'Comments': 3}] 
total_dislikes = 0
try:
    for post in instagram:
        if 'disLikes' not in post:
            continue
        else:
            total_dislikes = total_dislikes + post['disLikes']
            print(total_dislikes)
except:
    print("In except block")
else:
    print("Total number of dislikes on Instagram:",total_dislikes)