#!/bin/bash

source ~/anaconda3/etc/profile.d/conda.sh
eval $(conda deactivate)
eval $(conda activate normal-drawfee-pics-bot)

python main.py
