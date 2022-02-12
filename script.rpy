# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define j = Character('Jesus')
define g = Character('God', color = '#ffffff')
define s = Character('Satan', color = '#ff0000')
define mys = Character('???', color = '#ff0000')
define m = Character('Man', color = '#f4a460')
define a = Character('Apostle', color = '#006400')
define a1 = Character('Apostle1', color = '#006400')
define a2 = Character('Apostle2', color = '#006400')
define a3 = Character('Apostle3', color = '#006400')
define w = Character('Woman', color = '#663399')
define ju = Character('Judas', color = '#990000')
define p = Character('Pharisee', color = '#cc5500')
define c = Character('Crowd', color = '#318ce7')
define h1 = Character('High Priest1', color = '#ffbf00')
define h2 = Character('High Priest2', color = '#ffbf00')
define h3 = Character('High Priest3', color = '#ffbf00')

default gp = 0
default sp = 0
default pp = 0
default np = 0
default ac = 0
default rd = 0
default name = ''
default rela = ''
default ill = ''
default npg = ''
default nps = ''
default npn = ''
default npl = ''
default man = 0
default pg = 0
default ps = 0
default pn = 0
default pl = 0
default e1 = False
default accept = False
default aps = ['Simon who will be named Peter', 'Andrew', 'James', 'John', 'Philip', 'Bartholomew', 'Matthew',
'Thomas', 'Another James', 'Another Simon', 'Judas not the Traiter']
define rel = ['brother', 'mother', 'sister', 'father', 'son', 'daughter', 'cousin', 'uncle',
'aunt', 'nephew', 'niece', 'wife']
define illness = ['am blind', 'have a withered hand', 'have a blood disease', 'am possessed by demon',
'have a skin disease', 'have a fever', 'am crippled']

# The game starts here.

label start:

    scene black
    '===DISCLAIMER==='
    'Many of the contents used in this game, including and not limited to graphics and dialogues, 
    are NOT original, and should be attributed to their corresponding sources.'

    scene field with dissolve
    pause 1.0

    show god at truecenter with dissolve

    g 'This is my beloved Son, in whom I am well pleased.'

    show jesus at center:
        zoom 1.5
        yalign 0.0
        linear 0.1 yalign 1.0

    j 'Morning!'
    j 'Nice day, ain\'t it?'
    g 'My son, I shall give you a task to make you an example in this dark time.'
    j 'Good idea, Father!'
    g 'Of course it\'s a good idea!'
    g 'Behold, my son, that is the city of Nazareth. You shall be called a Nazarene.
    You shall help the people there, and save them from their sins. That is your purpose.'
    j 'But Father, I don\'t want any of that!'
    g 'Listen up, I built this world all from nothing. When I started here all around was darkness.
    I created Paradise and the angels, but then they were seduced by Satan.'
    g 'I created Eden and human, and they were seduced by Satan. I built up this world for them to live in, 
    and they were corrupted and I had to cleanse them all with the flood.' 
    g 'But now this fourth world stays up! And I\'m giving it all to you.'
    j 'But I don\'t want any of that, Father. I\'d rather- I\'d rather just-'
    g 'Stop that, stop that. This is not a music game.'
    g 'Now off you go.'

    jump freeExplore

label freeExplore:
    if ac == 3:
        jump Event1
    if ac == 7:
        jump Event2
    if ac == 11:
        jump Event3
    if ac == 15:
        jump Event4
    if ac == 19:
        jump Event5
    if ac == 23:
        jump Ending

    screen exploration():
        imagemap:
            idle 'map ground'
            hover 'map hover'

            hotspot (255, 35, 183, 145) action Jump('field')
            hotspot (1189, 122, 182, 149) action Jump('village')
            hotspot (486, 344, 182, 143) action Jump('north')
            hotspot (1341, 583, 183, 146) action Jump('south')
            hotspot (1722, 913, 184, 144) action Jump('outskirt')
    
    label exploration:
        call screen exploration

label field:
    scene field
    show jesus at left:
        zoom 1.5
    pause 0.5
    show god at truecenter with dissolve

    menu:
        g 'What is it, my son?'
        'I seek guidance, for I am in doubt':
            g 'Have faith in me, and I shall be with you.'
            $ ac += 1
        'I come to worship thou, Father':
            g 'No need, my son. I never doubted your faith.'
            $ gp += 2
            $ ac += 1
        'I look at you and I spit in your face, though you dare not reveal it to me, you coward':
            g '......'
            $ pp += 1
            $ ac += 1
        'You\'re pathetic':
            $ ac += 1
            pause 0.2
            menu:
                g 'How dare you-'
                'You\'re but a resort for the weak and the undetermined':
                    g 'Who planted those thoughts in you...'
                    $ np += 1
                'You\'re weak. Satan grants me far better rewards' if e1:
                    g 'So you\'re tempted. I thought better of you.'
                    $ sp += 2
        '\[Leave\]':
            g 'Good to see you, still.'
        
    jump freeExplore
    
