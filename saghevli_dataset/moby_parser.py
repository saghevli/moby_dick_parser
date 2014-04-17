import re

def main():
    keyword = raw_input("What word to search for? ")
    keyword = keyword.lower()
    chapter = 0
    wordcount = {}
    #line = raw_input()
    try :
        mbfile = open("moby_dick.txt")
        for line in mbfile :
            found = False
            cleanLine = re.sub('[-.,;!?&$()/"]', '', line)
            words = cleanLine.split(' ')
            if words[0] == "CHAPTER" :
                chapter += 1
                wordcount[chapter] = 0
            for word in words:
                if word.lower() == keyword :
                    found = True
                    wordcount[chapter] += 1
            if found:
                print "Ch. " + str(chapter) + ": " + line
            #line = raw_input()
        
    except EOFError :
        print "end of file"
    #except Exception as e:
     #   print "Error: " + str(e)
   
    total = 0
    for chapter, count in wordcount.items():
        total += count
        print str(chapter) + "|" + ('#' * count)

    print "Total matches: " + str(total)
    mbfile.close()

if __name__ == "__main__":
        main()
