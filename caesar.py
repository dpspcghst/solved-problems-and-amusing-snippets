import argparse
import string

def substitution_decryption(cipher_text, rotation: int):
    """
    Decrypts a substitution cipher.
    """

    letters = string.ascii_lowercase
    unmask = letters[len(letters) - rotation:] + letters[:len(letters) - rotation]
    trantab = str.maketrans(letters, unmask)
    print(cipher_text.translate(trantab))


def substitution_encryption(plain_text, rotation: int):
    """
    Passes a message through a substitution cipher.
    """

    letters = string.ascii_lowercase
    mask = letters[rotation:] + letters[:rotation]
    trantab = str.maketrans(letters, mask)
    print(plain_text.translate(trantab))


def main():
    """
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("--substitution_decryption",
                        action="store",
                        nargs=2,
                        help="Usage: ./kaOS.py --substitution_decryption [cipher_text] [rotation]",
                        dest="substitution_decryption_args")
    parser.add_argument("--substitution_encryption",
                        action="store",
                        nargs=2,
                        help="Usage: ./kaOS.py --substitution_encryption [plain_text] [rotation]",
                        dest="substitution_encryption_args")

    args = parser.parse_args()

    if args.substitution_decryption_args:
        cipher_text = str(args.substitution_decryption_args[0])
        rotation = int(args.substitution_decryption_args[1])
        substitution_decryption(cipher_text, rotation)

    elif args.substitution_encryption_args:
        plain_text = str(args.substitution_encryption_args[0])
        rotation = int(args.substitution_encryption_args[1])
        substitution_encryption(plain_text, rotation)

if __name__ == "__main__":
    """
    """

    main()
