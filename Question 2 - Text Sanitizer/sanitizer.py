import argparse
from collections import Counter

class TextSanitizer:
    def __init__(self, source, target):
        self.source = source
        self.target = target
        self.text = ""

    def read_file(self):
        with open(self.source, 'r', encoding='utf-8') as f:
            self.text = f.read()

    def sanitize(self):
        sanitized = self.text.lower()
        sanitized = sanitized.replace('\t', '____')
        self.text = sanitized

    def generate_statistics(self):
        return Counter(c for c in self.text if c.isalpha())

    def print_output(self, stats):
        print("=== Sanitized Text ===")
        print(self.text)
        print("\n=== Statistics ===")
        for char, count in sorted(stats.items()):
            print(f"{char}: {count}")
    
    def write_file(self):
        with open(self.target, 'w', encoding='utf-8') as f:
            f.write(self.text)

    def run(self):
        self.read_file()
        self.sanitize()
        stats = self.generate_statistics()
        self.print_output(stats)
        self.write_file()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Text Sanitizer")
    parser.add_argument("--source", required=True)
    parser.add_argument("--target", required=True)
    args = parser.parse_args()

    sanitizer = TextSanitizer(args.source, args.target)
    sanitizer.run()
