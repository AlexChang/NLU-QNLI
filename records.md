# QNLI - Records

* qnli_1
    * base model
    * batch 32
    * epoch 3
    * dev eval 91.36%
    * test 90.8%

* qnli_2
    * large model
    * batch 32
    * epoch 3
    * dev eval 91.93%
    * test 92.1%
  
* **structure mod**
    * merge train and dev
    
* qnli_3
    * large model
    * batch 32
    * epoch 5
    * train+dev
    * dev eval 49.46%

* qnli_4
    * large model
    * batch 32
    * epoch 3
    * train+dev
    * dev eval 99.87%
    * test 92.2%
  
* qnli_5(same as qnli_3)
    * large model
    * batch 32
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

* qnli_7
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
    * dev eval 91.80%
    * test 91.3%

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
    * dev eval 91.93%
    * test 91.9%

* qnli_10
    * large model
    * batch 40
    * epoch 3
    * tensorboard result
    * dev eval 91.56%
    * test 91.0%
    
* qnli_11(rerun qnli_2)
    * large model
    * batch 32
    * epoch 3
    * tensorboard result
    * dev eval 91.54%
    * test 91.9%

* qnli_12
    * large model
    * batch 40
    * epoch 4
    * **warmup_proportion 0.075**
    * tensorboard result
    * dev eval 92.40%
    * test 91.8%
    
* qnli_13(rerun qnli_2, torch 0.4.1)
    * large model
    * batch 32
    * epoch 3
    * dev eval 91.94%
    * test 91.6%

* qnli_ensemble_1(2,4,11,12)
    * test 92.7%
    
* qnli_14
    * large model
    * batch 32
    * epoch 5
    * tensorboard result
    * dev eval 91.81%
    * test 91.4%