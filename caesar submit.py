import os.path

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def welcome():
    # add your code here
    print("Welcome to the Caesar Cipher")
    print("This program encrypts and decrypts text with the Caesar Cipher")
    return


def enter_message():
    mode = ''
    message = ''
    shift = 0
    file_name = ''
    # add your code here
    print("Would you like to encrypt (e) or decrypt (d)?: ")
    mode = input()
    if mode == 'e':
        option = ''
        print("Would you like to read from a file (f) or the console (c)? f")
        option = input()
        if option == 'f':
            message_or_file()
        elif option == 'c':
            print("What message would you like to encrypt: ")
            message = input()
            print("What is the shift number: ")
            shift = int(input())
            encrypt(message, shift)
    elif mode == 'd':
        option = ''
        print("Would you like to read from a file (f) or the console (c)? f")
        option = input()
        if option == 'f':
            message_or_file()
        elif option == 'c':
            print("What message would you like to decrypt: ")
            message = input()
            print("What is the shift number: ")
            shift = int(input())
            decrypt(message, shift)
    else:
        print("Invalid Mode")

    return mode, message, shift


def encrypt(message, shift):
    result = ""
    for i in message:
        if i in alphabet:
            index = alphabet.index(i)
            position = index + shift
            result += alphabet[position]
        else:
            result += i
    result = result.upper()
    print(result)
    return result


def decrypt(message, shift):
    # add your code here
    encryptmessage.lower(), 26 - shift
    


def process_file(filename, mode, shift):
    list_messages = []
    # add your code here
    if is_file(filename):
        with open(r'C:\Codeforces\messages.txt', 'w') as file:
            if mode == 'e':
                for line in file:
                    line = line.strip()
                    print(line)
                    list_messages.append(encrypt(line, shift))
            elif mode == 'd':
                for line in file:
                    line = line.strip()
                    list_messages.append(decrypt(line, shift))
    else:
        print("File not Found!")

    write_messages(list_messages)


def write_messages(lines):
    # add your code here
    with open('C:\Codeforces\results.txt', 'w') as f:
        for line in lines:
            f.write("%s\n" % line)
    return


def is_file(filename):
    if os.path.exists(filename):
        return True
    return False


def message_or_file():
    mode = ''
    filename = ''
    shift = 0
    print("Enter a filename: ")
    filename = input()
    print("What is the shift number: ")
    shift = int(input())

    process_file(filename, mode, shift)
    # add your code here


def main():
    # add your code here
    welcome()
    enter_message()
    choice = ''
    while True:
        print("Would you like to encrypt or decrypt another message? (y/n): ")
        choice = input()
        if choice == 'y' or choice == 'Y':
            enter_message()
        elif choice == 'n' or choice == 'N':
            print("Thanks for using the program, goodbye!")
            break
        else:
            continue

    return


# Program execution begins here
if __name__ == '__main__':
    main()
