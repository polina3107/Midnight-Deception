default escape_current_key = ""
default escape_active = False
default escape_x = 0.5
default escape_y = 0.5
default escape_time_left = 10.0
default escape_hits = 0
default escape_target = 5

init python:
    import random
    import string

    def handle_escape_input(key):
        return key == escape_current_key.lower()

    def generate_escape_key():
        global escape_x, escape_y

        key = random.choice(string.ascii_uppercase)

        escape_x = random.uniform(0.1, 0.9)
        escape_y = random.uniform(0.1, 0.9)

        return key

screen escape_game():

    if escape_active:

        fixed at screen_shake:

            add Solid("#00000088")

            text escape_current_key:
                size 100
                xalign escape_x
                yalign escape_y

            text "Time: [escape_time_left:.1f]":
                size 40
                xalign 0.95
                yalign 0.05

        timer 0.1 repeat True action SetVariable("escape_time_left", max(0, escape_time_left - 0.1))

        if escape_time_left <= 0:
            timer 0.01 action Return("timeout")

screen escape_input():

    for letter in "abcdefghijklmnopqrstuvwxyz":
        key "K_" + letter action Return(handle_escape_input(letter))
