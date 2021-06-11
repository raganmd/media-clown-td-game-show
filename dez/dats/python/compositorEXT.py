class controls:

	def __init__(self, myOp):
		self.MyOp = myOp
		
		print(f'controls init from {myOp}')
	
	def Toggle_glitch(self, value):
		print(type(value))
		if value == '1': 
			ipar.Settings.Glitchfx = value
		
		else:
			ipar.Settings.Toggleglitch = value			
			delayScript = "setattr(args[0], args[1], args[2])"
			delayTime = op('filter1').par.width.eval() * me.time.rate
			run(delayScript, 
				ipar.Settings,
				"Glitchfx",
				int(value), 
				delayFrames = delayTime)
			
		ipar.Settings.Toggleglitch = value