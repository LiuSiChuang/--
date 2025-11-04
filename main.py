"""
main.py
Главный файл игры "Изгиб Питона".
"""

import pygame
from config import WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE, BLACK, FPS
from game_objects import Snake, Apple


def handle_keys(snake):
    """Обрабатывает нажатия клавиш и задаёт новое направление змейки."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.next_direction = (0, -CELL_SIZE)
            elif event.key == pygame.K_DOWN:
                snake.next_direction = (0, CELL_SIZE)
            elif event.key == pygame.K_LEFT:
                snake.next_direction = (-CELL_SIZE, 0)
            elif event.key == pygame.K_RIGHT:
                snake.next_direction = (CELL_SIZE, 0)


def main():
    """Главная функция игры, содержит основной игровой цикл."""
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Изгиб Питона")
    clock = pygame.time.Clock()

    snake = Snake()
    apple = Apple()

    while True:
        handle_keys(snake)
        snake.update_direction()
        snake.move()

        # Проверка, съела ли змейка яблоко
        if snake.get_head_position() == apple.position:
            snake.length += 1
            apple.randomize_position()

        # Отрисовка объектов
        screen.fill(BLACK)
        snake.draw(screen)
        apple.draw(screen)
        pygame.display.update()

        # Ограничение FPS
        clock.tick(FPS)


if __name__ == "__main__":
    main()
