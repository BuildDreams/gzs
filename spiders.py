import json
import re
import requests



#--------------------------天气预报爬虫-----------------------------------------------------------
def spider_weath():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36"
    }
    url1 = 'https://mat1.gtimg.com/pingjs/ext2020/weather/2017/scripts/main-b0d370c158.js'

    resw = requests.get(url=url1, headers=headers)
    resw.encoding = 'utf-8'

    sf = re.search(r'"(//apis.map.qq.com/.*?)",', resw.text).groups(1)[0]


    city_info = requests.get(url="http:" + sf )
    new_str = 'QQmap&&QQmap\('

    js = re.sub(new_str, "", city_info.text).strip(')')
    result = json.loads(js)
    current_ip = result['result']['ip']
    province = result['result']['ad_info']['province']
    city = result['result']['ad_info']['city']
    district = result['result']['ad_info']['district']
    adcode = result['result']['ad_info']['adcode']
    result = weather(province,city,district,adcode)

    return result


def weather(provinces,city,district,adcode):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36",
        "Referer": "https://tianqi.qq.com/index.htm?dc212.htm"
    }
    url = 'https://wis.qq.com/weather/common'
    params={
        "source": "pc",
        # "weather_type": "observe|forecast_1h|forecast_24h|index|alarm|limit|tips|rise",
        "weather_type":'forecast_1h|observe|air|tips',
        "province": "%s"%provinces,
        "city": "%s"%city
    }
    response = requests.get(url=url,params=params,headers=headers)

    response  = json.loads(re.sub('jQuery1113045821053825236335_1550813982681\(', '', response.text).strip(')'))['data']

    degree = response['observe']['degree']#温度
    humidity = response['observe']['humidity']  # 湿度
    wind_power = response['observe']['wind_power']  # 风级
    weather = response['observe']['weather']  # 多云
    wind_direction = response['forecast_1h']['0']['wind_direction']  # 风风向
    weather_short = response['air']['aqi_name']  # 霾


    tips1= response['tips']['observe']['0']
    tips2 = response['tips']['observe']['1']
    return (provinces,city,district,adcode,degree,humidity,wind_power,weather,wind_direction,weather_short,tips1,tips2)

