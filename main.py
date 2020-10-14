import json
import xml.etree.ElementTree as ET
import collections


def top_words(words, word_quantity=10):

    result = collections.Counter(words).most_common(word_quantity)

    # number_of_reqest = {}
    # result2 = {}
    # quantity = 0
    # for word in words:
    #     number_of_reqest[word] = number_of_reqest.setdefault(word, 0) + 1
    # сharacters_list = list(set(sorted(number_of_reqest.values())))
    # сharacters_list.reverse()
    # for item in сharacters_list[:word_quantity]:
    #     for x, y in number_of_reqest.items():
    #         if item == y and quantity < word_quantity:
    #             result2[x] = y
    #             quantity += 1
    return result


def top_json(filename, word_quantity=10, min_len=6):
    text = []
    result = []
    with open(filename, encoding='utf-8') as file:
        file = json.load(file)
        news = file['rss']['channel']['items']
    for item in news:
        text += item['description'].split()
    for item in text:
        if len(item) > min_len:
            result.append(item)
    return top_words(result, word_quantity)


def top_xml(filename, word_quantity=10, min_len=6):
    tree = ET.parse(filename)
    root = tree.getroot()
    items = root.findall('channel/item')
    text = []
    result = []
    for item in items:
        text += item.find('description').text.split()
    for item in text:
        if len(item) > min_len:
            result.append(item)
    return top_words(result, word_quantity)


print(top_json('newsafr.json'))
print(top_xml('newsafr.xml'))

