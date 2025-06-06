## Predictive Cricket Game 🎯🏏

A fun, interactive command-line cricket game where you predict numbers between 1–50. The closer your guess is to the computer's number, the more runs you score!

## 🎮 Game Rules

1. Choose the number of overs and your target score.
2. You have 10 wickets and (overs × 6) balls.
3. On each ball, guess a number between 1 and 50.
4. The computer generates a random number between 1 and 50.
5. The closer your guess, the more runs you get:

| Difference         | Outcome     |
|--------------------|-------------|
| < 5                | 6 runs      |
| 5–9                | 4 runs      |
| 10–14              | 3 runs      |
| 15–19              | 2 runs      |
| 20–24              | 1 run       |
| 25–29              | 0 runs      |
| ≥ 30               | Wicket lost |

## 🛠️ Technologies Used

- Python 3
- Random module
- Console input/output

## ▶️ How to Run

1. Run the script:
   
2. Select an option:
    
    1 to play
    2 to view rules
    3 to exit

    Enter overs and target runs, and start playing by guessing numbers.

## 🧠 What I Learned

- Implementing a turn-based game loop
- Handling user input and game state
- Simulating probability-based scoring logic
- Use of randomness in gameplay design