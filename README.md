# Vancouver Welcomes You! 
# Minimalist Location Metonymy Resolution

Welcome to the home of the code and data accompanying the publication.

---
## Python libraries requirements
* keras - www.keras.io
* nltk - www.nltk.org
* spacy - www.spacy.io

## Embeddings
To fully replicate the results, you need to download the GloVe embeddings and save in a local directory. Go to http://nlp.stanford.edu/projects/glove/ and change the PATH to the embeddings in the LSTM(train/test).py files.

## How to replicate
* ensemble.py -> this is the evaluation script (accuracy, precision, recall, f-score). It can be used for ReLocaR and SemEval evaluation (see internal comments for usage instructions). Both, the ensemble approach and single model results will be calculated, see output.
* create_input.py -> this is the preprocessing script used for taking TEXT files and outputting the processed pickled files for LSTM_train(and test).py. For replication purposes, this script applies the PREWIN method to text, see paper. There are ready pickled files in the /pickle/ directory (for replication) but feel free to create new input from new text.
* create_baseline.py - > another preprocessing script for TEXT to PICKLED input (for replication purposes, use this script for ALL baseslines in the paper). See internal comments for details of usage.
* LSTM_test.py -> The MAIN script for training the classifier. Please check the paths to input files (choose from /pickle/ or prepare your own with the create....py scripts), edit path to embeddings file and RUN :-) To get the EXACT numbers as reported in the paper, you may have to adjust the number of epochs in training (± 1).
* LSTM_train.py -> The MAIN script for testing the classifier with the trained/saved weights. The output of the clasifier is saved (please uncomment code first) in either /semeval/ or /relocar/ folders. This is then used as input to ensemble.py to produce evaluation metrics. Please see internal comments for details.
* /ReLocaR/ -> this folder contains the RAW xml files (one of the paper contributions). There is the ReLocaR.xml for __testing__ and ReLocaR-T.xml for __training__. Processed versions of both of these files are available for easy replication in the /pickle/ folder.
* /gold/ -> The gold standard results used for evaluation, no need to change.
* /data/ -> this directory contains text data from four different datasets (relocar, semeval, conll, wikipedia). Feel free to dabble and add new files, however, for replication purposes, these have already been processed and sit inside the /pickle/ folder.
* /pickle/ -> this directory holds the input files (already processed with our methods such as PREWIN and BASELINE) ready to be plugged into the neural networks. The naming scheme should be selfexplanatory (famous last words). Get in touch if unclear.
* /weights/ -> this directory stores the neural network trained weights. No need to change or modify.

---
Have fun and thanks for stopping by. In case something is missing, please raise an issue here: https://github.com/milangritta/Minimalist-Location-Metonymy-Resolution/issues and I will address the feedback.
