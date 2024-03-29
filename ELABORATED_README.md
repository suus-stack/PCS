Authors:      Suze Frikkee, Luca Pouw, Eva Nieuwenhuis
University:   UvA
Course:       Project computational science
Student id's: 14773279, 15159337, 13717405

THE GOAL  
The main goal of this project is to make a 2D agent-based model that simulates the
behaviour of a herring school. The aim is to assess the influence of the three Boid
rules, as well as the impact of environmental changes, rocks and predators (barracuda),
on the killing rate within a herring school. For the parameter values of the predator
the values from barracudas are taken.

PYTHON AND LIBRARY VESIONS
Python version 3.11.4 is used. To run the different codes in the code file some
libraries need to be installed.

Boids.py
* numpy (version 1.26.0)
    - install: pip install numpy==1.26.0
* matplotlib (version 3.8.2)
    - install: pip install matplotlib==3.8.2

Herring_simulation.py
* numpy (version 1.26.0)
    - install: pip install numpy==1.26.0
* pygame (version 2.5.2)
    - install: pip install pygame==2.5.2

Statistic_tests.py
* numpy (version 1.26.0)
    - install: pip install numpy==1.26.0
* pandas (version 2.1.3)
    - install: pip install pandas==2.1.3
* scipy (version 1.11.4)
    - install: pip install scipy==1.11.4

Visualisation.py
* numpy (version 1.26.0)
    - install: pip install numpy==1.26.0
* matplotlib (version 3.8.2)
    - install: pip install matplotlib==3.8.2
* seabron (version 0.13.0)
    - install: pip install seaborn==0.13.0
* pandas (version 2.1.3)
    - install: pip install pandas==2.1.3

The link to the GitHub containing the code is https://github.com/suus-stack/PCS

THE MODEL: herring_simulation.py  
Herring_simulation.py contains the code to run an 2-dimensional agent-based model in
which the herring, rocks and predators are represented as agents with their own
positions and velocities.

Herring features  
The movement of a herring (Boid) is based on three rules:
- Separation: Herring maintain a minimum distance between each other.
- Alignment: Herring aligns their direction with that of their closest neighbours
- Cohesion: Herring remains in close proximity to their nearest neighbours.

The speed of the herring is the average speed for a herring. For a diversity of natural
speeds within the group, a value of the standard deviation (SD) spread, ranging between
-1 and 1, is also added to this.
The presence of rocks and predators in the environment influences the behavior of herring,
when it is in their perception range. Rocks alter the direction of herring, while predators
can affect both their speed and direction. As predators comes closer, the herring's speed
increases.

Barracuda features  
The movement of a barracuda is initially random, but it changes when it encounters
anotherbarracuda, causing it to change directions. For a diversity of natural speeds
within the group, a value of the SD spread, ranging between -1 and 1, is also added to
this. Additionally, the presence of rocks and herring in the environment also influences
a barracuda's movement. Rocks can alter the direction of a barracuda, while herring can
impact both its speed and direction. When a herring is within the perception range of a
barracuda, the predator's speed increases, and it will move towards the herring.
Moreover, the closer the herring, the greater the acceleration of the barracuda's speed.

Rock features  
The stones are randomly distributed. No creature can traverse these obstacles. When
parameter 'connect_rocks' is set to true, the stones will cluster. This is achieved
by identifying stones within a Euclidean distance of less than 60 units and placing
additional rocks along this distance line.

THE FUNCTION  
Experiment(herring_nr, predator_nr, rock_nr, simulation_duration, connect_rocks,
  start_school, perception_change_predator, perception_change_herring, alignment_distance,
  cohesion_distance, separation_distance, boids_influence, weighted_x)

In the default function, the rocks get a random position, and connect_rocks is set to
true. Start_school is also set to True, so the herring get different positions
close to each other to form a school. The barracudas are assigned random positions that
lie outside the perception range of any herring. This ensures that the entire attack is
shown. The simulation is run for a with the 'simulation_duration' parameter specified
number of seconds.
In the perception length of the herring and predator do not change, perception_change
_predator and perception_change_herring are set to False. And every Boid rule has the
same amount of influence.

Specifications in model
For longer simulation durations, the perception length of barracuda can dynamically change
over time using the 'perception_change' parameter. Additionally, the alignment distance,
cohesion distance, and separation distance are subject to modification to evaluate their
individual effects. This adjustment aims to explore whether these rule alterations affect
the killing rate of herring. If the 'boids_influence' parameter is set to a value other
than 0, the impact of a rule will be assigned a weighted indicted with 'weighted_x'