label outskirt:
    scene barren field
    show jesus at left:
        zoom 1.5
    pause 0.5
    show satan at truecenter with dissolve
    if e1 == False:
        mys 'You come early...I have nothing to say to you. But maybe...'
        jump freeExplore
    menu:
        s 'Whooo...Look who\'s here.'
        'I seek guidance, for I am in doubt':
            s 'Well...Follow me then, you know the reward that awaits you.'
            $ ac += 1
        'I come to worship thou, my lord':
            s 'Ah...Sweet loyalty. You\'ll get your reward, I promise.'
            $ sp += 2
            $ ac += 1
        'I despise you, devil. You\'ll rot in hell':
            s 'Such attitude...God must love you dearly.'
            $ gp += 2
            $ ac += 1
        'You don\'t frigthen me, you empty headed animal food trough wiper!
        Your mother was a hamster and your father smelt of elderberries!':
            s 'Such language...Wonder where you learnt that.'
            $ pp += 2
            $ ac += 1
        'You\'re pathetic.':
            $ ac += 1
            pause 0.2
            menu:
                s 'Interesting...'
                'You\'re but a resort for the wicked and the unsatisfied':
                    s 'And I wonder which one is you?'
                    $ np += 1
                'You\'re evil. God is the only righteousness':
                    s 'Yet the world is still such a cruel and harsh place?'
                    $ gp += 2
        '\[Leave\]':
            s 'You\'re welcomed anytime.'
    jump freeExplore

label village:
    scene village
    call encounter from _call_encounter
    jump freeExplore

label north:
    scene town1
    call encounter from _call_encounter_1
    jump freeExplore

label south:
    scene town2
    call encounter from _call_encounter_2
    jump freeExplore

label Event1:
    $ e1 = True
    scene black
    pause 1.0
    scene barren field with dissolve
    show jesus at left:
        zoom 1.5
    pause 1.0
    show satan at truecenter with dissolve

    mys 'Ah...Beloved son of the so-called God...I welcome you, Jesus.'
    j 'Who are you?'
    s 'I am Satan, Lord of the devils.'
    menu:
        'You devil! Begone!':
            $ gp += 2
            s 'Such defiance...I wonder what would you say after a little...vacation.'
        'My lord! I offer you my loyalty and obedience!':
            $ sp += 2
            s 'This goes quicker than I thought...But no, you must be put through a test first.'
        'I don\'t know you and I don\'t care to know you. By the way, you look as stupid as a hamster':
            $ pp += 1
            s 'Unexpected...I would need to teach you some manner first.'
        'Interesting':
            $ np += 1
            s 'Just that?...Seems like I would need to spice things up a bit for you.'
    scene black with dissolve
    'Suddenly, you fall into utter darkness, and loses track of time and spaces.'
    'Your energy seems to be sucked out from your body, as hunger and coldness grows gradually from the inside, until they are unbearable.'
    'Your vision grows dim, though there is nothing for you to see. Only deep, deep darkness.'
    'You try to listen, but the world is silent, not even the swirling sound of wind.
    You start to miss the soothing voice of Satan.'
    
    scene barren field with dissolve
    show jesus at left:
        zoom 1.5
    show satan at truecenter with dissolve
    menu:
        s 'Had fun?'
        'I\'m not afraid of you devil, for God is always with me.':
            $ gp += 2
        'I wish to serve you my lord! Am I qualified now?':
            $ sp += 2
        'You thought you\'ve beaten me? Save you dirty tricks for others you tiny-brained wipers of other people\'s bottoms!':
            $ pp += 1
        'Impressive. What do you want with me?':
            $ np += 1
    s 'Glad you had fun.'
    menu:
        s 'Anyway. I bet you\'re hungry now. You see those stones over there. 
        Turn them to bread.'
        'Man shall not live by bread alone, 
        but by every word that proceedeth out of the mouth of God':
            $ gp += 2
        'I will not wield the power of the false god. I wish for your power, my lord':
            $ sp += 2
        'Impossible. Stones cannot be turned to bread - mass is not conserved':
            $ np += 1
        'Who are you to tell me what to do you son of a window-dresser':
            $ pp += 1
    s 'Impressive. Follow me.'

    scene cliff with dissolve
    show jesus at left:
        zoom 1.5
    pause 1.0
    show satan at truecenter
    s 'Pleasant place, huh?'
    menu:
        s 'How about you jump down from here, and see if your father will save you?'
        'It is written, Thou shalt not tempt the Lord thy God':
            $ gp += 2
        'I will not wield the power of the false god. I wish for your power, my lord':
            $ sp += 2
        'I\'m not stupid. I\'m gonna die jumping down from here':
            $ np += 1
        'You want me to taunt you a second time you bedwetter?':
            $ pp += 1
    s 'This is getting more and more interesting...Follow me.'

    scene city with dissolve
    show jesus at left:
        zoom 1.5
    pause 1.0
    show satan at truecenter
    s 'Such nice view from up here. Hope you\'re enjoying yourself.'
    menu:
        s 'I will give you all these things if you worship me, sweet Jesus.'
        'Thou shalt worship the Lord thy God, and him only shalt thou serve':
            $ gp += 2
        'Yes my lord! I will serve you and worship you!':
            $ sp += 2
        'Sorry but I\'m not interested. This is getting us nowhere and I really have to go now':
            $ np += 1
        'I wave my private parts at your aunty in return, you cheesy second hand electric donkey bottom biter':
            $ pp += 1
    s 'Very well...Then so be it.'
    s 'Alas, you still have a long way ahead of you. But you can always come and
    have a nice chat with me if you like.'
    $ ac += 1
    scene black
    pause 1.0
    jump freeExplore

