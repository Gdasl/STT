import base64

"""
source: https://laconicwolf.com/2018/06/30/cryptopals-challenge-6-break-repeating-key-xor/
"""


def get_english_score(input_bytes):
    """Compares each input byte to a character frequency 
    chart and returns the score of a message based on the
    relative frequency the characters occur in the English
    language.
    """

    # From https://en.wikipedia.org/wiki/Letter_frequency
    # with the exception of ' ', which I estimated.
    character_frequencies = {
        'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
        'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
        'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
        'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
        'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
        'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
        'y': .01974, 'z': .00074, ' ': .13000
    }
    return sum([character_frequencies.get(chr(byte), 0) for byte in input_bytes.lower()])


def single_char_xor(input_bytes, char_value):
    """Returns the result of each byte being XOR'd with a single value.
    """
    output_bytes = b''
    for byte in input_bytes:
        output_bytes += bytes([byte ^ char_value])
    return output_bytes


def bruteforce_single_char_xor(ciphertext):
    """Performs a singlechar xor for each possible value(0,255), and
    assigns a score based on character frequency. Returns the result
    with the highest score.
    """
    potential_messages = []
    for key_value in range(256):
        message = single_char_xor(ciphertext, key_value)
        score = get_english_score(message)
        data = {
            'message': message,
            'score': score,
            'key': key_value
            }
        potential_messages.append(data)
    return sorted(potential_messages, key=lambda x: x['score'], reverse=True)[0]


def break_repeating_key_xor(ciphertext):
    """Attempts to break repeating-key XOR encryption.
    """
    average_distances = []

    # Take the keysize from suggested range 
    for keysize in range(2,41):

        # Initialize list to store Hamming distances for this keysize 
        distances = []

        # Break the ciphertext into chunks the length of the keysize
        chunks = [ciphertext[i:i+keysize] for i in range(0, len(ciphertext), keysize)]
        
        while True:
            try:
                # Take the two chunks at the beginning of the list and 
                # get the Hamming distance 
                chunk_1 = chunks[0]
                chunk_2 = chunks[1]
                distance = calculate_hamming_distance(chunk_1, chunk_2)

                # Normalize this result by dividing by KEYSIZE
                distances.append(distance/keysize)

                # Remove these chunks so when the loop starts over, the
                # Hamming distance for the next two chunks can be calculated
                del chunks[0]
                del chunks[1]

            # When an exception occurs (indicating all chunks have 
            # been processed) break out of the loop.
            except Exception as e:
                pass
        result = {
            'key': keysize,
            'avg distance': sum(distances) / len(distances)
            }
        average_distances.append(result)
    possible_key_lengths = sorted(average_distances, key=lambda x: x['avg distance'])[0]
    possible_plaintext = []

    # Will populate with a single character as each transposed 
    # block has been single-byte XOR brute forced
    key = b''
    possible_key_length = possible_key_lengths['key']
    for i in range(possible_key_length):
        
        # Creates an block made up of each nth byte, where n
        # is the keysize
        block = b''
        for j in range(i, len(ciphertext), possible_key_length):
            block += bytes([ciphertext[j]])
        key += bytes([bruteforce_single_char_xor(block)['key']]) 
    possible_plaintext.append((repeating_key_xor(ciphertext, key), key)) 
    return max(possible_plaintext, key=lambda x: get_english_score(x[0]))


def repeating_key_xor(message_bytes, key):
    """Returns message XOR'd with a key. If the message, is longer
    than the key, the key will repeat.
    """
    output_bytes = b''
    index = 0
    for byte in message_bytes:
        output_bytes += bytes([byte ^ key[index]])
        if (index + 1) == len(key):
            index = 0
        else:
            index += 1
    return output_bytes


def calculate_hamming_distance(input_bytes_1, input_bytes_2):
    """Finds and returns the Hamming distance (number of differing 
    bits) between two byte-strings
    """
    hamming_distance = 0
    for b1, b2 in zip(input_bytes_1, input_bytes_2):
        difference = b1 ^ b2

        # Count the number of differences ('1's) and add to the hamming distance
        hamming_distance += sum([1 for bit in bin(difference) if bit == '1'])
    return hamming_distance
