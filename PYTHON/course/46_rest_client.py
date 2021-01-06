from rest import get_users, add_user, update_user, delete_user, get_user

record = {
    'nickname': 'test',
    'email': 'kolejny',
    'password': 'ddd'
}

add_user(**record)

update_user(30, nickname='YOLO', email='xxx@qqq.pl')

# delete_user(22)
# get_user(19)



users = get_users()

print(users)









