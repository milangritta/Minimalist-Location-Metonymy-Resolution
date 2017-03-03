import nltk
from lxml import etree as et

sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')


def serve_examples(test=True):
    if test:
        tree = et.parse("./data/countries.test.correct")
    else:
        tree = et.parse("./data/countries.train")
    root = tree.getroot()
    out, labels = [], []
    for node in root.findall("./sample"):
        node = node.find("./par")
        l = node.text.split("\n")[-1]
        if len(l) > 0:
            l = sent_detector.tokenize(l)[-1]
        annot = node.find("./annot")
        label = annot.find("./location").attrib['reading'][:3]
        entity = annot.find("./location").text.strip()
        r = annot.tail.split("\n")[0]
        if len(r) > 0:
            r = sent_detector.tokenize(r)[0]
        labels.append(label)
        out.append(entity + "<SEP>" + l.replace("[mdash]", "-").replace("[ndash]", "-")
                   + "<ENT>" + entity + "<ENT>" + r.replace("[mdash]", "-").replace("[ndash]", "-"))
    return out, labels


def score_examples(predictions, test=True):
    correct, total = 0, 0
    if test:
        tree = et.parse("../data/countries.test.correct")
    else:
        tree = et.parse("../data/countries.train")
    root = tree.getroot()
    for node, p in zip(root.findall("./sample/par"), predictions):
        total += 1
        annot = node.find("./annot")
        label = annot.find("./location").attrib['reading'][:3]
        if p == label:
            correct += 1
    print("Percentage Correct:", (1.0 * correct) / total)
