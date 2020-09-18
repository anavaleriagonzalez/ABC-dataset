#!/bin/bash

ontonotes_path=$1
data_dir=$2

dlx() {
  wget  $1/$2
  echo $1/$2
  mv $2 data/conll
  tar -xvzf data/conll/$2

}
'''
conll_url=http://conll.cemantix.org/2012/download
dlx $conll_url conll-2012-train.v4.tar.gz
dlx $conll_url conll-2012-development.v4.tar.gz
dlx $conll_url/test conll-2012-test-key.tar.gz
dlx $conll_url/test conll-2012-test-official.v9.tar.gz

dlx $conll_url conll-2012-scripts.v3.tar.gz
dlx http://conll.cemantix.org/download reference-coreference-scorers.v8.01.tar.gz
'''

bash conll-2012/v3/scripts/skeleton2conll.sh -D /home/fcm220/ontonotes-release-5.0/data/files/data conll-2012

function compile_partition() {
    rm -f $2.$5.$3$4
    cat $data_dir/conll-2012/$3/data/$1/data/$5/annotations/*/*/*/*.$3$4 >> $data_dir/$2.$5.$3$4
}

function compile_language() {
    compile_partition development dev v4 _gold_conll $1
    compile_partition train train v4 _gold_conll $1
    compile_partition test test v4 _gold_conll $1
}

#compile_language english
compile_language chinese
#compile_language arabic

vocab_file=data/chinese_L-12_H-768_A-12/vocab.txt
python minimize.py $vocab_file $data_dir $data_dir false
