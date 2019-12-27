#-*- coding:utf-8 -*-
from aip import AipSpeech

APP_ID = '18121869'
API_KEY = 'hXP7nEXfrd6qTBGAWFOpDneT'
SECRET_KEY = '02npZZGmkbX8RA184fn64GPSy9WEnAq2'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

s = '我的第一个语音识别脚本'
sound = client.synthesis(s, 'zh',1,{
		'vol': 5,   #音量，取值0-15，默认为5中音量
		'per': 3,
		'spd': 6,	#语速，取值0-9， 默认为5中语速
		'pit': 8,	#音调，取值0-9， 默认为5中语调
		})
if not isinstance(sound, dict):
	with open('./tts.mp3', 'wb') as f:
		f.write(sound)

print('ok')
