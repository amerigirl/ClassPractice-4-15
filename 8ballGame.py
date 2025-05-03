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
        num = random.randint(1, 8)
        print("***********************************")
        print(f"Question: {question}")
        print("Magic 8-Ball says: ")
        print("***********************************")
        print(get_response(num), "\n")


def get_response(rand_num):
    match rand_num:
        case 1:
            return "Yes, definitely."
        case 2:            
            return "Ask again later."
        case 3:            
            return "Don't count on it."
        case 4:            
            return "My sources say no."      
        case 5:            
            return "It is certain."        
        case 6:            
            return "Outlook not so good."
        case 7:            
            return "Yes, in due time."        
        case 8:            
            return "Very doubtful."




#runs game
def run_game():
   while True:
    print_menu()
    choice = input("select a menu item 1-3: ").strip()
    if choice == "1":
        ask_question()
    elif choice == "2":
        print(show_help())
    elif choice == "3":
        print("Thank you for playing! Goodbye!")
        break
   

#Lets us run the file in the console and prevents the code from runing automatically if imported to antoher file
if __name__ == "__main__":
    run_game()
   