import morse_code


def main():
    message = "I LOVE YOU"
    result = morse_code.encode(message)
    print(result)
    morse_code.play_morse_code(message)


if __name__ == '__main__':
    main()
