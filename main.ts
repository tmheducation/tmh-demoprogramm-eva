input.onGesture(Gesture.TiltRight, function () {
    if (showDot == 0) {
        music.startMelody(music.builtInMelody(Melodies.Nyan), MelodyOptions.Once)
    }
})
input.onGesture(Gesture.LogoUp, function () {
    if (dotY <= 0) {
        dotY = 4
    } else {
        dotY += -1
    }
})
input.onPinTouchEvent(TouchPin.P1, input.buttonEventDown(), function () {
    if (dotX <= 0) {
        dotX = 4
    } else {
        dotX += -1
    }
})
input.onButtonEvent(Button.A, input.buttonEventClick(), function () {
    if (showDot == 0) {
        basic.showIcon(IconNames.Angry)
        basic.clearScreen()
    }
})
input.onGesture(Gesture.TiltLeft, function () {
    if (showDot == 0) {
        music.startMelody(music.builtInMelody(Melodies.Funeral), MelodyOptions.Once)
    }
})
input.onButtonEvent(Button.AB, input.buttonEventClick(), function () {
    if (showDot == 0) {
        basic.showNumber(input.lightLevel())
        if (input.lightLevel() < 128) {
            basic.setLedColor(0xff0000)
        } else {
            basic.setLedColor(0x00ff00)
        }
    }
})
input.onButtonEvent(Button.B, input.buttonEventClick(), function () {
    if (showDot == 0) {
        basic.showIcon(IconNames.SmallHeart)
        basic.showIcon(IconNames.Heart)
        basic.showIcon(IconNames.SmallHeart)
        basic.clearScreen()
    }
})
input.onGesture(Gesture.LogoDown, function () {
    if (dotY >= 4) {
        dotY = 0
    } else {
        dotY += 1
    }
})
input.onPinTouchEvent(TouchPin.P0, input.buttonEventDown(), function () {
    showDot = 1
})
input.onPinTouchEvent(TouchPin.P2, input.buttonEventDown(), function () {
    if (dotX >= 4) {
        dotX = 0
    } else {
        dotX += 1
    }
})
input.onPinTouchEvent(TouchPin.P3, input.buttonEventDown(), function () {
    showDot = 0
    basic.clearScreen()
})
let showDot = 0
let dotY = 0
let dotX = 0
dotX = 2
dotY = 2
showDot = 1
basic.forever(function () {
    if (showDot == 1) {
        basic.clearScreen()
        led.plot(dotX, dotY)
    }
})
