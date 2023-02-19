# Example from chatGPT😉

import pulp

# Define the problem variables
x = pulp.LpVariable('x', lowBound=0, cat='Continuous')
y = pulp.LpVariable('y', lowBound=0, cat='Continuous')

# Define the problem constraints and objective function
prob = pulp.LpProblem('Example', pulp.LpMaximize)
prob += x + y <= 5
prob += 2*x + 3*y <= 12
prob += 4*x + y <= 15
prob += x + 2*y >= 3
prob += x + y # objective function

# Solve the problem and print the results
status = prob.solve()
print(pulp.LpStatus[status])
print('x =', pulp.value(x))
print('y =', pulp.value(y))
print('Objective value =', pulp.value(prob.objective))
