
print("Welcome to your Horoscope")

star_sign = str(input("Type your star sign to get your horoscope: "))
print("\n")

#Aquarius
aq = ["Jan 20 - Feb 18", "Air", "Light-Blue, Silver", "Fixed", "Saturday", "Uranus, Saturn", "Leo, Sagittarius", "4, 7, 11, 22, 29"]
aq_traits = ["Progressive, original, independent, humanitarian", "Runs from emotional expression, temperamental, uncompromising, aloof", "Fun with friends, risky business, fighting for causes, intellectual conversations", "Limitations, broken promises, being lonely, dull or boring situations"]

#Pisces
pi = ["Feb 19 - March 20", "Mauve", "Lilac, Purple, Violet, Sea Green", "Mutable", "Thursday", "Neptune, Jupiter", "Virgo, Taurus", "3, 9, 12, 15, 18, 24"]
pi_traits = ["Compassionate, artistic, intuitive, gentle, wise, musical", "Fearful, overly trusting, sad, desire to escape reality, can be a victim or a martyr", "Being alone, love, sleeping, music, romance, swimming, spiritual themes", "Know-it-all, being criticized, the past coming back to haunt, cruelty of any kind"]


#Aries
ar = ["Mar 21 - Apr 19", "Fire", "Red", "Cardinal", "Tuesday", "Mars", "Libra, Leo", "1, 8, 17"]
ar_traits = ["Courageous, determined, confident, enthusiastic, optimistic, honest, passionate", "Impatient, moody, short-tempered, impulsive, aggressive", "Comfortable clothes, taking on leadership roles, physical challenges, individual sports", "Inactivity, delays, work that does not use one's talents"]


#Taurus
ta = ["Apr 20 - May 20", "Earth", "Green, Pink", "Fixed", "Friday, Monday", "Venus", "Scorpio, Cancer", "2, 6, 9, 12, 24"]
ta_traits = ["Reliable, patient, practical, devoted, responsible, stable", "Stubborn, possessive, uncompromising", "Gardening, cooking, music, romance, high quality clothes, working with hands", "Sudden changes, complications, insecurity of any kind, synthetic fabrics"]


#Gemnini
ge = ["May 21 - Jun 20", "Air", "Light-Green, Yellow", "Mutable", "Wednesday", "Mercury", "Sagittarius, Aquarius", "5, 7, 14, 23"]
ge_traits = ["Gentle, affectionate, curious, adaptable, ability to learn quickly and exchange ideas", "Nervous, inconsistent, indecisive", "Music, books, magazines, chats with nearly anyone, short trips around the town", "Being alone, being confined, repetition and routine"]


#Cancer
ca = ["Jun 21 - Jul 22", "Water", "White", "Cardinal", "Monday, Thursday", "Moon", "Capricorn, Taurus", "2, 3, 15, 20"]
ca_traits = ["Tenacious, highly imaginative, loyal, emotional, sympathetic, persuasive", "Moody, pessimistic, suspicious, manipulative, insecure", "Art, home-based hobbies, relaxing near or in water, helping loved ones, a good meal with friends", "Strangers, any criticism of Mom, revealing of personal life"]

#Leo
leo = ["Jul 23 - Aug 22", "Fire", "Gold, Yellow, Orange", "Fixed", "Sunday", "SUn", "Aquarius, Gemini", "1, 3, 10, 19"]
leo_traits = ["Creative, passionate, generous, warm-hearted, cheerful, humorous", "Arrogant, stubborn, self-centered, lazy, inflexible", "Theater, taking holidays, being admired, expensive things, bright colors, fun with friends", "Being ignored, facing difficult reality, not being treated like a king or queen"]


#Virgo
vi = ["Aug 23 - Sep 22", "Earth", "Grey, Beige, Pale-Yellow", "Mutable", "Wednesday", "Mercury", "Pisces, Cancer", "5, 14, 15, 23, 32"]
vi_traits = ["Loyal, analytical, kind, hardworking, practical", "Shyness, worry, overly critical of self and others, all work and no play", "Animals, healthy food, books, nature, cleanliness", "Rudeness, asking for help, taking center stage"]


