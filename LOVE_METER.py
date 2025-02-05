def get_user_name():
    """Function to get the user's name with basic validation."""
    while True:
        name = input("Welcome to the 'Love Calculator'! Please enter your name: ").strip()
        if name:
            return name
        else:
            print("You didn't enter a name. Please try again.")

def get_partner_name():
    """Function to get the partner's name with basic validation."""
    while True:
        partner_name = input("Please enter your partner's name: ").strip()
        if partner_name:
            return partner_name
        else:
            print("You didn't enter a partner's name. Please try again.")

def calculate_score(name1, name2):
    """Function to calculate the love compatibility score based on the letters in 'TRUE' and 'LOVE'."""
    # Combine both names for the calculation and make them uppercase for uniformity
    name = (name1 + name2).upper()

    # Counting occurrences of letters in 'TRUE'
    t = name.count("T")
    r = name.count("R")
    u = name.count("U")
    e = name.count("E")

    # Calculate the 'TRUE' score
    true_score = t + r + u + e

    # Counting occurrences of letters in 'LOVE'
    l = name.count("L")
    o = name.count("O")
    v = name.count("V")
    e = name.count("E")

    # Calculate the 'LOVE' score
    love_score = l + o + v + e

    return true_score, love_score

def display_score(true_score, love_score):
    """Function to display the compatibility score message."""
    total_score = str(true_score) + str(love_score)

    print("\nCalculating your Love Compatibility Score...")

    # Determine the compatibility based on the total score
    if int(total_score) < 30:
        print(f"Your compatibility score is {total_score}. It seems you're alright together. Keep trying to understand each other!")
    elif 30 <= int(total_score) < 70:
        print(f"Your compatibility score is {total_score}. You are perfect for each other!")
    else:
        print(f"Your compatibility score is {total_score}. You two are the BEST couple ever!")

def main():
    """Main function to run the Love Calculator program."""
    name1 = get_user_name()  # Get the user's name
    name2 = get_partner_name()  # Get the partner's name
    true_score, love_score = calculate_score(name1, name2)  # Calculate the love compatibility score
    display_score(true_score, love_score)  # Display the result

    # Thanking the user for playing
    print("\nThank you for playing the 'Love Calculator'! ❤️ Have a wonderful day!")

# Run the program
if __name__ == "__main__":
    main()
