# Welcome statement
print("----------------------------------------------")
print("Welcome to the Jamaican Driver's License Test!")
print("----------------------------------------------")

print("\nYou need at least 75% to pass.")

begin = input("\nWould you like to begin the test? ")

if begin.lower() != "yes":
    quit()

print("\nOkay, lets begin.")
score = 0

# Questions
answer = input("\nThe driver of any motor vehicle, when traveling down a hill, must not coast with the gears or "
               "transmission of the vehicle in neutral. True or False? ")
if answer.lower() == "true":
    print('\nCorrect!')
    score += 1
else:
    print("\nIncorrect! Answer: True")

answer = input("\nA short road on which vehicles join or leave a main road is called? ")
if answer.lower() == "Slip Road":
    print('\nCorrect!')
    score += 1
else:
    print("\nIncorrect! Answer: Slip Road")

answer = input("\nWhat is the first rule of the road? ")
if answer.lower() == "Keep well to the left unless you are about to overtake or turn right":
    print('\nCorrect!')
    score += 1
else:
    print("\nIncorrect! Answer: Keep well to the left unless you are about to overtake or turn right")

answer = input("\nWhom do you consider most, of all road users? ")
if answer.lower() == "All road users but most of all pedestrians":
    print('\nCorrect!')
    score += 1
else:
    print("\nIncorrect! Answer: All road users but most of all pedestrians")

answer = input("\nWhen the road is divided into three lanes and there is no other marking or direction, what is the "
               "center lane used for? ")
if answer.lower() == "For overtaking only":
    print('\nCorrect!')
    score += 1
else:
    print("\nIncorrect! Answer: For overtaking only")

answer = input("\nHow close to a fire hydrant are you allowed to park? ")
if answer.lower() == "9m (30 feet)":
    print('\nCorrect!')
    score += 1
else:
    print("\nIncorrect! Answer: 9m (30 feet)")

answer = input("\nWhat is a cul-de-sac? ")
if answer.lower() == "It is a dead end road":
    print('\nCorrect!')
    score += 1
else:
    print("\nIncorrect! Answer: It is a dead end road")

answer = input("\nAfter overtaking a vehicle what should you do before rejoining the line? ")
if answer.lower() == "Check your rear view mirror":
    print('\nCorrect!')
    score += 1
else:
    print("\nIncorrect! Answer: Check your rear view mirror")

answer = input("\nIf two vehicles of different sizes meet on a hill, which one had the right of way? ")
if answer.lower() == "The larger one":
    print('\nCorrect!')
    score += 1
else:
    print("\nIncorrect! Answer: The larger one")

answer = input("\nGive two causes of skidding: ")
if answer.lower() == "Faulty driving, smooth tyres":
    print('\nCorrect!')
    score += 1
else:
    print("\nIncorrect! Answer: Faulty driving, smooth tyres")

answer = input("\nIf you wish to turn with when traveling on a one way street, what should you do? ")
if answer.lower() == "Keep to the right of the road":
    print('\nCorrect!')
    score += 1
else:
    print("\nIncorrect! Answer: Keep to the right of the road")

answer = input("\nWhat is a soft shoulder? ")
if answer.lower() == "The unpaved side of the road which is not intended for vehicular traffic":
    print('\nCorrect!')
    score += 1
else:
    print("\nIncorrect! Answer: The unpaved side of the road which is not intended for vehicular traffic")

answer = input("\nHow far should you travel behind an emergency vehicle? ")
if answer.lower() == "Approximately 150m (500 feet)":
    print('\nCorrect!')
    score += 1
else:
    print("\nIncorrect! Answer: Approximately 150m (500 feet)")

answer = input("\nWho has the right of way on a hill? ")
if answer.lower() == "The vehicle coming down, but a heavier vehicle has the right of way up or down":
    print('\nCorrect!')
    score += 1
else:
    print("\nIncorrect! Answer: The vehicle coming down, but a heavier vehicle has the right of way up or down")

answer = input("\nWho has the right of way at a crossing which is not controlled by a police, traffic lights or signs? ")
if answer.lower() == "No one":
    print('\nCorrect!')
    score += 1
else:
    print("\nIncorrect! Answer: No one")

answer = input("\nWhen should a driver make use of the right of way? ")
if answer.lower() == "When it is safe to do so":
    print('\nCorrect!')
    score += 1
else:
    print("\nIncorrect! Answer: When it is safe to do so")

answer = input("\nShould a driver yield the right of way if a pedestrian enters the crossing? ")
if answer.lower() == "Yes":
    print('\nCorrect!')
    score += 1
else:
    print("\nIncorrect! Answer: Yes")

answer = input("\nWhat is meant by yield right of way? ")
if answer.lower() == "To give way":
    print('\nCorrect!')
    score += 1
else:
    print("\nIncorrect! Answer: To give way")

answer = input("\nWhen may you use a slip road at the traffic light? ")
if answer.lower() == "On any light":
    print('\nCorrect!')
    score += 1
else:
    print("\nIncorrect! Answer: On any light")

answer = input("\nIf you are driving along and your rear wheels skid, what should you do? ")
if answer.lower() == "Steer in the direction of the skid":
    print('\nCorrect!')
    score += 1
else:
    print("\nIncorrect! Answer: Steer in the direction of the skid")

# Calculations for the score
print("\nYou got " + str(score) + " question(s) correct!")
print("\nYou got " + str((score / 20) * 100) + "%.")
if answer < str(15):
    print("\nYou failed!")
else:
    print("\nYou passed!")
