import pygame
import sys
import help
import game


# 초기화
pygame.init()

# 오디오 초기화
pygame.mixer.init()

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
# 게임 시작 버튼 이미지 불러오기
start_button = pygame.image.load("../graphic/start-button.png")
start_button = pygame.transform.scale(start_button, (200, 50))
start_button_rect = start_button.get_rect(center=(screen_width // 2, 650))

# 이미지의 위치 설정
help_icon_rect = help_icon.get_rect(topleft=(20, 20))
volume_down_icon_rect = volume_down_icon.get_rect(topleft=(1100, 20))
volume_up_icon_rect = volume_up_icon.get_rect(topleft=(1200, 20))

# 배경음악 불러오기 및 재생
pygame.mixer.music.load('../sound/bg.wav')
pygame.mixer.music.play(-1)  # -1은 무한 반복을 의미합니다.

# 현재 볼륨 설정
current_volume = 1.0  # 볼륨은 0.0에서 1.0 사이의 값으로 설정할 수 있습니다.

# 게임 루프
running = True
game_started = False  # 게임이 시작되었는지 여부를 나타내는 플래그 추가

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if help_icon_rect.collidepoint(event.pos):
                help.show_help(screen)
            elif volume_down_icon_rect.collidepoint(event.pos):
                # 볼륨 감소
                current_volume = max(0, current_volume - 0.1)  # 볼륨은 0 아래로 내려가지 않도록 합니다.
                pygame.mixer.music.set_volume(current_volume)
            elif volume_up_icon_rect.collidepoint(event.pos):
                # 볼륨 증가
                current_volume = min(1, current_volume + 0.1)  # 볼륨은 1 이상으로 올라가지 않도록 합니다.
                pygame.mixer.music.set_volume(current_volume)
            if not game_started:
                if start_button_rect.collidepoint(event.pos):
                    game_started = True
                    pygame.mixer.music.stop()  # 배경음악 정지
                    game.main()  # game.py 모듈 실행
                    running = False  # game.py 실행 후 게임 종료

    # 배경 이미지 표시
    screen.blit(background, (0, 0))

    # 이미지 그리기
    screen.blit(help_icon, help_icon_rect)
    screen.blit(volume_down_icon, volume_down_icon_rect)
    screen.blit(volume_up_icon, volume_up_icon_rect)
    # 게임 시작 버튼을 화면에 그립니다.
    screen.blit(start_button, start_button_rect)

    # 화면 업데이트
    pygame.display.update()

# 게임 종료
pygame.quit()
sys.exit()
