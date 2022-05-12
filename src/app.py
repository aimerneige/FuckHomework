# -*- coding: utf-8 -*-
# @Time    : 2022/5/12 14:37
# @Author  : 陈昊
# @Email   : i@umb.ink
# @File    : app.py
# @Software: PyCharm
'''文本转手写pdf Flask'''
import os
import time

from flask_apscheduler import APScheduler
from flask import Flask, render_template, request, send_file, session, after_this_request

from src.tranisition import txt_to_pdf

app = Flask(__name__)
'''
文本转手写pdf api
method: post
params: text
return: pdf
'''


@app.route('/', methods=['POST', 'GET'])
def index():
    text = request.form['text']
    if len(text) > 1000:
        return '文本过长'
    path = f'{time.time()}+{request.remote_addr}'

    # @after_this_request
    # def remove_file(response):
    #     if response.status_code != 200:
    #         return response
    #     try:
    #         os.remove(path)
    #     except Exception as e:
    #         print(e)

    return send_file(txt_to_pdf(text, path))


'''定时删除pdf文件'''


class ASPConfig(object):
    JOBS = [
        {
            'id': 'job1',  # 一个标识
            'func': 'app:apscheduler_remove_file',  # 指定运行的函数
            'args': ["../pdf"],  # 传入函数的参数
            'trigger': 'interval',  # 指定 定时任务的类型
            'seconds': 10*3600 # 运行的间隔时间
        }
    ]

    SCHEDULER_API_ENABLED = True


def apscheduler_remove_file(path):
    print('删除文件')
    for file in os.listdir(path):
        if file.endswith('.pdf'):
            os.remove(f'{path}/' + file)


if __name__ == '__main__':
    app.config.from_object(ASPConfig())
    scheduler = APScheduler()
    scheduler.init_app(app)
    scheduler.start()
    app.run(debug=True)
