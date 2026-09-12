import tkinter as tk
from random import choice

CHOICES = ["Камінь", "Ножиці", "Папір"]

WINNING_COMBINATIONS = {
    "Камінь": "Ножиці",
    "Ножиці": "Папір",
    "Папір": "Камінь"
}

wins = 0
losses = 0
draws = 0


# =========================
# АНІМАЦІЇ
# =========================

def victory_animation():
    colors = ["#00FFD5", "#00E5FF", "#FFFFFF", "#00FFD5"]
    sizes = [20, 24, 28, 24, 20]

    def animate(step=0):
        if step < len(colors):
            result_label.config(
                fg=colors[step],
                font=("Arial", sizes[step], "bold")
            )
            window.after(100, lambda: animate(step + 1))

    animate()


def lose_animation():
    colors = ["#FF4D6D", "#FF1744", "#FFFFFF", "#FF1744", "#FF4D6D"]
    positions = [0, -8, 8, -8, 8, 0]

    def animate(step=0):
        if step < len(positions):
            result_label.config(
                fg=colors[step],
                font=("Arial", 20, "bold"),
                padx=positions[step]
            )
            window.after(80, lambda: animate(step + 1))

    animate()


def draw_animation():
    colors = ["#FFD166", "#FFF3B0", "#FFD166", "#FFF3B0", "#FFD166"]

    def animate(step=0):
        if step < len(colors):
            result_label.config(
                fg=colors[step],
                font=("Arial", 20, "bold")
            )
            window.after(120, lambda: animate(step + 1))

    animate()


# =========================
# ГРА
# =========================

def play(player_choice):
    global wins, losses, draws

    computer_choice = choice(CHOICES)

    player_label.config(
        text=f"👤 Ви: {player_choice}"
    )

    computer_label.config(
        text=f"🤖 Комп'ютер: {computer_choice}"
    )

    if player_choice == computer_choice:
        result = "🤝 НІЧИЯ!"
        draws += 1
        result_label.config(text=result)
        draw_animation()

    elif WINNING_COMBINATIONS[player_choice] == computer_choice:
        result = "🏆 ПЕРЕМОГА!"
        wins += 1
        result_label.config(text=result)
        victory_animation()

    else:
        result = "💥 ПРОГРАШ!"
        losses += 1
        result_label.config(text=result)
        lose_animation()

    score_label.config(
        text=f"🏆 {wins}    💥 {losses}    🤝 {draws}"
    )


# =========================
# ВІКНО
# =========================

window = tk.Tk()
window.title("🎮 Камінь, Ножиці, Папір")
window.geometry("600x500")
window.resizable(False, False)


# НОВА ПАЛІТРА
BG_COLOR = "#101827"
BUTTON_COLOR = "#3949AB"
BUTTON_ACTIVE = "#5C6BC0"

TEXT_COLOR = "#F5F7FF"
SECONDARY_COLOR = "#9AA8C7"

WIN_COLOR = "#00FFD5"
LOSE_COLOR = "#FF4D6D"
DRAW_COLOR = "#FFD166"

window.configure(bg=BG_COLOR)


# =========================
# ЗАГОЛОВОК
# =========================

title = tk.Label(
    window,
    text="🎮 КАМІНЬ, НОЖИЦІ, ПАПІР",
    font=("Arial", 24, "bold"),
    fg=TEXT_COLOR,
    bg=BG_COLOR
)
title.pack(pady=25)


instruction = tk.Label(
    window,
    text="Оберіть свій варіант:",
    font=("Arial", 16),
    fg=SECONDARY_COLOR,
    bg=BG_COLOR
)
instruction.pack(pady=10)


# =========================
# КНОПКИ
# =========================

buttons_frame = tk.Frame(
    window,
    bg=BG_COLOR
)
buttons_frame.pack(pady=20)


rock_button = tk.Button(
    buttons_frame,
    text="🪨\nКАМІНЬ",
    font=("Arial", 14, "bold"),
    width=12,
    height=3,
    bg=BUTTON_COLOR,
    fg=TEXT_COLOR,
    activebackground=BUTTON_ACTIVE,
    activeforeground=TEXT_COLOR,
    relief="flat",
    command=lambda: play("Камінь")
)
rock_button.grid(row=0, column=0, padx=8)


scissors_button = tk.Button(
    buttons_frame,
    text="✂️\nНОЖИЦІ",
    font=("Arial", 14, "bold"),
    width=12,
    height=3,
    bg=BUTTON_COLOR,
    fg=TEXT_COLOR,
    activebackground=BUTTON_ACTIVE,
    activeforeground=TEXT_COLOR,
    relief="flat",
    command=lambda: play("Ножиці")
)
scissors_button.grid(row=0, column=1, padx=8)


paper_button = tk.Button(
    buttons_frame,
    text="📄\nПАПІР",
    font=("Arial", 14, "bold"),
    width=12,
    height=3,
    bg=BUTTON_COLOR,
    fg=TEXT_COLOR,
    activebackground=BUTTON_ACTIVE,
    activeforeground=TEXT_COLOR,
    relief="flat",
    command=lambda: play("Папір")
)
paper_button.grid(row=0, column=2, padx=8)


# =========================
# РЕЗУЛЬТАТ
# =========================

player_label = tk.Label(
    window,
    text="👤 Ви: —",
    font=("Arial", 15),
    fg=TEXT_COLOR,
    bg=BG_COLOR
)
player_label.pack(pady=8)


computer_label = tk.Label(
    window,
    text="🤖 Комп'ютер: —",
    font=("Arial", 15),
    fg=TEXT_COLOR,
    bg=BG_COLOR
)
computer_label.pack(pady=8)


result_label = tk.Label(
    window,
    text="Зробіть свій вибір!",
    font=("Arial", 20, "bold"),
    fg=SECONDARY_COLOR,
    bg=BG_COLOR
)
result_label.pack(pady=20)


# =========================
# РАХУНОК
# =========================

score_label = tk.Label(
    window,
    text="🏆 0    💥 0    🤝 0",
    font=("Arial", 13, "bold"),
    fg=SECONDARY_COLOR,
    bg=BG_COLOR
)
score_label.pack(pady=10)


window.mainloop()
