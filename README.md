# LEEN
Implementations of a model described in the following paper related to sequence matching:

- [LEEN: an novel bio-event normalization method based on calculating semantic similarity](https://arxiv.org/abs/1512.08849) by ××(with link)

## Requirements
- [Torch7](https://github.com/torch/torch7) with specifying Lua 5.2 (otherwise you will meet [LuaJIT memory issue](https://github.com/OpenNMT/OpenNMT/issues/26))
- [nn](https://github.com/torch/nn)
- [nngraph](https://github.com/torch/nngraph)
- [optim](https://github.com/torch/optim)
- Python 3.5

## Datasets
- [The Stanford Natural Language Inference (SNLI) Corpus](http://nlp.stanford.edu/projects/snli/)

## Usage

1. To use our libary in your project, you have to clone our project into your project. If you haven't get Git, just install it with the following steps:
  * ```sudo apt-get update```
  * ```sudo apt-get install git```

2. To include our libary in your working project (presumbly named `MyProject`) , ensure you have accessed into your project directory - so be sure to `cd MyProject` 

3. Clone the project from gitlab into your Project, you can choose to Clone it either with SSH or HTTPS way:

* Clone with SSH
 ```git clone git@gitlab.com:BioAI/leen.git```
* Clone with HTTPS
 ```git clone https://gitlab.com/BioAI/leen.git```

4. After the steps above, you can use our library by import it, just using this statement:
```python
import leen.leen.test as le
```

5. You can use our provided functions with the prefix `le.` now, click [FunctionUsage](#FunctionUsage) for more details.
```python
le.tran_stat("EBI-2638567")
le.predict_sim("EBI-2625447",s1)
```

## FunctionUsage
* description(EBI-id)
	* a fuction getting the description corresponding to idcode
	* input:str EBI-id
	* return:str description

* same(EBI-id, sentence)
	* a function judging whether a EBI-id correspond to a description，return True/False 
    * input:str idcode,str sentence
	* output:bool True/False

## Copyright
Copyright 2015 Singapore Management University (SMU). All Rights Reserved.
