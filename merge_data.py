import os
import codecs

def main():
    origin_data_path = './data/QNLI/'
    revised_data_path = './data/QNLI_r/'
    if not os.path.exists(revised_data_path):
        os.mkdir(revised_data_path)

    train_tsv_file= codecs.open(os.path.join(origin_data_path, 'train.tsv'), 'r', encoding='utf-8')
    train_tsv = train_tsv_file.readlines()
    train_tsv_file.close()
    # print(train_tsv[-1])
    last_id = int(train_tsv[-1].split('\t')[0])
    # print(last_id)
    print('train lines: {}'.format(len(train_tsv)))

    dev_tsv_file = codecs.open(os.path.join(origin_data_path, 'dev.tsv'), 'r', encoding='utf-8')
    dev_tsv = dev_tsv_file.readlines()
    dev_tsv_file.close()
    print('dev lines: {}'.format(len(dev_tsv)))

    new_train_tsv = train_tsv.copy()
    next_id = last_id + 1
    for line in dev_tsv[1:]:
        line_split = line.split('\t')
        line_split[0] = str(next_id)
        next_id += 1
        new_line = '\t'.join(line_split)
        new_train_tsv.append(new_line)

    print('new lines: {}'.format(len(new_train_tsv)))
    new_train_tsv_file = codecs.open(os.path.join(revised_data_path, 'train.tsv'), 'w', encoding='utf-8')
    new_train_tsv_file.writelines(new_train_tsv)
    new_train_tsv_file.close()
    return

if __name__ == '__main__':
    main()