# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    new_file = open(filename, "r")
    read_file = new_file.read()

    new_file.close() 
    return read_file



#function to count the words in the file
def count_words(str):
    text = read_file_content(str)
    # [assignment] Add your code here
    
    def counter(str):
        wordcount = dict()
        words = str.split()

        for word in words:
            if word in wordcount:
                wordcount[word] += 1

            else:
                wordcount[word] = 1

        return (wordcount)       
    return(counter(text))

print(count_words("story.txt"))
