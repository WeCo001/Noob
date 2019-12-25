import jieba
import wordcloud
f = open("threekingdoms.txt", "r", encoding = "utf-8")
t = f.read()
f.close()
ls = jieba.lcut(t)
text = " ".join(ls)
w = wordcloud.WordCloud(font_path = "STHeiti Light.ttc",\
                        width = 1000, height = 700,\
                        background_color = "white",\
                        max_words = 15
                        )
w.generate(text)
w.to_file("Three Kingdom.png")
