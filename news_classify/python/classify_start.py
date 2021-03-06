# -*- coding: utf-8 -*-

import os
import csv
import re
from sta_ad import start_ad,cut_weibo

def main(name,flag):#数据输入

    weibo = []
    weibo_dict = dict()
    reader = csv.reader(file('./news/train_%s.csv' % name, 'rb'))
    for line in reader:
        row = [line[0],line[2],line[1],line[3],line[4],line[5],line[6],\
                line[7],line[8],line[9],line[10],line[11],\
                line[12],line[13],line[14],line[15],line[16],line[17],\
                line[18]]
        weibo.append(row)
        weibo_dict[str(line[0])] = line[2]
    label = classify(weibo,flag)

    with open('./test/test_label_%s.csv' % flag, 'wb') as f:
        writer = csv.writer(f)
        for k,v in label.iteritems():
            writer.writerow(([k,weibo_dict[str(k)],v]))

def classify(weibo,flag):
    '''
    分类主函数:
    输入数据:weibo(list元素)，示例：[[mid,text,...],[mid,text,...]...]
            flag(标记变量，任意设置)
    输出数据:label_data(字典元素)，示例：{{'mid':类别标签},{'mid':类别标签}...}
            1表示垃圾文本，0表示新闻文本，-1表示评论文本
    '''
    label_data = start_ad(weibo,flag)#垃圾分类

    news_weibo = []
    for i in range(0,len(weibo)):
        if label_data[str(weibo[i][0])] == 0:
            news_weibo.append(weibo[i])
    
    label = cut_weibo(news_weibo)#新闻与非新闻分类
    for i in range(0,len(label)):
        if label[i] == 0:
            mid = news_weibo[i][0]
            label_data[str(mid)] = -1

    return label_data

if __name__ == '__main__':
    main('huge','0125')
