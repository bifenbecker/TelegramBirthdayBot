import requests
from time import sleep
import parse
# https://api.telegram.org/bot<token>/METHOD_NAME
# 1324260176:AAG3UEoGFZYaFVtHrCntwU3wNLzglnBTyHY

TOKEN = '1324260176:AAG3UEoGFZYaFVtHrCntwU3wNLzglnBTyHY'
URL = 'https://api.telegram.org/bot' + TOKEN + '/'
nums = [0,1,2,3,4,5,6,7,8,9]


global last_update_id
last_update_id = 0

def get_updates():
    url = URL + 'getUpdates'
    r = requests.get(url)
    return r.json()

def send_message(chat_id, text="Hello"):

    url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id,text)
    requests.get(url)

def stop():
    data = get_updates()
    text_message = data['result'][-1]['message']['text']
    if text_message in 'stop':
        return False
    else:
        return True

def get_data(text_message):
    data = {'dd':text_message[0:2],'mm':text_message[3:5],'yy':text_message[5:]}
    return data

def main():
    Data = get_updates()
    chat_id = Data['result'][-1]['message']['chat']['id']
    send_message(chat_id,'Hello, write your birhday date like this dd.mm.yy')
    while stop():
        data = get_updates()

        chat_id = data['result'][-1]['message']['chat']['id']
        text_message = data['result'][-1]['message']['text']
        if int(text_message[0]) in nums:
            current_data = get_data(text_message)
        else:
            continue


        dd = int(current_data['dd'])
        mm = int(current_data['mm'])




        name = data['result'][-1]['message']['from']['first_name']
        update_id = data['result'][-1]['update_id']

        global last_update_id

        if last_update_id != update_id:
            if last_update_id == 0:
                last_update_id = update_id
                continue
            last_update_id = update_id
            if dd > 0 and dd < 32 and mm > 0 and mm < 13:
                text_data = parse.main(dd,mm)
                send_message(chat_id,text_data['title'])
                send_message(chat_id,text_data['text'])
            else:
                send_message(chat_id,'Write again')
        else:
            continue



        sleep(2.2)





if __name__ == '__main__':
    main()
