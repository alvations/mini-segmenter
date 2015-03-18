A lightweight lexicon/dictionary based Chinese text segmenter; it adds whitespace to separate and tokenize the text. For example,

**Input:**
```
应有尽有的丰富选择定将为您的旅程增添无数的赏心乐事
```
**Output:**
```
应有尽有 的 丰富 选择 定 将 为 您 的 旅程 增添 无数 的 赏 心 乐事
```

The advantage of using a lexicon/dictionary for text segmentation is the ability to localize and scale according to the text's language or domain. Supporting the open source movement, the default dictionary used by `mini-segmenter` is MDBG's [CC-CEDICT](http://www.mdbg.net/chindict/chindict.php?page=cedict).

The test suite sentences for mini-segmenter are from the [Nanyang Technological University - Multilingual Corpus](http://aclweb.org/anthology-new/Y/Y11/Y11-1038.pdf) (NTU-MC)

**[Download mini-segmenter here](https://mini-segmenter.googlecode.com/files/minisegmenter-v1.1.tar.gz)** =)

_NOTE: The preferred encoding for mini-segmenter is utf8_

---


### Mini-segmenter Usage ###

```
$ tar -zxvf minisegmenter-v1.1.tar.gz
$ cd minisegmenter-v1.1/
$ python
>>> import sys; reload(sys); sys.setdefaultencoding("utf-8")
>>> import minisegmenter as mini
>>> sentence = u"应有尽有的丰富选择定将为您的旅程增添无数的赏心乐事"
>>> print mini.segmenter(sentence.decode('utf8'))
应有尽有 的 丰富 选择 定 将 为 您 的 旅程 增添 无数 的 赏 心 乐事
```

---


### Algorithm ###

Firstly, the mini-segmenter splits a sentence into _mini-chunks_ by using punctuation as cues. In addition to punctuation, later versions of mini-segmenter uses _superspliters_ tokens such as `"在"` and `"的"`.

```
punctuations = ["，","、","。","！",'"','(',')','[',']','？','；','-',
                  '（','）','/','-','：', ' ','《','》','…',]
superspliter = ["在","的"]
cues = punctuations + superspliter
```

**Input:**
```
文化遗产、畅快购物以及饕餮美食在此汇聚，应有尽有的丰富选择定将为您的旅程增添无数的赏心乐事，让您满意而归。
```

**Output _mini-chunks_ (one per line):**
```
文化遗产
、
畅快购物以及饕餮美食在此汇聚
，
应有尽有的丰富选择定将为您
的旅程增添无数的赏心乐事
，
让您满意而归
。
```

Then mini-segmenter uses a dictionary to generate all possible tokens that can occur in the given sentence.

**_mini-chunk_:**
```
应有尽有的丰富选择定将为您的旅程增添无数的赏心乐事
```

**Possible Tokens (Nodes)**
```
#NodePosition Token
0-1 应
0-2 应有
1-2 有
2-3 尽
0-4 应有尽有
3-4 有
3-5 有的
4-5 的
5-6 丰
5-7 丰富
6-7 富
7-8 选
7-9 选择
8-9 择
8-10 择定
9-10 定
10-11 将
11-12 为
12-13 您
13-14 的
14-15 旅
14-16 旅程
15-16 程
16-17 增
16-18 增添
17-18 添
18-19 无
18-20 无数
19-20 数
20-21 的
21-22 赏
22-23 心
23-24 乐
23-乐事
24-事
```

Then using the **`LargestChunksParser`** module with its **`mini-square scoring`**, `mini-segmenter` determines which is the best set of tokens that can provide the output:

```
应有尽有 的 丰富 选择 定 将 为 您 的 旅程 增添 无数 的 赏 心 乐事
```


---


### Choosing the correct segmentation sequence ###

Using the nodes, the function **`LargestChunksParser`** will generate a list of possible segmentation sequence that is possible given the nodes as such (the exact list is much much longer):

```
25 应 有 尽 有 的 丰 富 选 择 定 将 为 您 的 旅 程 增 添 无 数 的 赏 心 乐 事
27 应 有 尽 有 的 丰 富 选 择 定 将 为 您 的 旅 程 增 添 无 数 的 赏 心 乐事
27 应 有 尽 有 的 丰 富 选 择 定 将 为 您 的 旅 程 增 添 无数 的 赏 心 乐 事
29 应 有 尽 有 的 丰 富 选 择 定 将 为 您 的 旅程 增 添 无 数 的 赏 心 乐事
31 应 有 尽 有 的 丰 富 选 择定 将 为 您 的 旅 程 增 添 无数 的 赏 心 乐事
31 应 有 尽 有 的 丰富 选 择 定 将 为 您 的 旅 程 增添 无 数 的 赏 心 乐事
41 应有尽有 的 丰 富 选 择定 将 为 您 的 旅程 增 添 无 数 的 赏 心 乐 事
41 应有尽有 的 丰 富 选择 定 将 为 您 的 旅 程 增 添 无 数 的 赏 心 乐事
41 应有尽有 的 丰 富 选择 定 将 为 您 的 旅 程 增 添 无数 的 赏 心 乐 事
43 应有尽有 的 丰 富 选 择定 将 为 您 的 旅程 增 添 无数 的 赏 心 乐 事
43 应有尽有 的 丰 富 选 择定 将 为 您 的 旅程 增添 无 数 的 赏 心 乐 事
43 应有尽有 的 丰富 选择 定 将 为 您 的 旅程 增 添 无 数 的 赏 心 乐 事
45 应有尽有 的 丰 富 选 择 定 将 为 您 的 旅程 增添 无数 的 赏 心 乐事
45 应有尽有 的 丰 富 选 择定 将 为 您 的 旅 程 增添 无数 的 赏 心 乐事
45 应有尽有 的 丰富 选择 定 将 为 您 的 旅程 增 添 无数 的 赏 心 乐 事
47 应有尽有 的 丰富 选择 定 将 为 您 的 旅程 增添 无 数 的 赏 心 乐事
49 应有尽有 的 丰富 选择 定 将 为 您 的 旅程 增添 无数 的 赏 心 乐事
```

The number on the left (aka **`mini-square score`**) is allocated to each sequence. It is calculated using the summation of the square of the length of each segment. This novel scoring is based on the preference for larger chunks than smaller chunks in a sentence:
> `\sum { len({ segment) }^{ 2 } }`