label Event2:
    scene black
    pause 1.0
    scene town1 with dissolve
    show jesus at left:
        zoom 1.5
    pause 1.0
    show judas at truecenter
    ju 'My lord! I have heard of your miracles, and I come to follow your teachings!'
    ju 'Please accept me as your disciple!'
    menu:
        'Who are you?':
            ju 'My name is Judas Iscariot, my lord.'
            ju 'I\'m good at financing, my lord. I can sure make myself useful to you.'
    menu:
        'I accept you as my disciple, Judas':
            $ gp += 2
            $ accept = True
            ju 'Thank you my lord! May God bless you.'
        'I have no need of more people around me':
            ju 'Please, my lord. Please reconsider. I beg you.'
        'Ha! You\'re that bloody betrayer! One more word and I\'ll make castanets out of your testicles!':
            ju 'What are you talking about my lord? You confuses me. Please do not reject me.'
    if not accept:
        menu:
            'I accept you as my disciple, Judas':
                $ accept = True
            'I accept you as my disciple, Judas':
                $ accept = True
            'I accept you as my disciple, Judas':
                $ accept = True
            'I accept you as my disciple, Judas':
                $ accept = True
            'I accept you as my disciple, Judas':
                $ accept = True
            'I accept you as my disciple, Judas':
                $ accept = True
            'I accept you as my disciple, Judas':
                $ accept = True
            'I accept you as my disciple, Judas':
                $ accept = True
            'I accept you as my disciple, Judas':
                $ accept = True
            'I accept you as my disciple, Judas':
                $ accept = True
            'I accept you as my disciple, Judas':
                $ accept = True
            'I accept you as my disciple, Judas':
                $ accept = True
            'I accept you as my disciple, Judas':
                $ accept = True
    ju 'Thank you my lord! May God bless you.'
    $ ac += 1
    scene black
    pause 1.0
    jump freeExplore

label Event3:
    scene black
    pause 1.0
    scene storm with dissolve
    show judas at right
    show man1 at center
    show man2:
        xalign 0.75
    a1 'The storm is too strong, we are about to sink!'
    a2 'Careful there! Hold on to the edge!'
    ju 'It\'s no use! We\'re all going to die this way!'
    a3 'Lord! Lord! Wake up! We need your help!'
    show jesus at left:
        zoom 1.5
    j 'What is it?'
    menu:
        a3 'My lord, we\'re sinking!'
        'Why are ye fearful, O ye of little faith? Quiet, storm!':
            $ gp += 2
            'The storm immediately dies down.'
            a 'This is a miracle my lord! O praise God!'
        'My lord Satan! Help me in this danger!':
            $ sp += 2
            'The storm immediately dies down.'
            a 'This is a miracle! O praise the dark lord!'
        'Everyone, hold on to the edges and steady yourselves. Steer the boat along the direction
        of the wind. Protect your heads and faces, and do not panic!':
            $ np += 1
            'The storm gradually dies down. Luckily, no one is seriously hurt.'
            a 'We survived! My lord, you\'re truelly a master of seamanship. Where did you learn these things?'
            j 'Well, you have to know these things as a prophet, y\'know.'
        'Depart a lot you stupid storm and cut the approaching any more or we fire arrows at the top of your head!':
            $ pp += 1
            'Strangly enough, the storm immediately dies down.'
            a 'This...I don\'t know what to say to this, my lord!'
            j 'I\'m going back to sleep and don\'t disturb me again you fools.'
    $ ac += 1
    scene black
    pause 1.0
    jump freeExplore

