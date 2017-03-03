## Vancouver Welcomes You! Minimalist Location Metonymy Resolution

Welcome to the home of the code and data accompanying the publication.

---
## Python libraries requirements
* keras - www.keras.io
* nltk - www.nltk.org
* spacy - www.spacy.io

## How to replicate
* ensemble.py -> the evaluation script (accuracy, precision, recall, f-score). It can be used for ReLocaR and SemEval evaluation (see internal comments). Both, the ensemble approach and single model results will be calculated, see output.
* create_input.py -> the preprocessing script used for taking TEXT files and outputting the pickled files for LSTM.py. There are ready pickled files in the /pickle/ directory (for replication) so feel free to create new input from new text.
* create_baseline.py - > another preprocessing script for TEXT to PICKLED input. See internal comments for details of use.
* LSTM_test.py -> 
