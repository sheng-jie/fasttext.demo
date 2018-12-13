import fastText

# user pretrained vectors
# classifier = fastText.train_supervised(
#     input="news_fasttext_train.txt", dim=300, wordNgrams=2, lr=0.5, epoch=20, pretrainedVectors="cc.zh.300.vec")

classifier = fastText.train_supervised(input="news_fasttext_train.txt")

labels = classifier.get_labels()
print(labels)

result = classifier.test("news_fasttext_train.txt")
print(result)

classifier.quantize()

classifier.save_model("news.model.bin")
