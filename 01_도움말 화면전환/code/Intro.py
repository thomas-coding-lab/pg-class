import pygame
import sys
import help  # help 모듈을 임포트합니다.

# 초기화
pygame.init()

# 화면 크기 설정
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

# 게임 화면 배경 이미지 불러오기
background = pygame.image.load("../graphic/IntroBG.png")

# 주황색 원의 위치와 반지름 설정
orange_circle_rect = pygame.Rect(20, 20, 60, 60)  # 원의 클릭 가능 영역을 정의합니다.

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if orange_circle_rect.collidepoint(event.pos):
                help.show_help(screen)  # 주황색 원을 클릭하면 help 모듈의 화면으로 전환합니다.

    # 배경 이미지 표시
    screen.blit(background, (0, 0))

    # 주황색 원 그리기
    pygame.draw.circle(screen, (255, 165, 0), (50, 50), 30)
    pink_circle = pygame.draw.circle(screen, (255, 182, 193), (1100, 50), 30)
    gray_circle = pygame.draw.circle(screen, (169, 169, 169), (1200, 50), 30)

    # 파란색 사각형 설정
    blue_rect = pygame.draw.rect(screen, (0, 0, 255), (screen_width // 2 - 100, 600, 200, 50))

    # 화면 업데이트
    pygame.display.update()

# 게임 종료
pygame.quit()
sys.exit()
