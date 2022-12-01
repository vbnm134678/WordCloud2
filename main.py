from wordcloud import WordCloud
from konlpy.tag import Okt
# 컨테이너에 동일한 값의 자료가 몇 개인지 파악하는데 사용되는 모듈
from collections import Counter
from PIL import Image
import matplotlib.pyplot as plt

# text data read
with open('대한민국헌법.txt', 'r', encoding='utf-8') as txt:
    text = txt.read()

okt = Okt()

# okt.pos 를 통해 data의 형태소가 명사, 형용사인 것만 저장 / 길이가 1인 단어는 제외
sentences_tag = []
sentences_tag = okt.pos(text)

noun_adjective_list = []
for word, tag in sentences_tag:
    if tag in ['Noun', 'Adjective']:
        if len(word) > 1:
            noun_adjective_list.append(word)

print(word)
# 많이 추출되는 단어 max_count 만큼 저장
max_count = 40
counts = Counter(noun_adjective_list)
counts_num = counts.most_common(max_count)
print(counts_num)
# WordCloud 생성
# 한글 분석에는 font를 한글로 지정해 주어야한다.
# 템플릿 wc 준비
wc = WordCloud(font_path=r'C:\Windows\Fonts\malgun.ttf', width=200, height=200, scale=2.0, max_font_size=100, background_color='white')
wc_view = wc.generate_from_frequencies(dict(counts_num))
print(type(wc_view))
plt.figure()
plt.imshow(wc_view)
wc_view.to_file('test2.png')