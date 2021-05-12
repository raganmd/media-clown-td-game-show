class Par_exec:
	def __init__(self, my_op, actions):
		self.My_op = my_op
		self._actions = actions
		print(f"Par Exec MOD init from {my_op}")
		
	def get_func(self, target_func):
		try:
			func = getattr(self._actions, target_func)
			func()
		except:
			pass
		
		return
	
	def Run_pulse_par(self, par):
		pass
	
	def Run_par_change(self, par):
		pass