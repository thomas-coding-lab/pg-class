import pygame

def show_help(main_screen):
    # 해상도 설정
    screen_width = 1280
    screen_height = 720

    # 이미지 불러오기 및 크기 조정
    background = pygame.image.load("../graphic/helpBG.png")
    help_icon = pygame.image.load("../graphic/help.png")
    help_icon_size = (60, 60)
    help_icon = pygame.transform.smoothscale(help_icon, help_icon_size)
    help_icon_original = help_icon  # 원래 크기의 이미지를 저장

    # 이미지의 위치 설정
    help_icon_rect = help_icon.get_rect(topleft=(20, 20))

    # 버튼 크기 조정에 필요한 변수 설정
    hover_scale_factor = 1.1  # 마우스 호버 시 버튼 크기 조정 비율

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if help_icon_rect.collidepoint(event.pos):
                    return

        # 마우스 호버 효과 적용
        if help_icon_rect.collidepoint(pygame.mouse.get_pos()):
            help_icon = pygame.transform.smoothscale(help_icon_original, (int(help_icon_original.get_width() * hover_scale_factor),
                                                                       int(help_icon_original.get_height() * hover_scale_factor)))
        else:
            help_icon = help_icon_original

        # 배경 이미지 표시
        main_screen.blit(background, (0, 0))

        # 이미지 그리기
        main_screen.blit(help_icon, help_icon_rect)

        # 화면 업데이트
        pygame.display.update()
