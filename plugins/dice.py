from pyrogram 			import filters
from classes.client	import app
from random					import randint

def dice(app, msg, n):
	username = app.name(msg.from_user)
	app.send_msg(msg, f"{username} кинул(а) кубик на {n}.\nВыпало **{randint(1, int(n))}**.")

@app.on_message(filters.command(["d10", "d10@teto_randombot"]))
@app.decorator
def d10(app, msg):
	dice(app, msg, 10)

@app.on_message(filters.command(["d6", "d6@teto_randombot"]))
@app.decorator
def d6(app, msg):
	dice (app, msg, 6)