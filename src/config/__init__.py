# -*- coding: utf-8 -*-
# @Time    : 2022/5/12 13:55
# @Author  : 陈昊
# @Email   : i@umb.ink
# @File    : __init__.py.py
# @Software: PyCharm
import os

from PIL import Image, ImageFont
from handright import Template


class Config:

    out_dir = '../pdf/'
    font_bo = './fonts/Bo.ttf'
    font_jing = './fonts/Jing.ttf'
    font_lan = './fonts/Lan.ttf'
    font_wan = './fonts/Wan.ttf'
    font_xing = './fonts/Xing.ttf'
    template = Template(
        background=Image.new(mode="1", size=(3665, 5183), color=1),
        font=ImageFont.truetype(font_bo, size=100),
        line_spacing=150,
        fill=0,  # 字体“颜色”
        left_margin=240,
        top_margin=120,
        right_margin=240,
        bottom_margin=140,
        word_spacing=5,
        line_spacing_sigma=2,  # 行间距随机扰动
        font_size_sigma=2,  # 字体大小随机扰动
        word_spacing_sigma=2,  # 字间距随机扰动
        end_chars="，。；：！",  # 防止特定字符因排版算法的自动换行而出现在行首
        perturb_x_sigma=6,  # 笔画横向偏移随机扰动
        perturb_y_sigma=3,  # 笔画纵向偏移随机扰动
        perturb_theta_sigma=0.08,  # 笔画旋转偏移随机扰动
    )
