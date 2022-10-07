def on_gesture_tilt_right():
    if showDot == 0:
        music.start_melody(music.built_in_melody(Melodies.NYAN), MelodyOptions.ONCE)
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)

def on_gesture_logo_up():
    global dotY
    if dotY <= 0:
        dotY = 4
    else:
        dotY += -1
input.on_gesture(Gesture.LOGO_UP, on_gesture_logo_up)

def on_pin_touch_p1():
    global dotX
    if dotX <= 0:
        dotX = 4
    else:
        dotX += -1
input.on_pin_touch_event(TouchPin.P1, input.button_event_down(), on_pin_touch_p1)

def on_button_a():
    if showDot == 0:
        basic.show_leds("""
            # . . . #
                        . # . # .
                        . . . . .
                        # # # # #
                        # . # . #
        """)
input.on_button_event(Button.A, input.button_event_click(), on_button_a)

def on_gesture_tilt_left():
    if showDot == 0:
        music.start_melody(music.built_in_melody(Melodies.FUNERAL), MelodyOptions.ONCE)
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

def on_button_ab():
    if showDot == 0:
        basic.show_number(input.light_level())
        if input.light_level() < 128:
            basic.set_led_color(0xff0000)
        else:
            basic.set_led_color(0x00ff00)
input.on_button_event(Button.AB, input.button_event_click(), on_button_ab)

def on_button_b():
    if showDot == 0:
        images.icon_image(IconNames.SMALL_HEART).show_image(0)
        images.icon_image(IconNames.HEART).show_image(0)
        images.icon_image(IconNames.SMALL_HEART).show_image(0)
input.on_button_event(Button.B, input.button_event_click(), on_button_b)

def on_gesture_logo_down():
    global dotY
    if dotY >= 4:
        dotY = 0
    else:
        dotY += 1
input.on_gesture(Gesture.LOGO_DOWN, on_gesture_logo_down)

def on_pin_touch_p0():
    global showDot
    showDot = 1
input.on_pin_touch_event(TouchPin.P0, input.button_event_down(), on_pin_touch_p0)

def on_pin_touch_p2():
    global dotX
    if dotX >= 4:
        dotX = 0
    else:
        dotX += 1
input.on_pin_touch_event(TouchPin.P2, input.button_event_down(), on_pin_touch_p2)

def on_pin_touch_p3():
    global showDot
    showDot = 0
    basic.clear_screen()
input.on_pin_touch_event(TouchPin.P3, input.button_event_down(), on_pin_touch_p3)

showDot = 0
dotY = 0
dotX = 0
dotX = 2
dotY = 2
showDot = 1

def on_forever():
    if showDot == 1:
        basic.clear_screen()
        led.plot(dotX, dotY)
basic.forever(on_forever)
