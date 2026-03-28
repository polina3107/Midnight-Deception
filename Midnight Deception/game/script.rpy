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
    with fade

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
    '''

    $ config.allow_skipping = False

    '''
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

    $ config.allow_skipping = True

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

    scene daniel_office
    with fade

    'When I enter, several people are already inside.'

    'They all turn to look at me.'

    'That look lingers a little too long.'

    '...Noted.'

    show sophie scared at left3
    show ann shoked at right3

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

    $ renpy.notify('If I don`t escape they will suspect me...')

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
    
    $ config.allow_skipping = False 

    'Just walk away.'

    '...'

    'But my hand freezes on the handle.'

    'Why does this feel like a mistake?'

    $ renpy.block_rollback()

    call screen minigame_warning

    jump escape_minigame

#warning screen to mini-game "Escape" (maybe use for every mg)
screen minigame_warning():

    modal True

    add Solid("#000000CC")

    text "❗GET READY❗":
        size 80
        xalign 0.5
        yalign 0.4

    text "Press the correct keys to escape":
        size 40
        xalign 0.5
        yalign 0.6

    timer 5.0 action Return()

#mini-game "Escape"
label escape_minigame:

    play music "audio/mg_escape_music.mp3"
    # play sound "audio/mg_escape_breathing.mp3" loop

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

            $ escape_active = False
            hide screen escape_game
            hide screen escape_input

            jump escape_lose

        elif result == "timeout":

            $ escape_active = False
            hide screen escape_game
            hide screen escape_input

            if escape_hits >= escape_target:
                jump escape_win
            else:
                jump escape_lose

#after mini-game "Escape" - win
label escape_win:
    
    "You managed to escape."
    $ renpy.block_rollback()
    $ config.allow_skipping = True

    window hide

    scene ending1 with fade

    pause

    $ persistent.ending1 = True

    return
    # ending 1

#after mini-game "Escape" - lose
label escape_lose:
    
    $ suspicion_mc += 2

    'I press the handle-'

    'Locked.'

    'No-'

    'I try again. Harder.'

    'Nothing.'

    $ config.allow_skipping = True

    'My hands slip slightly.'

    'Why isn`t it opening?!'

    'The sequence - I messed it up.'

    'Damn it.'

    'Footsteps.'

    'Voices.'

    'They`re getting closer.'

    'Too late.'

    scene hall
    with fade

    show victor disgust at left2
    show ann disgust at right2

    'Someone stops.'

    'They see me.'

    victor '...What are you doing here?'

    'I freeze.'

    'Think.'

    'Say something.'

    menu:
        'I heard the scream and got lost.':
            # $ suspicion_mc += 1

            player 'I- I heard the scream and I was trying to find where it came from.'

            ann 'The exit is the opposite direction.'

            '...Right.'

            'That doesn`t sound convincing.'

        'I just needed some air.':
            player 'I just needed some air. That`s all.'

            victor 'At a time like this?'

            'His voice tightens.'

        'Stay silent.':
            # $ suspicion_mc += 1

            'I say nothing.'

            'That might have been worse.'

            ann '...That`s not suspicious at all.'

    'More footsteps approach.'

    'The others are heading somewhere deeper into the mansion.'

    'The office.'

    'That`s where the scream came from.'

    'No way out now.'

    'I have to go back.'

    jump go_to_office_late

#scene after murder
label first_group_scene:

    scene daniel_office
    with fade

    'The room feels smaller than before.'

    'Too many people.'

    'Too much silence.'

    'And one thing no one wants to say out loud.'

    'This wasn`t an accident.'

    show sophie scared at left3
    show ann disgust at right3
    show victor scared at left2
    show miles angry at right2

    sophie 'I didn`t— I just came in and he was already—'

    'Her voice breaks.'

    sophie 'I didn`t touch anything! I swear!'

    miles 'Then why were you the one who found him?'

    sophie 'I heard something! I thought— I thought he needed help!'

    ann 'Or you knew exactly where to go.'

    victor 'That`s enough.'

    'Victor`s voice is quiet, but tense.'

    victor 'Accusing each other won`t help.'

    miles 'It might.'

    'Silence.'

    'They all understand the same thing now.'

    'One of us did this.'

    menu:
        'Take control of the situation.':
            jump interrogate_group

        'Try to calm everyone down.':
            jump calm_group

