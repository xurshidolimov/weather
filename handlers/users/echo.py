from aiogram import types
from loader import dp, db
from .functions import city_code
from keyboards.default import main, city
import datetime
import requests
from bs4 import BeautifulSoup as BS


@dp.message_handler(text="⛅ Bugungi ob-havo")
async def day_weather(message: types.Message):

    # foydalanuvchi manzilini olish
    user = await db.select_user(telegram_id=message.from_user.id)
    address = user[2]
    city_code_id = await city_code(address)

    # ma'lumotlarni yig'ish
    t = requests.get(f'https://weather.com/uz-UZ/ob-havo/bugun/l/{city_code_id}')
    html_t = BS(t.content, 'html.parser')
    for el in html_t.select('#MainContent'):
        moment = el.select('.CurrentConditions--primary--2DOqs')[0].text[0:2]
        description = el.select('.CurrentConditions--phraseValue--mZC_p')[0].text
        if description == 'Msaffo': description = 'Musaffo'
        minmax = el.select('.CurrentConditions--tempHiLoValue--3T1DG')[0].text
        wind = el.select('.WeatherDetailsListItem--wxData--kK35q')[1].text[14:]
        humidity = el.select('.WeatherDetailsListItem--wxData--kK35q')[2].text
        sunrise = el.select('.SunriseSunset--dateValue--3H780')[0].text
        sunset = el.select('.SunriseSunset--dateValue--3H780')[1].text

        time1 = el.select('#WxuHourlyWeatherCard-main-29584a07-3742-4598-bc2a-f950a9a4d900 .Ellipsis--ellipsis--3ADai')[0].text
        temp_m1 = el.select('#WxuHourlyWeatherCard-main-29584a07-3742-4598-bc2a-f950a9a4d900 .Column--temp--1sO_J')[0].text
        humidity1 = el.select('#WxuHourlyWeatherCard-main-29584a07-3742-4598-bc2a-f950a9a4d900 .Column--precip--3JCDO')[0].text

        time2 = el.select('#WxuHourlyWeatherCard-main-29584a07-3742-4598-bc2a-f950a9a4d900 .Ellipsis--ellipsis--3ADai')[1].text
        temp_m2 = el.select('#WxuHourlyWeatherCard-main-29584a07-3742-4598-bc2a-f950a9a4d900 .Column--temp--1sO_J')[1].text
        humidity2 = el.select('#WxuHourlyWeatherCard-main-29584a07-3742-4598-bc2a-f950a9a4d900 .Column--precip--3JCDO')[1].text

        time3 = el.select('#WxuHourlyWeatherCard-main-29584a07-3742-4598-bc2a-f950a9a4d900 .Ellipsis--ellipsis--3ADai')[2].text
        temp_m3 = el.select('#WxuHourlyWeatherCard-main-29584a07-3742-4598-bc2a-f950a9a4d900 .Column--temp--1sO_J')[2].text
        humidity3 = el.select('#WxuHourlyWeatherCard-main-29584a07-3742-4598-bc2a-f950a9a4d900 .Column--precip--3JCDO')[2].text

        time4 = el.select('#WxuHourlyWeatherCard-main-29584a07-3742-4598-bc2a-f950a9a4d900 .Ellipsis--ellipsis--3ADai')[3].text
        temp_m4 = el.select('#WxuHourlyWeatherCard-main-29584a07-3742-4598-bc2a-f950a9a4d900 .Column--temp--1sO_J')[3].text
        humidity4 = el.select('#WxuHourlyWeatherCard-main-29584a07-3742-4598-bc2a-f950a9a4d900 .Column--precip--3JCDO')[3].text

        time5 = el.select('#WxuHourlyWeatherCard-main-29584a07-3742-4598-bc2a-f950a9a4d900 .Ellipsis--ellipsis--3ADai')[4].text
        temp_m5 = el.select('#WxuHourlyWeatherCard-main-29584a07-3742-4598-bc2a-f950a9a4d900 .Column--temp--1sO_J')[4].text
        humidity5 = el.select('#WxuHourlyWeatherCard-main-29584a07-3742-4598-bc2a-f950a9a4d900 .Column--precip--3JCDO')[4].text

        # foydalanuvchiga ma'lumot yuborish
        await message.answer(f'<b>{address}</b> shahri  📎 {datetime.datetime.now().date()}\n\n'
                             f'<b>Hozir: {moment}</b>\n'
                             f'<i>{description}</i>\n'
                             f'🌕{minmax}🌑\n\n'
                             f'-----------\n\n'
                             f'Soatlar bo\'yicha:\n\n'
                             f'⏱<b>{time1}</b>: 🌡harorat <b>{temp_m1}</b>\n  <i>{humidity1}</i>\n\n'
                             f'⏱<b>{time2}</b>: 🌡harorat <b>{temp_m2}</b>\n  <i>{humidity2}</i>\n\n'
                             f'⏱<b>{time3}</b>: 🌡harorat <b>{temp_m3}</b>\n  <i>{humidity3}</i>\n\n'
                             f'⏱<b>{time4}</b>: 🌡harorat <b>{temp_m4}</b>\n  <i>{humidity4}</i>\n\n'
                             f'⏱<b>{time5}</b>: 🌡harorat <b>{temp_m5}</b>\n  <i>{humidity5}</i>\n\n'
                             f'-----------\n\n'
                             f'💦 <b>{humidity}</b>     Yomg\'ir yog\'ish ehtimoli\n'
                             f'🌅 <b>{sunrise}</b>     Quyosh chiqish vaqti\n'
                             f'🏙 <b>{sunset}</b>   Quyosh botish vaqti\n'
                             f'🌪 <b>{wind}</b>   Shamol tezligi\n'
                             f'@obhavoouz_robot')


