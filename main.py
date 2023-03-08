import difflib
import os
import re


def compare_notebooks(file1, file2, threshold=0.9):
    """
    Funkcja porównująca dwa pliki ipynb i zwracająca wartość
    True, jeśli podobieństwo między nimi przekracza próg,
    w przeciwnym razie zwraca wartość False.
    """

    with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

        # Porównaj listy linii i oblicz podobieństwo
        matcher = difflib.SequenceMatcher(None, lines1, lines2)

        # Calculate similarity ratio
        similarity_ratio = matcher.ratio()

        # If similarity ratio is greater than threshold, return True
        if similarity_ratio >= threshold:
            # Get matching blocks of code
            matching_blocks = matcher.get_matching_blocks()

            # Print matching code
            print(f"Code matching above threshold ({threshold}):")
            for block in matching_blocks:
                if block.size > 1:
                    print("".join(lines1[block.a:block.a + block.size]))
            return True

    return False


def find_plagiarism(directory, threshold=0.9):
    """
    Funkcja wyszukująca pliki ipynb w podanym katalogu i wykrywająca plagiat
    między nimi. Zwraca listę par plików, które przekraczają próg podobieństwa.
    """

    notebooks = [os.path.join(directory, f) for f in os.listdir(directory)
                 if f.endswith('.ipynb')]

    pairs = []
    for i in range(len(notebooks)):
        for j in range(i + 1, len(notebooks)):
            if compare_notebooks(notebooks[i], notebooks[j], threshold):
                pairs.append((notebooks[i], notebooks[j]))

    return pairs


if __name__ == "__main__":
    plagiarism_pairs = find_plagiarism('.', threshold=0.8)
    print(plagiarism_pairs)
