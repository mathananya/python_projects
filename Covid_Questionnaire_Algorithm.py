
def input_y_n(ques):
    answer = input(ques)
    while answer not in['y','n']:
        print("Sorry, please enter valid answer.")
        answer = input(ques)
    return answer
    
def input_int(ques):
    answer = input(ques)
    while not answer.isdigit():
        print("Sorry, please enter valid answer.")
        answer = input(ques)
    return int(answer)
    

print("Please give your PERSONAL DETAILS")

nam = input("\nPlease enter your name: ")
age = input_int("Please enter your age: ")
gender = input("Enter your gender [m/f]: ")

if age > 65:
    factor1 = 1.5        # risk factor based on age
elif age > 50:
    factor1 = 1.2
elif age < 10:
    factor1 = 1.25
else:
    factor1 = 1

if gender == "m":
    factor2 = 1.05       # risk factor based on gender
else:
    factor2 = 1


print("\nPlease give your RECENT MEDICAL HISTORY")
dia = input_y_n("Do you suffer from diabetes [y/n] ")
obe = input_y_n("Do you suffer from obesity [y/n] ")
cancer = input_y_n("Do you have cancer [y/n] ")
contact = input_y_n("Have you been in contact with a COVID-19 patient [y/n] ")

factor3 = 1             # risk factor based on medical history

if dia == "y":
    factor3 = factor3*1.2

if obe == "y":
    factor3 = factor3*1.1

if cancer == "y":
    factor3 = factor3*1.4

if contact == "y":
    factor3 = factor3*1.5


factor = factor1*factor2*factor3      # overall risk factor

score = 0         # score based on current symptoms

print("\nPlease give info on your SYMPTOMS")

acute = input_y_n("Do you have temperature over 38*C? [y/n] ")
if acute == "y":
    score += 10
acute = input_y_n("Do you suffer from shortness of breath? [y/n] ")
if acute == "y":
    score += 10
acute = input_y_n("Do you suffer from congestion/pressure in your chest? [y/n] ")
if acute == "y":
    score += 10
acute = input_y_n("Do you suffer from confusion and loss of appetite? [y/n] ")
if acute == "y":
    score += 10


mild = input_y_n("Do you suffer from dry cough [y/n] ")
if mild == "y":
    score += 5
mild = input_y_n("Do you suffer from loss of taste & smell [y/n] ")
if mild == "y":
    score += 5
mild = input_y_n("Do you suffer from muscle-joint pain [y/n] ")
if mild == "y":
    score += 5
mild = input_y_n("Do you suffer from fatigue [y/n] ")
if mild == "y":
    score += 3
mild = input_y_n("Do you suffer from chills and dizziness [y/n] ")
if mild == "y":
    score += 3
mild = input_y_n("Do you suffer from nasal congestion and headache [y/n] ")
if mild == "y":
    score += 3
mild = input_y_n("Do you suffer from conjunctivitis/skin rash [y/n] ")
if mild == "y":
    score += 3

score = score*factor

print("")

if score > 35:
    print("High Probability diagnosis for patient "+nam)
elif score > 25:
    print("Medium Probability diagnosis for patient "+nam)
else:
    print("Low Probability diagnosis for patient "+nam)




