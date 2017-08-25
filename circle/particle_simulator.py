# Simulating the position of the particle object
from particle import particle

class ParticleSimulator:
	def __init__(self, particles):
		self.particles=particles
	def evolve(self, dt):
		timestep= 0.00001
		nstep= int(dt/timestep)

		for in range(nsteps):
			for particle in self.particles:
				norm = (p**2 + q**2)**0.5
				v_x= (-p_y)/norm
				v_y= (p_x)/norm

				d_x= v_x * ang_speed * timestep
				d_y= v_y * ang_speed * timestep

				p_x += d_x
				p_y += d_y
