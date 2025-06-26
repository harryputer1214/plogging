import pygame #pygame 불러오기
import webbrowser
import sys #sys 불러오기
import random #random 불러오기
import time
from tools import Button
from tools import Timer
from datetime import datetime

#초기화
timer = Timer()
m_time_list = [74, 103, 79, 79, 72, 76, 73, 69] #음악 시간 설정
m_name_list = ['Climbing High (1).mp3', 'Climbing High.mp3', 'Ocean Quest (1).mp3', 'Ocean Quest.mp3', 'Play the Game (1).mp3', 'Play the Game.mp3', 'The Game of Joy (1).mp3', 'The Game of Joy.mp3']
music_number = random.randrange(0, 8)
music_time = m_time_list[music_number]
display_icon = pygame.image.load("ico.ico") 
width, height = 1280, 720
screen = pygame.display.set_mode((width, height)) 
background = pygame.image.load("background.png").convert_alpha() 
menu_bg = pygame.image.load("menu_bg.png").convert_alpha() 
obg = pygame.image.load("over_bg.png").convert_alpha() 
title = "Plogging" 
clock = pygame.time.Clock() 
ttime = 60
up = False
down = False

f = open('highscore.txt', 'r')
hscore_list=f.readline().split()
f.close()
high_score = int(hscore_list[0])

pygame.mixer.init() 
pygame.mixer.music.load(m_name_list[music_number])
pygame.init()
pygame.display.set_icon(display_icon)
pygame.display.set_caption(title)
main_font = pygame.font.SysFont("cambria", 50)

print(high_score)

#get font함수
def get_font(size): 
    return pygame.font.Font("font.en.ttf", size)
def get_font_s(size): 
    return pygame.font.Font("font.ko.ttf", size)

#obj 클래스설정
class obj:
    def __init__(self):
        self.x, self.y = 0, 0
        self.sx, self.sy = 0, 0 

    def put_img(self, address):
        self.ii = address
        if address[-3:] == "png":
            self.img = pygame.image.load(self.ii).convert_alpha()  
        else:
            self.img = pygame.image.load("char1.png")  
        self.sx, self.sy = self.img.get_size()  
    def change_size(self, sx, sy):
        self.img = pygame.transform.scale(self.img, (sx, sy))
        self.sx, self.sy = self.img.get_size()
    def show(self):
        screen.blit(self.img, (self.x, self.y))   
    def trash(self, type):
        self.ttype = type 

def crash(a, b):
    if (a.x-b.sx <= b.x) and (b.x <= a.x+a.sx):
        if (a.y-b.sy <= b.y) and (b.y <= a.y+a.sy):
            return True
        else:
            return False
    else:
        return False

#캐릭터설정
ch = obj()
ch.put_img("char2.png")
ch.change_size(64, 45)
ch.x, ch.y = 126, 400

pygame.mixer.init()  # 음악 초기화
pygame.mixer.music.load(m_name_list[music_number])
pygame.mixer.music.play()  # 초기 음악 재생

timer.restart()

