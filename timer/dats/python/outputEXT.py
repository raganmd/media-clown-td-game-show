class Output:
	def __init__(self, my_op):
		self.My_op = my_op
		print(f"Output init from {my_op}")

	def Get_timer_seconds(self):
		return ipar.Settings.Timerlength.eval()

	def Get_current_timer_count(self):
		timecode = self.My_op.op('info1')[0, 2].val[:-3]
		timecode_ints = [int(item) for item in timecode.split(':')]
		total_seconds = (timecode_ints[0] * 3600) + (timecode_ints[1] * 60) + timecode_ints[2]
		return total_seconds

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