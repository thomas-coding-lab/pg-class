import pygame


def show_help(main_screen):
    # 해상도 설정
    screen_width = 1280
    screen_height = 720

    # 이미지 불러오기 및 크기 조정
    background = pygame.image.load("../graphic/helpBG.png")
    help_icon = pygame.image.load("../graphic/help.png")
    help_icon = pygame.transform.scale(help_icon, (60, 60))

    # 이미지의 위치 설정
    help_icon_rect = help_icon.get_rect(topleft=(20, 20))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if help_icon_rect.collidepoint(event.pos):
                    return

        # 배경 이미지 표시
        main_screen.blit(background, (0, 0))

        # 이미지 그리기
        main_screen.blit(help_icon, help_icon_rect)

        # 화면 업데이트
        pygame.display.update()
