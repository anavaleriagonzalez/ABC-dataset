Repository for Antireflexive Bias Challenge Dataset presented in "Type B Reflexivization as an Unambiguous Testbed for Multilingual Multi-Task Gender Bias"

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


<h3> Coreference Resolution</h3>

<h3> Natural Language Inference </h3>
