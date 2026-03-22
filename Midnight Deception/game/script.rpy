#arriving in mansion
label start:
    scene street
    with fade
    $ letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZабвгґдеєжзиіїйклмнопрстуфхцчшщьюяАБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ- '
    $ player = renpy.input('What is your name?', length = 12, allow = letters).strip()
    if player == '':
        $ player = 'Lina'

    #if player == 'Polina'
        #secret ending

    'It was about to rain when I arrived at the mansion.'

    scene house 
    with fade

    '''
    The house stood tall in the darkness - beautiful, elegant... and somehow unsettling. The warm lights in the windows didn`t make it feel any less intimidating.

    Daniel.

    We`ve known each other since I was a kid and he was just a broke teenager hanging out at the computer club. We used to sit for hours in front of old monitors, dreaming about the future.

    And now...{w=1} look at him.

    I won`t lie. I`m jealous.

    He invited me to this party, said he wanted me to meet his friends.

    But everyone knows that`s not the real reason we`re here.
    '''

    scene hall
    with fade

    'I step inside.'

    'A soft voice greets me.'

    show sophie normal
    with fade

    unknown 'Good evening.'

    player 'Good evening... um, sorry, but you are..?'

    sophie happy 'I`m Sophie. I used to work with Daniel`s wife...'

    extend sad ' before she... you know.'

    player 'Oh... yes. Nice to meet you, Sophie. I`m [player].'

    show sophie sad at left2
    with move
    
    show ann disgust at right2
    with dissolve   

    'Another voice cuts in.'

    '???' 'One more person. How many does that make now?'

    sophie angry 'Ann, that`s not polite.'

    ann angry 'I don`t care. Everyone knows why we`re here.'

    ann 'The more people there are, the smaller the chances.'

    sophie 'I`d rather not talk about it.'

    '''
    Ann isn`t wrong, though.

    We all came here for the same reason. You just don`t usually say it out loud.

    I was about to ask Ann what Daniel meant to her when-
    '''

    show daniel normal
    show sophie normal at left3
    show ann disgust at right3

    with move

    daniel '[player]! I`m glad you made it. I`m so happy everyone`s here. Let`s not waste time - dinner is ready.'

    menu:
        'Go to dinner.':
            jump dinner
        'I`d rather look around the house first.':
            # $ suspicion_mc+=1
            jump lookaround

#going through rooms
label lookaround:
    scene living_room
    with fade

    'I slip away while the others head toward the dining room.'

    'The living room is enormous - high ceilings, antique furniture, paintings that seem to follow you with their eyes.'

    scene daniel_office_door 

    'A cabinet catches my attention - locked.'

    scene balcony
    with fade

    play music rain_thunder
    
    'The balcony doors are slightly open.'

    show miles sil at right2
    show victor sil at left2

    with dissolve 

    'Two men are standing there.'

    'One looks nervous, constantly checking his phone.'

    'The other seems irritated - jaw tight, arms crossed.'

    menu:
        'Eavesdrop.':
            # $ suspicion_mc+=1
            jump eavesdrop
        
        'Join the conversation.':
            jump conversation

        'Leave quietly.':
            jump dinner

#eavesdrop miles and victor
label eavesdrop:
    scene balcony

    show miles sil at right2
    show victor sil at left2

    with dissolve 

    'I stop just before stepping fully onto the balcony.'

    'The rain muffles their voices, but not enough.'

    voice1 'So he really invited all of us?'

    voice2 'Looks like it.'

    voice1 'That doesn`t make sense.'

    voice2 'Nothing about tonight makes sense.'

    #sound
    'A pause. I hear a lighter click.'

    voice1 'You think he`s going to choose?'

    voice2 'That`s what everyone assumes.'

    voice1 'I didn`t come here to lose.'

    #sound Victor lets out a dry chuckle
    voice2 'You `re talking like this is a competition.'

    voice1 'Isn`t it?'

    'Silence.'

    voice2 'Just... don`t do anything stupid.'

    voice1 'Depends on what he announces.'

    'The balcony door creaks slightly under my hand.'

    voice2 'Did you hear that?'

    'I quickly step back.'

    jump dinner
            
