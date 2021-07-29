"""#
#   Utilities.py -- class  has commonly used functions, such as for math calculation, words and list of lists processing
#
"""#

import string

class Utilities():

    def square_root(self, x):
        return round(math.sqrt(sum([a*a for a in x])),3)

    def cosine_similarity(self, x,y):
        numerator = sum(a*b for a,b in zip(x,y))
        denominator = square_root(x)*square_root(y)
        return round(numerator/float(denominator),3)

    def remove_punctuations(self, s):
        punctuation_set = set(string.punctuation)
        for punct in set(s).intersection(punctuation_set):
            s = s.replace(punct, '')
        return s

    def lists_to_string(self, ls):
        s = ""
        for l in ls:
            sc = ' '.join(str(c) for c in l)
            s += " " + sc
        return s

    def write_matrix_to_file(self, outfile, matrix, title):
        outfile.write("\n\n"+title+"\n\n")
        outfile.write(matrix.to_string(header=True, index=True))
        outfile.write("\n\n")
