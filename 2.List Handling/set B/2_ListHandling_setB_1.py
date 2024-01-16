import bisect

def binary_search(word_list, target):
    # Sort the word list alphabetically
    sorted_word_list = sorted(word_list)

    # Binary search implementation
    left, right = 0, len(sorted_word_list)

    while left < right:
        mid = (left + right) // 2
        mid_word = sorted_word_list[mid]

        if mid_word == target:
            return True
        elif mid_word < target:
            left = mid + 1
        else:
            right = mid

    return False

def bisect_main():
    # Accept word list from the user
    word_list = input("Enter the word list: ").split(' ')

    # Remove leading and trailing whitespaces from each word
    word_list = [word.strip() for word in word_list]

    # Accept the word to search
    target_word = input("Enter the word to search: ")

    # Check if the word is present using binary search
    result = binary_search(word_list, target_word)

    if result:
        print(f"The word '{target_word}' is present in the word list.")
    else:
        print(f"The word '{target_word}' is not present in the word list.")

if __name__ == "__main__":
    bisect_main()
