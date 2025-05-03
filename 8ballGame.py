import random;

def print_menu():
    print("*************Magic 8-Ball Game*************")
    print("Welcome to the Magic 8-Ball Game!")
    print("1. Ask a yes or no question and I will provide an answer.")
    print("2. Type 'help' to see this menu again.")
    print("3. Type 'exit' to quit the game.")
    print()

def show_help():
    print("*************Help Menu*************")
    print("In this game, you can ask any yes or no question.")
    print("In this app, just enter a yes or no question to receive your fate!")


def ask_question():
    question = input("Ask your yes or no question: ").strip()
    if question == "":
        print("Uh-oh! You didn't ask a question. Please try again.")
    else:
        print()







#runs game
def run_game():
    print_menu()

#Lets us run the file in the console and prevents the code from runing automatically if imported to antoher file
if __name__ == "__main__":
    run_game()
    show_help()