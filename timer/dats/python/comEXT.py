import oscinActions

class Com:
	def __init__(self, my_op):
		self.My_op = my_op
		print(f"Com init from {my_op}")
	
	def Parse_osc(self, **kwargs):
		args = kwargs.get('args')
		address = kwargs.get('address')[1:]
		try:
			func = getattr(oscinActions, address)
			func(args)
		except:
			pass
		pass