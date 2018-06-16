"""Generates a random date and uses that date to print information about
the corresponding Zodiac sign.

Zodiac date ranges come from here: 
- http://astrostyle.com/zodiac-sign-dates/

Zodiac sign characterstics come from here:
- http://nuclear.ucdavis.edu/~rpicha/personal/astrology/

Astrology is absolute BS and is not a science, but it's consistent enough
to use for an example like this.
"""
import random

aries = """Adventurous and energetic
Pioneering and courageous
Enthusiastic and confident
Dynamic and quick-witted 

Selfish and quick-tempered
Impulsive and impatient
Foolhardy and daredevil"""

taurus = """Patient and reliable
Warmhearted and loving
Persistent and determined
Placid and security loving

Jealous and possessive
Resentful and inflexible
Self-indulgent and greedy"""

gemini = """Adaptable and versatile
Communicative and witty
Intellectual and eloquent
Youthful and lively

Nervous and tense
Superficial and inconsistent
Cunning and inquisitive"""

cancer = """Emotional and loving
Intuitive and imaginative
Shrewd and cautious
Protective and sympathetic

Changeable and moody
Overemotional and touchy
Clinging and unable to let go"""

leo = """Generous and warmhearted
Creative and enthusiastic
Broad-minded and expansive
Faithful and loving

Pompous and patronizing
Bossy and interfering
Dogmatic and intolerant"""

virgo = """Modest and shy 
Meticulous and reliable 
Practical and diligent 
Intelligent and analytical 

Fussy and a worrier 
Overcritical and harsh 
Perfectionist and conservative"""

libra = """Diplomatic and urbane 
Romantic and charming 
Easygoing and sociable 
Idealistic and peaceable 

Indecisive and changeable 
Gullible and easily influenced
Flirtatious and self-indulgent"""

scorpio = """Determined and forceful 
Emotional and intuitive 
Powerful and passionate 
Exciting and magnetic 

Jealous and resentful 
Compulsive and obsessive 
Secretive and obstinate"""

sagittarius = """Optimistic and freedom-loving 
Jovial and good-humored 
Honest and straightforward 
Intellectual and philosophical 

Blindly optimistic and careless 
Irresponsible and superficial 
Tactless and restless"""

capricorn = """Practical and prudent 
Ambitious and disciplined 
Patient and careful 
Humorous and reserved 

Pessimistic and fatalistic 
Miserly and grudging"""

aquarius = """Friendly and humanitarian 
Honest and loyal 
Original and inventive 
Independent and intellectual 

Intractable and contrary 
Perverse and unpredictable 
Unemotional and detached"""

pisces = """Imaginative and sensitive 
Compassionate and kind 
Selfless and unworldly 
Intuitive and sympathetic 

Escapist and idealistic 
Secretive and vague 
Weak-willed and easily led"""

month = random.randint(1, 12)

if month == 2:
    day = random.randint(1, 29)
elif (month == 4) or (month == 6) or (month == 9) or (month == 11):
    day = random.randint(1, 30)
else:
    day = random.randint(1, 31)

msg = f"{month}/{day} is for "

if ((month == 1) and (day <= 20)) or ((month == 12) and (day >= 23)):
    print(msg + "Capricorn!\n")
    print(capricorn)
elif ((month == 1) and (day >= 21)) or (month == 2) and (day <= 19):
    print(msg + "Aquarius!\n")
    print(aquarius)
elif ((month == 2) and (day >= 20)) or (month == 3) and (day <= 20):
    print(msg + "Pisces!\n")
    print(pisces)
elif ((month == 3) and (day >= 21)) or (month == 4) and (day <= 20):
    print(msg + "Aries!\n")
    print(aries)
elif ((month == 4) and (day >= 21)) or (month == 5) and (day <= 21):
    print(msg + "Taurus!\n")
    print(taurus)
elif ((month == 5) and (day >= 22)) or (month == 6) and (day <= 21):
    print(msg + "Gemini!\n")
    print(gemini)
elif ((month == 6) and (day >= 22)) or (month == 7) and (day <= 22):
    print(msg + "Cancer!\n")
    print(cancer)
elif ((month == 7) and (day >= 23)) or (month == 8) and (day <= 21):
    print(msg + "Leo!\n")
    print(leo)
elif ((month == 8) and (day >= 22)) or (month == 9) and (day <= 23):
    print(msg + "Virgo!\n")
    print(virgo)
elif ((month == 9) and (day >= 24)) or (month == 10) and (day <= 23):
    print(msg + "Libra!\n")
    print(libra)
elif ((month == 10) and (day >= 24)) or (month == 11) and (day <= 22):
    print(msg + "Scorpio!\n")
    print(scorpio)
elif ((month == 11) and (day >= 23)) or (month == 12) and (day <= 22):
    print(msg + "Sagittarius!\n")
    print(sagittarius)
