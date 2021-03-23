from pyrogram 			import filters
from classes.client	import app
from random					import randint

def int_rand(app, msg, n1, n2):
	app.send_msg(msg, f"Твоё случайное число от {n1} до {n2}:\n{randint(int(n1), int(n2))}")

@app.on_message(filters.command([	"r", 			"r@teto_randombot",
																	"rand", 	"rand@teto_randombot",
																	"random", "random@teto_randombot"]))
@app.decorator
def rand(app, msg):
	txt = msg.text.split()

	if 		len(msg.command) >= 3:	int_rand(app, msg, txt[1], txt[2])
	elif	len(msg.command) == 2:	int_rand(app, msg, 1, txt[1])
	else:													app.send_msg(msg, "Может добавишь число или два?")