#Libra
li = ["Sep 23 - Oct 22", "Air", "Pink, Green", "Cardinal", "Friday", "Venus", "Aries, Sagittarius", "4, 6, 13, 15, 24"]
li_traits = ["Cooperative,diplomatic, gracious, fair-minded, social", "Indecisive, avoids confrontations, will carry a grudge, self-pity", "Harmony, gentleness, sharing with others, the outdoors", "Violence, injustice, loudmouths, conformity"]


#Scorpio
sc = ["Oct 23 - Nov 21", "Water", "Scarlet, Red, Rust", "Fixed", "Tuesday", "Pluto, Mars", "Taurus, Cancer", "8, 11, 18, 22"]
sc_traits = ["Resourceful, powerful, brave, passionate, a true friend", "Distrusting, jealous, manipulative, violent", "Truth, facts, being right, talents, teasing, passion", "Dishonesty, revealing secrets, superficiality, small talk"]


#Sagittarius
sa = ["Nov 22 - Dec 21", "Fire", "Blue", "Mutable", "Thursday", "Jupiter", "Gemini, Aries", "3, 7, 9, 12, 21"]
sa_traits = ["Generous, idealistic, great sense of humor", "Promises more than can deliver, very impatient, will say anything no matter how undiplomatic", "Freedom, travel, philosophy, being outdoors", "Clingy people, being constrained, off-the-wall theories, details"]


#Capricorn
cap = ["Dec 22 - Jan 19", "Earth", "Brown, Black", "Cardinal", "Saturday", "Saturn", "Taurus, Cancer", "4, 8, 13, 22"]
cap_traits = ["Responsible, disciplined, self-control, good managers", "Know-it-all, unforgiving, condescending, expecting the", "Family, tradition, music, understated status, quality craftsmanship", "Almost everything at some point"]



if star_sign == str("Aquarius") or star_sign == str("aquarius"):
    print("----------Aquarius Facts----------")
    print(f"Date: {aq[0]} \nElement: {aq[1]} \nColor: {aq[2]} \nQuality: {aq[3]} \nDay: {aq[4]} \nRuler: {aq[5]} \nGreatest Compatibility: {aq[6]} \nLucky Numbers: {aq[7]}")
    print("\n")
    print("----------Aquarius Traits----------")
    print(f"Strenghts: {aq_traits[0]} \nWeaknesses: {aq_traits[1]} \nAquarius likes: {aq_traits[2]} \nAquarius dislikes: {aq_traits[3]}")
    print("\n")
    ans = str(input("If you want to read more about your zodiac, type 'Yes'. If not 'No': "))
    if ans == str("Yes") or ans == str("yes"):
        print("\n")
        print("https://www.zodiacsign.com/zodiac-signs/aquarius/")
    else:
        pass


elif star_sign == str("Pisces") or star_sign == str("pisces"):
    print("----------Pisces Facts----------")
    print(f"Date: {pi[0]} \nElement: {pi[1]} \nColor: {pi[2]} \nQuality: {pi[3]} \nDay: {pi[4]} \nRuler: {pi[5]} \nGreatest Compatibility: {pi[6]} \nLucky Numbers: {pi[7]}")
    print("\n")
    print("----------Pisces Traits----------")
    print(f"Strenghts: {pi_traits[0]} \nWeaknesses: {pi_traits[1]} \nPisces likes: {pi_traits[2]} \nPisces dislikes: {pi_traits[3]}")
    print("\n")
    ans = str(input("If you want to read more about your zodiac, type 'Yes'. If not 'No': "))
    if ans == str("Yes") or ans == str("yes"):
        print("\n")
        print("https://www.zodiacsign.com/zodiac-signs/pisces/")
    else:
        pass


elif star_sign == str("Aries") or star_sign == str("aries"):
    print("----------Aries Facts----------")
    print(f"Date: {ar[0]} \nElement: {ar[1]} \nColor: {ar[2]} \nQuality: {ar[3]} \nDay: {ar[4]} \nRuler: {ar[5]} \nGreatest Compatibility: {ar[6]} \nLucky Numbers: {ar[7]}")
    print("\n")
    print("----------Pisces Traits----------")
    print(f"Strenghts: {ar_traits[0]} \nWeaknesses: {ar_traits[1]} \nPisces likes: {ar_traits[2]} \nPisces dislikes: {ar_traits[3]}")
    print("\n")
    ans = str(input("If you want to read more about your zodiac, type 'Yes'. If not 'No': "))
    if ans == str("Yes") or ans == str("yes"):
        print("\n")
        print("https://www.zodiacsign.com/zodiac-signs/aries/")
    else:
        pass