#interrogate people to know extra info
label interrogate_group:

    'I take a step forward.'

    'No one else is going to do this.'

    player 'We need to stop panicking and figure out what happened.'

    'They all look at me.'

    'Good.'

    player 'Everyone. Say where you were before the scream.'

    'A pause.'

    'No one wants to go first.'

    player 'Now.'

    show sophie scared at left3

    sophie 'I was in the kitchen...'

    'Her voice shakes.'

    sophie 'I was making tea. I needed to calm down after dinner.'

    player 'And?'

    sophie 'I heard a sound. Something fell. Then I went to check the office... and—'

    'She looks at Daniel`s body and turns away.'

    show ann normal at right3

    ann 'I was here earlier.'

    'Everyone looks at her.'

    ann 'Not at the moment of the scream.'

    ann 'Before that.'

    ann 'I wanted to speak with Daniel privately.'

    miles 'About what?'

    ann 'That`s none of your business.'

    'Tension spikes again.'

    show victor scared at left2

    victor 'I was on the balcony.'

    victor 'I just needed air.'

    victor 'After what he said during dinner...'

    'He hesitates.'

    victor 'I did see something, though.'

    player 'What?'

    victor 'A shadow. In the hallway.'

    victor 'Someone moved toward the office.'

    'The room goes still.'

    show miles angry at right2

    player 'And you?'

    miles 'I was in the lounge.'

    miles 'Alone.'

    player 'That`s it?'

    miles 'That`s all you need.'

    player 'Or all you`re willing to say?'

    miles 'Careful.'

    'His tone drops.'

    miles 'You`re asking a lot of questions for someone who just got here.'

    '...Not wrong.'

    'All eyes shift to me for a second.'

    # $ suspicion_mc += 1

    'Noted.'

    'Still— now I know where everyone claims they were.'

    jump investigation

#calm group - no extra info for player
label calm_group:

    'I raise my hands slightly.'

    player 'Hey. Stop.'

    player 'This isn`t helping.'

    'They hesitate.'

    'Good.'

    player 'We`re all in shock.'

    player 'Accusing each other right now won`t change anything.'

    show sophie sad at left3

    sophie 'I... I didn`t do anything...'

    player 'I know.'

    'She looks at me like she actually believes that.'

    show victor normal at left2

    victor 'We should just... stay calm.'

    victor 'And think.'

    show ann normal at right3

    ann 'People rarely think clearly when they`re scared.'

    ann 'They reveal more than they intend.'

    'That didn`t sound comforting.'

    show miles disgust at right2

    miles 'So what? We just sit here and pretend nothing happened?'

    player 'No.'

    player 'But we don`t turn on each other either.'

    'Silence.'

    'Heavy. Uncertain.'

    'No one offers details.'

    'No one says where they were.'

    'Everyone is holding something back.'

    'Including me... maybe.'

    '...'

    'This isn`t going anywhere.'

    jump investigation

#choice that leads to 5 mini-games
label investigation:

    if minigames_done >= 2:
        jump check_endings

    scene daniel_office
    with fade

    'I need to choose my next step carefully.'

    menu:
        'Stay in the office.' if len(office_actions_done) < 2:
            jump location_office

        'Go to the living room.' if "living" not in visited_rooms:
            $ visited_rooms.append("living")
            jump location_livingroom

        'Go to the kitchen.' if "kitchen" not in visited_rooms:
            $ visited_rooms.append("kitchen")
            jump location_kitchen

        'Go to the balcony.' if "balcony" not in visited_rooms:
            $ visited_rooms.append("balcony")
            jump location_balcony

