class Output:
	def __init__(self, my_op):
		self.My_op = my_op
		print(f"Output init from {my_op}")
	
	def Timer_start(self):
		ipar.Settings.Timerstart.pulse()

	def Timer_init(self):
		ipar.Settings.Timerinit.pulse()

	def Update_timer_speed(self, val):
		ipar.Settings.Timerspeed = val

	def Toggle_play(self, state):
		ipar.Settings.Timerplay = state
		
	def Update_timer_length(self, val):
		ipar.Settings.Timerlength = val
		ipar.Settings.Timerstart.pulse()
		pass
	
	def Count_direction(self, direction):
		ipar.Settings.Countdirection = direction[0]