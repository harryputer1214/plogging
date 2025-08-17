'''

#Codespace 쓸 때

#VNC
vncserver :1
~/.local/bin/websockify --web ./ 6080 localhost:5901
2개 입력후 브라우저에서 접속    https://fictional-space-engine-4j7gg4p7g5xfjr5r-6080.app.github.dev/vnc.html

#VNC안 터미널에서 
sudo apt-get update
sudo apt-get install -y pulseaudio
pulseaudio --start
cd ~/workspaces/plogging
python3 main.py

#가상 오디오
pulseaudio --start

https://github.com/codespaces?repository_id=994197085
들어가서 'Stop codespace'하고 마치기

#python프로그램 종료 시
터미널에서    'Ctrl + C'

#저장
cd /workspaces/plogging
git add .
git commit -m "작업 내용 설명"
git push

'''






#Plogging#

import pygame #pygame 불러오기
import webbrowser #webbrowser 불러오기
import sys #sys 불러오기
import random #random 불러오기
import time #time 불러오기
from assets.modules.tools import Button #Button 불러오기
from assets.modules.tools import Timer #Timer 불러오기
from datetime import datetime #datetime 불러오기

#초기화
timer = Timer()
m_time_list = [74, 103, 79, 79, 72, 76, 73, 69] #음악 시간 설정
m_name_list = ['assets/musics/Climbing High (1).mp3', 'assets/musics/Climbing High.mp3', 'assets/musics/Ocean Quest (1).mp3', 'assets/musics/Ocean Quest.mp3', 'assets/musics/Play the Game (1).mp3', 'assets/musics/Play the Game.mp3', 'assets/musics/The Game of Joy (1).mp3', 'assets/musics/The Game of Joy.mp3']
music_number = random.randrange(0, 8)
music_time = m_time_list[music_number]
display_icon = pygame.image.load("assets/icons/ico.ico") 
width, height = 1280, 720
screen = pygame.display.set_mode((width, height)) 
background = pygame.image.load("assets/images/backgrounds/background.png").convert_alpha() 
park_bg = pygame.image.load("assets/images/backgrounds/park_bg.png").convert_alpha() 
city_bg = pygame.image.load("assets/images/backgrounds/city_bg.png").convert_alpha() 
menu_bg = pygame.image.load("assets/images/backgrounds/menu_bg.png").convert_alpha() 
obg = pygame.image.load("assets/images/backgrounds/over_bg.png").convert_alpha() 
title = "Plogging" 
clock = pygame.time.Clock() 
ttime = 60
up = False
down = False
tuto_img = ['assets/images/tutorials/1.jpg', 'assets/images/tutorials/2.jpg', 'assets/images/tutorials/3.jpg', 'assets/images/tutorials/4.jpg', 'assets/images/tutorials/5.jpg', 'assets/images/tutorials/6.jpg', 'assets/images/tutorials/7.jpg', 'assets/images/tutorials/8.jpg', 'assets/images/tutorials/9.jpg']

#최고점수 작성
f = open('assets/highscore.txt', 'r')
hscore_list=f.readline().split()
f.close()
high_score = int(hscore_list[0])

#pygame 초기화
pygame.mixer.init() 
pygame.mixer.music.load(m_name_list[music_number])
pygame.init()
pygame.display.set_icon(display_icon)
pygame.display.set_caption(title)
main_font = pygame.font.SysFont("cambria", 50)

#최고점수 출력
print(high_score)

#get font함수
def get_font(size): 
    return pygame.font.Font("assets/fonts/font.en.ttf", size)
def get_font_s(size): 
    return pygame.font.Font("assets/fonts/font.ko.ttf", size)

#obj 클래스설정
class obj:
    def __init__(self):
        self.x, self.y = 0, 0
        self.sx, self.sy = 0, 0 

    def put_img(self, address):
        self.ii = address
        #print(self.ii)
        if address[-3:] == "png":
            self.img = pygame.image.load(self.ii).convert_alpha()  
        else:
            self.img = pygame.image.load("assets/images/characters/char1.png")  
        self.sx, self.sy = self.img.get_size()  
    def change_size(self, sx, sy):
        self.img = pygame.transform.scale(self.img, (sx, sy))
        self.sx, self.sy = self.img.get_size()
    def show(self):
        screen.blit(self.img, (self.x, self.y))   
    def trash(self, type):
        self.ttype = type 

