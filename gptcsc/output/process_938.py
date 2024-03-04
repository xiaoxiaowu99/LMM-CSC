label_path = 'data_by_ours_938.txt'
predict_path = 'data_by_ours_938_zeroshot_output.txt'
output_path = 'data_by_ours_938_zeroshot_reslut.txt'
lost_data_path = '937_lost_data.txt'
human_data_path = 'human_eval.txt'
label_list = {}
predict_list = {}
lost_data_list = {}

with open(label_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    i = 1
    for line in lines:
        if i % 2 == 1:
            id = line
            id = id.replace('\n', '', 1)
        if i % 2 == 0:
            label = line
            label = label.replace('\n', '', 1)
            label_data = {id: label}
            label_list.update(label_data)
        i = i + 1

with open(predict_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    i = 1
    for line in lines:
        if i % 2 == 1:
            id = line
            id = id.replace('\n', '', 1)
        if i % 2 == 0:
            predict = line
            predict = predict.replace('\n', '', 1)
            predict_data = {id: predict}
            predict_list.update(predict_data)
        i = i + 1

# for id in label_list:
    # if id in predict_list:
    #     label = label_list[id]
    #     predict = predict_list[id]
    #     with open(output_path, 'a', encoding='utf-8') as writer:
    #         writer.write('id:' + id)
    #         writer.write('\n')
    #         writer.write('pre:' + predict)
    #         writer.write('\n')
    #         writer.write('lab:' + label)
    #         writer.write('\n')
    # if id not in predict_list:
    #     with open(lost_data_path, 'a', encoding='utf-8') as writer:
    #         writer.write(id)
    #         writer.write('\n')
    #         writer.write(label_list[id])
    #         writer.write('\n')


#  human_eval
with open(human_data_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    i = 1
    T = 0
    F = 0
    wrong_data = []
    for line in lines:
        if i % 2 == 1:
            id = line
            id = id.replace('\n', '', 1)
        if i % 2 == 0:
            predict = line
            if int(predict[0]) == 1:
                T = T + 1
            if int(predict[0]) == 0:
                wrong_data.append(predict)
                F = F + 1
                print(id)
                print(label_list[id])
                print(predict)
        i = i + 1
        if i == 1002:
            break
    print(T)
    print(F)