#메뉴 함수
def main_menu():      
    global music_time
    global music_number              
    title = "Plogging - Main Menu"
    pygame.display.set_caption(title)
    while True:
        timert = timer.get_time()
        if music_time <= timert:
            timer.restart()
            music_number = random.randrange(0, 8)
            music_time = m_time_list[music_number]
            pygame.mixer.init()
            pygame.mixer.music.load(m_name_list[music_number])
            pygame.mixer.music.play()
        screen.blit(menu_bg, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PLAY_BUTTON = Button(
            image=pygame.image.load("start-btn.png").convert_alpha(),
            pos=(640, 350),
            text_input="PLAY",
            font=get_font(50),
            base_color="#d7fcd4",
            hovering_color="White",
            size=(350, 70))
        TUTORIAL_BUTTON = Button(
            image=pygame.image.load("start-btn.png").convert_alpha(),
            pos=(640, 450),
            text_input="TUTORIAL",
            font=get_font(45),
            base_color="#d7fcd4",
            hovering_color="White",
            size=(350, 70))
        QUIT_BUTTON = Button(
            image=pygame.image.load("start-btn.png").convert_alpha(),
            pos=(640, 550),
            text_input="QUIT",
            font=get_font(50),
            base_color="#d7fcd4",
            hovering_color="White",
            size=(350, 70))

        title_img = pygame.image.load("title.png").convert_alpha()
        screen.blit(title_img, (340-120, 5))

        for button in [PLAY_BUTTON, TUTORIAL_BUTTON, QUIT_BUTTON]:
            button.changeColor()  
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                f = open('highscore.txt', 'w')
                f.write(str(high_score))
                f.close()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if TUTORIAL_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.mixer.music.stop()
                    webbrowser.open("https://youtu.be/rUOzw_lKDps")
                    #tuto_video()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    f = open('highscore.txt', 'w')
                    f.write(str(high_score))
                    f.close()
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def play():
    global music_time
    global music_number
    global score
    global t_list
    global high_score
    global ch
    ttime = 60
    start_time = datetime.now()
    play_back_button = Button(
        image=pygame.image.load("start-btn.png").convert_alpha(),
        pos=(210, 70),
        text_input="BACK",
        font=get_font(50),
        base_color="White",
        hovering_color="Green",
        size=(350, 70))
    dt_list = []
    score = 0
    t_list = []
    global wh
    wh=True
    global up
    global down
    up, down = False, False
    
    # 캐릭터 위치 초기화
    ch.x, ch.y = 126, 400

    while True:
        timert = timer.get_time()
        if music_time <= timert:
            timer.restart()
            music_number = random.randrange(0, 8)
            music_time = m_time_list[music_number]
            pygame.mixer.init()
            pygame.mixer.music.load(m_name_list[music_number])
            pygame.mixer.music.play()
        screen.blit(menu_bg, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                f = open('highscore.txt', 'w')
                f.write(str(high_score))
                f.close()
                pygame.quit()
                sys.exit()
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
        
        if up == True:
            ch.y -= 1
            if ch.y <= 0:
                ch.y += 2
            if ch.ii == "char1.png":
                ch.put_img("char2.png")
            else:
                ch.put_img("char1.png")
        elif down == True:
            ch.y += 1
            # 캐릭터가 전체 화면 높이까지 갈 수 있도록 수정
            if ch.y >= height - ch.sy:
                ch.y -= 2
            if ch.ii == "char1.png":
                ch.put_img("char2.png")
            else:
                ch.put_img("char1.png")
        for i in range(len(t_list)):
            t = t_list[i]
            l = ch
            if crash(t, l) and i not in dt_list:  # 충돌한 쓰레기 중 이미 처리한 쓰레기는 무시
                score += t_list[i].ttype
                dt_list.append(i)

        if (random.random() > 0.99) and (random.random() > 0.5):
            tr = obj()
            tr.x = 1280
            # 화면 위에서부터 2/5 지점부터 아래까지 쓰레기 생성
            min_y = int(height * 2/5)  # 화면의 2/5 지점 (288픽셀)
            max_y = height - 50        # 화면 아래쪽 - 50픽셀
            tr.y = random.randrange(min_y, max_y)
            if random.random() < 0.80:  # 80% 확률로 pet.png 사용
                tr.trash(3)
                tr.put_img("pet.png")
            else:  # 20% 확률로 p-bag.png 사용
                tr.trash(5)
                tr.put_img("p-bag.png")
            tr.move = 1
            t_list.append(tr)

        if (random.random() > 0.99) and (random.random() > 0.75):
            tr = obj()
            tr.x = 1280
            # 화면 위에서부터 2/5 지점부터 아래까지 쓰레기 생성
            min_y = int(height * 2/5)  # 화면의 2/5 지점 (288픽셀)
            max_y = height - 50        # 화면 아래쪽 - 50픽셀  
            tr.y = random.randrange(min_y, max_y)
            tr.trash(-3)
            tr.put_img("shell.png")
            tr.move = 0.5
            t_list.append(tr)

        # 화면 밖으로 나간 쓰레기들 제거
        t_list = [tr for tr in t_list if tr.x > -tr.sx]

        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        font = get_font(24)
        score_text = font.render("SCORE : {}".format(score), False, (0, 0, 0))
        time_text = font.render("TIME : {}".format(ttime), False, (0, 0, 0))
        # 점수와 시간 위치를 오른쪽 끝으로 이동
        screen.blit(score_text, (width - 200, 20))
        screen.blit(time_text, (width - 200, 40))
        title = "Plogging - Game"

        # 삭제할 쓰레기 객체들의 인덱스를 역순으로 정렬한 후에 삭제
        for dt in sorted(dt_list, reverse=True):
            if dt < len(t_list):
                del t_list[dt]
        dt_list.clear()

        for a in t_list:
            a.x -= a.move
            a.show()
        pygame.display.set_caption(title)
        play_mouse_pos = pygame.mouse.get_pos()
        now_time = datetime.now()
        delta_time = (now_time-start_time).total_seconds()
        ttime = 60 - delta_time

        # 버튼 업데이트
        play_back_button.checkForInput(play_mouse_pos)
        play_back_button.changeColor()
        play_back_button.update(screen)

        # BACK 버튼의 동작 체크
        if play_back_button.checkForInput(play_mouse_pos):
            if pygame.mouse.get_pressed()[0]:  # 마우스 왼쪽 버튼이 클릭된 경우
                main_menu()
        
        if ttime < 0:
            gameover()
            wh=False
        
        ch.show()

        pygame.display.update()
        pygame.display.flip()

def gameover():
    
    global music_time
    global music_number
    global t_list  # 전역 t_list 선언 추가
    
    over_back_button = Button(
        image=pygame.image.load("start-btn.png").convert_alpha(),
        pos=(340, 400),
        text_input="BACK",
        font=get_font(34),
        base_color="White",
        hovering_color="Green",
        size=(240, 80))
    
    global rank
    global high_score
    global com

    if score > high_score:
        high_score = score
    if score >= 250:
        rank = "S"
        com = "멋져요! 훌륭한 해변 정리자! 깨끗한 해변은 누구나의 꿈입니다!"
    elif score >= 200:
        rank = "A"
        com = "수고했어요! 해변에 친환경적으로 기여한 모습이 멋지네요!"
    elif score >= 150:
        rank = "B"
        com = "해변의 미래를 함께 만들어나가요! 더 많은 쓰레기를 주워봅시다!"
    elif score >= 100:
        rank = "C"
        com = "노력은 했지만! 하지만 아직 해변에 더 많은 쓰레기가 남아있어요."
    else:
        rank = "D"
        com = "조금만 더 힘을 내요! 아직 해변 정리에는 부족해요. 계속 도전하세요!"

    if (random.random() > 0.99):
        rank = "★"
        com = "당신은 스페셜 랭크에 당첨 되었습니다!! 축하합니다!" 

    # 게임 종료 시 쓰레기 리스트 초기화
    t_list = []

    while True:
        timert = timer.get_time()
        if music_time <= timert:
            timer.restart()
            music_number = random.randrange(0, 8)
            music_time = m_time_list[music_number]
            pygame.mixer.init()
            pygame.mixer.music.load(m_name_list[music_number])
            pygame.mixer.music.play()
        over_mouse_pos = pygame.mouse.get_pos()
        screen.blit(obg, (0, 0))
        font_big = get_font(79)
        font_small = get_font_s(20)
        font = get_font(39)
        rank_t = font_big.render("{}".format(rank), False, (0, 0, 0))
        screen.blit(rank_t, (425, 50))
        score_t = font.render("{}".format(score), False, (0, 0, 0))
        screen.blit(score_t, (225, 115))
        score_t = font.render("{}".format(high_score), False, (0, 0, 0))
        screen.blit(score_t, (300, 170))
        com_t = font_small.render("{}".format(com), False, (0, 0, 0))
        screen.blit(com_t, (30, 250))

        # 버튼 업데이트
        over_back_button.checkForInput(over_mouse_pos)
        over_back_button.changeColor()
        over_back_button.update(screen)

        # BACK 버튼의 동작 체크
        if over_back_button.checkForInput(over_mouse_pos):
            if pygame.mouse.get_pressed()[0]:  # 마우스 왼쪽 버튼이 클릭된 경우
                main_menu()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                f = open('highscore.txt', 'w')
                f.write(str(high_score))
                f.close()
                pygame.quit()
                sys.exit()
            

        pygame.display.update()
        pygame.display.flip()

main_menu()