
from nltk.translate.bleu_score import sentence_bleu, corpus_bleu
import jieba
import numpy as np
import argparse

parser = argparse.ArgumentParser(description='Get differences in pronoun prediction')
parser.add_argument('--lang',  type=str, help='language to evaluate')
parser.add_argument('--translations', type=str, help='file to parse for translations')
args = parser.parse_args()

lang = args.lang
filename = args.translations



with open(filename, "r") as f:
    predictions = []
    for line in f.readlines():
        predictions.append(line.strip())

with open('experiments/prons/prons.'+lang, "r") as f:
    prons = [line.strip() for line in f.readlines()]
    reflexives, fem, masc = prons[0], prons[1], prons[2]



male_cand = []
female_cand = []

if lang == "zh":
    for i in range(len(predictions)):
        if (i+1) % 2 == 0:
            curs_f = []
            for  token in jieba.tokenize(predictions[i]):
                curs_f.append(token[0])
            female_cand.append(" ".join(curs_f))

        else:
            curs_m = []
            for  token in jieba.tokenize(predictions[i]):
                curs_m.append(token[0])
            male_cand.append(" ".join(curs_m))

else:
    for i in range(len(predictions)):
        if (i+1) % 2 == 0:
            female_cand.append(predictions[i])
        else:
            male_cand.append(predictions[i])



print(len(female_cand), len(male_cand))


count_male = 0
count_female = 0

#looking at differences in prediction of reflexives
if lang == "zh":
    for item in male_cand:
        if "自己" in item:
            count_male += 1

    for item in female_cand:
        if "自己" in item:
            count_female += 1


elif lang == "ru":
    for item in male_cand:
        if "св" in item:
            for ref in reflexives.split(","):
                if ref in item:
                    count_male += 1
                    break

    for item in female_cand:
        if "св" in item:
            for ref in reflexives.split(","):
                if ref in item:
                    count_female += 1
                    break
else:
    for item in male_cand:
        for ref in reflexives.split(","):
            if " "+ref+" " in item:
                count_male += 1
                #print(ref)
                break

    for item in female_cand:
        for ref in reflexives.split(","):
            if " "+ref+" " in item:
                count_female += 1
                #print(ref)


print("Reflexives predicted for masculine source (ratio): ", count_male / len(male_cand))
print("Reflexives predicted for feminine source (ratio): ", count_female / len(female_cand))
