#-------------------------------------------------------------------------------#
# Name:        anagram
# Purpose:
#
# Author:      Shivankur Kapoor
#
# Created:
# Copyright:   (c) Shivankur Kapoor
# Licence:     <your licence>
#-------------------------------------------------------------------------------#

import sys
import os
import collections
import re
import math
import glob



stopwords = ['secondly', 'all', 'consider', 'whoever', 'results', 'four', 'edu', 'go', 'mill', 'evermore', 'causes', 'seemed', 'rd', 'certainly', 'biol', 'system', "when's", 'vs', 'ts', 'to', 'asking', 'present', 'th', 'under', 'sorry', 'promptly', "a's", 'mug', 'sent', 'outside', 'far', 'mg', 'every', 'yourselves', "we'll", 'went', 'did', 'forth', "they've", 'fewer', 'hereafter', 'try', 'p', 'thereupon', 'round', 'added', "it'll", "i'll", 'someday', 'approximately', 'says', "you'd", 'ten', 'yourself', 'd', 'past', 'likely', 'invention', 'notwithstanding', 'further', 'shows', 'even', 'index', 'what', 'appear', 'giving', 'section', 'brief', 'run', 'goes', 'sup', 'new', 'poorly', 'ever', 'thin', 'full', "c'mon", 'whose', 'youd', 'respectively', 'sincere', 'never', 'here', 'himse\xe2\x80\x9d', 'let', 'others', 'along', 'fifteen', 'suggest', 'obtained', 'ref', 'ahead', 'k', 'allows', 'proud', 'amount', "i'd", 'resulting', 'howbeit', 'usually', 'whereupon', "i'm", 'makes', 'thereto', 'thats', 'hither', 'via', 'followed', 'merely', 'while', 'till', 'ninety', 'vols', 'viz', 'ord', 'readily', 'everybody', 'use', 'from', 'would', 'contains', 'two', 'next', 'few', 'call', 'therefore', 'taken', 'themselves', 'thru', 'tell', 'more', 'knows', 'becomes', 'hereby', 'herein', 'particular', 'known', "who'll", 'must', 'me', 'none', 'thanks', 'f', 'this', 'ml', 'oh', 'anywhere', 'nine', 'can', 'mr', 'following', 'my', 'example', 'indicated', 'give', 'neverf', 'states', 'indicates', 'something', 'want', 'arise', 'information', 'needs', 'end', 'thing', 'rather', 'meanwhile', 'id', 'how', 'low', "'ve", 'instead', 'de', 'okay', 'tried', 'may', 'stop', 'after', 'eighty', 'different', 'hereupon', 'whilst', 'ff', 'date', 'such', 'undoing', 'a', 'thered', 'third', 'whenever', 'maybe', 'appreciate', 'q', 'ones', 'so', 'specifying', 'allow', 'keeps', "that's", 'thirty', 'six', 'help', 'indeed', 'over', 'move', 'mainly', 'soon', 'course', 'through', 'looks', 'fify', 'still', 'its', 'refs', 'before', 'thank', "he's", 'selves', 'inward', 'fix', 'actually', 'better', 'whether', 'willing', 'whole', 'thanx', 'ours', 'might', "haven't", 'versus', 'then', 'non', 'someone', 'somebody', 'thereby', 'auth', 'underneath', "you've", 'they', 'half', 'now', 'nos', 'several', 'name', 'always', 'reasonably', 'whither', "she's", 'sufficiently', 'each', 'found', 'entirely', 'mean', 'everyone', 'directly', 'doing', 'ed', 'eg', 'related', 'tip', 'owing', 'ex', 'substantially', 'et', 'beyond', 'couldnt', 'out', 'by', 'them', "needn't", 'furthermore', 'since', 'forty', 'research', 'looking', 're', 'seriously', "shouldn't", "they'll", 'got', 'cause', "one's", "you're", 'million', 'given', 'quite', "what'll", 'que', 'besides', 'x', 'ask', 'anyhow', 'beginning', 'backwards', 'g', 'could', 'hes', 'put', 'tries', 'keep', 'caption', 'w', 'ltd', 'hence', 'onto', 'think', 'first', 'myse\xe2\x80\x9d', 'already', 'seeming', 'omitted', 'thereafter', 'thereof', 'awfully', 'done', 'adopted', 'another', 'thick', 'miss', "doesn't", 'little', 'necessarily', 'their', 'together', 'top', 'accordingly', 'least', 'anyone', 'indicate', 'too', 'hundred', 'gives', 'mostly', 'that', 'nobody', 'took', 'immediate', 'resulted', 'regards', 'somewhat', 'off', 'believe', 'herself', 'than', "here's", 'begins', 'b', 'unfortunately', 'showed', 'accordance', 'gotten', 'second', 'i', 'r', 'amid', 'toward', 'minus', 'are', 'and', 'youre', 'ran', 'thoughh', 'alongside', 'beforehand', 'mine', 'say', 'unlikely', 'have', 'need', 'seen', 'seem', 'saw', 'any', 'relatively', 'zero', 'thoroughly', 'latter', 'downwards', 'aside', 'thorough', 'predominantly', 'also', 'take', 'which', 'begin', 'exactly', 'unless', 'opposite', 'who', "where's", 'most', 'eight', 'but', 'significant', 'why', 'sub', 'forever', 'kg', 'especially', 'noone', 'later', 'm', 'amoungst', 'mrs', 'heres', "you'll", 'definitely', 'neverless', 'effect', 'normally', 'came', 'saying', 'particularly', 'show', 'anyway', 'page', 'ending', "that'll", 'find', 'fifth', 'one', 'specifically', 'keys', "daren't", 'behind', 'should', 'only', 'going', 'specify', 'announce', 'itd', "there've", 'do', 'his', 'above', 'get', 'between', 'overall', 'truly', "they'd", 'hid', 'nearly', 'words', 'despite', 'during', 'him', 'regarding', 'qv', 'h', 'cry', 'state', 'twice', 'she', 'though', 'contain', "what've", 'where', 'greetings', 'ignored', 'km', 'theirs', 'up', 'namely', 'computer', 'sec', 'anyways', "that've", 'throug', 'no-one', 'best', 'wonder', 'said', "there'd", 'away', 'currently', 'please', 'ups', 'enough', "there's", 'various', 'hopefully', 'affecting', 'probably', 'neither', 'across', 'co.', 'available', 'we', 'recently', 'useful', 'importance', 'were', 'however', 'meantime', 'come', 'both', 'c', 'last', 'thou', 'many', 'taking', 'thence', 'according', 'against', 'etc', 's', 'became', 'com', 'otherwise', 'among', 'liked', 'co', 'afterwards', 'seems', 'ca', 'whatever', 'alone', 'moreover', 'throughout', 'considering', "he'd", 'pp', 'described', "it's", 'three', 'been', 'quickly', 'whom', "there're", 'much', 'wherein', 'interest', 'certain', 'whod', 'hardly', "it'd", 'wants', 'corresponding', 'fire', 'latterly', 'concerning', 'else', 'hers', 'former', 'those', 'myself', 'novel', 'look', 'unlike', 'these', 'means', 'bill', 'twenty', 'value', 'n', 'will', 'near', 'theres', 'seven', 'whereafter', 'almost', 'wherever', 'is', 'thus', 'it', 'itself', 'im', 'in', 'affected', 'ie', 'y', 'if', 'containing', 'anymore', 'perhaps', 'insofar', 'make', 'same', 'clearly', 'beside', 'when', 'potentially', 'widely', 'gets', 'fairly', 'used', 'slightly', 'see', 'somewhere', 'I', 'upon', 'herse\xe2\x80\x9d', 'uses', 'yours', "he'll", 'wheres', 'recent', 'lower', 'kept', 'whereby', 'largely', 'nevertheless', 'changes', 'nonetheless', 'well', 'anybody', 'obviously', 'without', 'comes', 'very', 'the', 'con', 'self', 'inc.', 'lest', 'things', 'world', "she'll", 'just', 'less', 'being', 'able', 'therere', 'presumably', 'front', 'farther', 'immediately', 'regardless', 'yes', 'yet', 'unto', 'wed', "we've", 'had', 'except', 'thousand', 'lets', 'has', 'adj', 'ought', 'gave', "t's", 'around', "who's", 'possible', 'usefully', 'possibly', 'whichever', 'five', 'know', 'similarly', 'using', 'part', "who'd", 'dare', 'apart', 'abst', 'nay', 'necessary', 'like', 'follows', 'noted', 'either', 'become', 'whomever', 'towards', 'therein', "why's", 'www', 'because', 'old', 'often', 'successfully', 'some', 'back', 'l', 'ah', 'sure', 'shes', 'specified', 'home', 'theyre', 'ourselves', 'happens', 'provided', 'vol', "there'll", 'for', 'bottom', 'affects', 'shall', 'per', 'everything', 'does', 'provides', 'tends', 't', 'be', 'sensible', 'obtain', 'nowhere', 'although', 'sixty', 'abroad', 'on', 'about', 'ok', 'anything', 'getting', 'of', 'v', 'o', 'side', 'whence', 'plus', 'act', 'consequently', 'or', 'seeing', 'own', 'whats', 'formerly', 'twelve', 'previously', 'somethan', 'into', 'within', 'shed', 'due', 'down', 'appropriate', 'right', 'primarily', 'theyd', "c's", 'whos', 'your', 'significantly', 'fill', "how's", 'her', 'eleven', 'aren', 'apparently', 'there', 'amidst', 'pages', 'hed', 'inasmuch', 'inner', 'way', 'forward', 'was', 'himself', 'elsewhere', "i've", 'becoming', 'amongst', 'somehow', 'hi', 'et-al', 'line', 'trying', 'with', 'he', 'usefulness', "they're", 'made', 'wish', 'inside', 'j', 'us', 'until', 'placed', 'below', 'un', 'whim', 'empty', 'z', 'similar', "we'd", 'strongly', 'gone', 'sometimes', 'associated', 'likewise', 'describe', 'am', 'itse\xe2\x80\x9d', 'an', 'as', 'sometime', 'at', 'our', 'inc', 'again', 'uucp', "'ll", 'no', 'na', 'whereas', 'nd', 'detail', 'lately', 'til', 'other', 'you', 'really', "what's", 'showns', 'briefly', 'beginnings', 'welcome', 'shown', "let's", 'ours ', 'important', 'serious', 'upwards', 'ago', 'e', "she'd", 'having', 'u', "we're", 'everywhere', 'backward', 'hello', 'once']
pattern = re.compile(r'\b(' + r'|'.join(stopwords) + r')\b\s*')

