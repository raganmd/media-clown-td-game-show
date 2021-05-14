import oscinActions

class Com:
	def __init__(self, my_op):
		self.My_op = my_op
		print(f"Com init from {my_op}")
	
	def Parse_osc(self, **kwargs):
		args = kwargs.get('args')
		address = kwargs.get('address')
		oscCommand = address.split('/')[-1]

		try:
			func = getattr(oscinActions, oscCommand)
			func(args)
		except Exception as e:
			print("This address is not yet mapped")
			print(e)
		pass