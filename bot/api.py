import requests
import json

BASE_URL = 'http://localhost:8000/api'

def create_user(username,name,user_id):
    url = f"{BASE_URL}/bot-users/"
    response = requests.get(url=url).text
    data = json.loads(response)
    user_exist = False
    for i in data:
        if i['user_id'] == str(user_id):
            user_exist = True
            break 
    if user_exist == False:
        requests.post(url=url,data={'username':username,'name':name,'user_id':user_id})
        return "Foydalanuvchi yaratildi."
    else:
        return "Foydalanuvchi mavjud."


def create_feedback(user_id,body,age,name):
    url = f"{BASE_URL}/feedbacks/"
    if body and user_id and age:
        post = requests.post(url=url,data={"user_id":user_id,"body":body,'age':age,'name':name})
        return "Adminga jo'natildi. Fikr berganingiz uchun katta raxmat."
    else:
        return "Amal oxirigacha ishlamadi qaytadan urinib kuring!"