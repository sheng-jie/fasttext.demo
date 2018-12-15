from bottle import route, run, template, get, post, request, redirect
import bottle
import fastText
import jieba.analyse
import sys
import os     

classifer = fastText.load_model("news.model.bin")
msgs = []
stopwords = []
title = ""

categories = {
    "home": "首页",
    "affairs": "时事",
    "edu": "教育",
    "economic": "财经",
    "house": "家居",
    "game": "游戏",
    "sports": "体育",
    "fashion": "潮流",
    "stock": "股票",
    "science": "科学",
    "ent": "娱乐",
    "lottery": "彩票",
    "constellation": "星座",
}


@get('/')
def check():
    return template('check', msgs=reversed(msgs), title=title)


@post('/clear')
def clear():
    msgs.clear()
    redirect('/')


@post('/check')
def do_check():
    msg = request.forms.msg.replace('\r\n', '')

    if check_contain_chinese(msg) == False:
        msgs.append(msg + "：不支持纯英文检测！")
        redirect('/')
    cutmsg = cut_sentence(msg)

    result = classifer.predict(cutmsg, k=4)
    predictResults = []
    for index, lable in enumerate(result[0]):
        lableNum = lable[len("__lable__"):]
        strResult = "{}={:.0%}".format(categories[lableNum], result[1][index])
        predictResults.append(strResult)

    predictResult = "{}：[{}]".format(msg, ",".join(predictResults))
    msgs.append(predictResult)
    savetohistory(predictResult)
    redirect('/')


def cut_sentence(sentence):
    """
    对句子进行分词,去停用词处理
    """
    sentence_seged = jieba.lcut(sentence.strip())
    outstr = ''
    for word in sentence_seged:
        word = word.replace(".", "").replace("\t", "").replace(" ", "")
        if word not in stopwords:
            if word != '\n':
                outstr += word
                outstr += " "
    return outstr


def savetohistory(msg):
    with open('check.history.txt', 'a') as file:
        file.write(msg + "\n")


def check_contain_chinese(check_str):
    for ch in check_str:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False


if __name__ == "__main__":
    abs_app_dir_path = os.path.dirname(os.path.realpath(__file__))
    abs_views_path = os.path.join(abs_app_dir_path, 'views')
    bottle.TEMPLATE_PATH.insert(0, abs_views_path )
    title = " ".join(categories.values())
    stopwords = [
        line.strip()
        for line in open('stopwords.txt', 'r', encoding='utf-8').readlines()
    ]
    run(host="localhost", port=8090, debug=True)
