#!/usr/bin/python3
"""100-count"""
from requests import get


def count_words(subreddit, word_list, word_count=[], page_after=None):
    """count words"""
    headers = {'User-Agent': 'HolbertonSchool'}

    word_list = [word.lower() for word in word_list]

    if bool(word_count) is False:
        for word in word_list:
            word_count.append(0)

    if page_after is not None:
        url = ('https://www.reddit.com/request/{}/hot.json?after={}'
               .format(subreddit,
                       page_after))
        request = get(url, headers=headers, allow_redirects=False)

        if request.status_code == 200:
            for child in request.json()['data']['children']:
                i = 0
                for i in range(len(word_list)):
                    for word in [w for w in child['data']['title'].split()]:
                        word = word.lower()
                        if word_list[i] == word:
                            word_count[i] += 1
                    i += 1
            if request.json()['data']['after'] is not None:
                count_words(subreddit, word_list,
                            word_count, request.json()['data']['after'])
            else:
                dicto = {}
                for key_word in list(set(word_list)):
                    i = word_list.index(key_word)
                    if word_count[i] != 0:
                        dicto[word_list[i]] = (word_count[i] *
                                               word_list.count(word_list[i]))

                for key, value in sorted(dicto.items(),
                                         key=lambda x: (-x[1], x[0])):
                    print('{}: {}'.format(key, value))
    else:
        url = 'https://www.reddit.com/request/{}/hot.json'.format(subreddit)
        request = get(url, headers=headers, allow_redirects=False)
        if request.status_code == 200:
            for child in request.json()['data']['children']:
                i = 0
                for i in range(len(word_list)):
                    for word in [w for w in child['data']['title'].split()]:
                        word = word.lower()
                        if word_list[i] == word:
                            word_count[i] += 1
                    i += 1

            if request.json()['data']['after'] is not None:
                count_words(subreddit, word_list,
                            word_count, request.json()['data']['after'])
