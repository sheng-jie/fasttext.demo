import fastText
import jieba

classifier = fastText.load_model("news.model.bin")

testNews = "腾讯报道 周杰伦将于年第在北京举行跨年演唱会 "
test = jieba.cut(testNews)
result = classifier.predict(" ".join(test))
print(result)
