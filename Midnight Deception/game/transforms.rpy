init:
    transform left2:
        xalign 0.3
        yalign 1.0
        anchor (0.5, 1.0)

    transform right2:
        xalign 0.7
        yalign 1.0
        anchor (0.5, 1.0)

    transform left3:
        xalign 0.2
        yalign 1.0
        anchor (0.5, 1.0)

    transform right3:
        xalign 0.8
        yalign 1.0
        anchor (0.5, 1.0)

    transform left4:
        xalign 0.05
        yalign 1.0
        anchor (0.5, 1.0)

    transform right4:
        xalign 0.95
        yalign 1.0
        anchor (0.5, 1.0)
        
    transform left5:
        xalign 0.05
        yalign 1.0
        anchor (0.5, 1.0)

    transform right5:
        xalign 0.95
        yalign 1.0
        anchor (0.5, 1.0)

    transform screen_shake:
        subpixel True
        parallel:
            linear 0.05 xoffset -5 yoffset 3
            linear 0.05 xoffset 4 yoffset -4
            linear 0.05 xoffset -3 yoffset 2
            linear 0.05 xoffset 2 yoffset -3
            repeat
