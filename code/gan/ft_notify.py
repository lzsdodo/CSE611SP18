#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from datetime import datetime
from time import sleep

sckey = 'SCU25730T63e3614416fc25707f8b06b42da473e45ae8d1c49b316'
sendkey = '3520-76150a4e33b7d59016fd1441cff56104'

self_api = 'https://sc.ftqq.com/{sckey}.send'
channel_api = 'https://pushbear.ftqq.com/sub?sendkey={sendkey}&text={text}&desp={desp}'

def send_to_self(api, sckey, title, content):    
    url = api.format(sckey=sckey)
    
    text = title
    time = datetime.now().strftime('*%Y-%m-%d %H:%M:%S*')
    desp = content + '\n'*2 + time
    
    payload = {
        'text': title,
        'desp': desp
    }
    
    r = requests.post(url, params=payload)
    print(r.text)

def send_to_channel(api, sendkey, title, content):
    text = title
    time = datetime.now().strftime('*%Y-%m-%d %H:%M:%S*')
    desp = content + '\n'*2 + time
    
    payload = {
        'sendkey': sendkey,
        'text': title,
        'desp': desp
    }
    
    r = requests.post(api, params=payload)
    print(r.text)


def send_notification(title, content):
    sendkey = '3520-76150a4e33b7d59016fd1441cff56104'
    channel_api = 'https://pushbear.ftqq.com/sub?sendkey={sendkey}&text={text}&desp={desp}'
    
    text = title
    time = datetime.now().strftime('*%Y-%m-%d %H:%M:%S*')
    desp = content + '\n'*2 + time
    
    payload = {
        'sendkey': sendkey,
        'text': title,
        'desp': desp
    }
    
    r = requests.post(channel_api, params=payload)
    print(r.text)


def main():
    title = 'Server Status'
    content = '**Testing API...**'
    
    send_to_self(self_api, sckey, title, content)
    #sleep(1)    
    #send_to_channel(channel_api, sendkey, title, content)

if __name__ == '__main__':
    main()
