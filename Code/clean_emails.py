import re
#from nltk.stem.wordnet import WordNetLemmatizer
from string import punctuation

ham_files = "regular-00"
spam_files = "spam-00"
testing_ham_files = "regular-10"
testing_spam_files = "spam-10"
files_types = ".msg"
write_files_types = ".txt"
training_spam_email_count = 68
training_ham_email_count = 26
testing_spam_email_count = 68
testing_ham_email_count = 26
stopWordsFile = "H:\\PDM\\stopWords.txt"
htmlWordsFile = "H:\\PDM\\htmlWords.txt"

def clean_emails(corpus, corpus_size, fileCode):

    for i in range(corpus_size-1):

        email_words = get_email(i+1, corpus, fileCode)
        #process _email_words
        email_words = email_words.lower()
        email_words = email_words.replace('.', '')
        email_words = email_words.replace(',', '')
        email_words = email_words.replace('?', '')
        email_words = email_words.replace('0', '')
        email_words = email_words.replace('1', '')
        email_words = email_words.replace('2', '')
        email_words = email_words.replace('3', '')
        email_words = email_words.replace('4', '')
        email_words = email_words.replace('5', '')
        email_words = email_words.replace('6', '')
        email_words = email_words.replace('7', '')
        email_words = email_words.replace('8', '')
        email_words = email_words.replace('9', '')
        email_words = email_words.replace('_', '')
        email_words = email_words.replace(' this ', ' ')
        email_words = email_words.replace('$', ' ')
        email_words = email_words.replace('@', ' ')
        email_words = email_words.replace('!', ' ')
        email_words = email_words.replace(' very ', ' ')
        email_words = email_words.replace(' here ', ' ')
        email_words = email_words.replace(' even ', ' ')
        email_words = email_words.replace(' from ', ' ')
        email_words = email_words.replace(' them ', ' ')
        email_words = email_words.replace(' then ', ' ')
        email_words = email_words.replace(' than ', ' ')
        email_words = email_words.replace(' this ', ' ')
        email_words = email_words.replace(' that ', ' ')
        email_words = email_words.replace(' though ', ' ')
        email_words = email_words.replace(' is ', ' ')
        email_words = email_words.replace(' the ', ' ')
        email_words = email_words.replace(' on ', ' ')
        email_words = email_words.replace(' in ', ' ')
        email_words = email_words.replace(' it ', ' ')
        email_words = email_words.replace(' of ', ' ')
        email_words = email_words.replace(' to ', ' ')
        email_words = email_words.replace(' were ', ' ')
        email_words = email_words.replace(' was ', ' ')
        email_words = email_words.replace(' but ', ' ')
        email_words = email_words.replace(' are ', ' ')
        email_words = email_words.replace(' and ', ' ')
        email_words = email_words.replace(' am ', ' ')
        email_words = email_words.replace(' so ', ' ')
        email_words = email_words.replace(' too ', ' ')
        email_words = email_words.replace(' my ', ' ')
        email_words = email_words.replace(' your ', ' ')
        email_words = email_words.replace(' yours ', ' ')
        email_words = email_words.replace(' his ', ' ')
        email_words = email_words.replace(' her ', ' ')
        email_words = email_words.replace(' him ', ' ')
        email_words = email_words.replace(' he ', ' ')
        email_words = email_words.replace(' she ', ' ')
        email_words = email_words.replace(' we ', ' ')
        email_words = email_words.replace(' they ', ' ')
        email_words = email_words.replace(' them ', ' ')
        email_words = email_words.replace(' how ', ' ')
        email_words = email_words.replace(' you ', ' ')
        email_words = email_words.replace(' i ', ' ')
        email_words = email_words.replace(' a ', ' ')
        email_words = email_words.replace(' has ', ' ')
        email_words = email_words.replace(' may ', ' ')
        email_words = email_words.replace(' you ', ' ')
        email_words = email_words.replace(' also ', ' ')
        email_words = email_words.replace(' after ', ' ')
        email_words = email_words.replace(' have ', ' ')
        email_words = email_words.replace(' an ', ' ')
        email_words = email_words.replace(' all ', ' ')
        email_words = email_words.replace(' as ', ' ')
        email_words = email_words.replace(' not ', ' ')
        email_words = email_words.replace(' our ', ' ')
        email_words = email_words.replace(' us ', ' ')
        email_words = email_words.replace(' will ', ' ')
        email_words = email_words.replace(' which ', ' ')
        email_words = email_words.replace(' none ', ' ')
        email_words = strip_tags(email_words)
        email_words = strip_stop_words(email_words)
        email_words = strip_html(email_words)

        # lmtzr = WordNetLemmatizer()

        #for j in range(len(_email_words)):

          #  _email_words[j] = lmtzr.lemmatize(_email_words[j])

        write_stripped_email(i+1, corpus, email_words, fileCode)

def get_email(file_count, corpus, fileCode):
    
    email_path = corpus + "\\" + fileCode;
          
    if(file_count >=1 and file_count <= 9):
        email_path = email_path + "0" + str(file_count)
    else:
        email_path = email_path + str(file_count)
              
    email_path = email_path + files_types    
    f = open(email_path, 'rb')
    email = f.readlines()
    f.close()
    
    email_words = ""

    for line in email:
        email_words = email_words + line
     
    return email_words   

def strip_stop_words(words):

    f = open(stopWordsFile, 'r')
    stop_words = f.readlines()
    f.close()

    for w in stop_words:
        words = words.replace(' ' + w.strip() + ' ', ' ')

    return words

def strip_html(words):

    f = open(htmlWordsFile, 'r')
    html_words = f.readlines()
    f.close()

    for w in html_words:
        words = words.replace(w.strip(), ' ')

    return words
    
def strip_tags(value):
    "Return the given HTML with all tags stripped."
    return re.sub(r'<[^>]*?>', ' ', value) 

def write_stripped_email(file_count, corpus, words, fileCode):

    email_path = corpus + "\\" + fileCode;

    if(file_count >=1 and file_count <= 9):
        email_path = email_path + "0" + str(file_count)
    else:
        email_path = email_path + str(file_count)
              
    email_path = email_path + write_files_types

    f = open(email_path, 'w')
    f.writelines(words)
    f.close()

clean_emails("H:\\PDM\\SpamFilter\\spam-filter\\test\\spam", testing_spam_email_count, testing_spam_files)
clean_emails("H:\\PDM\\SpamFilter\\spam-filter\\test\\regular", testing_ham_email_count, testing_ham_files)
