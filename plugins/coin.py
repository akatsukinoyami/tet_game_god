from pyrogram 			import filters
from classes.client	import app
from random					import randint

@app.on_message(filters.command(["coin", "coin@teto_randombot"]))
@app.decorator
def coin(app, msg):

	username = app.name(msg.from_user)

	num = randint(1, 2)

	coin= " **орёл**" if num == 1 else "а **решка**"

	txt = f"{username} подкинул(а) монетку и выпал{coin}."

	app.send_msg(msg, txt)