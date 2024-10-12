from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

tilmenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🇺🇿 O'zbek tili", callback_data="uz"),
            InlineKeyboardButton(text="🇷🇺 Русский язык", callback_data="ru")
        ]
    ]
)

mainMenuuzb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="👨‍💻 Xodimlar", callback_data="xodimlar"),
            InlineKeyboardButton(text="📄 Kurslar", callback_data="kurslar")
        ],
        [
            InlineKeyboardButton(text="🗃 Vakansiya", callback_data="vakansiya"),
            InlineKeyboardButton(text="🏢 O'quv markaz haqida", callback_data="markaz")
        ],
        [
            InlineKeyboardButton(text="📲 Murojaat uchun", url="https://t.me/obozorboyev_bot")
        ]
    ])

mainMenurus = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="👨‍💻 Работники", callback_data="xodimlarrus"),
            InlineKeyboardButton(text="📄 Курсы", callback_data="kurslarrus")
        ],
        [
            InlineKeyboardButton(text="🗃 Вакансия", callback_data="vakansiyarus"),
            InlineKeyboardButton(text="🏢 Информация про Уч.центр", callback_data="markazrus")
        ],
        [
            InlineKeyboardButton(text="📲 Для обращения", url="https://t.me/obozorboyev_bot")
        ]
    ])

xodimlarMenuuzb = InlineKeyboardMarkup(
    inline_keyboard=[
          [
            InlineKeyboardButton(text="👨‍💻 Otajon Bozorboyev", callback_data="otajon"),
         ],
         [
            InlineKeyboardButton(text="👤 Xusan Xalilov", callback_data="xusan")
         ],
         [
            InlineKeyboardButton(text="🔙 Ortga", callback_data="uz")
         ]
    ]
) 

xodimlarMenurus = InlineKeyboardMarkup(
    inline_keyboard=[
          [
            InlineKeyboardButton(text="👨‍💻 Otajon Bozorboyev", callback_data="otajonrus"),
         ],
         [
            InlineKeyboardButton(text="👤 Xusan Xalilov", callback_data="xusanrus")
         ],
         [
            InlineKeyboardButton(text="🔙 Назад", callback_data="ru")
         ]
    ]
)

#Markaz haqida malumot,kurslar haqida malumot и тд
canceluzb = InlineKeyboardMarkup(
    inline_keyboard=[
          [
            InlineKeyboardButton(text="🔙 Ortga", callback_data="uz")
         ]
    ]
)

cancelrus = InlineKeyboardMarkup(
    inline_keyboard=[
          [
            InlineKeyboardButton(text="🔙 Назад", callback_data="ru")
         ]
    ]
)

cancelxodimlarrus = InlineKeyboardMarkup(
    inline_keyboard=[
          [
            InlineKeyboardButton(text="🔙 Назад", callback_data="xodimlarrus")
         ]
    ]
)

cancelxodimlaruzb = InlineKeyboardMarkup(
    inline_keyboard=[
          [
            InlineKeyboardButton(text="🔙 Ortga", callback_data="xodimlar")
         ]
    ]
)

cancelkurslar = InlineKeyboardMarkup(
    inline_keyboard=[
          [
            InlineKeyboardButton(text="🔙 Ortga", callback_data="kurslar")
         ]
    ]
)

cancelkurslarrus = InlineKeyboardMarkup(
    inline_keyboard=[
          [
            InlineKeyboardButton(text="🔙 Назад", callback_data="kurslarrus")
         ]
    ]
)


kursMenuuzb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="💻🦾📶 Backend", callback_data="backend"),
            InlineKeyboardButton(text="⚙️🖼🌐 Frontend", callback_data="frontend")
        ],
        [
            InlineKeyboardButton(text="🛡🔒🖥 Cyber", callback_data="kiber"),
            InlineKeyboardButton(text="🎨✅🖼 Graphic", callback_data="graphic")
        ],
        [
            InlineKeyboardButton(text="🔙 Ortga", callback_data="uz")
        ]
    ]
)

kursMenurus = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="💻🦾📶 Backend", callback_data="backendrus"),
            InlineKeyboardButton(text="⚙️🖼🌐 Frontend", callback_data="frontendrus")
        ],
        [
            InlineKeyboardButton(text="🛡🔒🖥 Cyber", callback_data="kiberrus"),
            InlineKeyboardButton(text="🎨✅🖼 Graphic", callback_data="graphicrus")
        ],
        [
            InlineKeyboardButton(text="🔙 Назад", callback_data="ru")
        ]
    ]
)