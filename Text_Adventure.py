code_unlocked = 0
alligator_out = 0
robot_dead = 0
cellar_unlocked = 0
rope_tied = 0
sled_used = 0

code_taken = 0
banana_taken = 0
key_taken = 0
rope_taken = 0
sled_taken = 0

code_explore = 0
banana_explore = 0
sled_explore = 0


commands = ["north", "south", "east", "west", "up", "down", "grab", "use", "explore", "inventory", "commands"]
inventory = []


def user_command():
	global this_room
	this_command = input()
	if this_command == "north":
		north()
	elif this_command == "south":
		south()
	elif this_command == "east":
		east()
	elif this_command == "west":
		west()
	elif this_command == "up":
		up()
	elif this_command == "down":
		down()
	elif this_command == "grab":
		grab()
	elif this_command == "use":
		use()
	elif this_command == "explore":
		explore()
	elif this_command == "inventory":
		print_inventory()
		user_command()
	elif this_command == "commands":
		print_commands()
		user_command()
	elif this_command == "see you later alligator" and this_room == "room004":
		global alligator_out
		if alligator_out == 0:
			print("The alligator seems to be hypnotized by this rhyme and walks out of the room. Weird.")
		alligator_out = 1
		user_command()	
	else:
		print("What in the world do you mean?!?! (It's a rhetorical question - don't answer)")
		user_command()



def north():
	global this_room
	if this_room == "room002" and code_unlocked == 1:
		room003()
	elif this_room == "room004" and alligator_out == 1:
		room006()
	elif this_room == "room005" and robot_dead == 1:
		corridor001()
	elif this_room == "corridor001":
		room008()
	elif this_room == "room009":
		room010()
	elif this_room == "room010" and sled_used == 1:
		destination()
	elif this_room == "room010" and sled_used == 0:
		die()
	else:
		print("Path blocked")
		user_command()

def south():
	global this_room
	if this_room == "room008":
		corridor001()
	elif this_room == "corridor001":
		room005()
	elif this_room == "room006":
		room004()
	elif this_room == "room003":
		room002()
	else:
		print("Path blocked")
		user_command()

def east():
	global this_room
	if this_room == "start":
		room002()
	elif this_room == "room001":
		start()
	elif this_room == "room003":
		room005()
	elif this_room == "room004":
		room003()
	elif this_room == "corridor001" and cellar_unlocked == 1:
		room007()
	else:
		print("Path blocked")
		user_command()

def west():
	global this_room
	if this_room == "start":
		room001()
	elif this_room == "room002":
		start()
	elif this_room == "room003":
		room004()
	elif this_room == "room005":
		room003()
	elif this_room == "room007":
		corridor001()
	else:
		print("Path blocked")
		user_command()

def up():
	global this_room
	if this_room == "room009":
		room008()
	else:
		print("Path blocked")
		user_command()
		
def down():
	global this_room
	if this_room == "room008" and rope_tied == 1:
		room009()
	else:
		print("Path blocked")
		user_command()



def print_commands():
	global this_room
	print("Commands:",commands)

def print_inventory():
	global this_room
	print("Inventory:",inventory)



def grab():
	global this_room
	global inventory
	global code_taken
	global banana_taken
	global key_taken
	global rope_taken
	global sled_taken
	global code_explore , banana_explore , sled_explore
	if this_room == "room001" and code_taken == 0 and code_explore == 1:
		inventory.append("Code: 3xf2")
		print("Inventory:",inventory)
		code_taken = 1
	elif this_room == "room002" and banana_taken == 0 and banana_explore == 1:
		inventory.append("Banana Peel")
		print("Inventory:",inventory)
		banana_taken = 1
	elif this_room == "room006" and key_taken == 0:
		inventory.append("Rusty key")
		print("Inventory:",inventory)
		key_taken = 1
	elif this_room == "corridor001" and rope_taken == 0:
		inventory.append("Rope")
		print("Inventory:",inventory)
		rope_taken = 1
	elif this_room == "room007" and sled_taken == 0 and sled_explore == 1:
		inventory.append("Sled")
		print("Inventory:",inventory)
		sled_taken = 1
	elif this_room == "room003":
		print("The note is old; it starts crumbling in your hands. You will have to remember these words.")
	else:
		print("There is nothing for you to take from here, but you can try to explore.")
	user_command()
		
		
def use():
	global this_room
	global code_unlocked
	global robot_dead
	global cellar_unlocked
	global rope_tied
	global sled_used
	if this_room == "room002" and "Code: 3xf2" in inventory:
		print("You use your code which turns out successful. The hatch opens.")
		inventory.remove("Code: 3xf2")
		code_unlocked = 1
	elif this_room == "room005" and "Banana Peel" in inventory:
		print("You throw the banana peel in the robot's path due to which it slips and it's wiring disconnects. Your path is clear!")
		inventory.remove("Banana Peel")
		robot_dead = 1
	elif this_room == "corridor001" and "Rusty key" in inventory:
		print("You use your rusty key and the door on the right opens with a creak")
		inventory.remove("Rusty key")
		cellar_unlocked = 1
	elif this_room == "room008" and "Rope" in inventory:
		print("You tie your rope to a rock. Now is your chance of going into the depths of the abyss.")
		inventory.remove("Rope")
		rope_tied = 1
	elif this_room == "room010" and "Sled" in inventory:
		print("You jump into your sled ready to slide .... are you going north or not???")
		inventory.remove("Sled")
		sled_used = 1
	else:
		print("There is nothing you have which you can use here")
	user_command()
		
		
