#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from datetime import datetime
from time import sleep

sckey = '***'
sendkey = '***'

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
    sendkey = '***'
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