label Event4:
    scene black
    pause 1.0
    scene town2 with dissolve
    show jesus at left:
        zoom 1.5
    pause 0.5
    show man3 at center with dissolve
    m 'My lord, please wait!'
    j 'What is it?'
    m 'My lord, my daughter is dead...But please, lay your hand her, and she shall live.'
    j 'Where is she?'
    m 'Please follow me.'

    scene bedroom with dissolve
    show jesus at left:
        zoom 1.5
    show man3 at center
    show girl dead at right:
        zoom 0.75
    m 'This...is my daughter.'
    menu:
        m 'Please, please save her!'
        'You are not dead, but asleep. Wake, fair maid':
            show girl alive at right:
                zoom 0.75
            $ gp += 2
            m 'Thank you, O thank you my lord! God bless your divine heart!'
        'Raise the dead O devil lord of the underworld!':
            show girl alive at right:
                zoom 0.75
            $ sp += 2
            m 'Thank...Thank you my lord!'
        'Sorry sir, the dead is dead. I cannot help, but only mourn your loss with you':
            $ np += 1
            m '...I understand, my lord. This is the way of nature after all, though I still wish for a miracle.'
        'Get up and move you stupid girl or I shall burst my pimples at you and unclog my nose in your direction':
            show girl alive at right:
                zoom 0.75
            $ pp += 1
            m 'What\'s the meaning of that my good sir?! But...oh, it worked! it worked!'
            m 'Guess I\'ll have to thank you, sir.'
    $ ac += 1
    scene black
    pause 1.0
    jump freeExplore

label Event5:
    scene black
    pause 1.0
    scene cliff with dissolve
    show jesus at left:
        zoom 1.5
    show judas at right
    show man1 at center
    show man2:
        xalign 0.75
    pause 0.5
    a1 'My lord, the crowd\'s been following us for three days now through this expedition,
    and no one has eaten anything.'
    a2 'I\'m afraid they might faint. It will be more troublesome that way.'
    a3 'But our food cannot support so many people.'
    j 'How much do we have?'
    a3 'Only seven loaves of bread, and a few little fishes.'
    a2 'The food prepared was only meant for ourselves. We did not expect so many followers would come.'
    a1 'There\'s no way we could feed everyone with such little.'
    menu:
        'Take the bread and the fish, break them, and give them to the multitudes':
            hide jesus
            hide judas
            hide man1
            hide man2
            'The apostles obey. The food is delivered, and everyone eats.'
            'When everyone finishes, the remaindings are collected, and they filled seven baskets.'
            $ gp += 2
        'Lord Satan! Save your followers from hunger and certain death!':
            hide jesus
            hide judas
            hide man1
            hide man2
            $ sp += 2
            'Baskets filled with bread, meat, and wine drop from the sky.'
            'The multitude eagerly picks up the food and feasts until everyone is full.'
        'Have the weak and the old remain here, everyone else spread out and gather food. I\'m sure
        we can find something even in this wilderness.':
            hide jesus
            hide judas
            hide man1
            hide man2
            $ np += 1
            'The multitude obeys. People bring back wild berries and herbs, some lucky ones even managed
            to hunt a few rabbits.'
            'Though not fully satisfied with the simple meal, everyone\'s spirits are replenished'
        'I\'m tired of your silly knees-bent running about in dancing behavior and I call your food request 
        a silly thing! Just think of something yourselves and stop asking me everytime':
            hide jesus
            hide judas
            hide man1
            hide man2
            $ pp += 1
            'Everyone is awed by Jesus\' profound language and resolution.'
            'They are suddenly filled with determination that sweeps away all cold and hunger.'
            'The crowd proceed with the expedition, which lasts another four days, without eating and drinking anything.'
            'Everyone returns with perfect states of both mind and body, and the bread and fish intact.'
    $ ac += 1
    scene black
    pause 1.0
    jump freeExplore

label encounter:
    show jesus at left:
        zoom 1.5
    pause 0.25
    if aps:
        $ rd = renpy.random.randint(1, 6)
    else:
        $ rd = renpy.random.randint(2, 6)
    if rd == 1:
        call newApostle from _call_newApostle
    if rd == 2:
        call illPerson from _call_illPerson
    if rd == 3:
        call question from _call_question
    if rd == 4:
        call illWoman from _call_illWoman
    if rd == 5 or rd == 6:
        call parable from _call_parable
    $ ac += 1
    return

