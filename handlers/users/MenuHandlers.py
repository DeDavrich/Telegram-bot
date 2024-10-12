import logging
from aiogram.types import Message, CallbackQuery
from aiogram.types import InputFile

from keyboards.inline.InlineKeyboards import mainMenuuzb,mainMenurus,kursMenurus,kursMenuuzb,xodimlarMenurus,xodimlarMenuuzb,cancelrus,canceluzb,cancelxodimlarrus,cancelxodimlaruzb,cancelkurslar,cancelkurslarrus
from . import help
from loader import dp

@dp.callback_query_handler(text='uz')
async def command_bio(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await call.message.delete()
    photo_file = InputFile(path_or_bytesio="D:\Downloads\Tramplin_TelegramBot\photos/pramplin_rasm.jpg")
    msg = """'Tramplin' o'quv markaziga xush kelibsiz!\n Sizga kerak bo'lishi mumkin bo'lgan malumotni olish uchun tanlang:"""
    await call.message.answer_photo(photo=photo_file,caption = msg, reply_markup=mainMenuuzb)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='ru')
async def command_bio(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await call.message.delete()
    photo_file = InputFile(path_or_bytesio="D:\Downloads\Tramplin_TelegramBot\photos\pramplin_rasm.jpg")
    msg = """Добро пожаловать на учебный центр 'Tramplin'!\nЕсли вам нужна какая либо информация про наш учебный центр выберите ниже:"""
    await call.message.answer_photo(photo=photo_file,caption = msg, reply_markup=mainMenurus)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='xodimlar')
async def command_bio(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await call.message.delete()
    photo_file = InputFile(path_or_bytesio="D:\Downloads\Tramplin_TelegramBot\photos\iuch.webp")
    await call.message.answer_photo(photo=photo_file,caption="Bizning markazimiz oqituvchilari:",reply_markup=xodimlarMenuuzb)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='xodimlarrus')
async def command_bio(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await call.message.delete()
    photo_file = InputFile(path_or_bytesio="D:\Downloads\Tramplin_TelegramBot\photos\iuch.webp")
    await call.message.answer_photo(photo=photo_file,caption="Учителя нашего центра:",reply_markup=xodimlarMenurus)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='kurslar')
async def command_bio(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await call.message.delete()
    #Kurslar rasmi
    photo_file = InputFile(path_or_bytesio="D:\Downloads\Tramplin_TelegramBot\photos\i.jpg")
    await call.message.answer_photo(photo=photo_file,reply_markup=kursMenuuzb)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='kurslarrus')
async def command_bio(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await call.message.delete()
    photo_file = InputFile(path_or_bytesio="D:\Downloads\Tramplin_TelegramBot\photos\i.jpg")
    await call.message.answer_photo(photo=photo_file,reply_markup=kursMenurus)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='markaz')
async def command_bio(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await call.message.delete()
    photo_file = InputFile(path_or_bytesio="D:\Downloads\Tramplin_TelegramBot\photos\pamplin.jpg")
    msg = """
Tramplin IT Akademiyasida siz Dasturlashni Professionallardan o'rganishingiz mumkin!
Kurs davomida yuqori malakali dasturchilardan maxsus metodika asosida sifatli ta’lim olishingiz va o’zlashtirgan bilimlaringizni amaliyotda 50 dan ortiq loyiha asosida o’z portfolioingizni yaratishingiz mumkin

📞 +998 (90) 805 51 95
"""
    await call.message.answer_photo(photo=photo_file,caption = msg, reply_markup=canceluzb)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='markazrus')
async def command_bio(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await call.message.delete()
    photo_file = InputFile(path_or_bytesio="D:\Downloads\Tramplin_TelegramBot\photos\pamplin.jpg")
    msg = """
В Tramplin IT Academy вы можете научиться программированию у профессионалов!
В ходе курса вы сможете получить качественное образование по специальной методике у высококвалифицированных программистов и применить полученные знания на практике для создания собственного портфолио на основе более чем 50 проектов

📞 +998 (90) 805 51 95
"""
    await call.message.answer_photo(photo=photo_file,caption = msg, reply_markup=cancelrus)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='otajon')
