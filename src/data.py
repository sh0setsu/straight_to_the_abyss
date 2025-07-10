from src import button
from config import width
import os

bg_color = (0, 0, 0)
play_button = button.MenuButton(width / 2 - (252 / 2), 200, 252, 74, "Начать игру", os.path.join("assets", "ik.png"), os.path.join("assets", "ik2.png"), os.path.join("assets", "click.mp3"))
settings_button = button.MenuButton(width / 2 - (252 / 2), 300, 252, 74, "Настройки", os.path.join("assets", "ik.png"), os.path.join("assets", "ik2.png"),os.path.join("assets", "click.mp3"))
exit_button = button.MenuButton(width / 2 - (252 / 2), 400, 252, 74, "Выход", os.path.join("assets", "ik.png"), os.path.join("assets", "ik2.png"),os.path.join("assets", "click.mp3"))
# back_button = MenuButton(width / 2 - (252 / 2), 200, 252, 74, "Назад", "assets/pale.jpg", "assets/pale.jpg","assets/click.mp3")
buttons = [play_button, settings_button, exit_button]

# play_button = button.MenuButton(width / 2 - (252 / 2), 200, 252, 74, "Начать игру", "assets/pale.jpg", "assets/pale.jpg","assets/click.mp3")
# settings_button = button.MenuButton(width / 2 - (252 / 2), 300, 252, 74, "Настройки", "assets/red.jpg", "assets/red.jpg","assets/click.mp3")
# exit_button = button.MenuButton(width / 2 - (252 / 2), 400, 252, 74, "Выход", "assets/gold.jpg", "assets/gold.jpg","assets/click.mp3")
# # back_button = MenuButton(width / 2 - (252 / 2), 200, 252, 74, "Назад", "assets/pale.jpg", "assets/pale.jpg","assets/click.mp3")
# buttons = [play_button, settings_button, exit_button]
