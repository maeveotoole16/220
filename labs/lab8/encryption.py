# Add your encryption methods here
def encode(message, key):
    acc = " "
    for x in message:
        i = ord(x)
        i = i + key
        new = chr(i)
        acc = acc + new
    return acc

def encode_better(message1, message2):
    acc = ""
    for i in range(len(message1)):
        c = ord(message1[i])
        key = ord(message2[i % len(message2)])
        new_message = (c + key) - 97
        acc = acc + chr(new_message)
    return acc