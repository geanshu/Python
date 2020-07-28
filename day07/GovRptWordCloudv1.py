'''
wordcloud库
    wordcloud.WordCloud()   代表一个文本对应的词云
        width           指定词云对象生成图片的宽度，默认400像素
        height          指定词云对象生成图片的高度，默认200像素
        min_font_size   指定词云中字体的最小字号，默认4号
        max_font_size   指定词云中字体的最大字号，根据高度自动调节
        font_step       指定词云中字体字号的步进间隔，默认为1
        font_path       指定字体文件的路径，默认None
        max_words       指定词云显示的最大单词数量，默认200
        stop_words      指定词云的排除词列表，即不显示的单词列表
        mask            指定词云形状，默认为长方形，需要引用imread()函数
        background_color指定词云图片的背景颜色，默认为黑色
    w.generate(txt)         向WordCloud对象w中加载文本txt
    w.to_file(filename)     将词云输出为图像文件，.png或.jpg格式
'''
import jieba
import wordcloud

f=open('day07/新时代中国特色社会主义.txt','r',encoding='utf-8')
t=f.read()
f.close()

ls=jieba.lcut(t)
txt=' '.join(ls)
w=wordcloud.WordCloud(font_path='msyh.ttc',\
    width=1000,height=700,background_color='white',\
        max_words=20)
w.generate(txt)
w.to_file('day07/grwordcloud.png')