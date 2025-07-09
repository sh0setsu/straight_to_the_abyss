from button import MenuButton
from config import width

bg_color = (0, 0, 0)
play_button = MenuButton(width / 2 - (252 / 2), 200, 252, 74, "Начать игру", "assets/pale.jpg", "assets/pale.jpg","assets/click.mp3")
settings_button = MenuButton(width / 2 - (252 / 2), 300, 252, 74, "Настройки", "assets/red.jpg", "assets/red.jpg","assets/click.mp3")
exit_button = MenuButton(width / 2 - (252 / 2), 400, 252, 74, "Выход", "assets/gold.jpg", "assets/gold.jpg","assets/click.mp3")
# back_button = MenuButton(width / 2 - (252 / 2), 200, 252, 74, "Назад", "assets/pale.jpg", "assets/pale.jpg","assets/click.mp3")
buttons = [play_button, settings_button, exit_button]