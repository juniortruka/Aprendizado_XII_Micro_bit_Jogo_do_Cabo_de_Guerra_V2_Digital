// Cabo de guerra com LED (versão com sons e animações)
let rope = 2

// --- Função: animação de vitória ---
function winAnimation(player: string) {

    // Piscar forte no lado vencedor
    for (let i = 0; i < 3; i++) {
        basic.clearScreen()
        basic.pause(100)

        if (player == "A") {
            for (let y = 0; y < 5; y++) {
                led.plot(0, y)
                led.plot(1, y)
            }
        } else {
            for (let y = 0; y < 5; y++) {
                led.plot(3, y)
                led.plot(4, y)
            }
        }

        basic.pause(120)
    }

    // Toca som de vitória
    music.playTone(880, 200)
    music.playTone(988, 200)
    music.playTone(1100, 250)
    
    basic.clearScreen()
    basic.showString(player + " VENCE!")
    basic.clearScreen()
    basic.pause(1000)
    basic.showIcon(IconNames.Triangle)
    rope = 2  // reinicia o jogo
}

// --- Loop principal ---
basic.forever(function () {

    basic.clearScreen()
    led.plot(Math.round(rope), 2)

    // Vitória do jogador A
    if (rope < 0) {
        winAnimation("A")
    }

    // Vitória do jogador B
    if (rope > 4) {
        winAnimation("B")
    }
})

// --- Jogador A puxa para a esquerda ---
input.onButtonPressed(Button.A, function () {
    rope -= 0.1

    // Som de esforço (grave)
    music.playTone(220, 60)
})

// --- Jogador B puxa para a direita ---
input.onButtonPressed(Button.B, function () {
    rope += 0.1

    // Som de esforço (agudo)
    music.playTone(440, 60)
})

