# -*- coding: utf-8 -*-

import os
import img2pdf
from PIL import Image, ImageFont
from handright import Template, handwrite

article_dir = './article'
article_file = '荷塘月色.txt'
pdf_dir = './pdf'
img_dir = './img'
img_type = '.jpg'

font_bo = './fonts/Bo.ttf'
font_jing = './fonts/Jing.ttf'
font_lan = './fonts/Lan.ttf'
font_wan = './fonts/Wan.ttf'
font_xing = './fonts/Xing.ttf'

text = ""
article_path = os.path.join(article_dir, article_file)
with open(article_path, 'r') as f:
    lines = f.readlines()
    for line in lines:
        text += line

template = Template(
    background=Image.new(mode="1", size=(3665, 5183), color=1),
    font=ImageFont.truetype(font_lan, size=100),
    line_spacing=150,
    fill=0,  # 字体“颜色”
    left_margin=240,
    top_margin=120,
    right_margin=240,
    bottom_margin=140,
    word_spacing=5,
    line_spacing_sigma=2,  # 行间距随机扰动
    font_size_sigma=2,  # 字体大小随机扰动
    word_spacing_sigma=1,  # 字间距随机扰动
    end_chars="，。；：！",  # 防止特定字符因排版算法的自动换行而出现在行首
    perturb_x_sigma=3,  # 笔画横向偏移随机扰动
    perturb_y_sigma=3,  # 笔画纵向偏移随机扰动
    perturb_theta_sigma=0.04,  # 笔画旋转偏移随机扰动
)
images = handwrite(text, template)
for i, im in enumerate(images):
    assert isinstance(im, Image.Image)
    im.save(f'{img_dir}/{i}{img_type}')

pdf_file = article_file.split('.')[0] + '.pdf'
pdf_path = os.path.join(pdf_dir, pdf_file)
with open(pdf_path, "wb") as f:
    img_list = []
    for img in os.listdir(img_dir):
        if img.endswith(img_type):
            img_list.append(os.path.join(img_dir, img))
    f.write(img2pdf.convert(img_list))