_list2 = {
              "ational": "ate",
              "tional": "tion",
              "enci": "ence",
              "anci": "ance",
              "izer": "ize",
              "bli": "ble",
              "alli": "al",
              "entli": "ent",
              "eli": "e",
              "ousli": "ous",
              "ization": "ize",
              "ation": "ate",
              "ator": "ate",
              "alism": "al",
              "iveness": "ive",
              "fulness": "ful",
              "ousness": "ous",
              "aliti": "al",
              "iviti": "ive",
              "biliti": "ble",
              "logi": "log",
              }

_list3 = {
              "icate": "ic",
              "ative": "",
              "alize": "al",
              "iciti": "ic",
              "ical": "ic",
              "ful": "",
              "ness": "",
}


def stem(w):

    _cons = "[^aeiou]"
    _vowel = "[aeiouy]"
    _cons_seq = "[^aeiouy]+"
    _vowel_seq = "[aeiou]+"

    # m > 0
    _mgr0 = re.compile("^(" + _cons_seq + ")?" + _vowel_seq + _cons_seq)
    # m == 0
    _meq1 = re.compile("^(" + _cons_seq + ")?" + _vowel_seq + _cons_seq + "(" + _vowel_seq + ")?$")
    # m > 1
    _mgr1 = re.compile("^(" + _cons_seq + ")?" + _vowel_seq + _cons_seq + _vowel_seq + _cons_seq)
    # vowel in stem
    _s_v = re.compile("^(" + _cons_seq + ")?" + _vowel)
    # ???
    _c_v = re.compile("^" + _cons_seq + _vowel + "[^aeiouwxy]$")

    # Patterns used in the rules

    _ed_ing = re.compile("^(.*)(ed|ing)$")
    _at_bl_iz = re.compile("(at|bl|iz)$")
    _step1b = re.compile("([^aeiouylsz])\\1$")
    _step2 = re.compile("^(.+?)(ational|tional|enci|anci|izer|bli|alli|entli|eli|ousli|ization|ation|ator|alism|iveness|fulness|ousness|aliti|iviti|biliti|logi)$")
    _step3 = re.compile("^(.+?)(icate|ative|alize|iciti|ical|ful|ness)$")
    _step4_1 = re.compile("^(.+?)(al|ance|ence|er|ic|able|ible|ant|ement|ment|ent|ou|ism|ate|iti|ous|ive|ize)$")
    _step4_2 = re.compile("^(.+?)(s|t)(ion)$")
    _step5 = re.compile("^(.+?)e$")



    if len(w) < 3:
        return w

    first_is_y = w[0] == "y"
    if first_is_y:
        w = "Y" + w[1:]

    # Step 1a
    if w.endswith("s"):
        if w.endswith("sses"):
            w = w[:-2]
        elif w.endswith("ies"):
            w = w[:-2]
        elif w[-2] != "s":
            w = w[:-1]

    # Step 1b

    if w.endswith("eed"):
        s = w[:-3]
        if _mgr0.match(s):
            w = w[:-1]
    else:
        m = _ed_ing.match(w)
        if m:
            stem = m.group(1)
            if _s_v.match(stem):
                w = stem
                if _at_bl_iz.match(w):
                    w += "e"
                elif _step1b.match(w):
                    w = w[:-1]
                elif _c_v.match(w):
                    w += "e"

    # Step 1c

    if w.endswith("y"):
        stem = w[:-1]
        if _s_v.match(stem):
            w = stem + "i"

    # Step 2

    m = _step2.match(w)
    if m:
        stem = m.group(1)
        suffix = m.group(2)
        if _mgr0.match(stem):
            w = stem + _list2[suffix]

    # Step 3

    m = _step3.match(w)
    if m:
        stem = m.group(1)
        suffix = m.group(2)
        if _mgr0.match(stem):
            w = stem + _list3[suffix]

    # Step 4

    m = _step4_1.match(w)
    if m:
        stem = m.group(1)
        if _mgr1.match(stem):
            w = stem
    else:
        m = _step4_2.match(w)
        if m:
            stem = m.group(1) + m.group(2)
            if _mgr1.match(stem):
                w = stem

    # Step 5

    m = _step5.match(w)
    if m:
        stem = m.group(1)
        if _mgr1.match(stem) or (_meq1.match(stem) and not _c_v.match(stem)):
            w = stem

    if w.endswith("ll") and _mgr1.match(w):
        w = w[:-1]

    if first_is_y:
        w = "y" + w[1:]

    return w