#join conversation between miles and victor
label conversation:
    scene balcony

    show miles disgust at right2
    show victor normal at left2

    with dissolve 

    '''
    I step onto the balcony.

    Both men look at me.

    Victor and Miles are standing there.

    Daniel told me about them after I came to house.
    '''

    player 'Am I interrupting something?'

    victor happy 'Not at all.'

    miles normal 'Just discussing the weather.'

    victor 'Right. Stormy night for a reunion.'

    miles 'Or a decision.'

    player 'Decision?'

    'The man on the right studies me carefully.'

    miles disgust 'You don`t think Daniel brought us all here just for dinner, do you?'

    show miles normal

    'Before I can answer-'

    'The balcony door opens.'

    show daniel normal

    daniel 'There you are. Hiding from the others already?'

    'He smiles - warm, confident, but his eyes quickly scan our faces...'

    'Like he`s measuring something.'

    daniel 'Come inside. We shouldnt keep everyone waiting.'

    jump dinner

#dinner with everyone
label dinner:
    stop music fadeout 1
    play music main_theme
    
    scene dining_room
    with fade
    show daniel normal

    'Daniel looks... calm. Too calm.'

    'After dinner, he stands up, raising his glass.'

    daniel 'As you all know, I don`t have a son or daughter to leave my fortune to.'

    daniel 'Of course, I could choose one of you.'

    daniel 'But then I would have invited only that person.'

    daniel quest 'I have a better idea.'

    daniel 'After my death, most of my wealth will be donated to charity.'

    daniel 'Each of you will receive a generous amount.'

    daniel '...but it must be spent only on charity.'
    
    daniel normal '...perhaps you`ll become better people.'

    'Silence.'

    show sophie angry at left3

    'Even Sophie looks stunned, though she quickly hides it.'

    sophie normal 'That`s... such a wonderful idea.'

    show miles disgust at right3

    show sophie angry

    miles 'Are you serious? If you want to donate, just write it in your will.'

    daniel 'I believe doing good changes you spiritually. But no one is forced. If you refuse, I understand.'

    show ann normal at right4

    ann 'I`m fine with donating. But I want to choose the foundation.'

    sophie 'Guys, please... it`s not your money-'

    show victor normal at left4

    victor 'I agree with Sophie. If it`s Daniel`s will, we should respect it.'

    'Daniel turns to me.'

    'His eyes linger a little longer than they should.'

    daniel 'What about you, [player]?'
    
    menu:
        'Agree with Sophie and Victor.':

            player 'I think Victor is right. If it`s Daniel`s will, we should respect it. It`s his decision.'

            show sophie normal

            show victor happy

            show ann disgust

            show miles disgust

            sophie 'That`s very mature of you.'

            victor 'At least someone here understands loyalty.'

            miles 'Loyalty? That`s a strong word when money is involved.'

            ann 'Easy for you to say.'

            daniel 'I`m glad to hear that, [player]. I knew I could count on you.'

            'That sentence feels heavier than it should.'

            sophie 'Maybe we should open some wine?'

            'Sophie quickly changes the subject. The tension lowers - slightly.'

        'Agree with Ann and Miles.':

            # $suspicion_mc +=1

            player 'I think Ann has a point. If we`re the ones donating, we should decide where the money goes.'

            show sophie angry

            show victor disgust

            show ann normal

            show miles normal

            sophie 'But that wasn`t the idea...'

            victor 'It sounds like you`re already dividing something that isn`t yours.'

            miles 'Finally. Someone honest.'

            ann 'At least [player] isn`t pretending this is some moral test.'

            daniel 'Interesting. I didn`t expect that answer from you.'

            victor 'People show their true colors when they see an opportunity.'

            miles 'Or when they`re tired of being manipulated.'
            
            daniel 'Enough. This isn`t a battlefield. We`re guests here. Let`s not ruin the evening.'