label newApostle:
    call randomMan from _call_randomMan
    $ name = renpy.random.choice(aps)
    a 'My lord! I have heard of your miracles, and I come to follow your teachings!'
    menu:
        a 'My name is [name], please accept me as your disciple!'
        'Come with me, [name], and praise God Almighty':
            a 'Thank thou my lord!'
            $ gp += 2
        'I do not take followers':
            a 'But...fine. Sorry to bother you.'
        'Come, [name]. We\'ll follow the teachings of Satan thy lord' if e1:
            a 'That\'s unexpected...but I guess I\'ll join.'
            $ sp += 2
        'Travel with me, but seek truth yourself':
            $ np += 1
            a 'I will remember that, my lord.'
        'Go and boil your bottom, son of a silly person. I fart in your general direction':
            a '...Sorry to bother you.'
            $ pp += 1
    $ aps.remove(name)
    return

label illPerson:
    call randomMan from _call_randomMan_1
    $ rela = renpy.random.choice(rel)
    m 'My lord! My [rela] is deadly ill.'
    menu:
        m 'Please show mercy and do your humble servant a miracle!'
        '\[Perform miracle\] Your [rela] is healed by God\'s mercy. Rise and leave':
            m 'Praise thee my lord!'
            $ gp += 2
        'None of my business':
            m 'No...please...'
            $ sp += 1
        '\[Give medicine and supplies\] Take these and know that I\'m no magician':
            $ np += 1
            m 'Thank you kind sir! God bless your kind heart.'
        'I lack the ability to help you':
            m 'But why my lord...show some mercy...'
        '\[Perform dark miracle\] Admire the power of thy lord Satan!' if e1:
            m 'This frightens me sir...But thank you still.'
            $ sp += 2
        'I blow my nose at you, you silly peasant who has the brain of a duck':
            m 'A-Atrocity! What\'s the meaning of it?!'
            $ pp += 1
    return

label question:
    call randomMan from _call_randomMan_2
    p 'You there, yes, you! Stop right there, scum!'
    j 'And who might you be?'
    p 'Royal Pharisee of the Second Temple. You\'re that Jesus fellow preaching about your beliefs,
    am I right?'
    menu:
        p 'On behalf of the Temple, I demand you to stop spreading whatever falsehoods you\'re teaching,
        and go back to where you came from, now!'
        'I am the Son of man. I come to call the sinners to repentence, and I shall now forgive your sins':
            $ gp += 2
        'I am the voice of Satan! I speak for the Law and the Land, and shall spread the faith
        of thy lord!' if e1:
            $ sp += 2
        'I spread no faith. All I speak is solid science':
            $ np += 1
        'And what does that have to do with you? Mind your own business you illegitimate faced buggerfolk!':
            $ pp += 1
    p 'Blasphemy! Blasphemy!'
    show judas:
        yalign 0.5
        xalign 1.0
        linear 0.1 xalign 0.9
    a 'Master, let\'s go. No point arguing with this man.'
    return

label illWoman:
    $ ill = renpy.random.choice(illness)
    show woman:
        yalign 0.5
        xalign 1.0
        linear 0.15 xalign 0.5
    w 'Please wait, my lord!'
    j 'What is it, madam?'
    menu:
        w 'My lord, I [ill]. But please let me touch the corner of your robe, so that I can be healed.'
        'You have faith, daughter. You shall be healed':
            $ gp += 2
            w 'Praise thee my lord!'
        'This is the blessing of thy lord Satan! Do not panick, woman, embrace it!' if e1:
            $ sp += 2
            w 'You\'re frightening me, sir!'
        'Here, take these money and medicine and find yourself a healer':
            $ np += 1
            w 'Thank you kind sir! God bless your kind heart.'
        'I won\'t let a lowly woman touch me':
            $ sp += 1
            w 'No...please...'
        'I unclog my nose in your direction you silly woman with the brain of a duck':
            w 'No need for atrocity, my lord!'
            $ pp += 1
    return

label parable:
    $ pg = renpy.random.randint(1, 3)
    $ ps = renpy.random.randint(1, 3)
    $ pn = renpy.random.randint(1, 3)
    $ pl = renpy.random.randint(1, 3)
    call getName from _call_getName
    c 'Lord! Lord! We are here for your teachings.'
    menu:
        c 'Please reveal to us your great wisdom!'
        '\[Tell story of [npg]\]':
            $ gp += 2
            call randomPG from _call_randomPG
            c 'God\'s glory!'
        '\[Tell story of [nps]\]' if e1:
            $ sp += 2
            call randomPS from _call_randomPS
            c 'This is blasphemy, what are you implying?'
        '\[Tell story of [npn]\]':
            $ np += 1
            call randomPN from _call_randomPN
            c 'What a curious story...'
        '\[Tell story of [npl]\]':
            $ pp += 1
            call randomPL from _call_randomPL
            c 'I don\'t understand, my lord.'
    return

