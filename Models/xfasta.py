from Models import xpersistency


def create_position(start, end):
    return [start, end]


# Aligns the sequence with the reference sequence and returns the data [position, reference, sequence]
def align(sequence, positions):
    reference = get_rcrs_sequence()
    data = list()
    start = 1
    end = 0
    for position in positions:
        end += position[1] - position[0] + 1
        print(str(position[0]) + " - " + str(position[1])) # Prints the start and end of the reference
        ref = get_position(reference, position[0], position[1])
        print(str(start) + " - " + str(end))  # Prints the start and end of the sequence
        seq = get_position(sequence, start, end)
        start = end + 1
        data.append([position[0], ref, seq])
    return data


def polymorphism(data):
    polymorphisms = list()
    for variant in data:
        position = variant[0]
        reference = variant[1]
        sequence = variant[2]
        index = 0
        for base in reference:
            if base != sequence[index]:  # If finds a polymorphism add it to the array
                polymorphisms.append(position + index)
            else:
                pass
            index += 1
    return polymorphisms


def get_rcrs_sequence():
    index = 0
    sequence_string = ""
    for line in xpersistency.read_nolines("Utils/rcrs.fasta"):
        if index == 0:
            index += 1
            continue
        else:
            sequence_string += line
    return sequence_string


def get_position(sequence, start, end):
    start -= 1
    print("\n" + sequence[start:end])
    return sequence[start:end]


def get_header(fasta_format):
    return fasta_format[0]

def get_variant_id(data):
    labels = list()
    var = ""
    for variant in data:
        for char in variant[0]:
            if char == ">":
                continue
            elif char == " ":
                labels.append(var)
                var = ""
                break
            else:
                var += char
    return labels

def get_sequences(data):
    sequences = list()
    for variant in data:
        sequences.append(variant[1])
    return sequences

def fasta_to_dictionary(data):
    labels = get_variant_id(data)
    secuence = get_sequences(data)
    return dict(zip(labels, secuence))
