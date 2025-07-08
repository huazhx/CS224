# TODO: [part d]
# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.

import argparse
import utils

def main():
    accuracy = 0.0

    # Compute accuracy in the range [0.0, 100.0]
    ### YOUR CODE HERE ###
    total_number = 0
    correct = 0
    for line in open('birth_dev.tsv', encoding='utf-8'):
        birth_place = line.split('\t')[1].strip()
        if birth_place.lower() == 'london':
            correct += 1
        total_number += 1
    accuracy = correct / total_number * 100
    ### END YOUR CODE ###

    return accuracy

if __name__ == '__main__':
    accuracy = main()
    with open("london_baseline_accuracy.txt", "w", encoding="utf-8") as f:
        f.write(f"{accuracy}\n")
