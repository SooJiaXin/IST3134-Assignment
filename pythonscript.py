import csv
import re
import time
from collections import defaultdict

def word_count(csv_file_path):
    word_freq = defaultdict(int)

    # Increase the field size limit to handle large fields in the CSV file
    csv.field_size_limit(2147483647)  # Set a large limit

    with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header row if your CSV has one

        for row in reader:
            if len(row) > 0:
                text = row[0].lower()
                words = re.findall(r'\b\w+\b', text)
                for word in words:
                    word_freq[word] += 1

    return word_freq

def save_word_count_as_csv(word_freq, output_csv_path):
    # Sort the word_freq dictionary in descending order of the count
    sorted_word_freq = {k: v for k, v in sorted(word_freq.items(), key=lambda item: item[1], reverse=True)}
    
    with open(output_csv_path, 'w', newline='') as csvfile:
        fieldnames = ['Word', 'Count']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for word, count in word_freq.items():
            writer.writerow({'Word': word, 'Count': count})

if __name__ == "__main__":
    csv_file_path = "/home/hadoop/IST3134/Books_review.csv"  # Replace with the actual CSV file path
    output_csv_path = "/home/hadoop/IST3134/wordcount_output.csv"  # Replace with the desired output CSV file path

    print("Word count process started...")
    start_time = time.time()
    word_freq = word_count(csv_file_path)
    end_time = time.time()
    print("Word count process completed.")

    # Save the word count results as a CSV file
    save_word_count_as_csv(word_freq, output_csv_path)

    print("Word count results saved to:", output_csv_path)
    print("Execution time:", end_time - start_time, "seconds")
