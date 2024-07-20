def check_guess(chosen_word, guess):
    for letter in chosen_word:
        if letter == guess:
            print("Right")
            return  # Exit the function early if the guess is correct
    print("wrong")

# Example usage
chosen_word = "baboon"
guess = "b"
check_guess(chosen_word, guess)