def tuto_video():
    pygame.mixer.music.stop()
    webbrowser.open("https://youtu.be/rUOzw_lKDps")
    pygame.mixer.music.play()

#충돌 함수
def crash(a, b): #a: 쓰레기, b: 캐릭터
    if (a.x-b.sx <= b.x) and (b.x <= a.x+a.sx):
        if (a.y-b.sy <= b.y) and (b.y <= a.y+a.sy):
            return True
        else:
            return False
    else:
        return False

#캐릭터 설정
ch = obj()
ch.put_img("assets/images/characters/char2.png")
ch.change_size(64, 45)
ch.x, ch.y = 126, 400

pygame.mixer.init()  # 음악 초기화
pygame.mixer.music.load(m_name_list[music_number]) # 음악 파일 로드
pygame.mixer.music.play()  # 초기 음악 재생

# 타이머 초기화
timer.restart()

def tutorial(): 
    # 전역 변수
    global music_time
    global music_number

    # pygame 창 이름
    title = "Plogging - Tutorial"
    pygame.display.set_caption(title)

    # 변수 리셋
    tuto_img_num = 0

    while True:

        # 음악 타이머
        timert = timer.get_time()
        if music_time <= timert:
            timer.restart()
            music_number = random.randrange(0, 8)
            music_time = m_time_list[music_number]
            pygame.mixer.init()
            pygame.mixer.music.load(m_name_list[music_number])
            pygame.mixer.music.play()

        # 화면 설정
        tuto_img_file = pygame.image.load(tuto_img[tuto_img_num])
        screen.blit(tuto_img_file, (0, 0))

        # 마우스 위치
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        # 버튼 설정
        BACK_BUTTON = Button(
            image=pygame.image.load("assets/images/buttons/exit.png").convert_alpha(),
            pos=(1220, 60),
            text_input="",
            font=get_font(50),
            base_color="#ffffff",
            hovering_color="LightGray",
            size=(70, 70))
        PERV_BUTTON = Button(
            image=pygame.image.load("assets/images/buttons/perv.png").convert_alpha(),
            pos=(70, 660),
            text_input="",
            font=get_font(45),
            base_color="#ffffff",
            hovering_color="LightGray",
            size=(70, 70))
        NEXT_BUTTON = Button(
            image=pygame.image.load("assets/images/buttons/next.png").convert_alpha(),
            pos=(1210, 660),
            text_input="",
            font=get_font(50),
            base_color="#ffffff",
            hovering_color="LightGray",
            size=(70, 70))

        # BACK_BUTTON 버튼 색 바꾸기
        BACK_BUTTON.checkForInput(MENU_MOUSE_POS)
        BACK_BUTTON.changeColor()
        BACK_BUTTON.update(screen)

        # PERV_BUTTON 버튼 색 바꾸기
        PERV_BUTTON.checkForInput(MENU_MOUSE_POS)
        PERV_BUTTON.changeColor()
        PERV_BUTTON.update(screen)

        # NEXT_BUTTON 버튼 색 바꾸기
        NEXT_BUTTON.checkForInput(MENU_MOUSE_POS)
        NEXT_BUTTON.changeColor()
        NEXT_BUTTON.update(screen)
        
        # 버튼 클릭 이벤트
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                f = open('assets/highscore.txt', 'w')
                f.write(str(high_score))
                f.close()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_BUTTON.checkForInput(MENU_MOUSE_POS):
                    main_menu()
                if PERV_BUTTON.checkForInput(MENU_MOUSE_POS):
                    tuto_img_num -= 1
                if NEXT_BUTTON.checkForInput(MENU_MOUSE_POS):\
                    tuto_img_num += 1

        if tuto_img_num < 0:
            tuto_img_num = 0
        if tuto_img_num >= len(tuto_img):
            tuto_img_num = len(tuto_img) - 1

        pygame.display.update()

