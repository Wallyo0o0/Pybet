# python slot machine program
import random
import time

def spin_row():
    symbols = ["🍉", "⭐", "🍋", "🍓", "🍎"]

    results = []
    for symbol in range(3):
        results.append(random.choice(symbols))
    return results


def print_row(row):
    print(" ".join(row))

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
          if row[0] == "🍉":
            return bet * 1.5
          elif row[0] == "⭐":
            return bet * 2
          elif row[0] == "🍋":
            return bet * 2.5
          elif row[0] == "🍓":
            return bet * 3
          elif row[0] == "🍎":
            return bet * 5
    return 0
def main():
    balance = 100
    print("----------------")
    print("Welcome to pybet")
    print("Symbols: 🍉 ⭐ 🍋 🍓 🍎")
    print("----------------")

    while balance > 0:
        print(f"Current balance is ${balance}")

        bet = input("Plae your bet amount in dollars ")

        if not bet.isdigit():
            print("That is an invalid amount of money")
            continue
        bet = float(bet)

        if bet > balance:
            print("Bet amount is too large")
            continue

        if bet <= 0 :
            print("Please enter a valid amount to bet")
            continue

        balance -= bet

        row = spin_row()
        print("Spinning...\n")

        time.sleep(3)
        print_row(row)
        payout = get_payout(row, bet)

        if payout > 0:
           print(f"You won ${payout}")
        else:
           print("Sorry you lost ")

        balance += payout

        play_again = input("Do you want to play again (y/n)").lower()
        if play_again != "y":
           break


    print(f"Your final balance is ${balance}")




if __name__ == "__main__":
   main()