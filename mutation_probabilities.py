import numpy as np
data = []
with open('newyork_records_2003.txt', 'r') as reader:
    for line in reader:
        if line[0] == 'M':
            data.append(line.strip())


def get_freq(d):
    matrix = np.array(d)
    freq_per_seq = []

    freq_matrix = {}
    for seq in range(len(d[0])):
        res = [sub[seq] for sub in d]
        for i in res:
            if i in freq_matrix:
                freq_matrix[i] += 1
            else:
                freq_matrix[i] = 1
        freq_per_seq.append(freq_matrix)
        freq_matrix = {}
    return freq_per_seq


def get_prob(freq):
    mutations = []
    for i in range(len(freq)):
        if len(freq[i]) > 1:
            freq_values = freq[i].values()
            highest_n = max(freq[i].values())
            den = 90
            num = 0
            for n in freq_values:
                if n != highest_n:
                    num += n
            probability = num/den

            mutations.append({'location': i, 'mutation': freq[i], 'probability': probability})
    return mutations


freq = get_freq(data)
prob = get_prob(freq)
# get_prob(freq)

co_mut = []
for j in range(len(prob)):
    control = prob[j]['probability']
    for i in range(len(prob)):
        if j != i:
            if prob[i]['probability'] == control:
                co_mut.append([prob[j], prob[i]])

# print(prob)
# print(co_mut)
print(len(prob))
print(len(co_mut))