#메뉴 함수
def main_menu():      
    # 전역 변수
    global music_time
    global music_number

    # pygame 창 이름
    title = "Plogging - Main Menu"
    pygame.display.set_caption(title)

    while True:

        # 음악 타이머
        timert = timer.get_time()
        if music_time <= timert:
            timer.restart()
            music_number = random.randrange(0, 8)
            music_time = m_time_list[music_number]
            pygame.mixer.init()
            pygame.mixer.music.load(m_name_list[music_number])
            pygame.mixer.music.play()

        # 화면 설정
        screen.blit(menu_bg, (0, 0))

        # 마우스 위치
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        # 버튼 설정
        PLAY_BUTTON = Button(
            image=pygame.image.load("assets/images/buttons/btn.png").convert_alpha(),
            pos=(640, 350),
            text_input="PLAY",
            font=get_font(50),
            base_color="#ffffff",
            hovering_color="LightGray",
            size=(350, 70))
        TUTORIAL_BUTTON = Button(
            image=pygame.image.load("assets/images/buttons/btn.png").convert_alpha(),
            pos=(640, 450),
            text_input="TUTORIAL",
            font=get_font(45),
            base_color="#ffffff",
            hovering_color="LightGray",
            size=(350, 70))
        QUIT_BUTTON = Button(
            image=pygame.image.load("assets/images/buttons/btn.png").convert_alpha(),
            pos=(640, 550),
            text_input="QUIT",
            font=get_font(50),
            base_color="#ffffff",
            hovering_color="LightGray",
            size=(350, 70))

        # 타이틀 이미지 설정
        title_img = pygame.image.load("assets/images/titles/title.png").convert_alpha()
        title_img = pygame.transform.scale(title_img, (360, 240)) 
        screen.blit(title_img, (640-180, 30))

        # play 버튼 색 바꾸기
        PLAY_BUTTON.checkForInput(MENU_MOUSE_POS)
        PLAY_BUTTON.changeColor()
        PLAY_BUTTON.update(screen)

        # tutorial 버튼 색 바꾸기
        TUTORIAL_BUTTON.checkForInput(MENU_MOUSE_POS)
        TUTORIAL_BUTTON.changeColor()
        TUTORIAL_BUTTON.update(screen)

        # quit 버튼 색 바꾸기
        QUIT_BUTTON.checkForInput(MENU_MOUSE_POS)
        QUIT_BUTTON.changeColor()
        QUIT_BUTTON.update(screen)
        
        # 버튼 클릭 이벤트
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                f = open('assets/highscore.txt', 'w')
                f.write(str(high_score))
                f.close()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    level_menu()
                if TUTORIAL_BUTTON.checkForInput(MENU_MOUSE_POS):
                    tutorial()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    f = open('assets/highscore.txt', 'w')
                    f.write(str(high_score))
                    f.close()
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def level_menu():      
    # 전역 변수
    global music_time
    global music_number

    # pygame 창 이름
    title = "Plogging - Level Menu"
    pygame.display.set_caption(title)

    while True:

        # 음악 타이머
        timert = timer.get_time()
        if music_time <= timert:
            timer.restart()
            music_number = random.randrange(0, 8)
            music_time = m_time_list[music_number]
            pygame.mixer.init()
            pygame.mixer.music.load(m_name_list[music_number])
            pygame.mixer.music.play()

        # 화면 설정
        screen.blit(menu_bg, (0, 0))

        # 마우스 위치
        LEVEL_MOUSE_POS = pygame.mouse.get_pos()

        # 버튼 설정
        OCEAN_BUTTON = Button(
            image=pygame.image.load("assets/images/buttons/btn.png").convert_alpha(),
            pos=(640, 300),
            text_input="EASY(OCEAN)",
            font=get_font(50),
            base_color="#ffffff",
            hovering_color="LightGray",
            size=(350, 70))
        
        PARK_BUTTON = Button(
            image=pygame.image.load("assets/images/buttons/btn.png").convert_alpha(),
            pos=(640, 400),
            text_input="NORMAL(PARK)",
            font=get_font(50),
            base_color="#ffffff",
            hovering_color="LightGray",
            size=(350, 70))

        CITY_BUTTON = Button(
            image=pygame.image.load("assets/images/buttons/btn.png").convert_alpha(),
            pos=(640, 500),
            text_input="HARD(CITY)",
            font=get_font(50),
            base_color="#ffffff",
            hovering_color="LightGray",
            size=(350, 70))
        
        LEVEL_BACK_BUTTON = Button(
            image=pygame.image.load("assets/images/buttons/btn.png").convert_alpha(),
            pos=(640, 650),
            text_input="BACK",
            font=get_font(50),
            base_color="#ffffff",
            hovering_color="LightGray",
            size=(350, 70))
        
        # 타이틀 이미지 설정
        select_level_img = pygame.image.load("assets/images/titles/select_level.png").convert_alpha()
        select_level_img = pygame.transform.scale(select_level_img, (360, 240)) 
        screen.blit(select_level_img, (640-180, 20))

        # play 버튼 색 바꾸기
        OCEAN_BUTTON.checkForInput(LEVEL_MOUSE_POS)
        OCEAN_BUTTON.changeColor()
        OCEAN_BUTTON.update(screen)

        # tutorial 버튼 색 바꾸기
        PARK_BUTTON.checkForInput(LEVEL_MOUSE_POS)
        PARK_BUTTON.changeColor()
        PARK_BUTTON.update(screen)

        # quit 버튼 색 바꾸기
        CITY_BUTTON.checkForInput(LEVEL_MOUSE_POS)
        CITY_BUTTON.changeColor()
        CITY_BUTTON.update(screen)

        LEVEL_BACK_BUTTON.checkForInput(LEVEL_MOUSE_POS)
        LEVEL_BACK_BUTTON.changeColor()
        LEVEL_BACK_BUTTON.update(screen)

        # 버튼 클릭 이벤트
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                f = open('assets/highscore.txt', 'w')
                f.write(str(high_score))
                f.close()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OCEAN_BUTTON.checkForInput(LEVEL_MOUSE_POS):
                    ocean()
                if PARK_BUTTON.checkForInput(LEVEL_MOUSE_POS):
                    park()
                if CITY_BUTTON.checkForInput(LEVEL_MOUSE_POS):
                    city()
                if LEVEL_BACK_BUTTON.checkForInput(LEVEL_MOUSE_POS):
                    main_menu()

        pygame.display.update()