@dp.message_handler(text="🗓 10 kunlik ob-havo")
async def ten_day_weather(message: types.Message):

    # foydalanuvchi manzilini olish
    user = await db.select_user(telegram_id=message.from_user.id)
    address = user[2]
    city_code_id = await city_code(address)

    # ma'lumotlarni yig'ish
    m = await message.answer('⌛ ')
    txt = f'<b>{address}</b> shahri\n\n'
    t = requests.get(f'https://weather.com/uz-UZ/ob-havo/10kun/l/{city_code_id}')
    html_t = BS(t.content, 'html.parser')
    for el in html_t.select('#MainContent'):
        for n in range(0, 10):
            day = el.select('.DaypartDetails--DayPartDetail--2XOOV .DetailsSummary--daypartName--kbngc')[n].text
            description = el.select('.DetailsSummary--extendedData--307Ax')[2*n].text
            if description == 'Msaffo': description = 'Musaffo'
            maxx = el.select('.DailyContent--temp--1s3a7')[2*n].text
            minn = el.select('.DailyContent--temp--1s3a7')[2*n+1].text
            humidity = el.select('.DetailsSummary--precip--1a98O')[n].text[4:]
            wind = el.select('.Wind--windWrapper--3Ly7c')[3*n].text
            txt += f'----------------\n' \
                   f'📎<b>{day}</b>\n' \
                   f'<i>{description}</i>\n' \
                   f'🌕 Kunduzi: {maxx}\n' \
                   f'🌑 Kechasi: {minn}\n' \
                   f'💦 Namlik:  {humidity}\n' \
                   f'🌪 Shamol:  {wind}\n\n'
        txt += '@obhavoouz_robot'

        # foydalanuvchiga ma'lumotni yuborish
        await m.delete()
        await message.answer(txt)



@dp.message_handler(text="📍 Hududni o'zgartirish")
async def update_address(message: types.Message):
    await message.answer("Hududni tanlang:", reply_markup=city)