Output model  
In the default function, the model returns a dictionary that contains the number
of killed herring and the number of times herring came within the separation distance
of 6. If 'perception_change_herring' is set to True the returned dictionary also will
contain a list with the perception length of the herring and with the killed herring
count at every time point. If 'perception_change_predator' is set to True the returned
dictionary also will contain a list with the perception length of the predator and
with the killed herring count at every time point.

FIXED PARAMETERS  
* HERRING_SIZE (float) = the radius of the circle which represents herring in the simulation.
                         - Set to 3
* HERRING_SPEED (float) = the average speed of a herring.
                         - Set to 1.24 (SD = 0.05)
* HERRING_SPEED_MAX (float) = the maximum speed of a herring.
                         - Set to 18.44
* PERCEPTION_LENGHT_HERRING (float) = the length a herring can sense.
                         - Set to 32
* KILL_DISTANCE (float) = the distance where a predator wil kill a herring.
                         - Set to 3.6
* PREDATOR_SIZE (float) = radius of the wich represents a baracuda in the simulation.
                         - Set to 4
* PREDATOR_SPEED (float) = the normal average speed of a barracuda.
                         - Set to 3.6 (SD = 0.8)
* PREDATOR_SPEED_MAX (float) = the highest speed a barracuda can have.
                         - Set to 24.4
* PERCEPTION_LENGHT_PREDATOR (float)= the length a barracuda can sense.
                         - Set to 100
* ROCK_LENGHT (float) = the length of the square representing a rock in the simulation.
                         - Set to 10
* ROCK_AVOIDANCE_DIST (float) = the distance at which both creatures will start sensing rocks.
                         - Set to 16

CHANGEABLE PARAMETERS  
* herring_nr (int) = initial number of herring added to the simulation.
* predator_nr (int) = initial number of predators added to the simulation.
* rock_nr (int) = initial number of rocks added to the simulation.
* simulation_duration (int) = duration of a simulation in seconds.
* connected_rocks (bool) = parameter for adding clustering of the initial rocks.
                          True -- clustering of rocks,
                          False -- no clustering of rocks.
* start_school (bool) = herring start as one school instead of randomly.
                          True -- the herring start in one school,
                          False -- the herring start on random places no clustering of rocks.
* perception_change_predator (bool) = change of the barracuda perception length over time.
                          True -- the barracuda perception length changes over time,
                          False -- the barracuda perception length does not changes over time.
* perception_change_herring (bool) = change of the herring perception length over time.
                          True -- the herring perception length changes over time,
                          False -- the herring perception length does not changes over time.
* SEPARATION_DISTANCE (float) = if another herring is within this distance, it will be
                          included in the separation rule.
* ALIGNMENT_DISTANCE (float) = if another herring is within this distance, it will be
                          included in the alignment rule.
* COHESION_DISTANCE (float) = if another herring is within this distance, it will be
                          included in the cohesion rule.
* boids_influence (int) = Indicates the influence of Boids rules.
                            0 --  all rules are equal,
                            1 -- separation is weighted weighted_x times more,
                            2 -- alignment is weighted weighted_x times more,
                            3 -- cohesion is weighted weighted_x times more.
* weighted_x (int) = Indicates the weight of the Boid rule of which the influence is changed  

HOW TO RUN:  
Command in to simulate the default model with these values:
Experiment(herring_nr = 100, predator_nr = 3, rock_nr = 30, simulation_duration = 20,
      extra_rocks = False, start_school = True, perception_change_predator = False,
      perception_change_herring = False, alignment_distance = 32, cohesion_distance = 32,
      separation_distance = 6, boids_influence = 0, weight_x = 3)

- python herring_simulation.py

TEST CODE   
To test some functions in the model, doc test are added and automatically run when
a simulation is run.

THE VISUALISATION: herring_simulation.py  
Visualization.py contains the code to make plots that show the influence of environmental
changes on the killing rate and school density. It uses the herring_simulation.py code
to run an simulation.

Because the running of the figures takes a long time. All results are provided in the
folder data_visualisation.
* 4-perception_change_50_plot: Line graph that shows the change in perception length and
                  the influence on the number of killed herring over the time when there
                  are 50 herring at the beginning.

* 4-perception_change_250_plot: Line graph that shows the change in perception length and
                  the influence on the number of killed herring over the time when there
                  are 250 herring in the beginning.

* Change_alignment_distance_plot: Line graph of the average killed herring with SD
                  error bars at different alignment distances.

* Change_predator_nr_plot: Violin plot of the distribution of the killed herring for
                  different numbers of barracudas with and without rocks.

* Change_rock_nr_plot: Line graph of the average killed herring with the SD error bars
                  in environments with different numbers of rocks.

* Density_Killing_combination_plot: Boxplots with strip plot overlap that show the
                  distribution of the herring count within the original separation distance
                  of 6 and the herring killing count across various conditions.