#daniel is murdered, first branch
label murder_time:
    scene corridor
    with fade

    'Dinner ends, but the tension doesn`t.'

    'People stand up one by one, exchanging forced smiles, avoiding eye contact.'

    'No one says it out loud... but everyone feels it.'

    'Something is wrong.'

    scene guest_room
    with fade

    '''
    I step into the guest room Daniel prepared for me.

    It`s nice, carefully arranged - almost too perfect.

    Like a hotel room.

    Not like a home.

    I close the door behind me.

    Silence.

    For the first time tonight... I`m alone.

    ...

    Daniel.

    He hasn`t changed.

    Still controlling everything. Even now.

    Even this dinner felt less like an invitation... and more like a test.

    ...What was he planning?

    I sit on the edge of the bed.

    Something about tonight doesn`t make sense.

    The guests. The condition. The way he looked at everyone...

    Like he already knew how this would end.

    ...

    I should probably rest.

    Tomorrow, I can figure this out with a clear head.

    ...
    '''

    stop music fadeout 1

    play sound "audio/sophia_scream.mp3"

    'A sudden sound cuts through the silence.'

    'A scream.'


    'Sharp. Panicked.'

    'Sophie.'

    'My body freezes for a second.'

    'Then—'

    scene corridor
    with fade

    'The silence of the mansion shatters.'

    'Somewhere, doors open.'

    'Footsteps echo through the hallway.'

    'Something happened.'

    'Something bad.'

    'I step into the corridor... and stop.'

    'What should I do?'

    menu:
        'Run to Daniel`s office immediately.':
            jump go_to_office_fast

        'Wait for someone else to go first.':
            $ suspicion_mc += 1
            jump go_to_office_late

        'Try to leave the mansion.':
            jump try_escape

#go to office fast
label go_to_office_fast:

    scene corridor
    with fade

    'I don`t hesitate.'

    'My feet move before I can even think.'

    'The corridor feels longer than before.'

    'Voices. Movement. Panic.'

    scene office
    with fade

    'The door is already open.'

    'People are gathering inside.'

    'And then I see it.'

    show sophie shocked at left3
    show ann sad at right3
    show victor nervous at left2
    show miles angry at right2

    'Sophie stands near the desk, pale, trembling.'

    'On the floor—'

    'Daniel.'

    'Not moving.'

    'Not breathing.'

    'Something cold settles in my chest.'

    'This isn`t a misunderstanding.'

    'This is real.'

    'Daniel is dead.'

    jump first_group_scene

#go to office late
label go_to_office_late:

    scene corridor
    with fade

    'I hesitate.'

    'Just for a second.'

    '...or maybe longer.'

    'Footsteps rush past me.'

    'Someone else gets there first.'

    'Only then do I move.'

    scene office
    with fade

    'When I enter, several people are already inside.'

    'They all turn to look at me.'

    'That look lingers a little too long.'

    '...Noted.'

    show sophie shocked at left3
    show ann sad at right3

    'Sophie is shaking.'

    'Her voice barely works.'

    sophie 'I... I just came in and— and he was—'

    'I don`t hear the rest.'

    'Because my eyes lock onto the floor.'

    'Daniel.'

    'Dead.'

    'A strange thought crosses my mind—'

    'If I came earlier... would anything be different?'

    jump first_group_scene

#go to mini-game "Escape"
label try_escape:

    scene hall
    with fade

    'The scream echoes in my head.'

    'Something inside me twists.'

    'No.'

    'This is wrong.'

    'I shouldn`t be here.'

    'Whatever happened... it has nothing to do with me.'

    'I need to leave.'

    'Now.'

    'I move quickly through the hall, trying to stay quiet.'

    'The front door is right there.'

    'Almost within reach.'

    'If I leave now...'

    'No questions. No involvement.'

    'Just walk away.'

    '...'

    'But my hand freezes on the handle.'

    'Why does this feel like a mistake?'

    jump escape_minigame

label escape_minigame:

    $ escape_active = True
    $ escape_hits = 0
    $ escape_time_left = 10.0
    $ escape_target = 5

    show screen escape_game
    show screen escape_input

    while True:

        $ escape_current_key = generate_escape_key()

        $ result = ui.interact()

        if result == True:
            $ escape_hits += 1

        elif result == False:

            # ⬇️ ВАЖЛИВО
            $ escape_active = False
            hide screen escape_game
            hide screen escape_input

            jump escape_lose

        elif result == "timeout":

            # ⬇️ ТЕЖ САМО
            $ escape_active = False
            hide screen escape_game
            hide screen escape_input

            if escape_hits >= escape_target:
                jump escape_win
            else:
                jump escape_lose
    
label escape_win:
    
    "You managed to escape."
    # ending 1


label escape_lose:
    
    $ suspicion_mc += 2

    "You failed to escape."
