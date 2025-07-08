



from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector
import matplotlib.pyplot as plt
import numpy as np
import os

# Optional: ensure 'images' folder exists
if not os.path.exists("images"):
    os.makedirs("images")

# Define the state |ψ⟩ = √3/2 |0⟩ − 1/2 |1⟩
alpha = np.sqrt(3)/2
beta = -0.5
state = Statevector([alpha, beta])

# Plot the Bloch sphere
fig = plot_bloch_multivector(state, title="Bloch Sphere: Negative Relative Phase")
plt.tight_layout()
plt.show()

# Save figure (optional)
fig.savefig("images/bloch_negative_phase.png", dpi=300)
