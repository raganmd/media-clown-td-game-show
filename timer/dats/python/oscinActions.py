def run_me(args):
	print(args)
	return

def timer_start(args):
	op.output.Timer_start()

def timer_init(args):
	op.output.Timer_init()

def update_timer_speed(args):
	op.output.Update_timer_speed(args[0])

def update_timer_length(args):
	op.output.Update_timer_length(args[0])

def toggle_play(args):
	op.output.Toggle_play(args[0])
	
def count_down(args):
	op.output.Count_direction(args[0])
	
def count_up(args):
	op.output.Count_direction(args[0])
