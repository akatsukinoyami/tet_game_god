from pyrogram 			import filters

from classes.client	import app
from funcs.coin 		import coin

@app.on_message(filters.command(["coin", "coin@teto_randombot"]))
@app.decorator
def coin(app, msg):
	username = app.name(msg.from_user)

	answer = coin(username)
	
	app.send_msg(msg, answer)