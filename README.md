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
* ensemble.py -> the evaluation script (accuracy, precision, recall, f-score). It can be used for ReLocaR and SemEval evaluation (see internal comments). Both, the ensemble approach and single model results will be calculated, see output.
* create_input.py -> the preprocessing script used for taking TEXT files and outputting the pickled files for LSTM.py. There are ready pickled files in the /pickle/ directory (for replication) so feel free to create new input from new text.
* create_baseline.py - > another preprocessing script for TEXT to PICKLED input. See internal comments for details of use.
* LSTM_test.py -> The MAIN script for training the classifier. Please check the paths to input files (choose from /pickle/ or prepare your own with the create....py scripts) and RUN :-) To get the EXACT numbers, you may have to adjust the number of epochs in training.
* LSTM_train.py -> The MAIN script for testing the classifier with the trained/saved weights. The output of the clasifier is saved in either /semeval/ or /relocar/. This is then used as input to ensemble.py to produce evaluation metrics.
* /ReLocaR/ -> this folder contains the RAW xml files. There is the ReLocaR.xml for testing and ReLocaR-T.xml for training. Processed versions of both of these files are available for easy replication in the /pickle/ folder.
* /gold/ -> The gold standard used for evaluation, no need to change.
* /data/ -> this directory contains text data from four different datasets (relocar, semeval, conll, wikipedia). 
* /pickle/ -> this directory holds the input files (already processed with our methods) ready to be plugged into the neural networks.
* /weights/ -> this directory stores the neural network trained weights
---