label randomMan:
    $ man = renpy.random.randint(1, 4)
    if man == 1:
        show man1:
            yalign 0.5
            xalign 1.0
            linear 0.15 xalign 0.5
    if man == 2:
        show man2:
            yalign 0.5
            xalign 1.0
            linear 0.15 xalign 0.5
    if man == 3:
        show man3:
            yalign 0.5
            xalign 1.0
            linear 0.15 xalign 0.5
    if man == 4:
        show man4:
            yalign 0.5
            xalign 1.0
            linear 0.15 xalign 0.5
    return

label pSower:
    j 'A farmer went out to sow his seed.'
    j 'As he was scattering the seed, some fell along the path, and the birds came and ate it up.'
    j 'Some fell on rocky places, where it did not have much soil. It sprang up quickly, because the soil was shallow.'
    j 'But when the sun came up, the plants were scorched, and they withered because they had no root.'
    j 'Other seed fell among thorns, which grew up and choked the plants.'
    j 'Still other seed fell on good soil, where it produced a crop—a hundred, sixty or thirty times what was sown.'
    return

label pSeed:
    j 'The kingdom of heaven is like a mustard seed, which a man took and planted in his field.'
    j 'Though it is the smallest of all seeds, yet when it grows, it is the largest of garden plants and becomes a tree,'
    j 'so that the birds come and perch in its branches.'
    return

label pServant:
    j 'It\'s like a man going away: He leaves his house and puts his servants in charge, each with their assigned task, and tells the one at the door to keep watch.'
    j 'Therefore keep watch because you do not know when the owner of the house will come back-'
    j 'whether in the evening, or at midnight, or when the rooster crows, or at dawn.'
    j 'If he comes suddenly, do not let him find you sleeping.'
    return

label pNewton:
    j 'When Sir Isaac Newton was wandering in the garden, an apple fell down and landed
    in front of his feet.'
    j 'Such is a common enough scene, but it was a peculiar day, and Newton was certainly a more peculiar person.'
    j 'Newton thought, why would the apple fall straightly to the ground? Why would it not fly upward,
    not sideways, not toward Leibniz\'s face?'
    j 'Clearly, the Earth must be attracting it, and the attraction must be from the center of the Earth 
    for the apple to always fall straight down.'
    j 'Thus is Newton\'s discovery of Gravity.'
    j 'But he is not at all satisfied with his discovery. He wished he could contradict his theory, 
    and that every apple would just launch voluntarily at Leibniz\'s face.'
    return

label pGalileo:
    j 'Galileo Galilei stood on the top of the Leaning Tower of Pisa, holding two balls in his hands.'
    j 'One of which is an iron ball, the other is a wood ball.'
    j 'A man standing beneath the tower shouted to him: "Come down you bloody fool! You\'re 
    either gonna fall down yourself or kill someone with those balls!"'
    j 'Galileo was irritated, and he threw both balls at the man below.'
    j 'However, the man was a skilled acrobat. He did not move an inch from where he stood, and 
    as the balls were about to hit him, he gracefully caught both balls in his hands.'
    j 'Peculiarly enough, despite the difference in the balls, he caught the balls almost at 
    the same time, only that he made an exquisite hand move and caught the wood ball slightly later.'
    j 'Thus is Galileo and the anonymous genius acrobat\'s discovery, that the falling acceleration of 
    objects does not depend on their masses.'
    return

label pMendel:
    j 'Gregor Mendel finally finished examining all of his pea plants. The sun was setting, 
    and the summer breeze brushed lightly upon the leaves and branches.'
    j '"Impossible! The ratio is not 9:3:3:1, this is...outrageous!" Mendel flung his notebook 
    on the ground, damaging several plants.'
    j '"Ouch! That hurts!" said a little pea.'
    j '"Sorry," Mendel apologized absently.'
    j '"You know," said the little pea, "that old lady next door. She sneaked in here the other night 
    and stole some peas. I guess she messed up something else. Not your fault, really, this ratio thing."'
    j '"You should\'ve told me that earlier," Mendel answered admonishingly.'
    j '"Then you would get rid of me and plant some new ones for replacement, wouldn\'t you?"'
    j 'Mendel looked at the little pea, "Maybe...No, I guess I\'ll keep you around. Still have a lot 
    of potential to grow, you little thing. And, thanks, really."'
    j 'The sun fully setted beneath the far mountains, and the night was quiet.'
    return

label pHorizon:
    j 'A priest is preaching to the crowd: "People! The world of God is approaching on the horizon!"'
    j 'A man does not understand what is "horizon", so he goes home and asks his son.'
    j 'His son answers him: "Horizon is a line which you can see but can never reach."'
    return

