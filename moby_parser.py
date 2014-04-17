import re
from nltk.stem.wordnet import WordNetLemmatizer
import numpy as np
import matplotlib.pyplot as plt
import sys

colors = ['y', 'r', 'b']
chaps = 135

def main():
    lmtzr = WordNetLemmatizer()
    keywords = []
    if (len(sys.argv) == 1 or len(sys.argv) > 4):
        print "Usage: " + sys.argv[0] + " <up to 3 search words>"
    for i in range(1, len(sys.argv)):
        keywords.append(lmtzr.lemmatize(sys.argv[i].lower()))

    chapter = 0
    #list of lists
    wordcount = []
    for i in range(0, len(keywords)):
        wordcount.append([0] * 135)

    try :
        mbfile = open("moby_dick.txt")
        for line in mbfile :
            found = False
            cleanLine = re.sub('[-.,;!?&$()/"]', '', line)
            words = cleanLine.split(' ')
            if words[0] == "CHAPTER" :
                chapter += 1

            for word in words:
                try:
                    i = keywords.index(lmtzr.lemmatize(word.lower()))
                    wordcount[i][chapter] += 1
                    found = True
                except Exception:
                    pass
            if found:
                print "Ch. " + str(chapter) + ": " + line

    except EOFError :
        print "end of file"
    #except Exception as e:
     #   print "Error: " + str(e)

    total = 0
    # for chapter, count in wordcount.items():
    for i in range(0, len(keywords)):
        for j in range(0, chapter):
            total += wordcount[i][j]
            print str(j+1) + "|" + ('#' * wordcount[i][j])

    print "Total matches: " + str(total)
    mbfile.close()

    graph(wordcount, keywords)

def graph(wordcount, keywords):
    chap_labels = []
    for i in range(0, chaps):
        chap_labels.append(i+1)
    N = chaps

    ind = np.arange(N)  # the x locations for the groups
    width = 0.3       # the width of the bars

    fig, ax = plt.subplots()
    rects = []
    for i in range(0, len(wordcount)):
        rects.append(ax.bar(ind + i*width, wordcount[i], width, color=colors[i]));

    ax.set_ylabel('# Occurrences')
    ax.set_xlabel('Chapter')
    ax.set_title('Moby Dick Word Frequencies')
    # ax.set_xticks(ind+width)
    # ax.set_xticklabels( chap_labels )

    # ax.legend( (rects1[0], rects2[0]), ('Men', 'Women') )
    if len(keywords) == 1:
        ax.legend(rects[0], keywords)
    if len(keywords) == 2:
        ax.legend((rects[0][0], rects[1][0]), (keywords[0], keywords[1]))
    if len(keywords) == 3:
        ax.legend((rects[0][0], rects[1][0], rects[2][0]), (keywords[0], keywords[1], keywords[2]))
    plt.show()

if __name__ == "__main__":
        main()
