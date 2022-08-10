import random


print(" ")


name = input('Please enter player name: ')
print(" ")
print('Dear ', name+'. You have embarked on a new journey. You find yourself situated in a dangerous and horrible situation. There is a horrible curse contaminating your village. COVID-69. This curse was casted by the horrible witch near your village. The village folk have asked you to slay this witch and avenge the ones that have fell victim to this curse.')
print(' ')
enter = input('Press Enter')
print(' ')
print('Due to your nature and nourishment you have recieved in your upbringing, this is your stats.')
print(' ')
print(name)
charm = random.randint(1, 5)
strength = random.randint(1, 5)
intellegence = random.randint(1, 5)
print('Charm:', charm)
print('Strength:', strength)
print('Intellegence', intellegence)
print(' ')
enter = input('Press Enter')
print(' ')


print("You should start by finding out where is the witch")

print(" ")


# cartographer

print(name+", you procede to the cartographer's house. He lives ontop of the hill with a great view for optimal map producement")
print(' ')

option = int(
    input('Option: What will you do? (1)Knock on door.		(2)Break door down'))
print(" ")
if option == 1:
    print(' ')
    print("You knock on the door and a panting man with a pencil in his ear and a telescope in his hand opens the door")
    print(" ")
elif option == 2 and strength > 2:
    print(' ')
    print("You break down the door to find a strange man crying infront of his mirror")
    print(" ")
    print('He is schocked and embarresed')
else:
    print(' ')
    print('Your stength is not above 2. You run straigt into the door and fall backwards')

print(' ')

print("PinkEye the cartographer: What is the meaning of this? I Am busy drawing maps and watching a villager family from my beautiful hill view. I am very busy")
print(' ')
enter = input('Press Enter')
print(' ')
print(name+": I am", name, "and I am here to ask you to draw me a map!")
print("PinkEye the cartographer: For what reason will I ever draw you a map? You have invoked my private time")
print(' ')
enter = input('Press Enter')
print(' ')
print("I wish to recieve a map to the witch's lair so that I may slay her")
print(' ')
enter = input('Press Enter')
print(' ')
print('PinkEye the cartographer: Very well. I already have a map to the dreached witch lair. I will give it to you as the horrible curse is bugging me almost as much as you are.')
print(' ')
enter = input('Press Enter')
print(' ')
print('Awesome. I have obtained my map. Now to visit the scholar. He wil be able to tell me how I can slay the wicked witch')
print(' ')
enter = input('Press Enter')
print(' ')


chasity = False


print('Upon walking toe the scholar you encounter a fair maiden.')
option = int(input(
    'What will you do? (1)Give her a compliment		(2)Show her your muscles		(3)Talk about math'))

if option == 1 and charm >= 3:
    print(' ')
    print('The maidan is flusterd, never has a man spoken to her with such charm. She gives you her chasity key')
    chasity = True
    print(' ')
elif option == 1 and charm < 3:
    print(' ')
    print('She slaps you and walks away after you said she looks too healthy for this village')
    print(' ')
elif option == 2 and strength >= 3:
    print("The maidan is flusterd, never has a man ever showed her such big muscles. She gives you her chasity key")
    print(" ")
    chasity = True
elif option == 2 and strength < 3:
    print(' ')
    print('She runs to you and start feeding you her last bread, as you looked underfed and weak. strength +1')
    strength = strength + 1
elif option == 3 and intellegence >= 3:
    print(" ")
    print("The maidan is flusterd, never has a man spoken to her with such intellegance. She gives you her chasity key,you must be smart XD")
    chasity = True
elif option == 3 and intellegence < 3:
    print(' ')
    print('She starts to laugh. She is an actual mathmatician and knows you are talking ribbirish.')
print(" ")
print('You Walk away with a feeling of confusion')

print(' ')

print('You find the scholar in the librairy. He is coverd in gray hairs is you realise that he lives up to his name')

print(" ")
enter = input("please press enter")
print(" ")

print("Gray-ear the scholar: Geetings", name, "I have been expecting you")
option = int(input(
    "option: (1)Ask how to defeat the witch.		(2)Do a funky dance to show that you are confused"))

print(' ')

if option == 1:
    print(name+": You are indeed very wise, gray-ear the scholar, Do you know how i will be able to defeat the witch?")
else:
    print('Gray-ear the scholar: wow, you are indeed something special. The prophicy has foretold of your interesting dancing.')

print(" ")
print('Gray-ear the scholar: it is simple. You will have to do a dance. This dance will mislead the witch into letting off her guard. Then you shall stab her with the excaliber sword. Located at the blacksmith. This is the only sword that can slay the Witch and lift the COVID-69 curse.')

print(" ")

print(" ")
print('You approach the blacksmitch. He is in the kingdoms smithing ring.')
print(' ')
print('You see the magical sword is up for sale. What will you do?')
print('')
option = int(input("Option: (1)Charm your way into him giving you the sword.		(2)Beat him up and take the sword		(3)Trick him into giving you the sword		(4)Trade his daughters chasity key for the sword"))

print(' ')

if option == 1 and charm >= 3:
    print(' ')
    print('The blacksmith is impressed. He has never been so impressed in his 19 years of life. in appreciation, he gives you the sword')
    print(' ')
elif option == 1 and charm < 3:
    print(' ')
    print('The blacksmith is disgusted, he knocks you out')
    print(' You wake up, sneak around and steal the sword')
    print(' ')
elif option == 2 and strength >= 3:
    print("you kick the blacksmith in the nuts, poke him in the eyes, pull his goatee and take his magiccal sword.")
elif option == 2 and strength < 3:
    print('The blacksmith is disgusted, he knocks you out')
    print(' You wake up, sneak around and steal the sword')
elif option == 3 and intellegence >= 3:
    print("The blacksmith is confused, he feels obliged to give you the sword, he gives it")
    print("")
elif option == 3 and intellegence < 3:
    print(' ')
    print('The blacksmith takes pitty on you. He gives you the sword to defend yourself because he can see you are not very smart')
elif chasity == True:
    print('You show the blacksmith his daughters chasity key, he feels ashamed for having such a daughter. Then you trade it for the sword')
elif chasity == False:
    print("You do not have the key, so you spit in his eyes and steal the sword")

print(" ")

print('Now that I have all I need, The map, the plan and the sword- I can defeat the witch.')
print(" ")
print("I proceed to her cave. Sneak in and find the witch sleeping on a rag. She looks terrible.")
print("")
enter = input("Press enter")
print(" ")

option = int(input(
    'Option: What will you do now? (1) stab her while sleeping. (2)Do a Funky dance'))
print(" ")

if option == 1:
    print('The witch wakes up before you could stab her. She places you under a curse. You will be a Alone forever')
    print(" ")
elif option == 2:
    print("She wakes up, interessted by this funky dance, she lets her guard down and start dancing with you.")
    print(" ")
    print('You stab her with the special sword and lift the COVID-69 curse off your village')
print(" ")
print('end')
