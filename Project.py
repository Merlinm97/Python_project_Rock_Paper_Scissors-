import random
from colorama import Fore


choices = ["Rock", "Paper", "Scissors"]
cpu_score = 0
player_score = 0
t = 0
n = 1
while True:
    computer = random.choice(choices)
    print(f"round-{n}")
    player = input("Rock, Paper, Scissors or end? ").capitalize()
    if player not in ["Rock" , "Paper" , "Scissors","End"]:
        print("input a valid option")
    else:
        if player == "End" and n == 1:
            print("GAME OVER")
            break
        ## Conditions of Rock,Paper and Scissors
        if player == computer:
            print(Fore.CYAN + "Computer chose: " + computer + Fore.RESET)
            print(Fore.YELLOW + "Tie!" + Fore.RESET)
            t = t + 1
            print()
        elif player == "Rock":
            print(Fore.CYAN + "Computer chose: " + computer + Fore.RESET)
            if computer == "Paper":
                print(Fore.RED + "You lose!", computer, "covers", player + Fore.RESET)
                cpu_score += 1
            else:
                print(Fore.GREEN + "You win!", player, "smashes", computer + Fore.RESET)
                player_score += 1
            print()
        elif player == "Paper":
            print(Fore.CYAN + "Computer chose: " + computer + Fore.RESET)
            if computer == "Scissors":
                print(Fore.RED + "You lose!", computer, "cut", player + Fore.RESET)
                cpu_score += 1
            else:
                print(Fore.GREEN + "You win!", player, "covers", computer + Fore.RESET)
                player_score += 1
            print()
        elif player == "Scissors":
            print(Fore.CYAN + "Computer chose: " + computer + Fore.RESET)
            if computer == "Rock":
                print(Fore.RED + "You lose...", computer, "smashes", player + Fore.RESET)
                cpu_score += 1
            else:
                print(Fore.GREEN + "You win!", player, "cut", computer + Fore.RESET)
                player_score += 1
            print()
        elif player == 'End':
            print("-" * 170)
            if player_score > cpu_score:
                print("Final Scores:")
                print()
                print(f"total_rounds:{n - 1}")
                print(f"Ties:{t}")
                print(f"CPU:{cpu_score}")
                print(f"Player:{player_score}")
                print(Fore.GREEN + "Congratulations! you won 🏆" + Fore.RESET)
            elif player_score == cpu_score:
                print("Final Scores:")
                print()
                print(f"total_rounds:{n - 1}")
                print(f"Ties:{t}")
                print(f"CPU:{cpu_score}")
                print(f"Player:{player_score}")
                print(Fore.YELLOW + "It's a tie! 🤝" + Fore.RESET)
            else:
                print("Final Scores:")
                print()
                print(f"total_rounds:{n - 1}")
                print(f"Ties:{t}")
                print(f"CPU:{cpu_score}")
                print(f"Player:{player_score}")
                print(Fore.RED + "Sorry, you lost. Better luck next time 🤞" + Fore.RESET)
            break
        n=n+1