# 플레이 함수
def ocean():
    # 변수
    global music_time
    global music_number
    global score
    global t_list
    global high_score
    global ch
    global up
    global down
    global wh
    wh=True
    up, down = False, False
    score = 0

    # 리스트
    dt_list = [] # 지울 쓰레기 리스트
    t_list = [] # 쓰레기 리스트 초기화

    # 시간 설정
    ttime = 60
    start_time = datetime.now()

    # 나가기 버튼
    play_back_button = Button(
        image=pygame.image.load("assets/images/buttons/play-back-btn.png").convert_alpha(),
        pos=(210, 70),
        text_input="BACK",
        font=get_font(50),
        base_color="White",
        hovering_color="LightGray",
        size=(350, 70))
    
    # 캐릭터 위치 초기화
    ch.x, ch.y = 126, 400

    while True:
        # 음악 타이머
        timert = timer.get_time()
        if music_time <= timert:
            timer.restart()
            music_number = random.randrange(0, 8)
            music_time = m_time_list[music_number]
            pygame.mixer.init()
            pygame.mixer.music.load(m_name_list[music_number])
            pygame.mixer.music.play()

        # 화면 설정
        screen.blit(menu_bg, (0, 0))

        # x 누를 때 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                f = open('assets/highscore.txt', 'w')
                f.write(str(high_score))
                f.close()
                pygame.quit()
                sys.exit()

            # 키보드 입력
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    up = True
                    #ch.put_img("char2.png")    
                if event.key == pygame.K_DOWN:
                    down = True
                    #ch.put_img("char2.png")
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    up = False
                if event.key == pygame.K_DOWN:
                    down = False


            # 테스트용
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    gameover()


        # 캐릭터 이동
        if up == True:
            ch.y -= 1
            if ch.y <= int(height * 2/5):
                ch.y += 6
            if ch.ii == "assets/images/characters/char1.png":
                ch.put_img("assets/images/characters/char2.png")
            else:
                ch.put_img("assets/images/characters/char1.png")
        elif down == True:
            ch.y += 1
            if ch.y >= height - ch.sy:
                ch.y -= 6
            if ch.ii == "assets/images/characters/char1.png":
                ch.put_img("assets/images/characters/char2.png")
            else:
                ch.put_img("assets/images/characters/char1.png")

        # 쓰레기 충돌
        for i in range(len(t_list)):
            t = t_list[i]
            l = ch
            if crash(t, l) and i not in dt_list: 
                score += t_list[i].ttype
                dt_list.append(i)

        # 쓰레기 생성
        if (random.random() > 0.99) and (random.random() > 0.5):
            tr = obj()
            tr.x = 1280
            min_y = int(height * 2/5)
            max_y = height - 50
            tr.y = random.randrange(min_y, max_y)

            # 쓰레기 종류 설정
            if random.random() < 0.80:
                tr.trash(3)
                tr.put_img("assets/images/trashes/pet.png")
            else:
                tr.trash(5)
                tr.put_img("assets/images/trashes/p-bag.png")
            tr.move = 1
            t_list.append(tr)


        # 조개 생성
        if (random.random() > 0.99) and (random.random() > 0.75) and (random.random() > 0.25):
            tr = obj()
            tr.x = 1280
            min_y = int(height * 2/5)
            max_y = height - 50
            tr.y = random.randrange(min_y, max_y)
            tr.trash(-3)
            tr.put_img("assets/images/trashes/shell.png")
            tr.move = 0.5
            t_list.append(tr)

        # 나간 쓰레기 삭제
        t_list = [tr for tr in t_list if tr.x > -tr.sx]

        # 화면 설정
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))

        # 스코어/시간
        font = get_font(36)
        score_text = font.render("SCORE : {}".format(score), False, (0, 0, 0))
        time_text = font.render("TIME : {}".format(ttime), False, (0, 0, 0))
        screen.blit(score_text, (width - 250, 35))
        screen.blit(time_text, (width - 250, 70))
        title = "Plogging - Play(Easy Mode)"

        # 쓰레기 삭제
        for dt in sorted(dt_list, reverse=True):
            if dt < len(t_list):
                del t_list[dt]
        dt_list.clear()

        # 쓰레기 이동
        for a in t_list:
            a.x -= a.move
            a.show()

        # pygame 창 이름 설정
        pygame.display.set_caption(title)

        #마우스 위치
        play_mouse_pos = pygame.mouse.get_pos()

        # 시간 계산
        now_time = datetime.now()
        delta_time = (now_time-start_time).total_seconds()
        ttime = 60 - delta_time

        # 버튼 업데이트
        play_back_button.checkForInput(play_mouse_pos)
        play_back_button.changeColor()
        play_back_button.update(screen)

        # BACK 버튼 체크
        if play_back_button.checkForInput(play_mouse_pos):
            if pygame.mouse.get_pressed()[0]:  # 마우스 왼쪽 버튼이 클릭된 경우
                level_menu()
        
        # 게임오버
        if ttime < 0:
            gameover()
            wh=False
        
        #캐릭터 보여주기
        ch.show()

        # 화면 업데이트
        pygame.display.update()
        pygame.display.flip()

