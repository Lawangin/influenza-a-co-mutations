data = []
with open('newyork_records.txt', 'r') as reader:
    for line in reader:
        if line[0] == 'M':
            data.append(line.strip())


def get_freq(d):
    freq_per_seq = []
    freq = {}
    for seq in range(len(d)):
    # for seq in range(3):
        for resi in range(len(d[0])):
        # for resi in range(3):
            if d[seq][resi] in freq:
                freq[d[seq][resi]] += 1
            else:
                freq[d[seq][resi]] = 1
        # print(freq)
        # freq_per_seq.append(freq)
        # freq ={}
    return freq



# get_freq(data)
print(get_freq(data))