from mrjob.job import MRJob
import re

class WordCountMR(MRJob):

    def mapper(self, _, line):
        # Split the line into words using whitespace as the delimiter
        words = re.findall(r'\w+', line.lower())
        for word in words:
            # Yield each word as the key and 1 as the value
            yield word, 1

    def combiner(self, word, counts):
        # Sum the occurrences of each word locally at the combiner step
        yield word, sum(counts)

    def reducer(self, word, counts):
        # Check if the word contains only alphabetic characters
        if word.isalpha():
            # Sum the occurrences of each word globally at the reducer step
            yield word, sum(counts)

if __name__ == '__main__':
    WordCountMR.run()
