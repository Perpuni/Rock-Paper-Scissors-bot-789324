from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.lexicon_ru import LEXICON_RU


# ----- Клавиатура с кнопками "Давай" и "Не хочу" -----
button_yes: KeyboardButton = KeyboardButton(text=LEXICON_RU["yes_button"])
button_no: KeyboardButton = KeyboardButton(text=LEXICON_RU["no_button"])

yes_no_kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

yes_no_kb_builder.row(button_yes, button_no, width=2)
yes_no_kb = yes_no_kb_builder.as_markup(one_time_keyboard=True, resize_keyboard=True)


# ----- Клавиатура с кнопками "Камень", "Ножницы", "Бумага" -----
button_rock: KeyboardButton = KeyboardButton(text=LEXICON_RU["rock"])
button_scissors: KeyboardButton = KeyboardButton(text=LEXICON_RU["scissors"])
button_paper: KeyboardButton = KeyboardButton(text=LEXICON_RU["paper"])

game_kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

game_kb_builder.row(button_rock, button_scissors, button_paper, width=1)
game_kb = game_kb_builder.as_markup(resize_keyboard=True)