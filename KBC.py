questions = [
['What is the fullform of GST ?','Great service tax','Good service tax','Good sell trade','Gar sambhal tera',2],
['The largest petrol is found in ?','Iran','Russia','Saudi Arabia','Korea',3],
['Port diamond is located in ?','Brazil','Indonesia','Bangladesh','Pakistan',2],
['Where is INDIA located ?','Asia','Australia','China','Africa',1],
['Who is Dharmesh ?','Influencer','Tiktoker','Youtuber','Dancer',4],
["Which planet is known as the Red Planet?","Jupiter","Venus","Mars","Saturn",3],
[ "What is the capital of India?","Delhi", "Mumbai", "Kolkata", "Chennai",1],
['What is the fullform of GST','Great service tax','Good service tax','Good sell trade','Gar sambhal tera',2],
['What is the fullform of GST','Great service tax','Good service tax','Good sell trade','Gar sambhal tera',2],
['What is the fullform of GST','Great service tax','Good service tax','Good sell trade','Gar sambhal tera',2],
['What is the fullform of GST','Great service tax','Good service tax','Good sell trade','Gar sambhal tera',2],
['Who is Dharmesh ?','Influencer','Tiktoker','Youtuber','Dancer',4],
['Who is Dharmesh ?','Influencer','Tiktoker','Youtuber','Dancer',4],
['Who is Dharmesh ?','Influencer','Tiktoker','Youtuber','Dancer',4],
['Who is Dharmesh ?','Influencer','Tiktoker','Youtuber','Dancer',4],
['Who is Dharmesh ?','Influencer','Tiktoker','Youtuber','Dancer',4],
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000 ,1250000,2500000,5000000,10000000,70000000]
money = 0
for i in range(0, len(questions)):
  question = questions[i]
  print(f"\n\nQuestion for Rs.{levels[i]}")
  print(question[0])
  print(f"1. {question[1]},\n2. {question[2]},\n3. {question[3]},\n4. {question[4]} ")

  reply = int(input("Enter your Answer(1-4) or Press 0 to Quit:\n" ))
  if reply == 0 :
    money = levels[i-1]
    break
  if reply == question[-1]:
    print(f"Correct answer, You have won Rs.{levels[i]}")
    if(i == 4):
      money = 10000
      print("\n------Level 1 completed------")
      print(f"If you loose before completing Level 2 you will only get Rs.{money}")
    elif(i == 9):
      money = 320000
      print("------Level 2 completed------")
      print(f"If you loose before completing Level 3 you will only get Rs.{money}")
    elif(i == 14):
      money = 10000000
      print("------Level 3 completed------")
      print(f"If you loose before completing Level 4 you will only get Rs.{money}")
    elif(i == 15):
      money = 70000000
  else :
      print("Wrong Answer!")
      print(f'The correct answer is {question[question[-1]]}')
      break
print(f'\nYou have won Rs.{money} today in KBC')