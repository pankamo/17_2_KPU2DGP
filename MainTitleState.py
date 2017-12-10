from pico2d import *

import game_framework

name = "MainTitleState"
background = None
maintitle = None
text = None

def enter():
    global background, maintitle, text, x, xx, sound, font
    background = load_image('./Images/MainTitleBackground.png')
    maintitle = load_image('./Images/MainTitle.png')
    text = load_image('./Images/MainTitleText.png')
    font = load_font('./Fonts/aMonster.TTF', 40)
    sound_play()

    x = 540
    xx = x * 3
    pass

def sound_play():
    global sound
    sound = load_wav('./Sounds/TitleBGM.wav')
    sound.set_volume(54)
    sound.play()



def exit():
    global background, maintitle, text, sound
    del(background)
    del(maintitle)
    del(text)
    del(sound)
    pass

import LaunchState

def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key)  == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(LaunchState)
    pass


def update(frame_time):
    global x, xx
    x -= 100 * frame_time
    x = clamp(-540,x,1620)
    if x == -540:
        x = 1620
    xx -= 100 * frame_time
    xx = clamp(-540,xx,1620)
    if xx == -540:
        xx = 1620

def draw(frame_time):
    clear_canvas()
    background.draw(x, 300)
    background.draw(xx, 300)
    update(frame_time)
    maintitle.draw(540, 300)
    text.draw(540, 300)
    font.draw(330, 30, '스페이스를 눌러주세요!', (255, 255, 255))
    update_canvas()
    pass