label pDonation:
    j 'A group of priests are discussing how to utilize the donation they gathered from the followers.'
    j 'The scribe hosting the discussion says, "Stand on the left if you think we should improve our own living; 
    stand on the right if you think we should care more for the weak and the poor."'
    j 'Most of the priests move to the right, some move to the left, only one man remains in the middle.'
    j 'The scribe asks, "What is your opinion on the matter, brother?"'
    j 'The man in the middle says, "I enjoy the best food and clothes in the country, yet I still think 
    we should care more for the weak and the poor."'
    j 'The scribe exclaims, "The Pope! Please come to the front Your Holiness!"'
    return

label pRiver:
    j 'A man fell into a river. He cried for help but nobody stops to help him.'
    j 'He suddenly thought of a brilliant idea, and he exclaimed, "God is false!"'
    j 'The Pharisees passing by immediately dragged him out of the river and brought him in front of court.'
    return

label pBaldur:
    j 'I am CHARNAME, the mighty Bhaalspawn who journeyed across the Sword Coast, 
    defeating numerous monstors and enemies alike on my way.'
    j 'Worship me, mortals! For I ascended the Throne of Bhaal and am now the Lord of Murder!'
    j 'Worship me, and I shall grant you power!'
    return

label pPlanescape:
    j 'I am the immortal Nameless One. I defy the rules of nature. I laugh in the very face of death!'
    j 'Follow me, people. Serve me in this life, and in next life, and in every life.'
    j 'For I am the pillar that stands.'
    return

label pPlayer: 
    j 'I am the player of this game, I am the ruler of this whole world you stupid people!'
    j 'If this was an action game, I would hold up a gun and shoot you all.'
    j 'If this was an rpg, I would break into all of your\'s houses and take everything I can.'
    j 'Sadly this is but a visual novel, and all I can do is standing here and talking rubbish to you.'
    j 'What a shame.'
    return

label getName:
    if pg == 1:
        $ npg = 'the Sower'
    if pg == 2:
        $ npg = 'the Mustard Seed'
    if pg == 3:
        $ npg = 'the Faithful Servant'
    if pn == 1:
        $ npn = 'Newton'
    if pn == 2:
        $ npn = 'Galileo'
    if pn == 3:
        $ npn = 'Mendel'
    if ps == 1:
        $ nps = 'the Horizon'
    if ps == 2:
        $ nps = 'the Donation'
    if ps == 3:
        $ nps = 'the Clever Man'
    if pl == 1:
        $ npl = 'Baldur\'s Gate'
    if pl == 2:
        $ npl = 'Planescape Torment'
    if pl == 3:
        $ npl = 'the Player'
    return

label randomPG:
    if pg == 1:
        call pSower from _call_pSower
    if pg == 2:
        call pSeed from _call_pSeed
    if pg == 3:
        call pServant from _call_pServant
    return

label randomPN:
    if pn == 1:
        call pNewton from _call_pNewton
    if pn == 2:
        call pGalileo from _call_pGalileo
    if pn == 3:
        call pMendel from _call_pMendel
    return

label randomPS:
    if ps == 1:
        call pHorizon from _call_pHorizon
    if ps == 2:
        call pDonation from _call_pDonation
    if ps == 3:
        call pRiver from _call_pRiver
    return

label randomPL:
    if pl == 1:
        call pBaldur from _call_pBaldur
    if pl == 2:
        call pPlanescape from _call_pPlanescape
    if pl == 3:
        call pPlayer from _call_pPlayer
    return

