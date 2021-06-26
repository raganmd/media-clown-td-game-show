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

def toggle_room_accident(args):
	ipar.Settings.Roomaccident = args[0]

def toggle_prerecord(args):
	ipar.Settings.Prerecord = args[0]	

def set_video_file(args):
	cue_folder = ipar.Settings.Cuefolder.eval()
	new_path = f'{cue_folder}/{args[0]}'
	ipar.Settings.Prerecordfile = new_path
	pass

def toggle_override_output(args):
	ipar.Settings.Toggleoutputoverride = args[0]

def set_override_file(args):
	path = f"{ipar.Settings.Cuefolder}/{args[0]}"
	ipar.Settings.Overridefile = path

def distort(args):
	ipar.Settings.Lensdistortion = args[0]

def set_background(args):
	ipar.Settings.Background = args[0]