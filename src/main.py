# -*- coding: utf-8 -*-

import os
import time

import img2pdf
from PIL import Image, ImageFont
from handright import Template, handwrite
from config import *

# images = handwrite(text, template)
# img_out_dir = os.path.join(img_dir, article_name)
# if not os.path.isdir(img_out_dir):
#     os.mkdir(img_out_dir)
# for i, im in enumerate(images):
#     assert isinstance(im, Image.Image)
#     img_path = f'{img_out_dir}/{i}{img_type}'
#     im.save(img_path)
#     print(f'file {img_path} saved!')

# pdf_file = article_name + '.pdf'
# pdf_path = os.path.join(pdf_dir, pdf_file)
# with open(pdf_path, "wb") as f:
#     img_list = []
#     for img in os.listdir(img_out_dir):
#         if img.endswith(img_type):
#             img_list.append(os.path.join(img_out_dir, img))
#     f.write(img2pdf.convert(img_list))
#     print(f'pdf {pdf_path} saved!')
