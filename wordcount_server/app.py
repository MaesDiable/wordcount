from flask import Flask, request
import re

app = Flask(__name__)


def normalize_text(text):
    lowered_text = text.lower()
    only_text = re.sub('[^A-Za-z0-9_á-é-í-ó-ú+]+', ' ', lowered_text)
    if only_text[len(only_text)-1] == " ":
        only_text = only_text[:-1]
    return only_text


def obtain_word_count(text_list):
    word_dictionary = dict()
    for word in text_list:
        if word in word_dictionary:
            word_dictionary[word] = word_dictionary[word] + 1
        else:
            word_dictionary[word] = 1
    return word_dictionary


@app.route('/get_wordCount', methods=['POST'])
def get_word_count():
    text = request.data.decode("utf-8")
    normalized_text = normalize_text(text)
    word_list = normalized_text.split(" ")
    word_count = obtain_word_count(word_list)
    return word_count, 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
