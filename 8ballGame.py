import random;

def print_menu():
    print("*************Magic 8-Ball Game*************")
    print("Welcome to the Magic 8-Ball Game!")
    print("1. Ask a yes or no question and I will provide an answer.")
    print("2. Type 'help' to see this menu again.")
    print("3. Type 'exit' to quit the game.")
    print()



def run_game():
    print_menu()

#Lets us run the file in the console and prevents the code from runing automatically if imported to antoher file
if __name__ == "__main__":
    run_game()