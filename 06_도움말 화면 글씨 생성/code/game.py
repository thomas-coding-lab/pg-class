import pygame
import sys

# 초기화
pygame.init()

# 화면 크기 설정
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

# 게임 화면 배경 이미지 불러오기
background = pygame.image.load("../graphic/GameBG.png")
background = pygame.transform.scale(background, (screen_width, screen_height))

# 게임 루프
def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 게임 화면 표시
        screen.blit(background, (0, 0))

        # 게임 로직을 여기에 추가

        pygame.display.update()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
