import tkinter as tk
from tkinter import ttk
import random

# Payoff matrix
PAYOFFS = {
    ('C', 'C'): (3, 3),
    ('C', 'D'): (0, 5),
    ('D', 'C'): (5, 0),
    ('D', 'D'): (1, 1)
}

# Strategy functions
def always_cooperate(_, __):
    return 'C'

def always_defect(_, __):
    return 'D'

def tit_for_tat(my_history, opp_history):
    if not opp_history:
        return 'C'
    return opp_history[-1]

def random_strategy(_, __):
    return random.choice(['C', 'D'])

STRATEGIES = {
    'Always Cooperate': always_cooperate,
    'Always Defect': always_defect,
    'Tit for Tat': tit_for_tat,
    'Random': random_strategy
}

class PrisonersDilemmaGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Prisoner's Dilemma Game")

        # Histories and scores
        self.player_history = []
        self.cpu_history = []
        self.player_score = 0
        self.cpu_score = 0

        # GUI Components
        self.create_widgets()

    def create_widgets(self):
        # Dropdown for player strategy
        tk.Label(self.root, text="Select Your Strategy:").pack()
        self.strategy_var = tk.StringVar(value='Tit for Tat')
        self.strategy_dropdown = ttk.Combobox(
            self.root, textvariable=self.strategy_var,
            values=list(STRATEGIES.keys()), state="readonly")
        self.strategy_dropdown.pack()

        # CPU strategy display
        self.cpu_label = tk.Label(self.root, text="CPU Strategy: Random")
        self.cpu_label.pack()

        # Play button
        self.play_button = tk.Button(self.root, text="Play Next Round",
                                     command=self.play_round)
        self.play_button.pack(pady=10)

        # History and score display
        self.result_text = tk.Text(self.root, height=10, width=50, state='disabled')
        self.result_text.pack(pady=5)

        # Reset button
        self.reset_button = tk.Button(self.root, text="Reset Game",
                                      command=self.reset_game)
        self.reset_button.pack()

    def play_round(self):
        # Get selected player strategy function
        player_strategy = STRATEGIES[self.strategy_var.get()]
        cpu_strategy = random_strategy  # fixed CPU strategy

        # Get moves
        player_move = player_strategy(self.player_history, self.cpu_history)
        cpu_move = cpu_strategy(self.cpu_history, self.player_history)

        # Get payoffs
        payoff_player, payoff_cpu = PAYOFFS[(player_move, cpu_move)]

        # Update history and scores
        self.player_history.append(player_move)
        self.cpu_history.append(cpu_move)
        self.player_score += payoff_player
        self.cpu_score += payoff_cpu

        # Update text box
        self.result_text.config(state='normal')
        self.result_text.insert(tk.END, f"Round {len(self.player_history)}: You - "
                                        f"{player_move}, CPU - {cpu_move}\n")
        self.result_text.insert(tk.END, f"Scores -> You: {self.player_score} | CPU: "
                                        f"{self.cpu_score}\n\n")
        self.result_text.config(state='disabled')

    def reset_game(self):
        self.player_history.clear()
        self.cpu_history.clear()
        self.player_score = 0
        self.cpu_score = 0
        self.result_text.config(state='normal')
        self.result_text.delete(1.0, tk.END)
        self.result_text.config(state='disabled')

# Run GUI
if __name__ == "__main__":
    root = tk.Tk()
    game = PrisonersDilemmaGUI(root)
    root.mainloop()
