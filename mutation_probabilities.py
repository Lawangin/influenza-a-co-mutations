data = []
with open('newyork_records.txt', 'r') as reader:
    for line in reader:
        if line[0] == 'M':
            data.append(line.strip())


def get_freq(d):
    freq_per_seq = []
    freq = {}
    for seq in range(len(d)):
        for resi in range(len(d[0])):
            if d[seq][resi] in freq:
                freq[d[seq][resi]] += 1
            else:
                freq[d[seq][resi]] = 1
        print(freq)
        freq_per_seq.append(freq)
        freq ={}
    return freq_per_seq


get_freq(data)
# print(get_freq(data))