#!/usr/bin/env python
"""
Minimal Example
===============
Generating a square wordcloud from the US constitution using default arguments.
"""

from os import path

import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt


# get file path of directory
d = path.dirname(__file__)


# read the whole text.
# text = open(path.join(d,'constitution.txt')).read()
text = open('Bai+Ye+Zhui+Xiong++-+Zhi+Wen.txt').read()
font = path.join(d, 'NotoSansCJK-DemiLight.ttc')

wordlist_after_jieba = jieba.cut(text, cut_all = True)
wl_space_split = " ".join(wordlist_after_jieba)

# Generate a word cloud image
wordcloud = WordCloud(font_path=font).generate(wl_space_split)

# Display the generated image
# the matplotlib way:
# plt.imshow(wordcloud)
# plt.axis("off")

# lower max_font_size
wordcloud = WordCloud(
    background_color= 'white', # set backgroud color
    # mask= backgroud_image # set backgroud image
    # max_words= 2000,
    # stopwords= STOPWORDS, #
    font_path=font,
    max_font_size=100,
    random_state=30
    )
wordcloud.generate(wl_space_split)
plt.figure()
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
