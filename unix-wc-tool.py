import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Count bytes, lines, and words in a file."
    )
    parser.add_argument("file", metavar="file", type=str, help="File to analyze")
    parser.add_argument(
        "-c", "--bytes", action="store_true", help="Print the byte count"
    )
    parser.add_argument(
        "-l", "--lines", action="store_true", help="Print the line count"
    )
    parser.add_argument(
        "-w", "--words", action="store_true", help="Print the word count"
    )

    args = parser.parse_args()

    with open(args.file, "r", encoding="utf8") as file:
        text = file.read()
        noBytes = len(text)
        noLines = text.count("\n")
        noWords = sum(1 for line in text.split("\n") for word in line.split())

    if args.bytes:
        print(f"{noBytes} {args.file}")
    elif args.lines:
        print(f"{noLines} {args.file}")
    elif args.words:
        print(f"{noWords} {args.file}")
    else:
        print(f"{noBytes} {noLines} {noWords} {args.file}")


if __name__ == "__main__":
    main()
