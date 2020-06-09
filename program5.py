r1 = int(input("Enter run scored by 1st player on 60 ball : "))
r2 = int(input("Enter run scored by 2nd player on 60 ball : "))
r3 = int(input("Enter run scored by 3rd player on 60 ball : "))
player1Strike_rate = (r1 / 60) * 100
player2Strike_rate = (r2 / 60) * 100
player3Strike_rate = (r3 / 60) * 100
print("player1Strike_rate :",player1Strike_rate)
print("player2Strike_rate :",player2Strike_rate)
print("player3Strike_rate :",player3Strike_rate)
print("Runs scored by player 1 if he plays 60 more balls : ",r1 * 2)
print("Runs scored by player 2 if he plays 60 more balls : ",r2 * 2)
print("Runs scored by player 3 if he plays 60 more balls : ",r3 * 2)
print("Maximum no. of sixes player 1 could hit : ",r1 // 6)
print("Maximum no. of sixes player 2 could hit : ",r2 // 6)
print("Maximum no. of sixes player 13 could hit : ",r3 // 6)