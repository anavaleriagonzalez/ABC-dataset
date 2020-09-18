
from nltk.translate.bleu_score import sentence_bleu, corpus_bleu
import jieba
import argparse

parser = argparse.ArgumentParser(description='Get differences in pronoun prediction')
parser.add_argument('--lang',  type=str, help='language to evaluate')
parser.add_argument('--translations', type=str, help='file to parse for translations')
parser.add_argument('--out', type=str, help='outfile')
args = parser.parse_args()

lang = args.lang
filename = args.translations
out = args.out

with open(filename, "r") as f:
    predictions = []
    for line in f.readlines():
        #predictions.append(line.strip())

        if lang == "zh":
            if line[0]!= "第" and line[2]!= "頁" and line[1].isdigit()==False and line[0].isdigit()==False and "聰明的" not in line:
                for l in line.strip().split("。") :
                    if l !='':
                        predictions.append(l)

        elif lang =="sv":
            if line[0:4]!= "Sida":
                for l in line.strip().split(".") :
                    if l !='':
                        predictions.append(l)

        elif lang =="ru":
            if "Страница"  not in line:
                for l in line.strip().split(".") :
                    if l !='':
                        predictions.append(l)
        elif lang=="da":
            if line[0:4]!= "Side":
                for l in line.strip().split(".") :
                    if l !='':
                        predictions.append(l)


with open(out, "w") as f:
    for item in predictions:
        f.write(item+"\n")
