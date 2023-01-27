# Есть некоторый текст. Реализуйте следующую функциональность:
# ■ Изменить текст таким образом, чтобы каждое предложение начиналось с большой буквы;
# ■ Посчитайте сколько раз цифры встречаются в тексте;
# ■ Посчитайте сколько раз знаки препинания встречаются в тексте;
# ■ Посчитайте количество восклицательных знаков в тексте.

import re
import string

punct = string.punctuation


def capitalize_first_letter(match):
    txt = match.group(0)
    char = txt[len(txt)-1]
    modified = txt.replace(char, char.capitalize())
    return modified


def capitalize_sentences(s):
    capitalized = re.sub(r'([.?!]\s\w)|^\w', capitalize_first_letter, s)
    return capitalized


text = """lorem: ipsum dolor! sit amet consectetur adipisicing elit? nam - neque pariatur praesentium.
amet, sunt fugiat (13 845 - consequuntur). nulla distinctio delectus."""

digits = len(re.findall("\d", text))
punctuation = len(re.findall(f"[{punct}]", text))
exclamation = len(re.findall("!", text))

print(f"\n{text}")
print(f"\nCapitalized:\n{capitalize_sentences(text)}")
print(f"\nDigits: {digits}")
print(f"\nPunctuations: {punctuation}")
print(f"\nExclamations: {exclamation}")
