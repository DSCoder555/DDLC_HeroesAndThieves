label story:
    # show sayori 1a at t11 zorder 1
    # s "Hey, I think I got the basics!"
    # show sayori at t21
    # s "Time to give up and \"play smash\""

    # play music t3
    # scene bg club_day
    # show monika 1a at t11
    # m "{b}Hi!{/b}"
    # m 1b "{i}What's up?{/i}"
    # m "I am-{nw}"
    # mc "Shush!"
    # m "{w=1}.{w=1}.{w=1}."
    # m "{w=1}.{w=1}.{w=1}.{nw}"
    # m "Oof!" (what_size=50, what_color="#32a852")

    # Every comment above is from tutorials, the code below is my attempt to convert the script.

    # Friday: The first part needs a lot of new assets, so many parts use wrong assets, FIX LATER
    $ mc_name = renpy.input("What is your name?")# Uncentered need to fix
    narrator "Friday"
    pause(2.0)
    scene bg corridor with dissolve_scene_full
    show yuri 1a at t21
    h "Hey buddy! Wake up!"
    narrator "I groan as I’m woken up from whatever wonderful dream I was having to somebody tapping me repeatedly on the shoulder. I look to my left to see a middle aged man hovering over me."
    h "Do you mind getting up for me pal? I’m trying to get to the bathroom and I don’t wanna climb over you."
    mc "Oh {w=1}…{w=1} uhhh sure."
    narrator "Just then, I hear a small ding as an announcement comes on the speaker."
    narrator "Attention everyone, this is your captain speaking. We will be making our descent shortly so, I’m going to need everyone to either return to or stay in your seats. Thank you and welcome to Sakura City!"
    narrator "I chuckle a little"
    mc "Sorry, guess not man."
    h "Damn."
    narrator "He sits down again looking defeated. I contemplate going back to sleep when the man opens the window next to his seat, blinding me with the bright light."
    narrator "I shrug it off and decide to take in the reality of my situation instead."
    mc "What the hell am I doing here?" (what_size = 10)
    narrator "I whisper this to myself but it appears the man next to me heard me speak."
    h "You talking to yourself buddy?"
    mc "I’m just trying to collect my thoughts."
    h "Long flight?"
    mc "More like a long week."
    h "I know how that feels. I think everybody’s had weeks like that."
    narrator "I nod. The conversation goes quiet for a while until the man speaks up again."
    h "So why are you traveling? Personally, I’ve come to see my family. I was supposed to be on a business trip but my daughter’s having some kinda crisis right now."
    h "Work is important but family comes first, you know?"
    mc "Yeah, I understand that. Family is important. Oh and I’m here for work actually."
    h "Work? Kid, you look way too young to have a job that requires you to travel."
    mc "Yeah, but this isn’t an ordinary job, and I’m not an ordinary worker."
    narrator "He raises his eyebrow curiously."
    h "Oh? What kind of job do you have?"
    mc "One that requires discretion."
    $ h_name = "Hayato"
    h "Hah! Now you’ve got me hooked. I like you kid. You seem like you’ve got a bright future ahead of you. Oh and my name’s Hayato by the way."
    mc "[mc_name]"
    narrator "We talk for a few more minutes before we finally land. I grab my two suitcases before quickly waving Hayato goodbye and exiting the plane. I get to street level and step outside to the pickup area."
    narrator "After a few mere seconds, a silver SUV pulls up in front of me. All the windows are tinted so that I can’t see inside. The window closest to me rolls down slightly and I hear a man's voice."
    r "Get in"
    narrator "I put my bags in the trunk of the car and then attempt to open the passenger side door. It’s locked."
    r "The back."
    narrator "I open the back door and get in. There is a wall of tinted glass separating the back of the car from the front making me unable to see the driver. I close the door and the car starts to move."
    mc "Do you know where we’re going?"
    r "Yes."
    narrator "I figure that he isn’t in the mood for conversation so I wait patiently to arrive at my destination. Approximately forty minutes later, the car stops and the driver speaks up."
    scene bg house
    r "We’re here, get out."
    narrator "I exit the car and open the trunk. After taking my bags out and closing the trunk, the car immediately drives away."
    mc "What a prick."
    narrator "I look around and see that I’m in a residential neighborhood. Scanning the nearby houses for their addresses, I find the one I was supposed to go to."
    narrator "I take my bags and enter through the gate. I see a bald man with a black trench coat and sunglasses sitting on the steps next to the door. He has a black duffel bag and a brown suitcase which I recognize. It’s one of mine."
    mc "You don’t look suspicious at all!"