@dp.message_handler(state=None)
async def weather(message: types.Message):
    try:
        # foydalanuvchini adresini saqlash
        city_code_id = await city_code(message.text)
        await db.update_user_address(telegram_id=message.from_user.id, Address=message.text)

        # ma'lumotlarni yig'ish
        t = requests.get(f'https://weather.com/uz-UZ/ob-havo/bugun/l/{city_code_id}')
        html_t = BS(t.content, 'html.parser')
        for el in html_t.select('#MainContent'):
            moment = el.select('.CurrentConditions--primary--2DOqs')[0].text[0:2]
            description = el.select('.CurrentConditions--phraseValue--mZC_p')[0].text
            if description == 'Msaffo': description = 'Musaffo'
            minmax = el.select('.CurrentConditions--tempHiLoValue--3T1DG')[0].text
            wind = el.select('.WeatherDetailsListItem--wxData--kK35q')[1].text[14:]
            humidity = el.select('.WeatherDetailsListItem--wxData--kK35q')[2].text
            sunrise = el.select('.SunriseSunset--dateValue--3H780')[0].text
            sunset = el.select('.SunriseSunset--dateValue--3H780')[1].text

            time1 = el.select('#WxuHourlyWeatherCard-main-29584a07-3742-4598-bc2a-f950a9a4d900 .Ellipsis--ellipsis--3ADai')[0].text
            temp_m1 = el.select('#WxuHourlyWeatherCard-main-29584a07-3742-4598-bc2a-f950a9a4d900 .Column--temp--1sO_J')[0].text
            humidity1 = el.select('#WxuHourlyWeatherCard-main-29584a07-3742-4598-bc2a-f950a9a4d900 .Column--precip--3JCDO')[0].text[4:]

            time2 = el.select('#WxuHourlyWeatherCard-main-29584a07-3742-4598-bc2a-f950a9a4d900 .Ellipsis--ellipsis--3ADai')[1].text
            temp_m2 = el.select('#WxuHourlyWeatherCard-main-29584a07-3742-4598-bc2a-f950a9a4d900 .Column--temp--1sO_J')[1].text
            humidity2 = el.select('#WxuHourlyWeatherCard-main-29584a07-3742-4598-bc2a-f950a9a4d900 .Column--precip--3JCDO')[1].text

            time3 = el.select('#WxuHourlyWeatherCard-main-29584a07-3742-4598-bc2a-f950a9a4d900 .Ellipsis--ellipsis--3ADai')[2].text
            temp_m3 = el.select('#WxuHourlyWeatherCard-main-29584a07-3742-4598-bc2a-f950a9a4d900 .Column--temp--1sO_J')[2].text
            humidity3 = el.select('#WxuHourlyWeatherCard-main-29584a07-3742-4598-bc2a-f950a9a4d900 .Column--precip--3JCDO')[2].text[4:]

            time4 = el.select('#WxuHourlyWeatherCard-main-29584a07-3742-4598-bc2a-f950a9a4d900 .Ellipsis--ellipsis--3ADai')[3].text
            temp_m4 = el.select('#WxuHourlyWeatherCard-main-29584a07-3742-4598-bc2a-f950a9a4d900 .Column--temp--1sO_J')[3].text
            humidity4 = el.select('#WxuHourlyWeatherCard-main-29584a07-3742-4598-bc2a-f950a9a4d900 .Column--precip--3JCDO')[3].text

            time5 = el.select('#WxuHourlyWeatherCard-main-29584a07-3742-4598-bc2a-f950a9a4d900 .Ellipsis--ellipsis--3ADai')[4].text
            temp_m5 = el.select('#WxuHourlyWeatherCard-main-29584a07-3742-4598-bc2a-f950a9a4d900 .Column--temp--1sO_J')[4].text
            humidity5 = el.select('#WxuHourlyWeatherCard-main-29584a07-3742-4598-bc2a-f950a9a4d900 .Column--precip--3JCDO')[4].text[4:]

            # foydalanuvchiga ma'lumot yuborish
            await message.answer(f'<b>{message.text}</b> shahri  📎 {datetime.datetime.now().date()}\n\n'
                                 f'<b>Hozir: {moment}</b>\n'
                                 f'<i>{description}</i>\n'
                                 f'🌕{minmax}🌑\n\n'
                                 f'-----------\n\n'
                                 f'Soatlar bo\'yicha:\n\n'
                                 f'⏱<b>{time1}</b>: 🌡harorat <b>{temp_m1}</b>\n     {humidity1}\n\n'
                                 f'⏱<b>{time2}</b>: 🌡harorat <b>{temp_m2}</b>\n     {humidity2}\n\n'
                                 f'⏱<b>{time3}</b>: 🌡harorat <b>{temp_m3}</b>\n     {humidity3}\n\n'
                                 f'⏱<b>{time4}</b>: 🌡harorat <b>{temp_m4}</b>\n     {humidity4}\n\n'
                                 f'⏱<b>{time5}</b>: 🌡harorat <b>{temp_m5}</b>\n     {humidity5}\n\n'
                                 f'-----------\n\n'
                                 f'💦 <b>{humidity}</b>     Yomg\'ir yog\'ish ehtimoli\n'
                                 f'🌅 <b>{sunrise}</b>     Quyosh chiqish vaqti\n'
                                 f'🏙 <b>{sunset}</b>   Quyosh botish vaqti\n'
                                 f'🌪 <b>{wind}</b>   Shamol tezligi\n'
                                 f'@obhavoouz_robot', reply_markup=main)
    except:
        await message.answer('Xatolik')



