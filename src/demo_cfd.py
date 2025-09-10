import numpy as np
import matplotlib.pyplot as plt

# Définition des angles d'incidence
alpha = np.linspace(-5, 15, 30)  # degrés

# Coefficient de portance simplifié
Cl = 0.1 * (alpha + 2)

# Affichage
plt.plot(alpha, Cl, 'o-')
plt.xlabel("Angle d'incidence (deg)")
plt.ylabel("Coefficient de portance Cl")
plt.title("Courbe polaire simplifiée")
plt.grid(True)
plt.show()