def park():
    # 변수
    global music_time
    global music_number
    global score
    global t_list
    global high_score
    global ch
    global up
    global down
    global wh
    wh=True
    up, down = False, False
    score = 0

    # 리스트
    dt_list = [] # 지울 쓰레기 리스트
    t_list = [] # 쓰레기 리스트 초기화

    # 시간 설정
    ttime = 60
    start_time = datetime.now()

    # 나가기 버튼
    play_back_button = Button(
        image=pygame.image.load("assets/images/buttons/play-back-btn.png").convert_alpha(),
        pos=(210, 70),
        text_input="BACK",
        font=get_font(50),
        base_color="White",
        hovering_color="LightGray",
        size=(350, 70))
    
    # 캐릭터 위치 초기화
    ch.x, ch.y = 126, 400

    while True:
        # 음악 타이머
        timert = timer.get_time()
        if music_time <= timert:
            timer.restart()
            music_number = random.randrange(0, 8)
            music_time = m_time_list[music_number]
            pygame.mixer.init()
            pygame.mixer.music.load(m_name_list[music_number])
            pygame.mixer.music.play()

        # 화면 설정
        screen.blit(menu_bg, (0, 0))

        # x 누를 때 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                f = open('assets/highscore.txt', 'w')
                f.write(str(high_score))
                f.close()
                pygame.quit()
                sys.exit()

            # 키보드 입력
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    up = True
                    #ch.put_img("char2.png")    
                if event.key == pygame.K_DOWN:
                    down = True
                    #ch.put_img("char2.png")
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    up = False
                if event.key == pygame.K_DOWN:
                    down = False


            # 테스트용
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    gameover()


        # 캐릭터 이동
        if up == True:
            ch.y -= 1.5
            if ch.y <= int(height * 2/5):
                ch.y += 6
            if ch.ii == "assets/images/characters/char1.png":
                ch.put_img("assets/images/characters/char2.png")
            else:
                ch.put_img("assets/images/characters/char1.png")
        elif down == True:
            ch.y += 1.5
            if ch.y >= height - ch.sy:
                ch.y -= 6
            if ch.ii == "assets/images/characters/char1.png":
                ch.put_img("assets/images/characters/char2.png")
            else:
                ch.put_img("assets/images/characters/char1.png")

        # 쓰레기 충돌
        for i in range(len(t_list)):
            t = t_list[i]
            l = ch
            if crash(t, l) and i not in dt_list: 
                score += t_list[i].ttype
                dt_list.append(i)

        # 쓰레기 생성
        if (random.random() > 0.99) and (random.random() > 0.25):
            tr = obj()
            tr.x = 1280
            min_y = int(height * 1/2)
            max_y = height - 50
            tr.y = random.randrange(min_y, max_y)

            # 쓰레기 종류 설정
            if random.random() < 0.75:
                tr.trash(5)
                tr.put_img("assets/images/trashes/pet.png")
            else:
                tr.trash(7)
                tr.put_img("assets/images/trashes/smoke.png")
            tr.move = 2
            t_list.append(tr)


        # 돈 생성
        if (random.random() > 0.99) and (random.random() > 0.375):
            tr = obj()
            tr.x = 1280
            min_y = int(height * 1/2)
            max_y = height - 50
            tr.y = random.randrange(min_y, max_y)
            tr.trash(-6)
            tr.put_img("assets/images/trashes/money.png")
            tr.move = 1
            t_list.append(tr)

        # 나간 쓰레기 삭제
        t_list = [tr for tr in t_list if tr.x > -tr.sx]

        # 화면 설정
        screen.fill((0, 0, 0))
        screen.blit(park_bg, (0, 0))

        # 스코어/시간
        font = get_font(36)
        score_text = font.render("SCORE : {}".format(score), False, (0, 0, 0))
        time_text = font.render("TIME : {}".format(ttime), False, (0, 0, 0))
        screen.blit(score_text, (width - 250, 35))
        screen.blit(time_text, (width - 250, 70))
        title = "Plogging - Game(Normal Mode)"

        # 쓰레기 삭제
        for dt in sorted(dt_list, reverse=True):
            if dt < len(t_list):
                del t_list[dt]
        dt_list.clear()

        # 쓰레기 이동
        for a in t_list:
            a.x -= a.move
            a.show()

        # pygame 창 이름 설정
        pygame.display.set_caption(title)

        #마우스 위치
        play_mouse_pos = pygame.mouse.get_pos()

        # 시간 계산
        now_time = datetime.now()
        delta_time = (now_time-start_time).total_seconds()
        ttime = 60 - delta_time

        # 버튼 업데이트
        play_back_button.checkForInput(play_mouse_pos)
        play_back_button.changeColor()
        play_back_button.update(screen)

        # BACK 버튼 체크
        if play_back_button.checkForInput(play_mouse_pos):
            if pygame.mouse.get_pressed()[0]:  # 마우스 왼쪽 버튼이 클릭된 경우
                level_menu()
        
        # 게임오버
        if ttime < 0:
            gameover()
            wh=False
        
        #캐릭터 보여주기
        ch.show()

        # 화면 업데이트
        pygame.display.update()
        pygame.display.flip()