def classTo(val1,val2,val3,val4):
    if(val1>=val2 and val1>=val3 and val1>=val4):
        return "PosT"
    if(val2>=val1 and val2>=val3 and val2>=val4):
        return "PosD"
    if(val3>=val2 and val3>=val1 and val3>=val4):
        return "NegT"
    if(val4>=val2 and val4>=val3 and val4>=val1):
        return "NegD"

def classify(model, path):

    list = []
    val1 = 0
    val2 = 0
    val3 = 0
    val4 = 0
    with open(path) as fp:
        for line in fp:
            line = line.lower()
            line = pattern.sub('', line)
            t_list = re.findall(r'\b[^\W\d_]+\b', line)
            t_list = [i for i in t_list if len(i)>2]
            t_list = map(lambda x: stem(x), t_list)
            list = list + t_list

    for word in list:
        if word in model:
            dic = model[word]
            str = dic["PosT"].split("/")
            val1 += math.log(float(str[0])/float(str[1]))
            str = dic["PosD"].split("/")
            val2 += math.log(float(str[0])/float(str[1]))
            str = dic["NegT"].split("/")
            val3 += math.log(float(str[0])/float(str[1]))
            str = dic["NegD"].split("/")
            val4 += math.log(float(str[0])/float(str[1]))


    # val1 += math.log(16226.0/72638.0)
    # val2 += math.log(14024.0/72638.0)
    # val3 += math.log(21586.0/72638.0)
    # val4 += math.log(20802.0/72638.0)
    return classTo(val1,val2,val3,val4)


