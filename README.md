# LEEN
Implementations of a model described in the following paper related to sequence matching:

- [LEEN: an novel bio-event normalization method based on calculating semantic similarity](https://arxiv.org/abs/1512.08849) by ×××

## Requirements
- [Torch7](https://github.com/torch/torch7) with specifying Lua 5.2 (otherwise you will meet [LuaJIT memory issue](https://github.com/OpenNMT/OpenNMT/issues/26))
- [nn](https://github.com/torch/nn)
- [nngraph](https://github.com/torch/nngraph)
- [optim](https://github.com/torch/optim)
- Python 3.5

## Datasets
- [The Stanford Natural Language Inference (SNLI) Corpus](http://nlp.stanford.edu/projects/snli/)

## Usage

1. To use our libary in your project, you have to clone our this project into your current working directory (presumbly named `MyProject`) . So if you haven't get Git, just install it with the following steps:
  * ```sudo apt-get update```
  * ```sudo apt-get install git```

2. To include our libary in your working project , ensure you have entered your project directory - in other words, be sure that you are working under directory `MyProject/` 

3. Clone the project from gitlab into your Project, you can either choose to Clone it with SSH or HTTPS:

* Clone with SSH
 ```git clone git@gitlab.com:BioAI/leen.git```
* Clone with HTTPS
 ```git clone https://gitlab.com/BioAI/leen.git```

4. After the steps above, you can use our library by simply `import` it, just using this statement:
```python
import leen.leen.test as le
```

5. Then you can use our provided functions, simply prefixing `le.` now, click [FunctionUsage](#FunctionUsage) for more function details.
```python
le.predict_sim("EBI-2625447",s1) # one usage example of predict_sim(str,str)
le.tran_stat("EBI-2638567") # one usage example of tran_stat(str)
```

## FunctionUsage
We have developed two functions for users as following:
* predict_sim(str *EBI-id*,str *description*)
	* a function judging whether an *EBI-id* correspond to a *description*，return True/False 
    * input:str *EBI-id*(the accession number of the interaction in the IntAct database),str *description*(a senctence describing an interaction)
	* output:bool *True/False*

* tran_stat(str *EBI-id*)
	* a fuction getting the *description* corresponding to an *EBI-id*
	* input:str *EBI-id*
	* return:str *description*

# Copyright
Copyright 2015 Singapore Management University (SMU). All Rights Reserved.
