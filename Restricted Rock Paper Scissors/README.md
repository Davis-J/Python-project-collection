# 🪨📄✂️ Restricted Rock Paper Scissors — Inspired by *Kaiji*

This is a **strategic twist** on the classic Rock Paper Scissors game — each player starts with a **limited number of cards** for Rock, Paper, and Scissors.

### 🎌 Inspired By:  
The concept is heavily inspired by the **Restricted Rock-Paper-Scissors game** featured in the anime/manga series **Kaiji** (*Gyakkyou Burai Kaiji*), where characters battle using limited RPS cards under psychological and strategic pressure.

## 🧠 Game Concept

- Each player starts with:
  - 4 Rock cards
  - 4 Paper cards
  - 4 Scissors cards
- Once a card type is used up, it cannot be played again.
- The game ends after 12 rounds or when all cards are used.

## 🤖 VS Computer

- You play against a computer that randomly selects from remaining cards.
- Points are tracked, and the winner is declared at the end.

## 📋 Rules Recap

- Rock beats Scissors
- Scissors beats Paper
- Paper beats Rock
- If both play the same card, it's a draw
- Player with more points after 12 rounds wins

## 🛠️ Technologies Used

- Python 3
- Random module (`random.choice`)
- Custom card tracking and logic functions

## ▶️ How to Play

1. Run the script:

2. Input your name.

3. Use the numbers:

- 1 for Rock
- 2 for Paper
- 3 for Scissors

Make sure not to use a card type you've run out of — the game will warn you.

## 💡 What I Learned

- Implementing resource limits (cards)
- Creating turn-based mechanics
- Dynamic decision-making AI logic
- Structuring code for game logic and fairness