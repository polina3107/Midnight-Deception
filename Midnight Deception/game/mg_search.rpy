default screen_tooltip = ""

default clue1_found = False
default clue2_found = False
default clue3_found = False
default clue4_found = False
default clue5_found = False

default penalty_token = 0
default penalty_text = ""

default search_timer = 600

screen mg_search_intro():

    modal True

    timer 5.0 action Return()

    frame:

        xalign 0.5
        yalign 0.5

        background "#000000cc"

        padding (50, 40)

        vbox:

            spacing 25

            text "Search for Clues":
                size 50
                color "#fff"
                xalign 0.5

            text "Search Daniel’s office and find hidden evidence connected to the events of tonight.":
                size 28
                color "#ddd"

                text_align 0.5
                xalign 0.5

            text "The investigation will begin shortly...":
                size 24
                color "#999"

                xalign 0.5

screen search_object(idle_img, hover_img, tooltip_text, clue_variable=None):

    imagebutton:

        idle idle_img
        hover hover_img

        focus_mask True

        hovered SetVariable("screen_tooltip", tooltip_text)
        unhovered SetVariable("screen_tooltip", "")

        if clue_variable == "clue1":
            action SetVariable("clue1_found", True)

        elif clue_variable == "clue2":
            action SetVariable("clue2_found", True)

        elif clue_variable == "clue3":
            action SetVariable("clue3_found", True)

        elif clue_variable == "clue4":
            action SetVariable("clue4_found", True)

        elif clue_variable == "clue5":
            action SetVariable("clue5_found", True)

        else:
            action [
                SetVariable("search_timer", max(0, search_timer - 10)),
                SetVariable("penalty_text", "-10s"),
                SetVariable("penalty_token", penalty_token + 1)
            ]


screen mg_search():

    modal True
    
    timer 1.0 repeat True action SetVariable(
        "search_timer",
        max(0, search_timer - 1)
    )

    if penalty_token > 0:

        text penalty_text at penalty_pop:
            xpos 50
            ypos 70
            color "#ff4d4d"
            size 50
            outlines [(2, "#000000")]
    
    if penalty_token > 0:
        timer 0.6 action SetVariable("penalty_token", 0)
        
    use search_object(
        "images/mg_search/perfume.png",
        "images/mg_search/perfume-hover.png",
        "Perfume bottle",
        "clue1"
    )

    use search_object(
        "images/mg_search/sofa.png",
        "images/mg_search/sofa-hover.png",
        "A soft sofa with wrinkled upholstery"
    )

    use search_object(
        "images/mg_search/cloth.png",
        "images/mg_search/cloth-hover.png",
        "A piece of shiny fabric",
        "clue2"
    )

    use search_object(
        "images/mg_search/glass.png",
        "images/mg_search/glass-hover.png",
        "Glass with lipstick imprint",
        "clue3"
    )

    use search_object(
        "images/mg_search/amulet.png",
        "images/mg_search/amulet-hover.png",
        "Amulet with zodiac sign",
        "clue4"
    )

    use search_object(
        "images/mg_search/key.png",
        "images/mg_search/key-hover.png",
        "Office key",
        "clue5"
    )

    use search_object(
        "images/mg_search/book.png",
        "images/mg_search/book-hover.png",
        "An old book with financial statements"
    )

    use search_object(
        "images/mg_search/ashtray.png",
        "images/mg_search/ashtray-hover.png",
        "A regular ashtray. Nothing special"
    )

    use search_object(
        "images/mg_search/blood.png",
        "images/mg_search/blood-hover.png",
        "..."
    )

    use search_object(
        "images/mg_search/desk.png",
        "images/mg_search/desk-hover.png",
        "Empty drawer"
    )

    use search_object(
        "images/mg_search/lamp.png",
        "images/mg_search/lamp-hover.png",
        "The light is cold"
    )

    use search_object(
        "images/mg_search/papers.png",
        "images/mg_search/papers-hover.png",
        "Contracts and business documents"
    )

    use search_object(
        "images/mg_search/picture.png",
        "images/mg_search/picture-hover.png",
        "Expensive art. Part of the interior"
    )

    use search_object(
        "images/mg_search/watch.png",
        "images/mg_search/watch-hover.png",
        "Wall clock. Time has stopped"
    )

    use search_object(
        "images/mg_search/window.png",
        "images/mg_search/window-hover.png",
        "You can see the dark garden from here"
    )

    use search_object(
        "images/mg_search/wine.png",
        "images/mg_search/wine-hover.png",
        "An empty bottle of expensive wine"
    )

    if clue1_found and clue2_found and clue3_found and clue4_found and clue5_found:

        timer 0.1 action [
            SetVariable("suspicion_ann", suspicion_ann + 2),
            Return()
        ]

    if search_timer <= 0:

        timer 0.1 action [
            SetVariable("suspicion_mc", suspicion_mc + 1),
            Return()
        ]

    if screen_tooltip != "":
        frame at tooltip_fade:
            xpos renpy.get_mouse_pos()[0] + 20
            ypos renpy.get_mouse_pos()[1] + 20

            background "#00000088"
            xmaximum 220
            padding (10, 8)

            text screen_tooltip:
                color "#fff"
                size 18

    frame:
        xpos 30
        ypos 30

        background "#00000088"
        padding (12, 8)

        text "Time: [search_timer]":
            size 26
            color "#fff"

    frame:
        xpos 30
        ypos 150

        background "#00000088"
        padding (16, 16)

        vbox:
            spacing 8

            if clue1_found:
                text "{s}Clue #1{/s}":
                    size 24
                    color "#999"
            else:
                text "Clue #1":
                    size 24
                    color "#fff"

            if clue2_found:
                text "{s}Clue #2{/s}":
                    size 24
                    color "#999"
            else:
                text "Clue #2":
                    size 24
                    color "#fff"

            if clue3_found:
                text "{s}Clue #3{/s}":
                    size 24
                    color "#999"
            else:
                text "Clue #3":
                    size 24
                    color "#fff"

            if clue4_found:
                text "{s}Clue #4{/s}":
                    size 24
                    color "#999"
            else:
                text "Clue #4":
                    size 24
                    color "#fff"

            if clue5_found:
                text "{s}Clue #5{/s}":
                    size 24
                    color "#999"
            else:
                text "Clue #5":
                    size 24
                    color "#fff"
  