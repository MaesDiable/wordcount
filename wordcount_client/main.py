import sys

import json
import requests

if __name__ == '__main__':
    url = "http://127.0.0.1"
    port = "5000"
    endpoint = "get_wordCount"
    file = sys.argv[2]
    readed_file = open(file, 'rb')
    raw_word_list = requests.post(url+":"+port+"/"+endpoint, readed_file)
    word_list_string = raw_word_list.content.decode("utf-8")
    word_list = json.loads(word_list_string)
    for key in word_list:
        print(key, word_list[key])




