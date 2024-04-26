import pygame
import sys
import random

# Definir colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Tamaño de la pantalla
WIDTH, HEIGHT = 300, 300

# Tamaño de cada cuadro del puzzle
TILE_SIZE = WIDTH // 3

class PuzzlePiece:
    def __init__(self, number, row, col, image):
        self.number = number
        self.row = row
        self.col = col
        self.image = image

    def draw(self, screen):
        if self.number == 0:
            pygame.draw.rect(screen, BLACK, (self.col * TILE_SIZE, self.row * TILE_SIZE, TILE_SIZE, TILE_SIZE))
        else:
            screen.blit(self.image, (self.col * TILE_SIZE, self.row * TILE_SIZE))

class PuzzleGame:
    def __init__(self, images):
        self.images = images
        random.shuffle(self.images)
        self.board = [[PuzzlePiece(col + row * 3, row, col, self.images[col + row * 3]) for col in range(3)] for row in range(3)]
        self.empty_row = 2
        self.empty_col = 2

    def draw(self, screen):
        for row in self.board:
            for piece in row:
                piece.draw(screen)

    def move_piece(self, row, col):
        if (abs(self.empty_row - row) == 1 and self.empty_col == col) or (abs(self.empty_col - col) == 1 and self.empty_row == row):
            self.board[self.empty_row][self.empty_col], self.board[row][col] = self.board[row][col], self.board[self.empty_row][self.empty_col]
            self.empty_row, self.empty_col = row, col

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sliding Puzzle")

    # Cargar imágenes
    image_paths = ["imagenes/imagen1.jpeg",
                   "imagenes/imagen2.jpeg",
                   "imagenes/imagen3.jpeg",
                   "imagenes/imagen4.jpeg",
                   "imagenes/imagen5.jpeg",
                   "imagenes/imagen6.jpeg",
                   "imagenes/imagen7.jpeg",
                   "imagenes/imagen8.jpeg",
                   "imagenes/vacio.jpeg"]  # Una imagen vacía para la ficha vacía
    images = [pygame.image.load(path) for path in image_paths]

    puzzle_game = PuzzleGame(images)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and puzzle_game.empty_row < 2:
                    puzzle_game.move_piece(puzzle_game.empty_row + 1, puzzle_game.empty_col)
                elif event.key == pygame.K_DOWN and puzzle_game.empty_row > 0:
                    puzzle_game.move_piece(puzzle_game.empty_row - 1, puzzle_game.empty_col)
                elif event.key == pygame.K_LEFT and puzzle_game.empty_col < 2:
                    puzzle_game.move_piece(puzzle_game.empty_row, puzzle_game.empty_col + 1)
                elif event.key == pygame.K_RIGHT and puzzle_game.empty_col > 0:
                    puzzle_game.move_piece(puzzle_game.empty_row, puzzle_game.empty_col - 1)

        screen.fill(WHITE)
        puzzle_game.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()