# NLU-QNLI

Natural Language Understanding - Question Natural Language Inference

## Setup

The following setup instructions are mainly for the Linux platform.

1. Create a virtual environment for **Python 3(>= 3.5)** and activate it

    ```
    virtualenv -p /usr/bin/python3 nluEnv   #(in Ubuntu 16.04)
    source nluEnv/bin/activate
    ```
 
2. Install the following dependency libraries with 

    ```
    pip install -r requirements.txt
    ```

3. Select the corresponding PyTorch [installation](https://pytorch.org/get-started/locally/) command and execute it according to the Python version and CUDA version you have. For example, our experimental platform is Python 3.5.2 and CUDA 9.0.176 (Ubuntu16.04), so we can simply execute the following command

    ```
    pip install torch
    ```

4. Place vocab file (in txt format) and pre-trained model file(in tar.gz format) under directory ```./pytorch_pretrained_bert```. Download links are as follows:

    * For 'bert-base-uncased':
        * Model: https://s3.amazonaws.com/models.huggingface.co/bert/bert-base-uncased.tar.gz
        * Vocab: https://s3.amazonaws.com/models.huggingface.co/bert/bert-base-uncased-vocab.txt
        
    * For 'bert-large-uncased':
        * Model: https://s3.amazonaws.com/models.huggingface.co/bert/bert-large-uncased.tar.gz
        * Vocab: https://s3.amazonaws.com/models.huggingface.co/bert/bert-large-uncased-vocab.txt
        
5. Place vocab file (in txt format) and fine-tuned model files(```config.json``` and ```pytorch_model.bin```) under directory ```./out/qnli```. Download links are as follows:
    
    * For submission 'qnli_4' (**large** model):
        * Model & Vocab: https://pan.baidu.com/s/152OXQ1jQeWdS5C7xjMBYEQ
        * Extraction code: 0tv3
        
    * For submission 'qnli_2' (**large** model):
        * Model & Vocab: https://pan.baidu.com/s/15jmiVnNwF7Oxa1Ez98KfQQ 
        * Extraction code: 8x88 
        
    * For submission 'qnli_1' (**base** model):
        * Model & Vocab: https://pan.baidu.com/s/1v0mCJqAghQ5p813BH6LwGQ 
        * Extraction code: dm76 
    
6. Run the following command to evaluate the **large** fine-tuned model. To get the prediction result of the test set, replace ```--do_eval``` with ```--do_test```.

    ```
    python run_classifier.py \
      --bert_model=bert-large-uncased \
      --do_lower_case \
      --do_eval \
      --data_dir=./data/QNLI \
      --cache_dir=./pytorch_pretrained_bert \
      --output_dir=./out/qnli
    ```

7. Run the following command to fine tune a new **large** model.

    ```
    python run_classifier.py \
      --bert_model=bert-large-uncased \
      --do_lower_case \
      --do_train \
      --do_eval \
      --do_test \
      --train_batch_size=32 \
      --num_train_epochs=3.0 \
      --warmup_proportion=0.1 \
      --data_dir=./data/QNLI \
      --cache_dir=./pytorch_pretrained_bert \
      --output_dir=./out/qnli_new
    ```


## Project structure

* run_classifier.py