# Comparing Texts Using Similarity Scores
import re
import string
from math import sqrt
from math import pow
treasure = {}
paradise = {}
filelist = ['treasure island.txt', 'paradise lost.txt']
stopfile = open('stop.txt','r')
stop_list = stopfile.readlines()
stopfile.close()
phraseform = re.compile(r'^[a-z]+ [a-z ]+$')
for filename in filelist:
    in_text = open(filename, 'r')
    in_text_string = in_text.read()
    in_text.close()
    in_text_string = in_text_string.replace('\n',' ')
    for stopword in stop_list:
        stopword = str.rstrip(stopword)
        in_text_string = re.sub(r' *\b' + stopword + r'\b *','\n',in_text_string)
    in_text_string = re.sub(r'[\,\:\;\(\)]','\n',in_text_string)
    in_text_string = re.sub(r'[\.\!\?] +(?=[A-Z])', '\n',in_text_string)
    in_text_string = str.lower(in_text_string)
    item_list = re.split(r' *\n *', in_text_string)
    for phrase in item_list:
        phrase = re.sub(r' +',' ' , phrase)
        phrase = str.strip(phrase)
        phrasematch = phraseform.match(phrase)
        if not (phrasematch):
            continue
        if (filename == 'paradise lost.txt'):
            if phrase in paradise:
                paradise[phrase] = paradise[phrase] + 1
            else:
                paradise[phrase] = 1
            if phrase not in treasure:
                treasure[phrase] = 0
        if (filename == 'treasure island.txt'):
            if phrase in treasure:
                treasure[phrase] = treasure[phrase] + 1
            else:
                treasure[phrase] = 1
            if phrase not in paradise:
                paradise[phrase] = 0
count = 0; sumtally1 = 0; sumtally2 = 0; sqtally1 = 0; sqtally2 = 0
prodtally12 = 0; part1 = 0; part2 = 0; part3 = 0;
keylist = paradise.keys()
print('keys ',keylist)
for key in keylist:
    count = count + 1;
    print('Inside the loop ',count)
    sumtally1 = sumtally1 + paradise[key]
    sumtally2 = sumtally2 + treasure[key]
    sqtally1 = sqtally1 + pow(paradise[key],2)
    sqtally2 = sqtally2 + pow(treasure[key],2)
    prodtally12 = prodtally12 + (paradise[key] * treasure[key])
print('outside the loop ',count)
part1 = prodtally12 - (float(sumtally1 * sumtally2) / count)
part2 = sqtally1 - (float(pow(sumtally1,2)) / count)
part3 = sqtally2 - (float(pow(sumtally2,2)) / count)
similarity12 = float(part1) / float(sqrt(part2 * part3))
print('The Pearson score is', similarity12)