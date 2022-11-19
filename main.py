import morse_code


def main():
    message = "HELLO HELLO"
    result = morse_code.encode(message)
    print(result)
    # morse_code.play_morse_code(message)
    morse_code.generate_morse_code_wav(message)


if __name__ == '__main__':
    main()