def city():
    # 변수
    global music_time
    global music_number
    global score
    global t_list
    global high_score
    global ch
    global up
    global down
    global wh
    wh=True
    up, down = False, False
    score = 0

    # 리스트
    dt_list = [] # 지울 쓰레기 리스트
    t_list = [] # 쓰레기 리스트 초기화

    # 시간 설정
    ttime = 60
    start_time = datetime.now()

    # 나가기 버튼
    play_back_button = Button(
        image=pygame.image.load("assets/images/buttons/play-back-btn.png").convert_alpha(),
        pos=(210, 70),
        text_input="BACK",
        font=get_font(50),
        base_color="White",
        hovering_color="LightGray",
        size=(350, 70))
    
    # 캐릭터 위치 초기화
    ch.x, ch.y = 126, 400

    while True:
        # 음악 타이머
        timert = timer.get_time()
        if music_time <= timert:
            timer.restart()
            music_number = random.randrange(0, 8)
            music_time = m_time_list[music_number]
            pygame.mixer.init()
            pygame.mixer.music.load(m_name_list[music_number])
            pygame.mixer.music.play()

        # 화면 설정
        screen.blit(menu_bg, (0, 0))

        # x 누를 때 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                f = open('assets/highscore.txt', 'w')
                f.write(str(high_score))
                f.close()
                pygame.quit()
                sys.exit()

            # 키보드 입력
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    up = True
                    #ch.put_img("char2.png")    
                if event.key == pygame.K_DOWN:
                    down = True
                    #ch.put_img("char2.png")
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    up = False
                if event.key == pygame.K_DOWN:
                    down = False


            # 테스트용
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    gameover()


        # 캐릭터 이동
        if up == True:
            ch.y -= 2
            if ch.y <= int(height * 2/5):
                ch.y += 6
            if ch.ii == "assets/images/characters/char1.png":
                ch.put_img("assets/images/characters/char2.png")
            else:
                ch.put_img("assets/images/characters/char1.png")
        elif down == True:
            ch.y += 2
            if ch.y >= height - ch.sy:
                ch.y -= 6
            if ch.ii == "assets/images/characters/char1.png":
                ch.put_img("assets/images/characters/char2.png")
            else:
                ch.put_img("assets/images/characters/char1.png")

        # 쓰레기 충돌
        for i in range(len(t_list)):
            t = t_list[i]
            l = ch
            if crash(t, l) and i not in dt_list: 
                score += t_list[i].ttype
                dt_list.append(i)

        # 쓰레기 생성
        if (random.random() > 0.99) and (random.random() > 0.125):
            tr = obj()
            tr.x = 1280
            min_y = int(height * 2/5)
            max_y = height - 50
            tr.y = random.randrange(min_y, max_y)

            # 쓰레기 종류 설정
            if random.random() < 0.80:
                tr.trash(7)
                tr.put_img("assets/images/trashes/smoke.png")
            else:
                tr.trash(9)
                tr.put_img("assets/images/trashes/p-cup.png")
            tr.move = 4
            t_list.append(tr)


        # no쓰레기 생성
        if (random.random() > 0.99) and (random.random() > 0.25) :
            tr = obj()
            tr.x = 1280
            min_y = int(height * 2/5)
            max_y = height - 50
            tr.y = random.randrange(min_y, max_y)
            # no쓰레기 종류 설정
            if random.random() < 0.80:
                tr.trash(-6)
                tr.put_img("assets/images/trashes/money.png")
            else:
                tr.trash(-8)
                tr.put_img("assets/images/trashes/cat.png")
            tr.move = 3
            t_list.append(tr)

        # 나간 쓰레기 삭제
        t_list = [tr for tr in t_list if tr.x > -tr.sx]

        # 화면 설정
        screen.fill((0, 0, 0))
        screen.blit(city_bg, (0, 0))

        # 스코어/시간
        font = get_font(36)
        score_text = font.render("SCORE : {}".format(score), False, (0, 0, 0))
        time_text = font.render("TIME : {}".format(ttime), False, (0, 0, 0))
        screen.blit(score_text, (width - 250, 35))
        screen.blit(time_text, (width - 250, 70))
        title = "Plogging - Game(Hard Mode)"

        # 쓰레기 삭제
        for dt in sorted(dt_list, reverse=True):
            if dt < len(t_list):
                del t_list[dt]
        dt_list.clear()

        # 쓰레기 이동
        for a in t_list:
            a.x -= a.move
            a.show()

        # pygame 창 이름 설정
        pygame.display.set_caption(title)

        #마우스 위치
        play_mouse_pos = pygame.mouse.get_pos()

        # 시간 계산
        now_time = datetime.now()
        delta_time = (now_time-start_time).total_seconds()
        ttime = 60 - delta_time

        # 버튼 업데이트
        play_back_button.checkForInput(play_mouse_pos)
        play_back_button.changeColor()
        play_back_button.update(screen)

        # BACK 버튼 체크
        if play_back_button.checkForInput(play_mouse_pos):
            if pygame.mouse.get_pressed()[0]:  # 마우스 왼쪽 버튼이 클릭된 경우
                level_menu()
        
        # 게임오버
        if ttime < 0:
            gameover()
            wh=False
        
        #캐릭터 보여주기
        ch.show()

        # 화면 업데이트
        pygame.display.update()
        pygame.display.flip()

