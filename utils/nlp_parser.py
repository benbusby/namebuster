from bs4 import BeautifulSoup
import request
import spacy


def find_names(content):
    names = []
    nl = spacy.load('en_core_web_sm')
    doc = nl(content)
    prev_word = ''
    for token in doc:
        if token.pos_ != 'PROPN':
            prev_word = ''
            continue

        if not prev_word:
            prev_word = token.text
            continue
        else:
            names.append(token.text + ' ' + prev_word)
            prev_word = ''

    return names


def parse_web_content(url):
    content = ''
    get_body = request.fetch(url)

    soup = BeautifulSoup(get_body, 'html.parser')
    for tag in soup.findAll():
        print('TODO')



def parse_file_content(filepath):
    return find_names(open(filepath, 'r').read())

