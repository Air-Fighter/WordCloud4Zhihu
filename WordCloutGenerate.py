import jieba
import numpy
import codecs
import pandas
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
from os import listdir
from os.path import isfile, join

content = ''
for file_name in listdir('./result/'):
    if isfile(join('./result/', file_name)):
        file = codecs.open(join('./result/', file_name), 'r')
        content += file.read()
        file.close()
segment = []
segs = jieba.cut(content)
for seg in segs:
    if len(seg) > 1 and seg != '\r\n':
        segment.append(seg)

words_df = pandas.DataFrame({'segment':segment})
words_df.head()
stopwords = pandas.read_csv("stopwords_cn.txt", index_col=False, quoting=3, sep="\t",
                          names=['stopword'], encoding="utf8")
words_df = words_df[~words_df.segment.isin(stopwords.stopword)]

words_stat = words_df.groupby(by=['segment'])['segment'].agg({"count": numpy.size})
words_stat = words_stat.reset_index().sort(columns="count", ascending=False)

words_stat = words_df.groupby(by=['segment'])['segment'].agg({"count": numpy.size})
words_stat = words_stat.reset_index().sort(columns="count", ascending=False)

wordcloud = WordCloud(font_path='simhei.ttf', background_color='black')
wordcloud = wordcloud.fit_words(words_stat.head(1000).itertuples(index=False))
plt.axis('off')
plt.imshow(wordcloud)
plt.savefig('./result.png', dpi=600)
plt.show()