elif star_sign == str("Taurus") or star_sign == str("taurus"):
    print("----------Taurus Facts----------")
    print(f"Date: {ta[0]} \nElement: {ta[1]} \nColor: {ta[2]} \nQuality: {ta[3]} \nDay: {ta[4]} \nRuler: {ta[5]} \nGreatest Compatibility: {ta[6]} \nLucky Numbers: {ta[7]}")
    print("\n")
    print("----------Taurus Traits----------")
    print(f"Strenghts: {ta_traits[0]} \nWeaknesses: {ta_traits[1]} \nPisces likes: {ta_traits[2]} \nPisces dislikes: {ta_traits[3]}")
    print("\n")
    ans = str(input("If you want to read more about your zodiac, type 'Yes'. If not 'No': "))
    if ans == str("Yes") or ans == str("yes"):
        print("\n")
        print("https://www.zodiacsign.com/zodiac-signs/taurus/")
    else:
        pass

elif star_sign == str("Gemini") or star_sign == str("gemini"):
    print("----------Gemini Facts----------")
    print(f"Date: {ge[0]} \nElement: {ge[1]} \nColor: {ge[2]} \nQuality: {ge[3]} \nDay: {ge[4]} \nRuler: {ge[5]} \nGreatest Compatibility: {ge[6]} \nLucky Numbers: {ge[7]}")
    print("\n")
    print("----------Gemini Traits----------")
    print(f"Strenghts: {ge_traits[0]} \nWeaknesses: {ge_traits[1]} \nPisces likes: {ge_traits[2]} \nPisces dislikes: {ge_traits[3]}")
    print("\n")
    ans = str(input("If you want to read more about your zodiac, type 'Yes'. If not 'No': "))
    if ans == str("Yes") or ans == str("yes"):
        print("\n")
        print("https://www.zodiacsign.com/zodiac-signs/gemini/")
    else:
        pass

elif star_sign == str("Cancer") or star_sign == str("cancer"):
    print("----------Cancer Facts----------")
    print(f"Date: {ca[0]} \nElement: {ca[1]} \nColor: {ca[2]} \nQuality: {ca[3]} \nDay: {ca[4]} \nRuler: {ca[5]} \nGreatest Compatibility: {ca[6]} \nLucky Numbers: {ca[7]}")
    print("\n")
    print("----------Cancer Traits----------")
    print(f"Strenghts: {ca_traits[0]} \nWeaknesses: {ca_traits[1]} \nPisces likes: {ca_traits[2]} \nPisces dislikes: {ca_traits[3]}")
    print("\n")
    ans = str(input("If you want to read more about your zodiac, type 'Yes'. If not 'No': "))
    if ans == str("Yes") or ans == str("yes"):
        print("\n")
        print("https://www.zodiacsign.com/zodiac-signs/cancer/")
    else:
        pass

elif star_sign == str("Leo") or star_sign == str("leo"):
    print("----------Leo Facts----------")
    print(f"Date: {leo[0]} \nElement: {leo[1]} \nColor: {leo[2]} \nQuality: {leo[3]} \nDay: {leo[4]} \nRuler: {leo[5]} \nGreatest Compatibility: {leo[6]} \nLucky Numbers: {leo[7]}")
    print("\n")
    print("----------Leo Traits----------")
    print(f"Strenghts: {leo_traits[0]} \nWeaknesses: {leo_traits[1]} \nPisces likes: {leo_traits[2]} \nPisces dislikes: {leo_traits[3]}")
    print("\n")
    ans = str(input("If you want to read more about your zodiac, type 'Yes'. If not 'No': "))
    if ans == str("Yes") or ans == str("yes"):
        print("\n")
        print("https://www.zodiacsign.com/zodiac-signs/leo/")
    else:
        pass

