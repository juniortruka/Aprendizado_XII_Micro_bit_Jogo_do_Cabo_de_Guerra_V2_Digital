# Cabo de guerra com LED (versão com sons e animações)
rope = 2
# --- Função: animação de vitória ---
# reinicia o jogo
def winAnimation(player: str):
    global rope
    # Piscar forte no lado vencedor
    for i in range(3):
        basic.clear_screen()
        basic.pause(100)
        if player == "A":
            for y in range(5):
                led.plot(0, y)
                led.plot(1, y)
        else:
            for y2 in range(5):
                led.plot(3, y2)
                led.plot(4, y2)
        basic.pause(120)
    # Toca som de vitória
    music.play_tone(880, 200)
    music.play_tone(988, 200)
    music.play_tone(1100, 250)
    basic.clear_screen()
    basic.show_string(player + " VENCE!")
    basic.clear_screen()
    basic.pause(1000)
    basic.show_icon(IconNames.TRIANGLE)
    rope = 2
# --- Loop principal ---

def on_forever():
    basic.clear_screen()
    led.plot(Math.round(rope), 2)
    # Vitória do jogador A
    if rope < 0:
        winAnimation("A")
    # Vitória do jogador B
    if rope > 4:
        winAnimation("B")
basic.forever(on_forever)

# --- Jogador A puxa para a esquerda ---

def on_button_pressed_a():
    global rope
    rope -= 0.1
    # Som de esforço (grave)
    music.play_tone(220, 60)
input.on_button_pressed(Button.A, on_button_pressed_a)

# --- Jogador B puxa para a direita ---

def on_button_pressed_b():
    global rope
    rope += 0.1
    # Som de esforço (agudo)
    music.play_tone(440, 60)
input.on_button_pressed(Button.B, on_button_pressed_b)
