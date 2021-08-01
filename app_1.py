import gradio as gr
import nltk
from autocorrect import Speller
from gensim.summarization import summarize as g_sumn
import sys
import re
import PySimpleGUI as sg

'''
https://github.com/gradio-app/gradio
'''

# 1
def nlp(text,operation):
    if operation == 'Lower Case':
       return text.lower()
    if operation == 'Sent Tokenize':
        sent_tokenize = nltk.sent_tokenize(text)
        result = {
        # remove str() if you want the output as list
        "result": str(sent_tokenize)
        }
        result = {str(key): value for key, value in result.items()}
        return result['result']
    if operation == 'Word Tokenize':
        word_tokenize = nltk.word_tokenize(text)
        result = {
            "result": str(word_tokenize)  # remove str() if you want the output as list
        }
        result = {str(key): value for key, value in result.items()}
        return result['result']
    if operation == 'Lemmatize':
        from nltk.stem import WordNetLemmatizer
        wordnet_lemmatizer = WordNetLemmatizer()

        word_tokens = nltk.word_tokenize(text)
        lemmatized_word = [wordnet_lemmatizer.lemmatize(word) for word in
                           word_tokens]
        result = {
            "result": " ".join(lemmatized_word)
        }
        result = {str(key): value for key, value in result.items()}
        return result['result']
    if operation == 'Stemming':
        from nltk.stem import WordNetLemmatizer
        wordnet_lemmatizer = WordNetLemmatizer()

        word_tokens = nltk.word_tokenize(text)
        lemmatized_word = [wordnet_lemmatizer.lemmatize(word) for word in
                           word_tokens]
        result = {
            "result": " ".join(lemmatized_word)
        }
        result = {str(key): value for key, value in result.items()}
        return result['result']
    if operation == 'Remove Numbers':
        remove_num = ''.join(c for c in text if not c.isdigit())
        result = {
            "result": remove_num
        }
        result = {str(key): value for key, value in result.items()}
        return result['result']
    if operation == 'Remove Punctuation':
        from string import punctuation
        def strip_punctuation(s):
            return ''.join(c for c in s if c not in punctuation)

        text = strip_punctuation(text)
        result = {
            "result": text
        }
        result = {str(key): value for key, value in result.items()}
        return result['result']
    if operation == 'Spell Check':
        spell = Speller(lang='en')
        spells = [spell(w) for w in (nltk.word_tokenize(text))]
        result = {
            "result": " ".join(spells)
        }
        result = {str(key): value for key, value in result.items()}
        return result['result']
    if operation == 'Remove Stopwords':
        from nltk.corpus import stopwords
        stopword = stopwords.words('english')
        word_tokens = nltk.word_tokenize(text)
        removing_stopwords = [word for word in word_tokens if word not in stopword]
        result = {
            "result": " ".join(removing_stopwords)
        }
        result = {str(key): value for key, value in result.items()}
        return result['result']
    if operation == 'Keyword':
        word = nltk.word_tokenize(text)
        pos_tag = nltk.pos_tag(word)
        chunk = nltk.ne_chunk(pos_tag)
        NE = [" ".join(w for w, t in ele) for ele in chunk if isinstance(ele, nltk.Tree)]
        result = {
            "result": NE
        }
        result = {str(key): value for key, value in result.items()}
        return result['result'][0]
    if operation == 'Summarize':
        sent = nltk.sent_tokenize(text)
        if len(sent) < 2:
            summary1 = "please pass more than 3 sentences to summarize the text"
        else:
            summary = g_sumn(text)
            summ = nltk.sent_tokenize(summary)
            summary1 = (" ".join(summ[:2]))
        result = {
            "result": summary1
        }
        result = {str(key): value for key, value in result.items()}
        return result['result']
    if operation == 'Remove Tags':
        import re
        cleaned_text = re.sub('<[^<]+?>', '', text)
        result = {
            "result": cleaned_text
        }
        result = {str(key): value for key, value in result.items()}
        res = re.sub(' +', ' ', result['result'])
        return res


iface = gr.Interface(nlp,["text",gr.inputs.Radio(['Lower Case',
                                                  'Lemmatize',
                                                  'Summarize',
                                                  'Stemming',
                                                  'Keyword',
                                                  'Spell Check',
                                                  'Remove Tags',
                                                  'Sent Tokenize',
                                                  'Word Tokenize',
                                                  'Remove Punctuation',
                                                  'Remove Numbers',
                                                  'Remove Stopwords',
                                                  ])],"text")

iface.launch()