# A news classifier based on fasttext

# Requirements
* `pip install bottle`
* `pip install jieba`
* [Follow the guide to install fastText](https://github.com/facebookresearch/fastText/blob/master/python/README.md)
* `git clone https://github.com/sheng-jie/news.classifier.git`
* Download the corpus to `news.classifier/corpus` folder. 
  * [news_fasttext_train.txt](http://pan.baidu.com/s/1jH7wyOY)
  * [news_fasttext_test.txt](http://pan.baidu.com/s/1slGlPgx)
* Download the word vectors [cc.zh.300.vec.gz](https://s3-us-west-1.amazonaws.com/fasttext-vectors/word-vectors-v2/cc.zh.300.vec.gz) of Chinese to `news.classifier` folder of this project.(Optional)

# How to run
1. run `train.py`
2. run `web.py`