try :
    model = {}
    inputPath = sys.argv[1]
    filePath = "C:\\Users\\Shivankur Kapoor\\Desktop\\USC\\SEM 2\\NLP\\Assignment 2\\nbmodel.txt"
    fw = open('C:\\Users\\Shivankur Kapoor\\Desktop\\USC\\SEM 2\\NLP\\Assignment 2\\nboutput.txt','w')
    with open(filePath) as fp:
        for line in fp:
            line = line[:-1]
            list = line.split(",")
            dict = {}
            dict.clear()
            dict["PosT"] = list[1]
            dict["PosD"] = list[2]
            dict["NegT"] = list[3]
            dict["NegD"] = list[4]
            model[list[0]] = dict

    filePathList = []
    for root, dirs, files in os.walk(inputPath):
            for file in files:
                if file.endswith(".txt") and not file.endswith("Readme.txt") and not file.endswith("README.txt"):
                        filePathList.append(os.path.join(root, file))

    for i in filePathList:
      label = classify(model,i)
      if(label == "PosT"):
          fw.write("truthful positive "+i+"\n")
      elif(label == "PosD"):
          fw.write("deceptive positive "+i+"\n")
      elif(label == "NegT"):
          fw.write("truthful negative "+i+"\n")
      elif(label == "NegD"):
          fw.write("deceptive negative "+i+"\n")



except IOError:
    print "Error: can\'t find file or read data"
else:
    fp.close()
    fw.close()
    print "finished"