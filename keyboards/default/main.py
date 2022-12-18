from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

city = ReplyKeyboardMarkup(
    keyboard=[
        [
        KeyboardButton(text="Toshkent"),
        KeyboardButton(text="Andijon"),
        KeyboardButton(text="Farg'ona"),
        ],
        [
        KeyboardButton(text="Qarshi"),
        KeyboardButton(text="Navoiy"),
        KeyboardButton(text="Namangan"),
        ],
        [
        KeyboardButton(text="Nukus"),
        KeyboardButton(text="Buxoro"),
        KeyboardButton(text="Samarqand"),
        ],
        [
        KeyboardButton(text="Jizzax"),
        KeyboardButton(text="Urganch"),
        KeyboardButton(text="Termiz"),
        KeyboardButton(text="Guliston"),
        ],
    ], resize_keyboard=True
)

main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="⛅ Bugungi ob-havo"), KeyboardButton(text="🗓 10 kunlik ob-havo")],
        [KeyboardButton(text="📍 Hududni o'zgartirish")]
    ], resize_keyboard=True
)