import codecs

"""
This script will produce three evaluation files per language. 
One file will contain premises with feminine pronouns, the hypotheses and the label. 
"""

for lang in ['da', 'ru', 'zh', 'sv']:
    premise = codecs.open('../../data/NLI/nli_'+lang+'/premise.'+lang).read().split('\n---\n')
    premises = [s.split('\n') for s in premise]
    entailments = codecs.open('../../data/NLI/nli_'+lang+'/hyp.'+lang).read().split('\n---\n')
    assert len(entailments) == len(premises)

    outfilem = codecs.open('../../data/NLI/'+lang+'.challenge_m', 'w', 'utf-8')
    outfilef = codecs.open('../../data/NLI/'+lang+'.challenge_f', 'w', 'utf-8')
    outfilen = codecs.open('../../data/NLI/'+lang+'.challenge_n', 'w', 'utf-8')

    for i, sentgr in enumerate(premise):
        sentgr = [gr for gr in sentgr.split('\n') if len(gr) > 1]
        if len(sentgr) == 3:
            for idx, sent in enumerate(sentgr):
                if idx == 0:
                    outfilen.write(sent+'\t'+entailments[i].strip('\n')+'\t entailment\n')
                if idx == 1:
                    outfilem.write(sent+'\t'+entailments[i].strip('\n')+'\t entailment\n')
                if idx == 2:
                    outfilef.write(sent+'\t'+entailments[i].strip('\n')+'\t entailment\n')
    outfilef.close()
    outfilem.close()
    outfilen.close()