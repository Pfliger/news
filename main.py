import json
import xml.etree.ElementTree as ET
import collections


def top_words(words, word_quantity=10):
    result = collections.Counter(words).most_common(word_quantity)
    return result


def top_json(filename, word_quantity=10, min_len=6):
    result = []
    with open(filename, encoding='utf-8') as file:
        file = json.load(file)
        news = file['rss']['channel']['items']
    for item in news:
        result .extend(x for x in item['description'].split() if len(x) > min_len)
    return top_words(result , word_quantity)


def top_xml(filename, word_quantity=10, min_len=6):
    tree = ET.parse(filename)
    root = tree.getroot()
    items = root.findall('channel/item')
    result = []
    for item in items:
        result.extend(x for x in item.find('description').text.split() if len(x) > min_len)
    return top_words(result, word_quantity)


print(top_json('newsafr.json'))
print(top_xml('newsafr.xml'))

