class Output:
	def __init__(self, my_op):
		self.My_op = my_op
		print(f"Output init from {my_op}")
	
	def Start_timer(self):
		ipar.Settings.Timerstart.pulse()

	def Update_timer_speed(self, val):
		ipar.Settings.Timerspeed = val

	def Toggle_play(self, state):
		ipar.Settings.Timerplay = state