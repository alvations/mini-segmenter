# -*- coding: utf8 -*-
import minisegmenter as mini
import sys; reload(sys); sys.setdefaultencoding('utf8')
sentence = u"应有尽有的丰富选择定将为您的旅程增添无数的赏心乐事"
print mini.segmenter(sentence.decode('utf8'))
