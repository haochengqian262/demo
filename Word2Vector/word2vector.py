import  sys
reload(sys)
sys.setdefaultencoding('utf-8')
import gensim,logging,multiprocessing,os,re

from pattern.en import tokenize
from time import time

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',
                    level=logging.INFO)

def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, ' ', raw_html)
    return cleantext

class MySentences(object):
    def __init__(self, dirname):
        self.dirname = dirname

    def __iter__(self):
        for root, dirs, files in os.walk(self.dirname):
            for filename in files:
                file_path = root + '/' + filenam
                for line in open(file_path):
                    sline = line.strip()
                    if sline == "":
                        continue
                    rline = cleanhtml(sline)
                    tokenized_line = ' '.join(tokenize(rline))
                    is_alpha_word_line = [word for word in
                                          tokenized_line.lower().split()
                                          if word.isalpha()]
                    yield is_alpha_word_line

if __name__ == '__main__':
    data_path = '/Users/mac/Documents/CODE/GraduateDesign/Word2Vector/data/ts.txt'
    begin = time()
    sentences = MySentences(data_path)
    model = gensim.models.Word2Vec(sentences,
                                   size=200,
                                   window=10,
                                   min_count=10,
                                   workers=multiprocessing.cpu_count())
    model.save("data/model/word2vec_gensim")
    model.wv.save_word2vec_format("data/model/word2vec_org",
                                  "data/model/vocabulary",
                                  binary=False)

    end = time()
    print "Total procesing time: %d seconds" % (end - begin)
