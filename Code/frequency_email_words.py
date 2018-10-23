import orange
import count
import operator

ham_files = "regular-00"
spam_files = "spam-00"
files_types = ".txt"
HAM = 1
SPAM = 0
training_spam_email_count = 68
training_ham_email_count = 26
top = 400
top_words = [0 for x in range(top)] 
top_frequencies = [0 for x in range(top)] 

def get_most_frequent_words(corpus, corpus_flag):

    words = {}

    if(corpus_flag == HAM):
        corpus_size = training_ham_email_count
        file_code = ham_files
    elif(corpus_flag == SPAM):
        corpus_size = training_spam_email_count
        file_code = spam_files
    
    for i in range(corpus_size-1):

        filePath = get_email_path(i+1, corpus, file_code)
        #print(filePath)
        new = count.count(filePath)
        if(i+1 == 1):
           words.update(new)
        else:
            for n in new.keys():

                found_flag = 0
                
                for w in words.keys():

                    if(w == n):
                        words[w] = words.get(w) + new.get(w)
                        found_flag = 1
                        break
                    
                if(found_flag == 0):
                    words[n] = new.get(n)
                        
        #print(len(spam_words))
        
    words_sorted = sorted(words.iteritems(), key=operator.itemgetter(1))
    #print(spam_sorted)
              
    for j in range(top - 1):

        top_words[j] = words_sorted[-(j+1)][0]
        top_frequencies[j] = words_sorted[-(j+1)][1]

    print(top_words)
    print(top_frequencies)
    
                
def get_email_path(file_count, corpus, fileCode):
    
    email_path = corpus + "\\" + fileCode;
          
    if(file_count >=1 and file_count <= 9):
        email_path = email_path + "0" + str(file_count)
    else:
        email_path = email_path + str(file_count)
              
    email_path = email_path + files_types

    return email_path


get_most_frequent_words("J:\\PDM\\SpamFilter\\spam-filter\\train\\spam", 0)
print
print
print
print
get_most_frequent_words("J:\\PDM\\SpamFilter\\spam-filter\\train\\regular", 1)
