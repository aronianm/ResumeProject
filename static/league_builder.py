import csv
import random

sharks = []
raptors = []
dragons = []
soccer_experience = []
non_experience = []

#Reads CSV file and distributes players into two lists, soccer experience and no soccer_expeirence

def experience(soccer_experience,non_experience):
	with open('soccer_players.csv', 'r') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			if row['Soccer Experience'] == 'YES':
				soccer_experience.append(row['Name'] + ", " + " " + " " +row['Soccer Experience'] + ", " + " " + " " + " " + " " +  row['Guardian Name(s)'])
			else:
				non_experience.append(row['Name'] + ", " + " " + " " +row['Soccer Experience'] + ", " + " " + " " + " " + " " +  row['Guardian Name(s)'])
		return soccer_experience, non_experience
		
soccer_pros,soccer_begginners = experience(soccer_experience,non_experience)

#distributes players that have soccer experience evenly into dragons,raptors, and sharks

def experience_teams(soccer_pros,dragons,raptors,sharks):
  #Individual While loops for each team
  while len(sharks) < 3:
  	player = random.choice(soccer_pros)
  	if player in sharks:
  		continue
  	else:	
  		sharks.append(player)
  		continue
  

  while len(raptors) < 3:
  	player = random.choice(soccer_pros)
  	if player in sharks or player in raptors:
  		continue
  	else:
  		raptors.append(player)
  

  while len(dragons) < 3:
  	player = random.choice(soccer_pros)
  	if player in sharks or player in raptors or player in dragons:
  		continue
  	else:
  		dragons.append(player)
  
  return sharks,dragons,raptors

sharks,dragons,raptors = experience_teams(soccer_pros,dragons,raptors,sharks)

#distributes players that have no soccer experience evenly into dragons,raptors, and sharks
def non_experience_teams(soccer_begginners,dragons,raptors,sharks):

	while len(sharks) < 6:
	  	player = random.choice(soccer_begginners)
	  	if player in sharks:
	  		continue
	  	else:	
	  		sharks.append(player)
	  		continue
	  

	while len(raptors) < 6:
	  	player = random.choice(soccer_begginners)
	  	if player in sharks or player in raptors:
	  		continue
	  	else:
	  		raptors.append(player)
	  

	while len(dragons) < 6:
	  	player = random.choice(soccer_begginners)
	  	if player in sharks or player in raptors or player in dragons:
	  		continue
	  	else:
	  		dragons.append(player)
	  
	return sharks,dragons,raptors

shark,dragons,raptors = non_experience_teams(soccer_begginners,dragons,raptors,sharks)

#welcome_message creates a .txt file for each individual player.
#Includes(Team Roster,Childs name, Guardians name, and a welcome message)

def welcome_message(shark,dragons,raptors,soccer_experience,non_experience):
  with open('soccer_players.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
      file = open('{}.txt'.format(row['Name']), 'w')
      if (row['Name'] + ", " + " " + " " + row['Soccer Experience'] + ", " + " " + " " + " " + " " + row['Guardian Name(s)']) in sharks:
        file.write("Welcome {}".format(row['Guardian Name(s)']))
        file.write("\n" * 3)
        file.write("Your child, {} is on Team Sharks!".format(row['Name']) )
        file.write("\n" *2 )
        file.write("We are so happy to have your child be part of this Soccer League, and we hope you have a lot of fun this year!")
        file.write("\n" * 2)
        file.write("Your Team Roster is:")
        file.write("\n" *2)
        file.write("Name,    Soccer Experience,      Guardian Names(s)")
        file.write("\n" *2)
        for line in sharks:
          file.write(line)
          file.write("\n")
      if (row['Name'] + ", " + " " + " " + row['Soccer Experience'] + ", " + " " + " " + " " + " " + row['Guardian Name(s)']) in dragons:
        file.write("Welcome {}".format(row['Guardian Name(s)']))
        file.write("\n" * 3)
        file.write("Your child, {} is on Team Dragons!".format(row['Name']) )
        file.write("\n" *2 )
        file.write("We are so happy to have your child be part of this Soccer League, and we hope you have a lot of fun this year!")
        file.write("\n" * 2)
        file.write("Your Team Roster is:")
        file.write("\n" *2)
        file.write("Name,    Soccer Experience,      Guardian Names(s)")
        file.write("\n" *2)
        for line in dragons:
          file.write(line)
          file.write("\n")
      if (row['Name'] + ", " + " " + " " + row['Soccer Experience'] + ", " + " " + " " + " " + " " + row['Guardian Name(s)']) in raptors:
        file.write("Welcome {}".format(row['Guardian Name(s)']))
        file.write("\n" * 3)
        file.write("Your child, {} is on Team Raptors!".format(row['Name']) )
        file.write("\n" *2 )
        file.write("We are so happy to have your child be part of this Soccer League, and we hope you have a lot of fun this year!")
        file.write("\n" * 2)
        file.write("Your Team Roster is:")
        file.write("\n" * 2)
        file.write("Name,    Soccer Experience,      Guardian Names(s)")
        file.write("\n" * 2)
        for line in raptors:
          file.write(line)
          file.write("\n")
      file.close()

#team_roster, creates a .txt file that lists: team rosters, and a small welcome message

def team_roster(shark,dragons,raptors,soccer_experience,non_experience):
  file = open('teams.txt', 'w')
  file.write("\n")
  file.write("Welcome to The Soccer League")
  file.write("\n" *3)
  file.write("Here are The Official Rosters for 'The Raptors', 'The Sharks', and 'The Dragons'")
  file.write("\n"*2)
  file.write("Team Raptors")
  file.write("\n")
  file.write("Name,         Experience,             Guardians(s)")
  file.write("\n" *2)
  for line in raptors:
        file.write(line)
        file.write("\n")
  file.write("\n"*3)
  file.write("Team Sharks")
  file.write("\n")
  file.write("Name,         Experience,             Guardians(s)")
  file.write("\n"*2)
  for line in sharks:
    file.write(line)
    file.write("\n")
  file.write("\n"*3)
  file.write("Team Dragons")
  file.write("\n")
  file.write("Name,         Experience,             Guardians(s)")
  file.write("\n" *2)
  for line in dragons:
    file.write(line)
    file.write("\n")
  
  file.close()

if __name__ == "__main__":
  welcome_message(shark,dragons,raptors,soccer_experience,non_experience)
  team_roster(shark,dragons,raptors,soccer_experience,non_experience)
