import base64

def encode(string):
    string_bytes = str.encode(string)
    return base64.standard_b64encode(string_bytes).decode()

def decode(string):
    string_bytes = str.encode(string)
    return base64.standard_b64decode(string_bytes).decode()

if __name__ == "__main__":
    decoded_string = input("Put text that You want to encode\n")
    print(encode(decoded_string))
    coded_string = input("Put text that You want to decode\n")
    print(decode(coded_string))