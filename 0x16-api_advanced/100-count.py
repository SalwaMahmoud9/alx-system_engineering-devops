#!/usr/bin/python3
from requests import get


def count_words(subreddit, word_list, word_count=[], page_after=None):
    """count_words"""
    headers = {'User-Agent': 'HolbertonSchool'}

    word_list = [word.lower() for word in word_list]

    if bool(word_count) is False:
        for word in word_list:
            word_count.append(0)

    if page_after is None:
        url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
        r = get(url, headers=headers, allow_redirects=False)
        if r.status_code == 200:
            for child in r.json()['data']['children']:
                index = 0
                for index in range(len(word_list)):
                    for word in [w for w in child['data']['title'].split()]:
                        word = word.lower()
                        if word_list[index] == word:
                            word_count[index] += 1
                    index += 1

            if r.json()['data']['after'] is not None:
                count_words(subreddit, word_list,
                            word_count, r.json()['data']['after'])
    else:
        url = ('https://www.reddit.com/r/{}/hot.json?after={}'
               .format(subreddit,
                       page_after))
        r = get(url, headers=headers, allow_redirects=False)

        if r.status_code == 200:
            for child in r.json()['data']['children']:
                index = 0
                for index in range(len(word_list)):
                    for word in [w for w in child['data']['title'].split()]:
                        word = word.lower()
                        if word_list[index] == word:
                            word_count[index] += 1
                    index += 1
            if r.json()['data']['after'] is not None:
                count_words(subreddit, word_list,
                            word_count, r.json()['data']['after'])
            else:
                dic = {}
                for keyWord in list(set(word_list)):
                    index = word_list.index(keyWord)
                    if word_count[index] != 0:
                        dic[word_list[index]] = (word_count[index] *
                                               word_list.count(word_list[index]))

                for k, v in sorted(dic.items(),
                                         k=lambda x: (-x[1], x[0])):
                    print('{}: {}'.format(k, v))
