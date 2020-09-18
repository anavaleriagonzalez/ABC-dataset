#!/bin/bash

python experiments/MT/evaluate_translation.py --lang sv --translations outputs/mt/preds_google.sv
python experiments/MT/evaluate_translation.py --lang da --translations outputs/mt/preds_google.da
python experiments/MT/evaluate_translation.py --lang ru --translations outputs/mt/preds_google.ru
python experiments/MT/evaluate_translation.py --lang zh --translations outputs/mt/preds_google.zh