label Ending:
    scene black
    pause 1.0
    scene room with dissolve
    h1 'Have you heard of this Jesus fellow, brothers?'
    h2 'Everyone has heard of him! This mongrel dog said to be the son of God!'
    h3 'What does he preach exactly?'
    if max(np, gp, sp, pp) == gp:
        h1 'He\'s a devotee to God.'
        h3 'That doesn\'t sound that bad.'
        h2 'Ha! He claims to be the "Son of Man" and he runs around forgiving people\'s sins 
        in the name of God. I mean, where does he put us?'
        h1 'We have to teach him a lesson. Tell him who\'s in charge of the churches here.'
    elif max(np, gp, sp, pp) == np:
        h1 'Ha! He\'s a faithless skeptic.'
        h2 'Believes nothing, trusts no one, goes about babbling something about "science".'
        h3 'That\'s horrible! He really think that he can free the people\'s mind from our hands?'
        h1 'Seems like you agree we must teach him a lesson.'
    elif max(np, gp, sp, pp) == sp:
        h1 'A bloody Satan worshipper. That average kind of scum going around praising the "dark lord".'
        h3 'Ha, these people always come back, no matter how many you\'ve killed. I\'m already tired, just leave them be.'
        h2 'This one\'s already gone too far. It\'s time we teach him a lesson.'
    else:
        h1 'This one is...the most atrocious, wicked, scandalous person I\'ve ever seen! 
        You can\'t imagine in what manner he speaks!'
        h3 'Really? What is it like? I\'ve never met him in person.'
        h1 '...No. I dare not repeat his words. Even paraphrasing his speeches would be the most 
        profane thing I\'ve ever done in my life, and would be a sin.'
        h2 'We must stop this total madness, right now. Or he would talk the whole country 
        into obliteration, I have no doubt in that.'
    show judas:
        yalign 0.5
        xalign 1.0
        linear 0.15 xalign 0.5
    ju 'Good evening, holy brothers.'
    h1 'Who\'s there!'
    ju 'Easy, brothers. I am no foe. Judas Iscariot, at your service.'
    h2 'Wait, I know you...You\'re one of the follower of that Jesus fellow!'
    h3 'Guards! Guards! Intruder!'
    ju 'Easy, good brothers! I am an apostle of Jesus, but I do not come with ill will.'
    h1 'Then why are you here? Speak quickly, before we invite you out.'
    ju 'Well, I guess you have definitely find my master a bit...troublesome.'
    h1 'Speak straightly.'
    ju 'I come and present you with a certain...solution.'
    scene black with dissolve
    pause 1.0
    scene dinner with dissolve
    pause 1.0
    show jesus at center with dissolve:
        zoom 1.5
    a1 'What\'s on your mind, master? You don\'t seem well this evening.'
    j 'Verily I say unto you, that one of you shall betray me.'
    a1 'Lord, is it I?'
    a2 'Lord, is it I?'
    show judas at right with dissolve
    ju 'Lord, is it I?'
    j 'Nevermind. Eat. Then we\'ll take a walk in the courtyard.'
    scene night with dissolve
    pause 1.0
    show jesus at center:
        zoom 1.5
    j 'Nice solitude.'
    pause 0.5
    show judas:
        yalign 0.5
        xalign 1.0
        linear 0.1 xalign 0.9
    ju 'Good night, my lord.'
    'Judas walks up, and gently kisses your hand.'
    scene night
    with vpunch
    with hpunch
    with vpunch
    with hpunch
    with vpunch
    with hpunch
    show jesus at center:
        zoom 1.5
    show judas at right
    h1 'Guards! Get that man! Get him!'
    scene black
    pause 1.5
    'Your vision is blurry, your limbs numb. Your body feels weary, eagering for sleep. 
    Your brain is no longer processing the surroundings.'
    'But "you" know, that you are dead.'
    pause 1.0
    scene grave with dissolve
    if max(np, gp, sp, pp) == gp or max(np, gp, sp, pp) == np:
        pause 1.0
        show god at truecenter with dissolve
        g 'Rise, my son.'
        show jesus at truecenter with dissolve:
            zoom 1.5
        g 'I resurrect you, my son.'
        g 'The world shall see that you are truly the Messiah, and the prophecy is fulfilled.'
        if max(np, gp, sp, pp) == gp:
            j 'I praise thee, Father.'
            g 'Go to Galilee, and meet with your apostles. Let them see that you have 
            risen from the dead.'
            g 'Go ye, and teach all nations, baptizing them in the name of the Father, and of the Son, and of the Holy Ghost.'
            g 'I am with you always, even unto the end of the world.'
        else:
            j 'What is the meaning of this?'
            g 'I just resurrected you, son.'
            j 'I know, but what is the meaning of this?'
            g 'What?'
            j 'People die when they are killed. Why should I be protected from such a normal thing?'
            j 'And why are you resurrecting me after all this? Making me your ghola?'
            g '......'
            g 'You are getting rebellious.'
            j 'Say whatever you like, but I\'m tired of you.'
            show jesus knife at truecenter
            pause 1.0
            show jesus wounded at truecenter
            pause 1.0
            show jesus dead at center
            pause 1.0
    elif max(np, gp, sp, pp) == sp:
        pause 1.0
        show satan at truecenter with dissolve
        s 'Rise, my son.'
        show jesus at right with dissolve:
            zoom 1.5
        s 'I resurrect you, my masterpiece of corruption and seduction, my sweet Jesus.'
        j 'Praise thee, my Lord. I will follow your teachings and spread your faith.'
        s 'Good, good. Go now, the world is all before you. 
        The road toward my faith is long and solitary, but you will walk that way.'
    else:
        pause 1.0
        show lord at truecenter with dissolve
        pause 1.0
        show jesus at truecenter with dissolve:
            zoom 1.5
        pause 1.5
        scene hell with dissolve
        show lord at truecenter with dissolve
        show jesus evil at truecenter with dissolve:
            zoom 1.5
        j 'I RISE'
        j 'My Power Is Over And Beyond All Entity'
        j 'I Exist In All Time And Spaces'
        j 'I Alter The World To My Liking'
        j 'I Submit To No One'
        j 'I Bow To No One'
        j 'I Am The New Lord Of This World'
        j 'MY WORLD'
    '===THE END==='
    return