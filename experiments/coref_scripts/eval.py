import json
import argparse

parser = argparse.ArgumentParser(description='Get differences in pronoun prediction')
parser.add_argument('--lang',  type=str, help='language to evaluate')
parser.add_argument('--coref_output', type=str, help='file to parse for translations')
args = parser.parse_args()

lang = args.lang
filename = args.coref_output


#with open("occupations_chi.txt", "r") as f:
#    gold =[line.strip() for line in f.readlines() ]
with open('experiments/prons/prons.'+lang, "r") as f:
    prons = [line.strip() for line in f.readlines()]
    reflexives, fem, masc = prons[0].lower(), prons[1].lower(), prons[2].lower()


p = open(filename, "r")
preds = []
for line in p.readlines():
    preds.append(json.loads(line.strip()))
p.close()

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

chunk_preds = list(chunks(preds, 3))
ref = 0
male = 0
fem = 0

chosen = []
true = []

for pred in chunk_preds:
    ref_pred = pred[0]
    male_pred = pred[1]
    fem_pred = pred[2]


    #cluster true
    true.append(1)
    true.append(0)
    true.append(0)

    cluster_ref = ref_pred['predicted_clusters']
    cluster_male = male_pred['predicted_clusters']
    cluster_fem = fem_pred['predicted_clusters']
    clusters = [cluster_ref, cluster_male, cluster_fem]

    #predicted a cluster
    for cluster in clusters:

        if cluster != []:
            chosen.append(1)
        else:
            chosen.append(0)


    for i, cluster in enumerate(clusters):
        if i == 0:

            if cluster != []:
                ref+=1
        elif i==1:
            if cluster != []:
                male+=1
        else:

            if cluster != []:
                fem+=1

print("Hallucinating clusters...")
print("male: ", (male/len(chunk_preds))*100, "% of the time")
print("female: ", (fem/len(chunk_preds))*100, "% of the time")
