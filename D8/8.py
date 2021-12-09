outputs = []
for line in open("8.in"):
    output = line.split("|")[1].strip().split(" ")
    for element in output:
        outputs.append(element)

lengths = [2, 4, 3, 7]
n_instances = 0
for output in outputs:
    if len(output) in lengths:
        n_instances += 1

print(f"P1: {n_instances}")


def sort_signal(signal):
    return "".join(sorted(signal))


inputs = []
outputs = []
for line in open("8.in"):
    input = line.split("|")[0].strip().split(" ")
    input = [sort_signal(signal) for signal in input]
    output = line.split("|")[1].strip().split(" ")
    output = [sort_signal(signal) for signal in output]
    inputs.append(input)
    outputs.append(output)


def find_trans(input):
    D = {}
    for signal in input:
        if len(signal) == 2:  # 1
            D[1] = signal
        elif len(signal) == 3:  # 7
            D[7] = signal
        elif len(signal) == 4:  # 4
            D[4] = signal
        elif len(signal) == 7:  # 8
            D[8] = signal
    for signal in input:
        if len(signal) == 6:
            if (D[1][0] in signal) != (D[1][1] in signal):  # 6
                D[6] = signal
            else:  # 9 or 0
                is_nine = True
                for c in D[4]:
                    if c not in signal:
                        is_nine = False
                if is_nine:  # 9
                    D[9] = signal
                else:  # 0
                    D[0] = signal
    for signal in input:
        if len(signal) == 5:
            if (D[1][0] in signal) and (D[1][1] in signal):  # 3
                D[3] = signal
            else:  # 2 or 5
                is_five = True
                for c in signal:
                    if c not in D[9]:
                        is_five = False
                if is_five:  # 5
                    D[5] = signal
                else:  # 2
                    D[2] = signal
    return {v: k for k, v in D.items()}


ans = 0
for n in range(len(inputs)):
    D = find_trans(inputs[n])
    number = ""
    for signal in outputs[n]:
        number = number + str(D[signal])
    ans += int(number)

print(f"P2: {ans}")
