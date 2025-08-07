class Vocabulary:
    def __init__(self, vocab: str, read: str, mean: str, ja_sent: str, en_sent: str):
        self.vocab = vocab
        self.reading = read
        self.meaning = mean
        self.ja_sentence = ja_sent
        self.en_sentence = en_sent

    def __repr__(self) -> str:
        return f"{self.vocab} ({self.reading}):\n" +\
               f"  {self.meaning}\n  {self.ja_sentence}\n  {self.en_sentence}"

    def to_list(self) -> list[str]:
        return [
            self.vocab, self.reading, self.meaning, self.ja_sentence, self.en_sentence
        ]

    @classmethod
    def from_list(cls, lst: list[str]) -> "Vocabulary":
        assert len(lst) == 5
        return cls(lst[0], lst[1], lst[2], lst[3], lst[4])


def main():
    import argparse
    import csv
    import sys

    parser = argparse.ArgumentParser()
    parser.add_argument("csv", help="csv file to parse")
    parser.add_argument(
        "--fix",
        help="minimize quoting, fix bold styling, print new rows to stdout",
        action="store_true"
    )
    args = parser.parse_args()

    terms = set() # Used to check for duplicates.
    vocab = []
    with open(args.csv, "r") as f:
        reader = csv.reader(f)
        for row_num, row in enumerate(reader):
            v = Vocabulary.from_list(row)
            if v.vocab in terms:
                print(f"error: duplicate term on line {row_num + 1}: {v.vocab}")
                assert False
            terms.add(v.vocab)
            vocab.append(v)

    if args.fix:
        writer = csv.writer(sys.stdout, dialect="unix", quoting=csv.QUOTE_MINIMAL)
        for v in vocab:
            v.ja_sentence = v.ja_sentence.replace("<b>", "<strong>")
            v.ja_sentence = v.ja_sentence.replace("</b>", "</strong>")
            writer.writerow(v.to_list())

if __name__ == "__main__":
    main()
