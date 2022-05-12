# -*- coding: utf-8 -*-
# @Time    : 2022/5/12 13:56
# @Author  : 陈昊
# @Email   : i@umb.ink
# @File    : __init__.py.py
# @Software: PyCharm
'''保存文本为pdf文件'''
import os
import threading
from typing import Iterable, Tuple, Any

import img2pdf
from PIL import Image
from handright import handwrite

'''转换pdf文件并返回文件'''


def save(pdf_path, images):
    images[0].save(pdf_path, 'PDF', resolution=100.0, save_all=True, append_images=images[1:])
    return pdf_path


def iterable_to_pdf(iterables: Tuple[Iterable[Image.Image]], pdf_path) -> str:
    images = []
    for i in iterables:
        images.extend([image for image in i])
    return save(pdf_path, images)


from src.config import Config


def async_txt(txt):
    return handwrite(txt, Config.template)


class thread_transition(threading.Thread):

    def __init__(self, func, args=()):
        super(thread_transition, self).__init__()
        self.result = None
        self.func = func
        self.args = args

    def run(self):
        self.result = self.func(*self.args)

    def get_result(self):
        threading.Thread.join(self)
        try:
            return self.result
        except Exception as e:
            return None


def txt_to_pdf(text: str, file_name: str, out_dir: str = Config.out_dir) -> str:
    cut_count = Config.cut_count
    if len(text) > cut_count:
        threads = []
        for i in range(0, len(text), cut_count):
            thread = thread_transition(async_txt, (text[i:i + cut_count],))
            threads.append(thread)
            thread.start()
        images = (thread.get_result() for thread in threads)
    else:
        images = (handwrite(text, Config.template),)
    return iterable_to_pdf(images, os.path.join(out_dir, f'{file_name}.pdf'))