* School_size_plot: Boxplot with strip plot overlap that shows the proportion of killed
                  herring in large and small schools, with and without rocks.

* Boids_rules_influence_plot: Boxplot with strip plot overlap that shows the number of
                  killed herring when different Boid-flocking rules are emphasised

* Boid_rules_sensitivity_analysis_plot: Line plots of the average number of killed
                  herring + 1 SD error bars for different values of the alignment,
                  cohesion and separation distance as sensitivity analysis.

* Predator_killing_efficiency_plot = Line plot of the average number of killed herring per
                  predator + 1 SD error bars in an environment with and without rocks.

* Sensitivity_weight_plot = Line plots illustrating the mean number of killed herring + SD
                  for weight values ranging from -5 to 5 in increments of 1.

HOW TO RUN
- python visualisation.py.


THE STATISTICAL TESTS  
Statistic_tests.py contains the code to do the statistical test on the data obtained
in visualisation.py.

significant_test_school_size:
- Test to determine if school size significantly changes the killing proportion.

significant_test_close
- Test to determine if environmental changes significantly influence the school density.

significant_test_killed
- Test to determine if environmental changes significantly influence the killing rate.

significant_test_boidsrules
- Test to determine if the different Boid-flocking rules significantly influence the killing rate.

This cannot be run separately because it needs the data collected from visualisation.py.


INCOMPLETE MODEL: vectorized implementation  
boids.py contains code to run an agent-based simulation of herring schools and possibly
rocks and/or predators. This code works with matrices, making the implementation very clean
and concise. Implementing the three Boid flocking rules (separation, alignment and
cohesion) was possible and because of the matrices, simultaneously updating the herring
and predator was easy. However, with the limited amount of time, we chose to continue with
the classes implementation, since this model was the easiest to work with and to make small
adaptions on. So for that reason, the code is not complete and we did not use it for
analysis, it simply shows we tried a different approach.   

THE FUNCTION  
Experiment(lower_lim_flock, upper_lim_flock, lower_lim_veloc, upper_lim_veloc, nr_herring,
           nr_predators, nr_rocks)

In the default function the herring get a random position between the lower_lim_flock
and upper_lim_flock. The rocks and predators also get a random different position. The
herring also get a random velocity between the stated lower_lim_veloc and upper_lim_veloc.

FIXED PARAMETERS  
* perception_predator (float) = perception rate of predator.
                        - Set to 50.
* velocity_predator (float) = velocity of predator.
                        - Set to 2.
* attraction_to_center (float) = the strength of the centre movement method, where a
                    negative value implies repulsion and a positive value attraction.
                        - Set to 0.0008
* width_flock (float) = It determines the range or spread of the flocking behaviour
                    in the simulation.
                        - Set to upper_lim_flock - lower_lim_flock
* width_veloc (float) = It determines the range or spread of possible velocities for
                    entities in the simulation.
                        - Set to upper_lim_veloc - lower_lim_veloc
* iterations (int) = the number of times the experiment will be repeated.
                        - Set to 100.
* second_flock (bool) = enables/ disables a second flock of nr_herring.
                        - Set to False.
* min_distance (float) = minimum distance entities must maintain to avoid collisions
                    in the simulation.
                        - Set to 20.
* formation_flying_distance (float)= determines the distance at which entities align
                    with each other.
                        - Set to 10.
* formation_flying_strength (float)= controls the strength of the alignment. A higher value
                    increases the influence of alignment on entity direction within the
                    specified distance.
                        - Set to 0.8
* perception_length_herring (float)= the length a herring can sense.
                        - Set to 0.002

CHANGEABLE PARAMETERS  
* nr_herring (int) = initial number of herring added to the simulation.
* nr_predators (int) = initial number of predators added to the simulation.
* nr_rocks (int) = initial number of rocks added to the simulation.
* lower_lim_flock (float)= Minimum value where a herring of a flock can be placed.                        
* upper_lim_flock (float)= Maximum value where a herring of a flock can be placed.                
* lower_lim_veloc (float)= Minimum range of the velocity of a herring.                      
* upper_lim_veloc (float)= Maximum range of the velocity of a herring.


HOW TO RUN:  
Command to simulate the incomplete model with the values:
Experiment(lower_lim_flock = np.array([0, 100]), upper_lim_flock = np.array([0, 100]),
        lower_lim_veloc = np.array([10, 20]), upper_lim_veloc = np.array([0, -20]),
        nr_herring = 20, nr_predators = 2, nr_rocks = 10)

- python boids.py

TEST CODE   
To test some functions in the model, doc test are added and automatically run when
a simulation is run.
