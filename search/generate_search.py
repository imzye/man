#!/usr/bin/env python3

import json
import os

def main():
    DIR_PARSE = ['MacOS', 'Linux', 'FreeBSD']
    # DIR_PARSE = ['MacOS']
    with open('search_index.json', 'r') as f:
        data = json.load(f)

    for dir in DIR_PARSE:
        files = os.listdir('../' + dir)
        for f in files:
            dic = {'location': dir + '/' + f, 'text': dir + ' ' + f.replace('.txt', ''), 'title': dir + ' ' + f.replace('.txt', '')}
            data["docs"].append(dic)
            # print(dic)

    # for d in data["docs"]:
    #     d["text"] = d["title"]

    with open('search.json', 'w') as f:
        json.dump(data, f)

if __name__ == '__main__':
    main()
