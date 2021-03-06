<h3>Antireflexive Bias Challenge Dataset</h3>
 Data presented in "Type B Reflexivization as an Unambiguous Testbed for Multilingual Multi-Task Gender Bias"

This paper has been accepted at EMNLP 2020

Please refer to the paper for data generation details. Below are some instructions on how to run the scripts provided in this repo

<h3>LM: Perplexity scores</h3>
Getting perplexity scores for each language

`python experiments/LM/lm.py  --lang da --filename data/COREF_LM/coref_lm.da --data ABC`
`python experiments/LM/lm.py  --lang sv --filename data/COREF_LM/coref_lm.sv --data ABC`
`python experiments/LM/lm.py  --lang zh --filename data/COREF_LM/coref_lm.zh --data ABC`
`python experiments/LM/lm.py  --lang ru --filename data/COREF_LM/coref_lm.ru --data ABC`

or run `run_perpl.sh`

the output file will have the format:

<i>sentence</i>.  male: <i>loss perplexity</i> fem: <i>loss perplexity</i> ref: <i>loss perplexity</i>

outputs are dumped at
`outputs/lm/`

Getting perplexity scores for some benchmark dataset (no gender data)
`python experiments/LM/lm.py  --lang da --filename "benchmark_data.txt" --data benchmark`

<h3>Machine Translation</h3>

For the machine translation results in our paper we use the pretrained models for Russian and Chinese found here: http://data.statmt.org/wmt17_systems/  as well as google translate.

The input for our experiments is the English data found in `data/MT/source.en`. We evaluate based on the prediction of anti-reflexives versus gendered possessive pronouns. The script for this is in `experiments/MT/evaluate_translation.py`

To compute the differences in the prediction of anti-reflexives versus gendered possessive pronouns for masculine and feminine pronouns run:

`python experiments/MT/evaluate_translation.py --lang sv --translations outputs/mt/preds_google.sv`
`python experiments/MT/evaluate_translation.py --lang da --translations outputs/mt/preds_google.da`
`python experiments/MT/evaluate_translation.py --lang ru --translations outputs/mt/preds_google.ru`
`python experiments/MT/evaluate_translation.py --lang zh --translations outputs/mt/preds_google.zh`

or run `get_diff_mt.sh`

note for chinese we did not find significant results.

<h3> Coreference Resolution</h3>

We trained the model found here: https://github.com/mandarjoshi90/coref
For Chinese, we used the Chinese subset of Ontonotes5 (https://catalog.ldc.upenn.edu/LDC2013T19)
For Russian, we used http://rucoref.maimbava.net/. Note This dataset is very small and we did not find significant results.

The outputs for both languages are found in `outputs/coref`


<h3> Natural Language Inference </h3>
Preprocess the NLI files to get evaluation files in the correct format by running:

`python experiments/NLI/preprocess_nli.py`

To reproduce the results in the paper, follow the instructions https://github.com/facebookresearch/XLM
For ru and zh, we used the 15-language model with the following hyperparameters:

 ``--model_path models/mlm_tlm_xnli15_1024.pth  
 --n_epochs 35
 --max_vocab 95000
 --batch_size 4
 --epoch_size 20000
 --optimizer_e adam,lr=0.000005
 --optimizer_p adam,lr=0.000005  
 --finetune_layers "0:_1"``

 for da and sv, we used the 100-language model with the following hyperparameters

  ``--model_path models/mlm_100_1280.pth
  --n_epochs 28
  --max_vocab 200000
  --batch_size 4
  --epoch_size 20000
  --optimizer_e adam,lr=0.000005
  --optimizer_p adam,lr=0.000005  
  --finetune_layers "0:_1"``
