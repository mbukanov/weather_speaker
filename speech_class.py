# -*- coding: utf-8 -*-
import urllib

class YandexSpeech(object):
	def __init__(self, api_key, yformat = "mp3", lang = "ru-RU", speaker = "jane"):
		self.api_key = api_key;
		self.format = yformat;
		self.lang = lang;
		self.speaker = speaker;

	def getLink(self, text):
		link = "https://tts.voicetech.yandex.net/generate?key="+str(self.api_key)+"&text="+urllib.quote(text)+"&format="+str(self.format)+"&lang="+str(self.lang)+"&speaker="+str(self.speaker);
		return link;

	def downloadMp3File(self, link):
		urllib.urlretrieve(link, str("/tmp/yandex_speech.mp3"));
		
	def MakeVoiceFile(self, text):
		link = self.getLink(text);
		self.downloadMp3File(link);

		
		
		
