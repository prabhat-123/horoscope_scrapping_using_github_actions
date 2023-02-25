import requests
from bs4 import BeautifulSoup
import config as cfg
from datetime import datetime

date_today = datetime.now()
date_str = date_today.strftime("%B %d, %Y")
to_replace = date_str.split(',')[0].split(' ')[0]
replace_with = cfg.month_map.get(to_replace)
date_str = date_str.replace(to_replace, replace_with)
zodaic_sign = "Pisces"
zodaic_no = cfg.zodiac_sign_map.get(zodaic_sign)
url = "https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign={}".format(zodaic_no)
response = requests.get(url)
soup=BeautifulSoup(response.content,'html.parser')
# properties_links = []
data = soup.find('div', attrs={'class': 'main-horoscope'})
data = data.text
final_data = data.split('More Horoscopes for {}'.format(zodaic_sign))[0]
final_data = final_data.split(date_str + ' -')[1]
final_data = final_data.split('\n')
horoscope = ""
for item in final_data:
    if '$' in item:
        break
    else:
        print(item)
        horoscope = "".join(item)

print(horoscope)

