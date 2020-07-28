'''
    jieba库：中文分词第三方库
    lcut(s)
        精确模式，把文本精确的切分开，不存在冗余单词，返回一个列表类型的分词结果
    jieba.lcut(s, cut_all=True)
        全模式，把文本中所有可能的词语都扫描出来，返回一个列表类型的分词结果，存在冗余
    jieba.lcut_for_search(s)
        搜索引擎模式，在精确模式基础上，对长词再次切分
    jieba.add_word(w)
        向分词词典增加新词w
'''
import jieba
txt=open('day06/threekingdoms.txt','r',encoding='utf-8').read()
excludes={'将军','却说','荆州','二人','不可','不能','如此','商议','如何','主公','军士','左右','军马'}
words=jieba.lcut(txt)
counts={}

for word in words:
    if len(word)==1:
        continue
    elif word=='诸葛亮' or word=='孔明曰':
        rword='孔明'
    elif word=='关公' or word=='云长':
        rword='关羽'
    elif word=='玄德' or word=='玄德曰':
        rword='刘备'
    elif word=='蒙德' or word=='丞相曰':
        rword='曹操'
    else:
        rword=word
    counts[rword]=counts.get(rword,0)+1

for word in excludes:
    del counts[word]
items=list(counts.items())
items.sort(key=lambda x: x[1],reverse=True)
for i in range(10):
    word,count=items[i]
    print('{0:<10}{1:>5}'.format(word,count))
