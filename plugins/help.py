from pyrogram 			import filters

from classes.client	import app
from funcs.help	 		import help

@app.on_message(filters.command(["help", "help@teto_randombot"]))
@app.decorator
def coin(app, msg):
	answer = help()
	
	app.send_msg(msg, answer)