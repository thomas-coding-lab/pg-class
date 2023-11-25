import pygame
import sys
import help

# 초기화
pygame.init()

# 화면 크기 설정
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

# 게임 화면 배경 이미지 불러오기
background = pygame.image.load("../graphic/IntroBG.png")

# 이미지 불러오기 및 크기 조정
help_icon = pygame.image.load("../graphic/help.png")
help_icon = pygame.transform.scale(help_icon, (60, 60))
volume_down_icon = pygame.image.load("../graphic/volume-down.png")
volume_down_icon = pygame.transform.scale(volume_down_icon, (60, 60))
volume_up_icon = pygame.image.load("../graphic/volume-up.png")
volume_up_icon = pygame.transform.scale(volume_up_icon, (60, 60))

# 이미지의 위치 설정
help_icon_rect = help_icon.get_rect(topleft=(20, 20))
volume_down_icon_rect = volume_down_icon.get_rect(topleft=(1100, 20))
volume_up_icon_rect = volume_up_icon.get_rect(topleft=(1200, 20))

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if help_icon_rect.collidepoint(event.pos):
                help.show_help(screen)

    # 배경 이미지 표시
    screen.blit(background, (0, 0))

    # 이미지 그리기
    screen.blit(help_icon, help_icon_rect)
    screen.blit(volume_down_icon, volume_down_icon_rect)
    screen.blit(volume_up_icon, volume_up_icon_rect)

    # 파란색 사각형 설정
    blue_rect = pygame.draw.rect(screen, (0, 0, 255), (screen_width // 2 - 100, 600, 200, 50))

    # 화면 업데이트
    pygame.display.update()

# 게임 종료
pygame.quit()
sys.exit()
