#coding=utf-8
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import PIL.Image as Image
import numpy as np
import jieba
#导入必备的模块
stoplist = [line.strip() for line in open('stop.txt','r',encoding="utf8").readlines()]
#导入停用词
text_from_file_with_apath = open('comment.txt',encoding="utf8").read()
#打开本地数据文件signature.txt.注意文件名不能用中文
for stop in stoplist:
    jieba.del_word(stop)
#去除停用词
wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all=False)
wl_space_split = " ".join(wordlist_after_jieba)
#用jieba模块进行挖掘关键词
coloring=np.array(Image.open("new.jpg"))
#获取背景图片,new.jpg
my_wordcloud = WordCloud(background_color="white",
                         mask=coloring,
                         width=617, height=306,
                         font_path="方正悠黑_511M.ttf",
                         max_words=400,
                         max_font_size=100,
                         min_font_size=20,
                         random_state=42).generate(wl_space_split)
#用wordcloud设计显示字体
image_colors=ImageColorGenerator(coloring)
plt.imshow(my_wordcloud.recolor(color_func=image_colors))
#背景图片颜色与字体匹配
plt.imshow(my_wordcloud)
#显示图片
plt.axis("off")
# 关闭坐标轴
plt.show()
#显示词云图