#stay in office - 2 mini-games in choice
label location_office:

    scene daniel_office
    with fade

    'This room still holds answers.'

    menu:
        'Search for clues.' if "search" not in office_actions_done:
            $ office_actions_done.append("search")
            jump search_minigame

        'Analyze alibis.' if "match" not in office_actions_done:
            $ office_actions_done.append("match")
            jump match_minigame

label search_minigame:

    'I start looking around carefully.'

    menu:
        'You found important clues.':
            $ suspicion_ann += 2
            'Something here connects Ann to this room.'

        'You found nothing useful.':
            $ suspicion_mc += 1
            'I wasted time... and now I look suspicious.'

    $ minigames_done += 1
    jump investigation

label match_minigame:

    'I try to reconstruct everyone`s story.'

    menu:
        'You figured out contradictions.':

            $ max_susp = max(suspicion_sophie, suspicion_ann, suspicion_victor, suspicion_mc)

            if suspicion_sophie == max_susp:
                $ suspicion_sophie += 3
                'Sophie`s story starts falling apart.'

            elif suspicion_ann == max_susp:
                $ suspicion_ann += 3
                'Ann`s words don`t match the facts.'

            elif suspicion_victor == max_susp:
                $ suspicion_victor += 3
                'Victor`s story doesn`t hold up.'

            elif suspicion_mc == max_susp:
                $ suspicion_mc += 3
                'Miles is clearly hiding something.'

        'You got confused.':
            $ suspicion_mc += 3
            'Something doesn`t add up... or maybe I`m wrong.'

    $ minigames_done += 1
    jump investigation

#go to living room - 1 mini-game
label location_livingroom:

    scene living_room
    with fade

    'Voices overlap.'

    'Everyone is hiding something.'

    menu:
        'You identified lies.':
            $ max_susp = max(suspicion_sophie, suspicion_ann, suspicion_victor, suspicion_mc)

            if suspicion_sophie == max_susp:
                $ suspicion_sophie += 2
                'Sophie`s story starts falling apart.'

            elif suspicion_ann == max_susp:
                $ suspicion_ann += 2
                'Ann`s words don`t match the facts.'

            elif suspicion_victor == max_susp:
                $ suspicion_victor += 2
                'Victor`s story doesn`t hold up.'

            elif suspicion_mc == max_susp:
                $ suspicion_mc += 2
                'Miles is clearly hiding something.'

        'You couldn`t tell who was lying.':
            $ suspicion_mc += 2
            'I`m not convincing anyone like this.'

    $ minigames_done += 1
    jump investigation

#go to kitchen - 1 mini-game
label location_kitchen:

    scene kitchen
    with fade

    'Something feels off here.'

    menu:
        'You found inconsistencies.':
            $ suspicion_sophie += 2
            'Sophie`s story doesn`t match the scene.'

        'Everything seems normal.':
            $ suspicion_mc += 1
            'Maybe I`m overthinking this.'

    $ minigames_done += 1
    jump investigation

#go to balcony - 1 mini-game
label location_balcony:

    scene balcony
    with fade

    show victor nervous

    'Victor avoids eye contact.'

    menu:
        'You pressured him successfully.':
            $ suspicion_victor += 2
            'He breaks under pressure.'

        'He stayed calm.':
            $ suspicion_mc += 1
            'I couldn`t get anything out of him.'

    $ minigames_done += 1
    jump investigation

#after 2 mini-games

label check_endings:

    scene hall
    with fade

    'I`ve seen enough.'

    'Or at least... enough to make a decision.'

    'Everyone is already looking at each other differently.'

    'Suspicion is no longer hidden.'

    'It`s everywhere.'

    '...'

    'Now comes the hardest part.'

    'Who did it?'