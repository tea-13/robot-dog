import numpy as np
from numpy import cos, sin, radians


class MathUtils:

	def __init__(self):
		self.axisDict = {
							'x' : 0,
							'y' : 1,
							'z' : 2,
						}

	def RotMatrix3D(self, 
		rotation: list = [0, 0, 0], is_radians: bool = True, conf: str = 'xyz') -> np.matrix:

		# convert to radians is the input is in degrees
		if is_radians:
			roll, pitch, yaw = rotation
		else:
			roll, pitch, yaw = map(radians, rotation)

		# rotation matrix about each axis
		rotX = np.matrix([
			[1, 0, 0], 
			[0, cos(roll), -sin(roll)], 
			[0, sin(roll), cos(roll)]
			])

		rotY = np.matrix([
			[cos(pitch), 0, sin(pitch)], 
			[0, 1, 0], 
			[-sin(pitch), 0, cos(pitch)]
			])

		rotZ = np.matrix([
			[cos(yaw), -sin(yaw), 0], 
			[sin(yaw), cos(yaw), 0], 
			[0, 0, 1]
			])

		rot = [rotX, rotY, rotZ]

		# rotation matrix order (default: pitch -> roll -> yaw)
		rotationMatrix = rot[self.axisDict[conf[0]]] * rot[self.axisDict[conf[1]]] * rot[self.axisDict[conf[2]]]

		return np.round(rotationMatrix, 2) # roll pitch and yaw rotation 

	def RotMatrix2D(self, 
			alpha: int = 0, is_radians: bool = True) -> np.matrix:

			# convert to radians is the input is in degrees
			if not is_radians:
				alpha = radians(alpha)

			# rotation matrix
			rot = np.matrix([
				[cos(alpha), -sin(alpha)], 
				[sin(alpha), cos(alpha)]
				])

			return np.round(rot, 2)


if __name__ == '__main__':
	Unit = MathUtils()

	#print(Unit.RotMatrix3D([30, 60, 45], False))
	#print(Unit.RotMatrix2D(30, False))


	# link size
	alpha = np.pi / 3
	link1 = 0.024
		
	link = np.array([[0, 0], [0, link1]])
	res = np.dot(Unit.RotMatrix2D(alpha), np.array([link[0][1], link[1][1]]))
	print(res)
