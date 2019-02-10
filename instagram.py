#!/usr/bin/env python

# -*- coding: utf-8 -*-

import os

import time

from src import InstaBot

from src.check_status import check_status

from src.feed_scanner import feed_scanner

from src.follow_protocol import follow_protocol

from src.unfollow_protocol import unfollow_protocol

class instabot(object):

	login = None	password = None

	

	def __init__(self):

		self.login = login

		self.password = password

		self.bot = bot

	

	def bot(self, login=None, password=None):

		bot = InstaBot(login=login,password=password,

		like_per_day=1000,

		comments_per_day=0,

		tag_list=['follow4follow', 'f4f', 'cute', 'l:212999109'],

		tag_blacklist=['rain', 'thunderstorm'],

		user_blacklist={},

		max_like_for_one_tag=50,

		follow_per_day=300,

		follow_time=1 * 60,

		unfollow_per_day=300,

		unfollow_break_min=15,

		unfollow_break_max=30,

		log_mod=0,

		proxy='',

		comment_list=[["this", "the", "your"],["photo", "picture", "pic", "shot", "snapshot"],["is", "looks", "feels", "is really"],["great", "super", "good", "very good", "good", "wow","very cool", "stylish", "beautiful", "so beautiful","so stylish", "so professional", "lovely","so lovely", "very lovely", "glorious","so glorious","very glorious", "adorable", "excellent", "amazing"],[".", "..", "...", "!", "!!", "!!!"]],

		unwanted_username_list=['second', 'stuff', 'art', 'project', 'love', 'life', 'food', 'blog','free', 'keren', 'photo', 'graphy', 'indo', 'travel', 'art', 'shop','store', 'sex', 'toko', 'jual', 'online', 'murah', 'jam', 'kaos','case', 'baju', 'fashion', 'corp', 'tas', 'butik', 'grosir', 'karpet','sosis', 'salon', 'skin', 'care', 'cloth', 'tech', 'rental', 'kamera','beauty', 'express', 'kredit', 'collection', 'impor', 'preloved','follow', 'follower', 'gain', '.id', '_id', 'bags'],

		unfollow_whitelist=['example_user_1', 'example_user_2'])

		

	while True:

		mode = 0

		if mode == 0:

			bot.new_auto_mod()

		elif mode == 1:

			check_status(bot)

			while bot.self_following - bot.self_follower > 200:

				unfollow_protocol(bot)

				time.sleep(10 * 60)

				check_status(bot)

			while bot.self_following - bot.self_follower < 400:

				while len(bot.user_info_list) < 50:

					feed_scanner(bot)

					time.sleep(5 * 60)

					follow_protocol(bot)

					time.sleep(10 * 60)

					check_status(bot)

		elif mode == 2:

			bot.bot_mode = 1

			bot.new_auto_mod()

		elif mode == 3:

			unfollow_protocol(bot)

			time.sleep(10 * 60)

		elif mode == 4:

			feed_scanner(bot)

			time.sleep(60)

			follow_protocol(bot)

			time.sleep(10 * 60)

		elif mode == 5:

			bot.bot_mode = 2

			unfollow_protocol(bot)

		else:

			print("Wrong mode!")
