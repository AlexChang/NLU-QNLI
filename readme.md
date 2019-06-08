# QNLI

## Linux

python run_classifier.py \
  --bert_model=bert-large-uncased \
  --do_lower_case \
  --do_train \
  --do_eval \
  --do_test \
  --train_batch_size=24 \
  --num_train_epochs=4.0 \
  --warmup_proportion=0.075 \
  --data_dir=./data/QNLI \
  --cache_dir=./pytorch_pretrained_bert \
  --output_dir=./out/qnli_8
    
  
## Windows

python run_classifier.py --task_name=QNLI --bert_model=bert-base-uncased --do_lower_case --do_eval --data_dir=./data/QNLI --max_seq_length=128 --train_batch_size=32 --learning_rate=2e-5 --num_train_epochs=3.0 --cache_dir=C:\Users\zfmed\Desktop\NLU-QNLI\pytorch_pretrained_bert --output_dir=./out

## Records

* qnli_1
    * base model
    * epoch 3
    * dev eval 91.36%
    * test 90.8%

* qnli_2
    * large model
    * epoch 3
    * dev eval 91.93%
    * test 92.1%
  
* **structure mod**
    * merge train and dev
    
* qnli_3
    * large model
    * epoch 5
    * train+dev
    * dev eval 49.46%

* qnli_4
    * large model
    * epoch 3
    * train+dev
    * dev eval 99.87%
    * test 92.2%
  
* qnli_5(same as qnli_3)
    * large model
    * epoch 5
    * train+dev
    * dev eval 49.46%

* **structure mod**
    * clean up
    * add tensorboard

* qnli_6
    * large model
    * batch 24
    * epoch 5
    * dev eval 49.46%
    * tensorboard result(error format)

* **structure mod**
    * tensorboard format bug fix

* qnli_7(rerun qnli_2)
    * large model
    * batch 24
    * epoch 3
    * tensorboard result
    * dev eval 92.09%
    * test 91.6%
    
* **structure mod**
    * auto tensorboard log output dir
    * save best model
    * auto zip
    
* qnli_8
    * large model
    * batch 24
    * epoch 4
    * **warmup_proportion 0.075**
    * tensorboard result

* **structure mod**
    * test dataloader bug fix
    * auto zip bug fix
    * load model when necessary

* qnli_9
    * large model
    * batch 32
    * epoch 4
    * **warmup_proportion 0.075**
    * tensorboard result
