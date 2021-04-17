from pyrogram 			import filters

from classes.client	import app
from funcs.dice 		import dice

@app.on_message(filters.regex(r'\/\d*d\d'))
@app.decorator
def dice(app, msg):
	txt = msg.matches[0].group(0)
	username = app.name(msg.from_user)

	answer = coin(txt, username)

	app.send_msg(msg, answer)
	