async def command_bio(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await call.message.delete()
    photo_file = InputFile(path_or_bytesio="D:\Downloads\Tramplin_TelegramBot\photos\photo.jpg")
    msg = """
<b>Ismi-sharifi:</b>
Otajon Bozorboyev

<b>Tug'ilgan yili va joyi:</b>
08-yanvar 1999-yil;
Jizzax viloyati, Jizzax shahri.

<b>Ta'limi:</b> 
Toshkent temir yo'l transport kasb-hunar kolleji (2018)

<b>Ish tajribasi:</b> 
- "O'zbekiston temir yo'llari" AJ tashkiloti Jizzax temir yo'l masofasi xodimlar bo'limi nazoratchisi (HR) (2018-2023);
- Astro Education Python Beckend Mentor(2023-2024);
Tramplin IT Academy Backend dasturchi va Python backend mentor (2024-hozirgacha)

<b>Texnik ko'nikmalari:</b> 
C, Python, Django, Django Rest, SQLite, MySQL, PostgreSQL, Git, GitHub, HTML, CSS, Java Script, Telegram Bot, Microsoft Office(Word, Excel, Power Point, Paint, va h.k.lar)

<b>Tillar:</b> 
O'zbek tili (Ona tili);
Ingliz tili (B2);
Arab tili (O'qiy olish);
Yapon tili (N3)."""
    await call.message.answer_photo(photo=photo_file,caption = msg, reply_markup=cancelxodimlaruzb)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='otajonrus')
async def command_bio(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await call.message.delete()
    photo_file = InputFile(path_or_bytesio="D:\Downloads\Tramplin_TelegramBot\photos\photo.jpg")
    msg = """
<b>Имя и отчество:</b>
Otajon Bozorboyev

<b>Год и место рождения:</b>
08-января-1999;
Джизакская область, город Джизак.

<b>Образование:</b> 
Ташкентский профессиональный колледж железнодорожного транспорта (2018)

<b>Опыт работы:</b> 
- Руководитель отдела кадров (HR) Джизакской железнодорожной дистанции АО" Узбекистон темир йуллари " (2018-2023);
- Astro Education Python Beckend Mentor(2023-2024);
Бэкэнд-программист Tramplin IT Academy и бэкэнд-наставник Python (2024-настоящее время)

<b>Технические навыки:</b> 
C, Python, Django, Django Rest, SQLite, MySQL, PostgreSQL, git, github, HTML, CSS, Java Script, Telegram Bot, Microsoft Office(Word, Excel, Power Point, Paint и т. д.)k.s).
<b>Языки:</b> 
Узбекский язык (родной язык);
Английский (B2);
Арабский (умение читать);
Японский (N3)."""
    await call.message.answer_photo(photo=photo_file,caption = msg, reply_markup=cancelxodimlarrus)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='xusan')
async def command_bio(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await call.message.delete()
    photo_file = InputFile(path_or_bytesio="D:/Downloads/Tramplin_TelegramBot/photos/xusan.jpg")
    msg = """
Ma'lumot topilmadi
"""
    await call.message.answer_photo(photo=photo_file,caption = msg, reply_markup=cancelxodimlaruzb)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='xusanrus')
async def command_bio(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await call.message.delete()
    photo_file = InputFile(path_or_bytesio="D:/Downloads/Tramplin_TelegramBot/photos/xusan.jpg")
    msg = """
Информация не найдена
"""
    await call.message.answer_photo(photo=photo_file,caption = msg, reply_markup=cancelxodimlarrus)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='vakansiya')
async def command_bio(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await call.message.delete()
    msg = """
Bo'sh ish o'rini mavjud emas :(
"""
    await call.message.answer(msg, reply_markup=canceluzb)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='vakansiyarus')
async def command_bio(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await call.message.delete()
    msg = """
Нет вакансий :(
"""
    await call.message.answer(msg, reply_markup=cancelrus)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='backend')
async def command_bio(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await call.message.delete()
    msg = """
Tramplin IT Akademiyasida Backend-Python kursi sizga turli texnologiyalar va ramkalar yordamida veb-ilovalar va telegram botlarining backendini qanday yaratishni o'rgatadigan kursdir.
Siz Python tilining asoslari, uning sintaksisi, ma'lumotlar tuzilmalari, funksiyalari, sinflari va modullarini o'rganasiz.
Shuningdek, siz ma'lumotlar bazalari, xususan PostgreSQL bilan ishlash asoslari bilan tanishasiz va jadvallardan ma'lumotlarni qanday yaratish, o'zgartirish o'rganasiz. 

Backend Python kurslarimiz orqali siz

 Python 
 Python OOP
 Databases
 Telegram Bot
 Python Django Framework
 Serverlar bilan ishlash
 GIT
 Docker

bilimlariga ega bo'lasiz!"""
    photo_file = InputFile(path_or_bytesio="D:/Downloads/Tramplin_TelegramBot/photos/backend.jpg")
    await call.message.answer_photo(photo=photo_file,caption=msg,reply_markup=kursMenuuzb)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='backendrus')
