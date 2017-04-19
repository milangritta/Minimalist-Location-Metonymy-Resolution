import codecs
from os import listdir
import itertools

final = []
semeval = False  # TRUE if evaluating SEMEVAL files, FALSE for RELOCAR files.
for r in range(1, 4):
    directory = "./semeval/" if semeval else "./relocar/"
    for names in itertools.combinations(listdir(directory), r=r):
        files = []
        for f in names:
            f_results = []
            for line in codecs.open(directory + f, mode="r", encoding="utf-8"):
                f_results.append(float(line))
            files.append(f_results)

        all_predictions = []
        for prediction in range(len(files[0])):
            current_p = []
            for index in range(len(files)):
                current_p.append(files[index][prediction])
            if semeval:
                p = 1 if current_p.count(1) > current_p.count(0) else 0
            else:
                p = 1 if sum(current_p) > len(current_p) / 2.0 else 0
            all_predictions.append(p)

        correct = 0
        gold_file = "sem" if semeval else "rel"
        gold_file = codecs.open("./gold/gold_" + gold_file + ".txt", mode="r", encoding="utf-8")
        for line, p in zip(gold_file, all_predictions):
            if int(line) == p:
                correct += 1
        final.append((float(correct) / len(all_predictions), str(names), all_predictions))
final = sorted(final, key=lambda (x, y, z): x, reverse=True)
for res in final[:]:
    print('Processing:' + res[1], "Accuracy:", res[0])

# --------------------------- Precision and recall ----------------------------------#
met_count = 187 if semeval else 514
tp, fp = 0.0, 0.0
for index in range(met_count):
    if final[0][2][index] == 1:
        tp += 1
fn = met_count - tp
for prediction in final[0][2][met_count:]:
    if prediction == 1:
        fp += 1
precision = tp / (tp + fp)
recall = tp / (tp + fn)
print("Precision:", precision)
print("Recall:", recall)
print("F Score:", 2 * precision * recall / (precision + recall))

tp, fp = 0.0, 0.0
prediction_count = len(final[0][2])
for index in range(met_count, prediction_count):
    if final[0][2][index] == 0:
        tp += 1
fn = prediction_count - met_count - tp
for prediction in final[0][2][:met_count]:
    if prediction == 0:
        fp += 1
precision = tp / (tp + fp)
recall = tp / (tp + fn)
print("Precision:", precision)
print("Recall:", recall)
print("F Score:", 2 * precision * recall / (precision + recall))
