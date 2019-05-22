python run_classifier.py \
  --task_name=QNLI \
  --bert_model=bert-base-uncased \
  --do_lower_case \
  --do_train \
  --do_eval \
  --data_dir=./data/QNLI \
  --max_seq_length=128 \
  --train_batch_size=32 \
  --learning_rate=2e-5 \
  --num_train_epochs=3.0 \
  --cache_dir=./pytorch_pretrained_bert \
  --output_dir=./out
  
python run_classifier.py --task_name=QNLI --bert_model=bert-base-uncased --do_lower_case --do_eval --data_dir=./data/QNLI --max_seq_length=128 --train_batch_size=32 --learning_rate=2e-5 --num_train_epochs=3.0 --cache_dir=C:\Users\zfmed\Desktop\NLU-QNLI\pytorch_pretrained_bert --output_dir=./out