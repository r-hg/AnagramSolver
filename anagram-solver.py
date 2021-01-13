from collections import Counter
import time
import pytesseract


def get_dict():
    with open('C:\\Users\\BlahB\\Downloads\\words.txt') as words_file:  # Path of word file
        dictionary = words_file.read()
    dictionary = [x.lower() for x in
                  dictionary.split('\n')]
    return dictionary


def get_letters():
    pytesseract.pytesseract.tesseract_cmd = 'D:\\PyCharm Community Edition 2020.3.1\\tesseract'
    letters_in_image = pytesseract.image_to_string('D:\\angrm.png')  # Path of image to get string from
    letters_in_image = letters_in_image.replace(" ", "")
    return str(letters_in_image[0:-2])
    # Tesseract by default returns an EOF Character, Cutting it off


def return_anagrams(word_list, letters: str) -> list:
    letters = letters.lower()
    length_of_letters = len(letters)
    num_of_each_letter = Counter(letters)
    anagrams = set()

    for word in word_list:

        if not set(word) - set(letters):
            check_word = set()

            for letter, instances in Counter(word).items():
                if instances == num_of_each_letter[letter] and len(word) == length_of_letters:
                    check_word.add(letter)

            if check_word == set(word):
                anagrams.add(word)
    anagrams.discard("")

    return sorted(list(anagrams), key=lambda x: len(x))


if __name__ == '__main__':
    start = time.time()
    solved_letters = get_letters()
    solved_anagram = return_anagrams(get_dict(), solved_letters)
    stop = time.time()

    print(solved_anagram)
    print(f"Number of anagrams: {len(solved_anagram)}")
    print(f"Time Taken: {round(stop - start, 5)} seconds")