async def command_bio(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await call.message.delete()
    msg = """
Курс Backend-Python в TRAMPLIN IT Academy-это курс, который научит вас создавать бэкэнд веб-приложений и ботов Telegram с использованием различных технологий и фреймворков.
Вы изучите основы языка Python, его синтаксис, структуры данных, функции, классы и модули.
Вы также познакомитесь с основами работы с базами данных, в частности PostgreSQL, и узнаете, как создавать, преобразовывать данные из таблиц. 

Через наши курсы Backend Python

 Python 
 Python ООП
 Базы данных
 Telegram Бот
 Python Django Framework
 Работа с серверами
 GIT
 Docker
вы получите знания по этим разделам"""
    photo_file = InputFile(path_or_bytesio="D:/Downloads/Tramplin_TelegramBot/photos/backend.jpg")
    await call.message.answer_photo(photo=photo_file,caption=msg,reply_markup=kursMenurus)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='frontend')
async def command_bio(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await call.message.delete()
    msg = """
Front- End dasturlash - 
bu dasturlash kasbini eng asosiy tushunchalardan tortib to‘liq ish vositalariga ega bo‘lgan ishonchli mutaxassis darajasigacha o‘zlashtirish uchun mo‘ljallangan kurs hisoblanadi.

Ushbu kurs HTML, CSS va JavaScript asoslarini, shuningdek,web dasturlashning eng yaxshi amaliyotlari va adaptiv dizayn texnikasini qamrab oladi.

Kurs davomiyligi: 8 oy
Darslar soni: 96 ta
Modul: 7

Biz talabalarimizga nafaqat amaliyotda yordam beramiz balki kelajakdagi startup loyihalariga ham ko’maklashamiz.
Qulay maskanda va moslashuvchan grafikda ta’lim oling"""
    photo_file = InputFile(path_or_bytesio="D:/Downloads/Tramplin_TelegramBot/photos/frontend.png")
    await call.message.answer_photo(photo=photo_file,caption=msg,reply_markup=kursMenuuzb)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='frontendrus')
async def command_bio(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await call.message.delete()
    msg = """
Front-end Программирование - 
это курс, предназначенный для освоения профессии программиста от самых базовых концепций до уровня надежного профессионала с полным набором рабочих инструментов.

Этот курс охватывает основы HTML,CSS и JavaScript, а также передовые методы веб-программирования и методы адаптивного дизайна.

Продолжительность курса: 8 месяцев
Количество уроков: 96
Модуль: 7

Мы не только помогаем нашим студентам на практике, но и помогаем в будущих стартап-проектах.
Получите образование в удобном месте и по гибкому графику"""
    photo_file = InputFile(path_or_bytesio="D:/Downloads/Tramplin_TelegramBot/photos/frontend.png")
    await call.message.answer_photo(photo=photo_file,caption=msg,reply_markup=kursMenurus)
    await call.answer(cache_time=60)



@dp.callback_query_handler(text='kiber')
async def command_bio(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await call.message.delete()
    msg = """
<b>Talim tili:</b>
O‘zbekcha

<b>Qiyinligi:</b>
Boshlangich

<b>Davomiligi:</b>
8 oy

<b>Kurs tavsifi:</b>
Kiberxavfsizlik – bu axborot texnologiyalari tizimlari va tarmoklarini xujumlardan ximoya kiladi.
Xozirgi kunda xakerlar turli yullar bilan rakamli tizim orkali bankdagi pullarni o'marishadi, yeki plastik kartangizdan pullarni yechib ketishi mumkin.
Kiberxavfsizlik aynan ana shunday jinoiy ilarning oldini oladi."""
    photo_file = InputFile(path_or_bytesio="D:\Downloads\Tramplin_TelegramBot\photos\cyber.jpg")
    await call.message.answer_photo(photo=photo_file,caption=msg,reply_markup=kursMenuuzb)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='kiberrus')
async def command_bio(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await call.message.delete()
    msg = """
<b>Язык обучения:</b> 
Узбекский

<b>Сложность:</b>
Начальный

<b>Продолжительность:</b> 
8 месяцев

<b>Описание курса:</b> 
Кибербезопасность-это защита информационных технологических систем и сетей от атак.
В настоящее время хакеры могут взламывать банковские деньги через цифровую систему различными способами, либо снимать деньги с вашей пластиковой карты.
Кибербезопасность предотвращает именно такие преступления."""
    photo_file = InputFile(path_or_bytesio="D:\Downloads\Tramplin_TelegramBot\photos\cyber.jpg")
    await call.message.answer_photo(photo=photo_file,caption=msg,reply_markup=kursMenurus)
    await call.answer(cache_time=60)