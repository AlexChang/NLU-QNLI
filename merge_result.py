import os
from zipfile import ZipFile

def to_zip(output_path, zip_file_name='submission', sample_path='./cbow/'):
    sample_file_names = os.listdir(sample_path)
    if 'QNLI.tsv' in sample_file_names:
        sample_file_names.remove('QNLI.tsv')

    if not zip_file_name.endswith('.zip'):
        zip_file_name += '.zip'
    with ZipFile(os.path.join(output_path, zip_file_name), 'w') as myzip:
        for sample_file_name in sample_file_names:
            myzip.write(os.path.join(sample_path, sample_file_name), sample_file_name)
        myzip.write(os.path.join(output_path, 'QNLI.tsv'), 'QNLI.tsv')

results = []
for dirpath, dirnames, filenames in os.walk('./result'):
    if filenames:
        f = open(os.path.join(dirpath, filenames[0]), 'r')
        result = f.readlines()
        result = result[1:]
        results.append(result)

new_result = ['index\tprediction\n']
for line_idx in range(len(results[0])):
    new_result_line = "{}\t".format(line_idx)
    old_result_count = {}
    for result in results:
        old_result = result[line_idx].split('\t')[-1]
        if old_result in old_result_count:
            old_result_count[old_result] += 1
        else:
            old_result_count[old_result] = 1
    old_result_sorted = sorted(old_result_count.items(), key=lambda x:x[1], reverse=True)
    new_result_line += old_result_sorted[0][0]
    new_result.append(new_result_line)

merged_path = './merged'
if not os.path.exists(merged_path):
    os.mkdir(merged_path)
predict_output_file = os.path.join(merged_path, "QNLI.tsv")
with open(predict_output_file, "w") as writer:
    writer.writelines(new_result)

to_zip(merged_path)

