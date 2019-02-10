# -*- coding: utf-8 -*-

"""

Authorized by ALFINO NH ©FINBOT V3.0

contact us:

http://line.me/ti/p/~kangnur04

"""

from linepy import *

from akad.ttypes import *

from instagram import instabot

from datetime import datetime, timedelta, date

from bs4 import BeautifulSoup

from gtts import gTTS

from googletrans import Translator

from threading import Thread

from humanfriendly import format_timespan, format_size, format_number, format_length

import pytz

import pafy

import time

import timeit

import random

import sys

import ast

import re

import os

import json

import string

import codecs

import ctypes

import shutil

import atexit

import six

import urllib

import urllib.parse

import base64, tempfile

import traceback

import youtube_dl, livejson

bot_run = livejson.File("json/finbot1.json")

input_lib=livejson.File('json/line.json')

run_bot = livejson.File('json/logged.json')

mainlog=livejson.File('id.json')

listUser = livejson.File('json/admin.json')

Protect = livejson.File("protect.json")

passwd = mainlog["id"]["password"]

device = input_lib['RELOAD']['X-LineAccess']

id = mainlog['id']['email']

settings = {

        "block": 0,

        "cover": 0,

        "add": 0,

        "leave": 0,

        "join": 1,

        "ticket": 0,

        "foto": {},

        "photo": 0,

        "limiter": {

                "on": 1,

                "members": 15},

        "stickers": {

                "status": 0,

                "name": ""},

        "image": {

                "status": 0,

                "name": ""},

        "music": {

                "status": 0,

                "name": ""},

        "audio": {

                "status": 0,

                "name": ""},

        "video": {

                "status": 0,

                "name": ""},

        "videoPicture": 0,

        "videoProfilePicture": {

                "status": 0,

                "v_id": "",

                "p_id": ""},

        "groupPP": 0,

        "read": 0,

        "msg": 0,

        "post": 0,

        "reg_admin": 0,

        "unreg_admin": 0,

        "reg_bl": 0,

        "unreg_bl": 0,

        "contact": 0,

        "invite": 0,

        "regards": {

                "assalamu'alaikum warrahmatullahi wabbarakatuh": True,

                "Assalamu'alaikum warrahmatullahi wabbarakatuh": True,

                "assalamu'alaikum wr wb": True,

                "Assalamu'alaikum wr wb": True,

                "assalamu'alaikum": True,

                "Assalamu'alaikum": True,

                "assalamu alaikum": True,

                "السلام عليكم ورحمةالله وبركاتة": True,

                "السلام عليكم": True,

                "السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ ": True}

}

def instabot_login(login, password):

	instabot = (login,password)

def fositive():

	txt1 = ['тαrɢeт αdded', 'αdd ѕυcceѕѕ', 'αdded', 'нαѕ вeeɴ proмoтed']

	send1 = random.choice(txt1)

	return send1

	

def negative():

	txt2 = ['тαrɢeт reмoved', 'тαrɢeт deleтed', 'reмoved', 'deleтed', 'cleαr тαrɢeт']

	send2 = random.choice(txt2)

	return send2

	

def intro():

	txt3 = ['ѕend dιd yoυ мean тo υpdaтe', 'ѕend тargeт тo υp']

	send3 = random.choice(txt3)

	return send3

	

def fail():

	txt4 = ['fαílєd', 'fαílurє', 'ѕσmєthíng wєnt wrσng', 'αccєѕѕ nєgαtívє', 'єrrσr']

	send4 = random.choice(txt4)

	return send4

	

def on():

	txt5 = ['ѕtαtuѕ єnαвlєd', 'єnαвlєd', 'ѕtαtuѕ σn', 'αccєѕѕ grαntєd', 'αlrєαdч αctívє']

	send5 = random.choice(txt5)

	return send5

	

def off():

	txt6 = ['ѕtαtuѕ díѕѕαвlєd', 'díѕѕαвlєd', 'dєαctívαtєd', 'ѕtαtuѕ σff']

	send6 = random.choice(txt6)

	return send6

	

def cft():

	txt7 = ['phσtσ prσfílє updαtєd', 'pícturє updαtє', 'prσfílє updαtєd']

	send7 = random.choice(txt7)

	return send7

	

def dno():

	txt8 = ['ѕuccєѕѕ', 'dσnє', 'вєrєѕ вσѕ', 'clєαr вσѕѕ']

	send8 = random.choice(txt8)

	return send8

	

def up():

	txt9 = ['updαtє tσ: ', 'chαngєd tσ: ', 'rєplαcєd tσ: ']

	send9 = random.choice(txt9)

	return send9

	

def List():

	txt10 = ['nσ líѕt αddєd', 'єmptч líѕt', 'nσ tαrgєt αddєd', 'dαftαr mαѕíh kσѕσng', 'tαk αdα dαftαr чαng dí tαmвαhkαn']

	send10 = random.choice(txt10)

	return send10

	

def Bl():

	txt11 = ['вlαcklíѕt αddєd', 'uѕєr вlαcklíѕtєd', 'pєnggunα tєlαh dítαmвαhkαn dαlαm dαftαr hítαm']

	send11 = random.choice(txt11)

	return send11

	

def dBL():

	txt12 = ['вlαcklíѕt dєlєtєd', 'вlαcklíѕt rєmσvєd', 'uѕєr вlαcklíѕt rєmσvєd', 'dαftαr hítαm díhαpuѕ']

	send12 = random.choice(dBL)

	return send12

	

def ass():

	assa = ["وَعَلَيْكُمْ السَّلاَم","Wa'alaikumussalaam warrahmatullahi wabarakatuh","وَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ", "والسلام عليكم ورحمة الله وبركاته، ومعا حتى القدس الشريف بعونه تعالى!"]

	assalam = random.choice(assa)

	return assalam

def genTemporary(returnAs='path'):

	try:

		if returnAs not in ['file','path']:

			raise Exception('Invalid returnAs value')

		fName, fPath = 'finbotSQL-%s-%i.bin' % (int(time.time()), randint(0, 9)), tempfile.gettempdir()

		if returnAs == 'file':

			return fName

		elif returnAs == 'path':

			return os.path.join(fPath, fName)

	except Exception as e:

		print(e)

def download_img(url, file_name):

    r = requests.get(url, stream=True)

    if r.status_code == 200:

        with open(file_name, 'wb') as f:

            r.raw.decode_content = True

            shutil.copyfileobj(r.raw, f)

def random_string(length, seq='0123456789abcdefghijklmnopqrstuvwxyz'):

    sr = random.SystemRandom()

    return ''.join([sr.choice(seq) for i in range(length)])

def genImageB64(path):

    with open(path, 'rb') as img_file:

        encode_str = img_file.read()

        b64img = base64.b64encode(encode_str)

        return b64img.decode('utf-8')

def genUrlB64(url):

    return base64.b64encode(url.encode('utf-8')).decode('utf-8')

def waktu(secs):

    mins, secs = divmod(secs,60)

    hours, mins = divmod(mins,60)

    days, hours = divmod(hours, 24)

    return '%02d D %02d H %02d M %02d S' % (days, hours, mins, secs)

def runtime(secs):

    mins, secs = divmod(secs,60)

    hours, mins = divmod(mins,60)

    days, hours = divmod(hours, 24)

    return '%02d D %02d H %02d M %02d S' % (days, hours, mins, secs)

def cTime_to_datetime(unixtime):

    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))

def dt_to_str(dt):

    return dt.strftime('%H:%M:%S')
