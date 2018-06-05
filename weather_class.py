import requests
import json


class DAY_PARTS:
	NONE = 0;
	NIGHT = 1;
	MORNING = 2;
	DAY = 3;
	EVENING = 4;


class Weather(object):
	def __init__(self, api_key, my_lat, my_lon):
		self.api_key = api_key;
		self.lat = my_lat;
		self.lon = my_lon;
		pass

	def setLatLon(self, lat, lan):
		self.lat = lat;
		self.lon = lon;
		
	def getLink(self):
		url = "https://api.weather.yandex.ru/v1/forecast?lat="+str(self.lat)+"&lon="+str(self.lon)+"&hours=true&extra=true";
		return url

	def getHeaders(self):
		headers = { "X-Yandex-API-Key": self.api_key }
		return headers;

	def ParseDefaultPressure(self, json_text):
		parsed_res = json.loads(json_text);
		self.default_pressure = parsed_res["info"]["def_pressure_mm"];

	def ParseWeatherFromJson(self, json_text, part):
		parsed_res = json.loads(json_text);
		if part == DAY_PARTS.NONE:
			json_obj = parsed_res["fact"];
			temp_name = "temp";
		elif part == DAY_PARTS.NIGHT:
			json_obj = parsed_res["forecasts"][0]["parts"]["night"];
			temp_name = "temp_avg";
		elif part == DAY_PARTS.MORNING:
			json_obj = parsed_res["forecasts"][0]["parts"]["morning"];
			temp_name = "temp_avg";
		elif part == DAY_PARTS.DAY:
			json_obj = parsed_res["forecasts"][0]["parts"]["day"];
			temp_name = "temp_avg";
		elif part == DAY_PARTS.EVENING:
			json_obj = parsed_res["forecasts"][0]["parts"]["evening"];
			temp_name = "temp_avg";
	
		
		res = { "temperature" : json_obj[temp_name], 
				"feels_like" : json_obj["feels_like"],
				"condition" : json_obj["condition"],
				"wind_speed" : json_obj["wind_speed"],
				"pressure_mm" : json_obj["pressure_mm"],
				"season" : parsed_res["fact"]["season"],
				"prec_type" : json_obj["prec_type"],
				"prec_strength" : json_obj["prec_strength"],
				"cloudness" : json_obj["cloudness"] };

		return res;
		

	def getWeather(self, part = DAY_PARTS.NONE):
		r = requests.get(self.getLink(), headers = self.getHeaders());
		return self.ParseWeatherFromJson(r.text, part);