elif star_sign == str("Virgo") or star_sign == str("virgo"):
    print("----------Virgo Facts----------")
    print(f"Date: {vi[0]} \nElement: {vi[1]} \nColor: {vi[2]} \nQuality: {vi[3]} \nDay: {vi[4]} \nRuler: {vi[5]} \nGreatest Compatibility: {vi[6]} \nLucky Numbers: {vi[7]}")
    print("\n")
    print("----------Virgo Traits----------")
    print(f"Strenghts: {vi_traits[0]} \nWeaknesses: {vi_traits[1]} \nPisces likes: {vi_traits[2]} \nPisces dislikes: {vi_traits[3]}")
    print("\n")
    ans = str(input("If you want to read more about your zodiac, type 'Yes'. If not 'No': "))
    if ans == str("Yes") or ans == str("yes"):
        print("\n")
        print("https://www.zodiacsign.com/zodiac-signs/virgo/")
    else:
        pass

elif star_sign == str("Libra") or star_sign == str("libra"):
    print("----------Libra Facts----------")
    print(f"Date: {li[0]} \nElement: {li[1]} \nColor: {li[2]} \nQuality: {li[3]} \nDay: {li[4]} \nRuler: {li[5]} \nGreatest Compatibility: {li[6]} \nLucky Numbers: {li[7]}")
    print("\n")
    print("----------Libra Traits----------")
    print(f"Strenghts: {li_traits[0]} \nWeaknesses: {li_traits[1]} \nPisces likes: {li_traits[2]} \nPisces dislikes: {li_traits[3]}")
    print("\n")
    ans = str(input("If you want to read more about your zodiac, type 'Yes'. If not 'No': "))
    if ans == str("Yes") or ans == str("yes"):
        print("\n")
        print("https://www.zodiacsign.com/zodiac-signs/libra/")
    else:
        pass

elif star_sign == str("Scorpio") or star_sign == str("scorpio"):
    print("----------Scorpio Facts----------")
    print(f"Date: {sc[0]} \nElement: {sc[1]} \nColor: {sc[2]} \nQuality: {sc[3]} \nDay: {sc[4]} \nRuler: {sc[5]} \nGreatest Compatibility: {sc[6]} \nLucky Numbers: {sc[7]}")
    print("\n")
    print("----------Scorpio Traits----------")
    print(f"Strenghts: {sc_traits[0]} \nWeaknesses: {sc_traits[1]} \nPisces likes: {sc_traits[2]} \nPisces dislikes: {sc_traits[3]}")
    print("\n")
    ans = str(input("If you want to read more about your zodiac, type 'Yes'. If not 'No': "))
    if ans == str("Yes") or ans == str("yes"):
        print("\n")
        print("https://www.zodiacsign.com/zodiac-signs/scorpio/")
    else:
        pass

elif star_sign == str("Sagittarius") or star_sign == str("sagittarius"):
    print("----------Sagittarius Facts----------")
    print(f"Date: {sa[0]} \nElement: {sa[1]} \nColor: {sa[2]} \nQuality: {sa[3]} \nDay: {sa[4]} \nRuler: {sa[5]} \nGreatest Compatibility: {sa[6]} \nLucky Numbers: {sa[7]}")
    print("\n")
    print("----------Sagittarius Traits----------")
    print(f"Strenghts: {sa_traits[0]} \nWeaknesses: {sa_traits[1]} \nPisces likes: {sa_traits[2]} \nPisces dislikes: {sa_traits[3]}")
    print("\n")
    ans = str(input("If you want to read more about your zodiac, type 'Yes'. If not 'No': "))
    if ans == str("Yes") or ans == str("yes"):
        print("\n")
        print("https://www.zodiacsign.com/zodiac-signs/sagittarius/")
    else:
        pass

elif star_sign == str("Capricorn") or star_sign == str("capricorn"):
    print("----------Capricorn Facts----------")
    print(f"Date: {ca[0]} \nElement: {ca[1]} \nColor: {ca[2]} \nQuality: {ca[3]} \nDay: {ca[4]} \nRuler: {ca[5]} \nGreatest Compatibility: {ca[6]} \nLucky Numbers: {ca[7]}")
    print("\n")
    print("----------Capricorn Traits----------")
    print(f"Strenghts: {ca_traits[0]} \nWeaknesses: {ca_traits[1]} \nPisces likes: {ca_traits[2]} \nPisces dislikes: {ca_traits[3]}")
    print("\n")
    ans = str(input("If you want to read more about your zodiac, type 'Yes'. If not 'No': "))
    if ans == str("Yes") or ans == str("yes"):
        print("\n")
        print("https://www.zodiacsign.com/zodiac-signs/capricorn/")
    else:
        pass

else:
    print("Error! Type in an available zodiac sign.")