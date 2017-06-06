#coding=utf-8
from __future__ import print_function

from zhihu_oauth import ZhihuClient
import re

class AnswersFetcher(object):
    def __init__(self, username, password):
        self.client = ZhihuClient()
        self.client.login(username, password)

    def fetch_to_single_file(self, question_id, dir=''):
        def _delete_label_(str):
            return re.sub('<.*?>', '', str)

        question = self.client.question(question_id)
        clean_title = question.title.replace('/', ',')
        with open(dir + 'question_title.txt', 'w') as f:
            print(question.title.encode('utf-8'), file=f)

        print(dir + clean_title + '.txt')
        with open(dir + clean_title + '.txt', 'w') as f:
            for answer in question.answers:
                print(_delete_label_(answer.content).encode('utf-8'), file=f)

