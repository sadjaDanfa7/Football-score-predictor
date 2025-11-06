import random # allow random choices

print("welcome to football fan!")
name = input("whats your name ?")
team = input("whats your favourite football team ?")

print ("hello,", name, "you support", team)
#liverpool, aresnal, manchester city, manchetser united
results = ["win", "lose", "draw"] # Define the results variable
prediction = random.choices(results)

print("prediction for", team, "next match", prediction)

