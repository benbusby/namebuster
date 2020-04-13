from bs4 import BeautifulSoup
import utils.request as request
import spacy


def find_names(content):
    names = []

    try:
        nl = spacy.load('en_core_web_sm')
    except IOError:
        print('Unable to find pretrained models, downloading now...')
        spacy.cli.download('en_core_web_sm')
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
    print('Parsing web content...')
    content = ''
    get_body = request.fetch(url)

    soup = BeautifulSoup(get_body, 'html.parser')
    for text in soup.find_all(text=True):
        if not text.strip() or not ''.join(text.split()).isalpha():
            continue

        content += text + ' '

    return find_names(content)


def parse_file_content(filepath):
    print('Parsing file content...')
    return find_names(open(filepath, 'r').read())

