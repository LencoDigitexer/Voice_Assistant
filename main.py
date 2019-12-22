import os
from pocketsphinx import LiveSpeech, get_model_path
import requests
import lxml.html as html

model_path = get_model_path()

speech = LiveSpeech(
    verbose=False,
    sampling_rate=16000,
    buffer_size=2048,
    no_search=False,
    full_utt=False,
    hmm=os.path.join(model_path, 'zero_ru.cd_cont_4000'),
    lm=os.path.join(model_path, 'ru.lm'),
    dic=os.path.join(model_path, 'ru.dic')
)

print("Say something!")


for phrase in speech:
    print(phrase)
    if str(phrase) == "привет":
    	print("привет!!!!")
    	os.system("echo «привет» | RHVoice-test -p aleksandr")
    elif str(phrase) == "как дела":
     	print("Хорошо")
     	os.system("echo «хорошо» | RHVoice-test -p aleksandr")
    elif str(phrase) == "открой хром":
    	print("запускаю")
    	os.system("chromium")
    	os.system("echo «открываю браузер» | RHVoice-test -p aleksandr")
    elif str(phrase) == "хочу кодить":
    	print("кодер кодера найдет")
    	os.system("echo «кодер кодера найдет» | RHVoice-test -p aleksandr")
    	os.system("sublime-text")
    elif str(phrase) == "открой видео":
    	print("открываю")
    	os.system("echo «открываю ютуб» | RHVoice-test -p aleksandr")
    	os.system("chromium youtube.com")
    elif str(phrase) == "найди кота":
    	print("коты - это мило")
    	os.system("echo «коты это очень мило» | RHVoice-test -p aleksandr")
    	os.system("chromium https://yandex.ru/images/search?text=cat")
    else:
        voice = str(phrase)
        lst = voice.split()
        print(lst)
        print(len(lst))
        if lst[0] == 'новости':
            test = ""
            for i in range(1, len(lst)):
                test = test + " " + str(lst[i])
                r = requests.get('https://news.yandex.ru/yandsearch?text={}&rpt=nnews2&grhow=clutop&rel=rel'.format(test)).text
                parser = html.fromstring(r)
                news = ""
                for i in range(5):
                    try:
                        elem = parser.cssselect('a[class="link link_theme_normal title__link i-bem"]')[i]
                        print(elem.get('title'))
                        news = news + elem.get('title') + "\n\n"
                        #print(elem.get('href'))
                    except:
                        print("\nВсего " + str(i) + " новостей")
                        break
                os.system("echo '{}' | RHVoice-test -p aleksandr".format(news))
    #else: 
    #	print("Я тебя не понимаю")
    #	os.system("{}» | RHVoice-test -p aleksandr".format(phrase))
    print("-"*30)
