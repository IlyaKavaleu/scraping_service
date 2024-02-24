import json
#
# with open('newdata.json', 'r', encoding='utf-8') as f:
#     dates = json.load(f)
#     new = []
#     li = []
#
alpha = [
        'б'.title() or 'в'.title() or 'г'.title() or 'д'.title() or 'ж'.title() or 'з'.title() or 'й'.title() or 'к'.title() or
        'л'.title() or 'м'.title() or 'н'.title() or 'п'.title() or 'p'.title() or 'c'.title() or 'т'.title() or 'ф'.title() or 'x'.title() or 'ц'.title() or 'ч'.title() or 'ш'.title() or 'щ'.title() or
        'a'.title() or 'y'.title() or 'o'.title() or 'ы'.title() or 'э'.title() or 'я'.title() or 'ю'.title() or 'ё'.title() or 'и'.title() or 'e'.title()]
#
#     for data in dates:
#         new.append([str(data).replace(char, '') for char in alpha if char in str(data)])
#
#         if str(data).count('Ч'):
#             li.append(str(data).replace('Ч', ''))
#         else:
#             li.append(data)

with open('suodata.json', 'r', encoding='utf-8') as f:
    dates = json.load(f)
    for date in dates:
        print(date)
#     for data in dates:
#         print(data)
# for data in dates:
#     if str(data).count('Ч'):
#         data = str(data).replace('Ч', '')
#
# with open('newdata.json', 'w', encoding='utf-8') as file:
#     json.dump(dates, file, ensure_ascii=False, indent=4)
