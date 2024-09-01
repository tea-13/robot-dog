import numpy as np
from numpy import cos, sin, radians
import matplotlib.pyplot as plt
from matplotlib.widgets import Button, Slider
from matplotlib.lines import Line2D
from utils import MathUtils

class Joint:
	def __init__(self, jt : list) -> None:
		self.jt = jt


	def rotate_joint(self, ang : int) -> np.matrix:
		vec_start = np.array([self.jt[0][0], self.jt[1][0]])
		vec_end = np.array([self.jt[0][1], self.jt[1][1]])

		rot_matrix = MathUtils().RotMatrix2D(ang, False)

		res_start = np.dot(rot_matrix, vec_start)
		res_end = np.dot(rot_matrix, vec_end)

		self.jt[0][0], self.jt[1][0] = res_start[0], res_start[1]
		self.jt[0][1], self.jt[1][1] = res_end[0], res_end[1]

	def get_coord(self):
		return self.jt

	def get_line2D(self):
		return Line2D(*self.jt)




def update(val):
	link = np.array([[0, 0], [0, link1]])
	res = np.dot(mt.RotMatrix2D(1, sliderAlpha.val), np.array([link[0][1], link[1][1]]))
	ln.remove()
	link = np.array([[0, res[0, 0]], [0, res[0, 1]]])
	ln = Line2D(*link)
	axGraph.add_line(ln)



if __name__ == '__main__':
	# joints abs
	link1 = 0.024
	link2 = 0.1297
	link3 = 0.024
	link4 = 0.12
	link5 = 0.1

	# Joints zero position
	jt1 = Joint([[0, 0], [0, 0.024]])
	jt1.rotate_joint(45)
	
	jt2 = Joint([
		[jt1.jt[0][1], jt1.jt[0][1] + link2 * sin(radians(225))], 
		[jt1.jt[1][1], jt1.jt[1][1] + link2 * cos(radians(225))]
		])
	
	jt3 = Joint([
		[jt2.jt[0][1], jt2.jt[0][1] + (link3 + link4) * sin(radians(-225))], 
		[jt2.jt[1][1], jt2.jt[1][1] + (link3 + link4) * cos(radians(-225))]
		])
	
	alpha = np.arctan((jt3.jt[1][1] - jt3.jt[1][0]) / (jt3.jt[0][1] - jt3.jt[0][0]))
	jt4 = Joint([
		[jt3.jt[0][1] + link3 * cos(alpha), jt3.jt[0][1] + link3 * cos(alpha) + link5 * cos(radians(90) - alpha)],
		[jt3.jt[0][1] + link3 * sin(alpha), jt3.jt[0][1] + link3 * sin(alpha) + link5 * sin(radians(90) - alpha)]
		])

	
	fig = plt.figure(figsize=(8, 8))
	axGraph = fig.add_axes([0.1, 0.5, 0.5, 0.45])
	axGraph.grid()
	axGraph.set(xlim=(-.4, .4), ylim=(-.5, .5))

	axGraph.add_line(jt1.get_line2D())
	axGraph.add_line(jt2.get_line2D())
	axGraph.add_line(jt3.get_line2D())
	axGraph.add_line(jt4.get_line2D())


	plt.show()






'''
	# zero position
	link1 = np.dot(mt.RotMatrix2D(1, 45, False), np.array([0, 0.024]))
	print(link1)
	ln1 = np.array(
		[[0, 0], [0, 0.024]]
		)

	link2 = 0.1297
	ln2 = np.array([
		[link1[0, 0], link1[0, 0]], 
		[link1[0, 1], link1[0, 1] - link2]
		])
	link3 = np.array([[0, 0], [0, 0.144]])
	link4 = np.array([[0, 0], [0, 0.1]])
	
	ln_1 = Line2D(*ln1)
	ln_2 = Line2D(*ln2)

	


	# UI
	fig = plt.figure(figsize=(7, 7))
	axGraph = fig.add_axes([0.1, 0.4, 0.8, 0.5])
	axSlider = fig.add_axes([0.1, 0.25, 0.70, 0.04])
	btn = fig.add_axes([0.1, 0.1, 0.1, 0.04])
		
	axGraph.grid()
	axGraph.add_line(ln_1)
	axGraph.add_line(ln_2)
	axGraph.set(xlim=(-.5, .5), ylim=(-.5, .5))

	button = Button(btn, 'del', hovercolor='0.975')

	sliderAlpha = Slider(axSlider,
								label='alpha',
								valmin=-np.pi,
								valmax=np.pi,
								valinit=0,
								valfmt='%1.2f')

	sliderAlpha.on_changed(update)

	plt.show()

'''