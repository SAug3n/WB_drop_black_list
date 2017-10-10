# -*- coding: UTF-8 -*-
import requests
def add_black_list(uid):
	url='http://weibo.com/aj/f/addblack?ajwvr=6'
	cookies={'YF-Page-G0':'','SUB':''}  #这里填自己的cookie值，只需要这两项
	headers={'Content-Type':'application/x-www-form-urlencoded','Referer':'http://weibo.com/6264005608/follow?refer=usercard&wvr=5&from=usercardnew'}
	data="uid="+str(uid)+"&f=1"
	r=requests.post(url,data=data,cookies=cookies,headers=headers)
	if '{"code":"100000"' in r.text.encode('GB18030','ignore'):
		print "drop id:"+str(uid)+"to black_list succeed."
	else:
		print "drop id:"+str(uid)+"failed."

def read_list():
	f=open('black_list_id.txt','r')
	for uid in f:
		add_black_list(uid)

read_list()