# 게임 오버 함수
def gameover():
    # 변수
    global music_time
    global music_number
    global t_list
    global rank
    global high_score
    global com
    
    # 돌아가기 버튼
    over_back_button = Button(
        image=pygame.image.load("assets/images/buttons/over-back-btn.png").convert_alpha(),
        pos=(640, 580),
        text_input="MAIN MENU",
        font=get_font(40),
        base_color="White",
        hovering_color="LightGray",
        size=(240, 80))

    # 랭크 설정
    if score > high_score:
        high_score = score
    if score >= 250:
        rank = "S"
        com = "멋져요! 훌륭한 거리 정리자! 깨끗한 거리는 누구나의 꿈입니다!"
    elif score >= 200:
        rank = "A"
        com = "수고했어요! 거리에 친환경적으로 기여한 모습이 멋지네요!"
    elif score >= 150:
        rank = "B"
        com = "꺠끗한 거리를 함께 만들어나가요! 더 많은 쓰레기를 주워봅시다!"
    elif score >= 100:
        rank = "C"
        com = "노력은 했지만! 하지만 아직 거리에 더 많은 쓰레기가 남아있어요."
    else:
        rank = "D"
        com = "조금만 더 힘을 내요! 아직 거리 정리에는 부족해요. 계속 도전하세요!"

    if (random.random() > 0.99):
        rank = "★"
        com = "와우! 당신은 거리 정리의 슈퍼스타입니다! (스페셜 랭크)" 

    # 쓰레기 리스트 초기화
    t_list = []

    while True:
        # 음악 타이머
        timert = timer.get_time()
        if music_time <= timert:
            timer.restart()
            music_number = random.randrange(0, 8)
            music_time = m_time_list[music_number]
            pygame.mixer.init()
            pygame.mixer.music.load(m_name_list[music_number])
            pygame.mixer.music.play()
        
        # 마우스 위치
        over_mouse_pos = pygame.mouse.get_pos()

        # 화면 설정
        screen.blit(obg, (0, 0))

        #폰트/글씨
        font_big = get_font(256)
        font_small = get_font_s(36)
        font = get_font(39)

        # 랭크 글씨
        rank_t = font_big.render("{}".format(rank), False, (0, 0, 0))
        screen.blit(rank_t, (960, 100))

        # 점수 글씨
        score_t = font.render("{}".format(score), False, (0, 0, 0))
        screen.blit(score_t, (300, 205))

        # 최고 점수 글씨
        score_t = font.render("{}".format(high_score), False, (0, 0, 0))
        screen.blit(score_t, (410, 265))

        # 코멘트 글씨
        com_t = font_small.render("{}".format(com), False, (0, 0, 0))
        screen.blit(com_t, (100, 400))

        # 버튼 업데이트
        over_back_button.checkForInput(over_mouse_pos)
        over_back_button.changeColor()
        over_back_button.update(screen)

        # BACK 버튼 체크
        if over_back_button.checkForInput(over_mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                main_menu()

        # x 누를 때
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                f = open('assets/highscore.txt', 'w')
                f.write(str(high_score))
                f.close()
                pygame.quit()
                sys.exit()
            
        # 화면 업데이트
        pygame.display.update()
        pygame.display.flip()

# 메인 메뉴 실행
main_menu()