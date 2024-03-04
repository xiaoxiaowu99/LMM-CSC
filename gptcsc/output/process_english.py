
input_path = 'tran_data_en.txt'
output_path = 'train_en_data.txt'

with open(input_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    id = 1
    all_data = {}
    for line in lines:
        if line[0] == 'S':
            data = {id: line[2:]}
            all_data.update(data)
            id = id + 1

print(0)
for i in all_data:
    with open(output_path, 'a', encoding='utf-8') as writer:
        writer.write('id:' + str(i))
        writer.write('\n')
        writer.write('src:' + all_data[i])
