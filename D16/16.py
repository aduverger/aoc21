from functools import reduce
import operator


def decode(BIN):
    version = int("".join(BIN[:3]), 2)
    BIN[:] = BIN[3:]
    packet_type = int("".join(BIN[:3]), 2)
    BIN[:] = BIN[3:]
    if packet_type == 4:  # packet is a litteral value
        number = []
        number_len = 0
        while BIN[0] == "1":
            number += BIN[1:5]
            BIN[:] = BIN[5:]
            number_len += 4
        number += BIN[1:5]  # last four bits
        BIN[:] = BIN[5:]
        number = int("".join(number), 2)
        return (version, packet_type, number)
    else:  # packet is an operator
        packets = []
        length_type = BIN[0]
        BIN[:] = BIN[1:]
        if length_type == "0":
            len_subpackets = int("".join(BIN[:15]), 2)
            BIN[:] = BIN[15:]
            subpackets = BIN[:len_subpackets]
            BIN[:] = BIN[len_subpackets:]
            while subpackets:
                packets.append(decode(subpackets))
        else:
            n_subpackets = int("".join(BIN[:11]), 2)
            BIN[:] = BIN[11:]
            for subpacket in range(n_subpackets):
                packets.append(decode(BIN))
        return (version, packet_type, packets)


def get_versions_sum(decoded_bin):
    version = decoded_bin[0]
    packet_type = decoded_bin[1]
    if packet_type == 4:
        return version
    else:
        packets = decoded_bin[2]
        for packet in packets:
            version += get_versions_sum(packet)
        return version


def get_value(decoded_bin):
    packet_type = decoded_bin[1]
    if packet_type == 4:
        number = decoded_bin[2]
        return number
    else:
        packets = decoded_bin[2]
        if len(packets) == 1:  # if there is only 1 subpacket
            return get_value(packets[0])
        elif packet_type == 0:
            return sum(map(get_value, packets))
        elif packet_type == 1:
            return reduce(operator.mul, (map(get_value, packets)), 1)
        elif packet_type == 2:
            return min(map(get_value, packets))
        elif packet_type == 3:
            return max(map(get_value, packets))
        elif packet_type == 5:
            return 1 if get_value(packets[0]) > get_value(packets[1]) else 0
        elif packet_type == 6:
            return 1 if get_value(packets[0]) < get_value(packets[1]) else 0
        elif packet_type == 7:
            return 1 if get_value(packets[0]) == get_value(packets[1]) else 0


HEX = open("16.txt").read().strip()

BIN = [bin(int(h, 16))[2:].zfill(4) for h in HEX]
BIN = list("".join(b for b in BIN))
print(f"P1 : {get_versions_sum(decode(BIN))}")

BIN = [bin(int(h, 16))[2:].zfill(4) for h in HEX]
BIN = list("".join(b for b in BIN))
print(f"P2 : {get_value(decode(BIN))}")
