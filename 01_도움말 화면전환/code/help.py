import pygame

def show_help(main_screen):
    # 해상도 설정
    screen_width = 1280
    screen_height = 720

    # 주황색 원의 위치와 반지름 설정
    orange_circle_rect = pygame.Rect(20, 20, 60, 60)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if orange_circle_rect.collidepoint(event.pos):
                    return  # 주황색 원을 클릭하면 Intro.py 화면으로 돌아갑니다.

        # 화면을 매끄럽게 전환하기 위해 main_screen을 그대로 사용합니다.
        main_screen.fill((255, 255, 255))  # 배경을 흰색으로 설정합니다.

        # 주황색 원 그리기
        pygame.draw.circle(main_screen, (255, 165, 0), (50, 50), 30)

        # 화면 업데이트
        pygame.display.update()
