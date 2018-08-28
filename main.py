# -*- coding: utf-8 -*-                                                                                       

from weather_class import Weather
from speech_class import YandexSpeech

api_key = ""

condition_translate = {
	"clear": "ясно",
    "partly-cloudy": "малооблачно",
    "cloudy": "облачно с прояснениями",
    "overcast": "пасмурно",
    "partly-cloudy-and-light-rain": "небольшой дождь",
    "partly-cloudy-and-rain":"дождь",
    "overcast-and-rain":"сильный дождь",
    "overcast-thunderstorms-with-rain":"сильный дождь, гроза",
    "cloudy-and-light-rain":"небольшой дождь",
    "overcast-and-light-rain":"небольшой дождь",
    "cloudy-and-rain":"дождь",
    "overcast-and-wet-snow":"дождь со снегом",
    "partly-cloudy-and-light-snow":"небольшой снег",
    "partly-cloudy-and-snow":"снег",
    "overcast-and-snow":"снегопад",
    "cloudy-and-light-snow":"небольшой снег",
    "overcast-and-light-snow":"небольшой снег",
    "cloudy-and-snow":"снег"
};

season_translate = {
	"summer" : "лето",
	"autumn" : "осень",
	"winter" : "зима",
	"spring" : "весна"
};

prec_translate = {
	0 : "без осадков",
	1 : "дождь",
	2 : "дождь со снегом",
	3 : "снег"
};

cloudness_translate = {
	0 : "ясно",
	0.25 : "малооблачно",
	0.5 : "облачно с прояснениями",
	0.75 : "облачно",
	1: "пасмурно"
};

def main():
	weather = Weather(api_key, 55, 33);
	speech = YandexSpeech(api_key, speaker="oksana");
	weather_res = weather.getWeather();
	text = "";
	text += "; Температура на улице "+str(weather_res["temperature"])+".";
	text += "; Действительно температура ощущается как " + str(weather_res["feels_like"])+".";
	text += "; Скорость ветра "+str(weather_res["wind_speed"])+".";
	text += "; На улице "+str(condition_translate[weather_res["condition"]])+".";
	text += "; "+str(season_translate[weather_res["season"]])+".";
	text += "; "+prec_translate[weather_res["prec_type"]]+".";
	text += "; "+cloudness_translate[weather_res["cloudness"]]+".";

	text += "; Желаю хорошо дня!";
	speech.makeVoiceFile(text);

if __name__ == "__main__":
	main()
