# Vancouver Welcomes You! 
# Minimalist Location Metonymy Resolution

Welcome to the home of the code and data accompanying the publication. The talk took place on 2.8.2017 in Vancouver, Canada, you can view my personal video recording here https://www.youtube.com/watch?v=LwGWyxRCtwY&t=33s

---
## Python libraries requirements
* keras 1.2.2 - www.keras.io (for best replicability, go for Theano backend, not Tensorflow)
* spacy - www.spacy.io and also download the English embeddings as instructed on the website

## Embeddings
To fully replicate the results and due to GitHub's file size limits (100MB today), you need to download the GloVe embeddings and save in a local directory. Go to http://nlp.stanford.edu/projects/glove/ and change the PATH to the embeddings in the LSTM\_(Train/Test).py files. Please use the 50D embeddings for publication results unless you want to experiment with bigger dimensions. The final file size is around 175MB. You can also Google the DOI of our paper for the complete set of data.

## How to replicate
I fixed some random seeds, however, due to the complexity of Keras/Theano, there is still some random initiation happening, so please do multiple runs and take the average.
* _ensemble.py_ -> this is the ensemble method evaluation script (accuracy, precision, recall, f-score). It can be used for ReLocaR and SemEval evaluation (see internal comments for usage instructions). Both the ensemble approach and single model results will be calculated, see output.
* _create_prewin.py_ -> this is the preprocessing script used for taking TEXT files and outputting the processed pickled files for LSTM_train(and test).py. For replication purposes, this script applies the __PREWIN__ method to text, see paper. There are ready pickled files in the /pickle/ directory (for replication) but feel free to create new input from new text.
* _create_baseline.py_ - > another preprocessing script for TEXT to PICKLED input (for replication purposes, use this script for ALL __baselines__ in the paper). See internal comments for details of usage.
* _LSTM_Train.py_ -> The MAIN script for training the classifier. Please check the paths to input files (choose from /pickle/ or prepare your own with the create....py scripts), edit path to embeddings file and RUN :-) To get the EXACT numbers as reported in the paper, you may have to adjust the number of epochs in training (± 1).
* _LSTM_Test.py_ -> The MAIN script for testing the classifier with the trained/saved weights. The output of the clasifier is saved (please uncomment code first) in either /semeval/ or /relocar/ folders. This is then used as input to ensemble.py to produce evaluation metrics. Please see internal comments for details.
* _ReLocaR_XML/_ -> this folder contains the RAW xml files (one of the paper contributions). There is the ReLocaR_Test.xml for __testing__ and ReLocaR_Train.xml for __training__. Processed versions of both of these files are available for easy replication in the /pickle/ folder.
* _gold/_ -> The gold standard results used for evaluation, no need to change.
* _data/_ -> this directory contains text data from four different datasets (relocar, semeval, conll, wikipedia). Feel free to dabble and add new files, however, for replication purposes, these have already been processed and sit inside the /pickle/ folder.
* _data/locations.txt_ -> This is the list of locations used to construct ReLocaR as mentioned in the publication.
* _pickle/_ -> this directory holds the input files (already processed with our methods such as PREWIN and BASELINE) ready to be plugged into the neural networks. The naming scheme should be selfexplanatory (famous last words). Get in touch if unclear.
* _weights/_ -> this directory stores the neural network trained weights. No need to change or modify.

---
### Issues during replication
Have fun and thanks for stopping by my friend. I tried to make the replication efforts as smooth as possible. I take science replication extremely seriously. In case something is missing, please raise an [issue](https://github.com/milangritta/Minimalist-Location-Metonymy-Resolution/issues) or email me (not difficult to find) and I will address the feedback. Enjoy!
