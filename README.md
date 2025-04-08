# 🖱️ Mouse Click Anti-Sleep Script

This is a simple Python script that helps prevent your computer screen from going to sleep. It does so by simulating a mouse click at a user-defined location on the screen every few seconds.

## 🛠️ How It Works

1. When you run the script, it will prompt you to **click anywhere on the screen**.
2. It captures that screen coordinate.
3. Then, it repeatedly performs a **mouse click at that location** at regular intervals.
4. This small activity tricks the system into thinking there is user interaction, keeping the screen from going idle or going to sleep.

## 🧰 Requirements

- Python 3.x
- `pyautogui` module (install using `pip install pyautogui`)
- `pynput` module (install using `pip install pynput`)

## 🚀 Usage

1. Clone this repository or download the script file.
2. Install the required package:
        pip install pyautogui
        pip install pynput

3. Run the script:
        python screen_click.py

4. Follow the on-screen instruction to click anywhere on the screen.

> ⚠️ Note: Make sure your screen stays on the same resolution and layout during use to avoid misclicks.
