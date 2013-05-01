


def generate_text_grid(xmax, ymax, xstep=1, ystep=1):

	filename = 'result_' + str(xmax) + 'x' + str(ymax) + '.txt'
	f = open(filename, 'w+')

	grid = ''
	for i in xrange(0, xmax, xstep):
		for j in xrange(0, ymax, ystep):
			grid += str(i) + ' ' + str(j) + ', '
		grid += '\n'
	f.write(grid)

generate_text_grid(1000, 1000, 1024/20, 1024/20)