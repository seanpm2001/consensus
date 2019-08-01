import jinja2
import os
from jinja2 import Template
import io
latex_jinja_env = jinja2.Environment(
	block_start_string = '\BLOCK{',
	block_end_string = '}',
	variable_start_string = '\VAR{',
	variable_end_string = '}',
	comment_start_string = '\#{',
	comment_end_string = '}',
	line_statement_prefix = '%%',
	line_comment_prefix = '%#',
	trim_blocks = True,
	lstrip_blocks = True,
	autoescape = False,
	loader = jinja2.FileSystemLoader(os.path.abspath('templates'))
)

movesthing = []

def get_data():
	with io.open ('Consensus Book.md', encoding='utf-8') as f:
		l=0
		workingdoc = []
		global movestext
		for line in f:
			l += 1
			workingdoc.append(line)
			if line.startswith('# The Moves'):
				start = workingdoc[l-1]
				startnum = l-1
			if line.startswith('# The Master of Ceremonies'):
				end = workingdoc[l-1]
				endnum = l
				break


	movestext = workingdoc[startnum:endnum]
	f.closed
moves = {}	
class Move:

	def __init__(self):
		self.name = ''
		self.fulltext = ''
		self.is_basic = False
		self.is_advanced = False
		self.trigger = ''
		self.before = ''
		self.after = ''
		self.list = []
		self.after_list = ''
		self.description = ''


def movesdata():
	in_basic = False
	in_advanced = False
	in_move = False
	in_move_list = False
	moveslist = []
	move_number = -1
	move_list_number = 0
	for line in movestext:
		if line.startswith('When') or line.startswith('At the **end of session**'):
			move_number += 1
			moveslist.append([])
			in_move = True

		if line == '\n':
			in_move = False
		
		if line.startswith('- '):
			in_move = True

		if in_move:
			moveslist[move_number].append(line)

	for move in moveslist:
		num_of_moves += 1
			movedict['name'] = move[0].split('**')[1]
			movedict['trigger'] = move[0].split('**')[1]
			movedict['before'] = move[0].split('**')[0]
			movedict['after'] = move[0].split('**')[2]
		if len(move) == 2:
			movedict = movesthing[num_of_moves]
			movedict['name'] = move[0].split('**')[1]
			list = move[0].split('**')
			movedict['before'] = list[0]
			movedict['after'] = list[2]
			trigger =list[1]
			movedict['trigger'] = trigger			
			movedict['movestring'] = movedict['before'] + movedict['trigger'] + movedict['after'] 
		else:
			movedict = movesthing[num_of_moves]
			movedict['name'] = move[0].split('**')[1]
			movedict['list'] = move[1:]
				movedict['afterlist'] = movedict['list'][-1]
				movedict['list'] = movedict['list'][:-1]
			list = move[0].split('**')
			movedict['movestring'] = movedict['before'] + movedict['trigger'] + movedict['after'] + str(movedict['list']) + movedict['afterlist']
	get_data()
		f.write(output)	
		f.write(output)	
		
		