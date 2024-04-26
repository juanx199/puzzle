# Tarea de POO con gpt

- El siguiente archivo contiene las solicitudes que se le indicaron a chatgpt para que cree un juego implementando pygame y POO.

- Juan Camilo Carvjal Camargo 20232020026

## 1) Haz un juego en python con pygame se un  circulo que pueda mover con las flechas del teclado usando POO
- Claro, aquí tienes un ejemplo de cómo podrías crear un juego simple en Python utilizando Pygame y programación orientada a objetos. Este juego consistirá en controlar un círculo que se mueve en la pantalla con las flechas del teclado:

```python
import pygame
import sys

# Definir colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Definir dimensiones de la pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Crear un círculo como sprite del jugador
        self.image = pygame.Surface([50, 50])
        self.image.fill(WHITE)
        pygame.draw.circle(self.image, (255, 0, 0), (25, 25), 25)
        # Obtener el rectángulo del sprite
        self.rect = self.image.get_rect()
        # Establecer la posición inicial del jugador
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    def update(self):
        # Obtener las teclas presionadas
        keys = pygame.key.get_pressed()
        # Mover el jugador según las teclas presionadas
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5

def main():
    pygame.init()

    # Inicializar la pantalla
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Move the Circle")

    # Crear un grupo de sprites y añadir el jugador
    all_sprites = pygame.sprite.Group()
    player = Player()
    all_sprites.add(player)

    clock = pygame.time.Clock()

    # Bucle principal del juego
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Actualizar los sprites
        all_sprites.update()

        # Limpiar la pantalla
        screen.fill(BLACK)

        # Dibujar los sprites en la pantalla
        all_sprites.draw(screen)

        # Actualizar la pantalla
        pygame.display.flip()

        # Limitar la velocidad de fotogramas
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
```

Este código crea una ventana de juego utilizando Pygame y define una clase `Player` que representa al círculo controlable por el usuario. El jugador puede mover el círculo utilizando las teclas de flecha en el teclado. El juego se ejecuta en un bucle principal donde se actualizan y dibujan los sprites en la pantalla.


## 2) también que si sale de pantalla por derecha aparezca por la izquierda y lo mismo por arriba y abajo  

- Para implementar el rebote del círculo cuando sale de la pantalla por la derecha o por abajo, y que aparezca por la izquierda o arriba respectivamente, puedes hacer algunos ajustes en la clase `Player` y en la función `update()` del juego. Aquí tienes la versión modificada del código:

```python
import pygame
import sys

# Definir colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Definir dimensiones de la pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Crear un círculo como sprite del jugador
        self.image = pygame.Surface([50, 50])
        self.image.fill(WHITE)
        pygame.draw.circle(self.image, (255, 0, 0), (25, 25), 25)
        # Obtener el rectángulo del sprite
        self.rect = self.image.get_rect()
        # Establecer la posición inicial del jugador
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    def update(self):
        # Obtener las teclas presionadas
        keys = pygame.key.get_pressed()
        # Mover el jugador según las teclas presionadas
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5

        # Rebotar si el jugador sale de la pantalla
        if self.rect.right < 0:
            self.rect.left = SCREEN_WIDTH
        elif self.rect.left > SCREEN_WIDTH:
            self.rect.right = 0
        elif self.rect.bottom < 0:
            self.rect.top = SCREEN_HEIGHT
        elif self.rect.top > SCREEN_HEIGHT:
            self.rect.bottom = 0

def main():
    pygame.init()

    # Inicializar la pantalla
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Move the Circle")

    # Crear un grupo de sprites y añadir el jugador
    all_sprites = pygame.sprite.Group()
    player = Player()
    all_sprites.add(player)

    clock = pygame.time.Clock()

    # Bucle principal del juego
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Actualizar los sprites
        all_sprites.update()

        # Limpiar la pantalla
        screen.fill(BLACK)

        # Dibujar los sprites en la pantalla
        all_sprites.draw(screen)

        # Actualizar la pantalla
        pygame.display.flip()

        # Limitar la velocidad de fotogramas
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
```

Con estos cambios, el círculo rebotará al salir de la pantalla por cualquier borde y aparecerá en el lado opuesto de la pantalla.

## 3) la imagen aparece como un cuadrado y no como circulo :(

- Mis disculpas por el error. Parece que el círculo se está viendo como un cuadrado debido a que estamos utilizando un rectángulo para definir su área de colisión. Para corregir esto, podemos usar la función `pygame.draw.circle()` directamente para dibujar un círculo en lugar de dibujar sobre una superficie cuadrada. Aquí tienes la corrección:

```python
import pygame
import sys

# Definir colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Definir dimensiones de la pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Crear un círculo como sprite del jugador
        self.image = pygame.Surface([50, 50], pygame.SRCALPHA)  # SRCALPHA para canal alfa
        pygame.draw.circle(self.image, (255, 0, 0), (25, 25), 25)
        # Obtener el rectángulo del sprite
        self.rect = self.image.get_rect()
        # Establecer la posición inicial del jugador
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    def update(self):
        # Obtener las teclas presionadas
        keys = pygame.key.get_pressed()
        # Mover el jugador según las teclas presionadas
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5

        # Rebotar si el jugador sale de la pantalla
        if self.rect.right < 0:
            self.rect.left = SCREEN_WIDTH
        elif self.rect.left > SCREEN_WIDTH:
            self.rect.right = 0
        elif self.rect.bottom < 0:
            self.rect.top = SCREEN_HEIGHT
        elif self.rect.top > SCREEN_HEIGHT:
            self.rect.bottom = 0

def main():
    pygame.init()

    # Inicializar la pantalla
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Move the Circle")

    # Crear un grupo de sprites y añadir el jugador
    all_sprites = pygame.sprite.Group()
    player = Player()
    all_sprites.add(player)

    clock = pygame.time.Clock()

    # Bucle principal del juego
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Actualizar los sprites
        all_sprites.update()

        # Limpiar la pantalla
        screen.fill(BLACK)

        # Dibujar los sprites en la pantalla
        all_sprites.draw(screen)

        # Actualizar la pantalla
        pygame.display.flip()

        # Limitar la velocidad de fotogramas
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
```

Con esta modificación, el círculo ahora debería mostrarse correctamente en la pantalla.