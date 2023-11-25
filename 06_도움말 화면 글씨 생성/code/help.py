import pygame

def show_help(main_screen):
    # 해상도 설정
    screen_width = 1280
    screen_height = 720

    # 배경 이미지 불러오기
    background = pygame.image.load("../graphic/helpBG.png")

    # 이미지 불러오기 및 크기 조정
    help_icon = pygame.image.load("../graphic/help.png")
    help_icon_size = (60, 60)
    help_icon = pygame.transform.smoothscale(help_icon, help_icon_size)
    help_icon_original = help_icon  # 원래 크기의 이미지를 저장

    # 이미지의 위치 설정
    help_icon_rect = help_icon.get_rect(topleft=(20, 20))

    # 버튼 크기 조정에 필요한 변수 설정
    hover_scale_factor = 1.1  # 마우스 호버 시 버튼 크기 조정 비율

    # 텍스트 설정
    text = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis feugiat eu sapien a rhoncus. "
            "Cras malesuada, mi sed aliquet laoreet, sapien lectus convallis ante, nec feugiat arcu dui et libero. "
            "Duis id est ultrices, ultricies orci facilisis, pulvinar risus. Pellentesque egestas urna sit amet justo "
            "bibendum, eget pharetra elit facilisis. Cras luctus velit vel egestas pretium. Morbi non ex viverra, "
            "aliquet purus vitae, mollis tellus. Vestibulum pretium at lectus quis cursus. Maecenas eget urna ut "
            "augue mattis varius eu id est. Quisque posuere vitae dolor sed elementum.")
    font = pygame.font.Font(None, 36)  # 폰트 설정

    # 텍스트 렌더링
    text_surface = font.render(text, True, (0, 0, 0))  # 검정색 텍스트 렌더링
    text_rect = text_surface.get_rect(center=(screen_width // 2, screen_height // 2))  # 화면 중앙에 텍스트 위치 설정

    # 텍스트 줄바꿈 계산
    max_line_length = 50  # 한 줄의 최대 길이
    lines = []
    words = text.split()
    current_line = ""
    for word in words:
        if len(current_line) + len(word) + 1 <= max_line_length:  # 1은 공백
            current_line += word + " "
        else:
            lines.append(current_line)
            current_line = word + " "
    if current_line:
        lines.append(current_line)

    # 텍스트 그리기
    text_height = len(lines) * font.get_linesize()  # 텍스트 전체 높이 계산
    text_rect.y -= text_height // 2  # 텍스트를 화면 중앙에 위치하도록 y 좌표 조정

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

        # 텍스트 그리기
        for i, line in enumerate(lines):
            line_surface = font.render(line, True, (0, 0, 0))  # 검정색 텍스트 렌더링
            line_rect = line_surface.get_rect(center=(screen_width // 2, text_rect.y + i * font.get_linesize()))
            main_screen.blit(line_surface, line_rect)

        # 화면 업데이트
        pygame.display.update()
