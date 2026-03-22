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
        if key == escape_current_key.lower():
            return True
        else:
            return False

    def generate_escape_key():
        global escape_x, escape_y

        key = random.choice(string.ascii_uppercase)

        escape_x = random.uniform(0.1, 0.9)
        escape_y = random.uniform(0.1, 0.9)

        return key

screen escape_game():

    if escape_active:

        add Solid("#00000088")

        text escape_current_key:
            size 100
            xalign escape_x
            yalign escape_y

        text "Time: [escape_time_left:.1f]":
            size 40
            xalign 0.95
            yalign 0.05

        timer 0.1 repeat True action SetVariable("escape_time_left", escape_time_left - 0.1)

        if escape_time_left <= 0:
            timer 0.01 action Return("timeout")

screen escape_input():

    key "K_a" action Return(handle_escape_input("a"))
    key "K_b" action Return(handle_escape_input("b"))
    key "K_c" action Return(handle_escape_input("c"))
    key "K_d" action Return(handle_escape_input("d"))
    key "K_e" action Return(handle_escape_input("e"))
    key "K_f" action Return(handle_escape_input("f"))
    key "K_g" action Return(handle_escape_input("g"))
    key "K_h" action Return(handle_escape_input("h"))
    key "K_i" action Return(handle_escape_input("i"))
    key "K_j" action Return(handle_escape_input("j"))
    key "K_k" action Return(handle_escape_input("k"))
    key "K_l" action Return(handle_escape_input("l"))
    key "K_m" action Return(handle_escape_input("m"))
    key "K_n" action Return(handle_escape_input("n"))
    key "K_o" action Return(handle_escape_input("o"))
    key "K_p" action Return(handle_escape_input("p"))
    key "K_q" action Return(handle_escape_input("q"))
    key "K_r" action Return(handle_escape_input("r"))
    key "K_s" action Return(handle_escape_input("s"))
    key "K_t" action Return(handle_escape_input("t"))
    key "K_u" action Return(handle_escape_input("u"))
    key "K_v" action Return(handle_escape_input("v"))
    key "K_w" action Return(handle_escape_input("w"))
    key "K_x" action Return(handle_escape_input("x"))
    key "K_y" action Return(handle_escape_input("y"))
    key "K_z" action Return(handle_escape_input("z"))
