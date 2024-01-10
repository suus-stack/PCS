import numpy as np
from  matplotlib import pyplot as plt


def initialize_flock(nr_herring, lower_lim, upper_lim):
    """ if you want the x-axis to vary between 100 and 200 and the y-axis to be betweeb
    900 and 1100, you use: lower_lim = np.array([100, 900]) and upper_lim = np.array([200, 1100])"""
    width = upper_lim - lower_lim
    flock = lower_lim[:, np.newaxis] + np.random.rand(2, nr_herring) * width[:, np.newaxis]
    return flock

def initialize_velocities(nr_herring, lower_lim, upper_lim):
    """Random initializatio of velocitie for each herring."""
    width = upper_lim - lower_lim
    velocities = lower_lim[:, np.newaxis] + np.random.rand(2, nr_herring) * width[:, np.newaxis]
    return velocities 

def update_location(positions, velocities):
    positions += velocities 

def update(positions, velocities):
    # Initial movement being to the middle
    attraction_to_center = 0.01
    center = np.mean(positions, 1) # 1 because along the second axis 
    # Calculating direction vectors from each position to the center
    direction_to_center = positions - center[:, np.newaxis]

    velocities -= direction_to_center * attraction_to_center
    # Update all individual positions
    positions += velocities

def visualize(positions, ax1):
    
    ax1.axis([0, 2000, 0, 2000])
    ax1.scatter(positions[0, :], positions[1, :], c='blue', alpha=0.5, marker='o', s=10)

    plt.draw()
    plt.pause(0.01)
    ax1.cla()


def setup_plot():
    fig, ax1 = plt.subplots(1)
    ax1.set_aspect('equal')
    ax1.set_facecolor((0.7, 0.8, 1.0))
    ax1.axes.get_xaxis().set_visible(False)
    ax1.axes.get_yaxis().set_visible(False)

    return ax1

def run(iterations, positions, velocities):
    ax1 = setup_plot()
    for _ in range(iterations):
        update(positions, velocities)
        visualize(positions, ax1)


# USAGE 
positions = initialize_flock(10, np.array([100, 900]), np.array([200, 1100]))
velocities = initialize_velocities(10, np.array([0, -20]), np.array([10, 20]))
run(100, positions, velocities)