def explore():
	global this_room
	global code_taken
	global banana_taken
	global sled_taken
	global code_explore , banana_explore , sled_explore
	if this_room == "room001":
		if code_taken == 0:
			code_explore = 1
			print("You open the drawer and spot a paper with the words 'Code 3xf2' written on it.")
		else:
			print("Nothing here.")
	elif this_room == "room002":
		if banana_taken == 0:
			banana_explore = 1
			print("You spot a banana peel; the only thing that isn't wilting. Pretty useless.")
		else:
			print("Nothing here.")
	elif this_room == "room003":
		print("The typewriter has a paper in it. The words 'See you later alligator' are written on it. Some foolish rhyme most possibly.")
	elif this_room == "room007":
		if sled_taken == 0:
			sled_explore = 1
			print("You search the barrels for something useful and find a sled. Do you want to carry such a heavy thing?")
		else:
			print("Nothing here.")
	else:
		print("This place is pretty empty. Better try somewhere else.")
	user_command()



def die():
	print("You run towards the light with all the strength you had. But all was to waste.")
	print("The giant had a delicious supper that night.")
	
def destination():
	print("At last, you skid north leaving the giant far behind")
	print("You reach the light and jump into it. It transports you back to your cosy home.")
	print("Thanks for playing Text Adventure - Metamorphosis")


def start():
	global this_room
	this_room = "start"
	print("The room is dark and empty. Pitch black. Their are only 2 exits on your right and left.")
	directions = ["east", "west"]
	print (directions)
	user_command()
		
def room001():
	global this_room
	this_room = "room001"
	print("You enter a cave. The thing that really catches your attention is the drawer in the corner.")
	directions = ["east"]
	print (directions)
	user_command()
	
def room002():
	global this_room
	this_room = "room002"
	print("You are in a metalled room; the door to the place ahead has a large code lock. Some garbage is thrown in a corner")
	directions = ["north", "west"]
	print (directions)
	user_command()
	
def room003():
	global this_room
	this_room = "room003"
	print("The smell of burnt paper wafts to your nose. You find yourself in a study. A typewriter is on a table.")
	directions = ["south", "east", "west"]
	print (directions)
	user_command()
	
def room004():
	global this_room
	this_room = "room004"
	print("OK. Weird. You are now in a rainforest.(The rooms seem too be undergoing metamorphosis)")
	if alligator_out == 0:
		print("You are face-to-face with an alligator.")
		print("The alligator is blocking the path to an archway. I guess you will have to talk your way in.")
	directions = ["north", "east"]
	print (directions)
	user_command()
	
def room005():
	global this_room
	this_room = "room005"
	print("You are in a completely white-washed domed room. In front of you is a swirling magical portal.")
	if robot_dead == 0:
		print("But right in front of the portal, an armed robot is marching continuously from side to side; obviously guarding it.")
	directions = ["north", "west"]
	print (directions)
	user_command()
	
def room006():
	global this_room
	global key_taken
	this_room = "room006"
	print("Wow. From a rainforest into an attic. Can things get as abnormal as this?")
	if key_taken == 0:
		print("Anyway, there is a rusty key right in front of your eyes if you want it.")
	directions = ["south"]
	print (directions)
	user_command()
	
def corridor001():
	global this_room
	global rope_taken
	this_room = "corridor001"
	print("The world is now abstract. A wiggly and wobbly and colour-splashed corridor is where you are standing.")
	if rope_taken == 0:
		print("In the middle of the corridor a coil of rope is thrown.")
	print("An exit is barely visible in the colours on your right, and one straight ahead.")
	directions = ["north", "east"]
	print (directions)
	user_command()

def room007():
	global this_room
	this_room = "room007"
	print("You are now in a dusty cellar full of barrels.")
	directions = ["west"]
	print (directions)
	user_command()
	
def room008():
	global this_room
	this_room = "room008"
	print("Wheeps! Careful please. Nobody likes to fall into a seemingly endless abyss, do they? Well, I guess you can't go anywhere now.")
	directions = ["south", "down"]
	print (directions)
	user_command()

def room009():
	global this_room
	this_room = "room009"
	print("Ok Great. From abyss to gigantic monster's den. At least it's still asleep - hopefully.")
	print("So, are you going to risk getting eaten up by a monster or not?")
	directions = ["north", "up"]
	print (directions)
	user_command()
	
def room010():
	global this_room
	this_room = "room010"
	print("You move forward with the hopeless hope of not waking the beast. You are now on a snowy slope and you see a light ahead.")
	print("....Oh no! the giant has woken up, and it's hungry. There is no way you can run faster than it, and your path back to the safety of the abyss is blocked.")
	print("What are you going to do?")
	directions = ["north"]
	print (directions)
	user_command()


print("")
print("Welcome to the Text Adventure -- Metamorphosis")
print("WARNING! Do not give any commands in caps-lock, commas etc.")
print("")
start()








#FIXING
	#DON'T ALLOW GRAB UNTIL EXPLORE DONE

