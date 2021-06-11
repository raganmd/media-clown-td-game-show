def run_me(args):
	print(args)
	return

def toggle_logo(args):
	ipar.Settings.Logo = args[0]

def set_audio(args):
	ipar.Settings.Audiolevel = args[0]

def toggle_glitch(args):
	parent(2).Toggle_glitch(args[0])

def set_glitch(args):
	ipar.Settings.Glitch = args[0]