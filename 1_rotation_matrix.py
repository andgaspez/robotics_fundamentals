import numpy as np
import matplotlib.pyplot as plt
import argparse

def rotate(x, y, theta):
    """
    Rotate a set of point (x, y) by an angle theta (in radians).
    """
    rotation_matrix = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta), np.cos(theta)]
    ])
    #print(rotation_matrix)
    original_vector = np.array([x, y])
    rotated_vector = np.dot(rotation_matrix, original_vector)
    return rotated_vector

# A triangle shape
points = np.array([
    [0, 1],    # Top vertex
    [1, -1],   # Bottom-right vertex
    [-1, -1],  # Bottom-left vertex
    [0, 1]     # Close the loop at Top vertex
])

parser = argparse.ArgumentParser(description='Simple script to check rotation matrix')

# Arguments definition
parser.add_argument('rot_deg', type=float, help='Angle should be a float number')

args = parser.parse_args()

# Rotation angle in radians
rot_rad = np.radians(args.rot_deg)

print(f"Rot deg: {args.rot_deg}, Rot rad: {rot_rad}")

# Rotate each point
rotated_points = np.array([rotate(x, y, rot_rad) for x, y in points])

# Original and rotated points plot
plt.figure(figsize=(8, 8))
plt.axhline(0, color='grey', linewidth=0.5)
plt.axvline(0, color='grey', linewidth=0.5)
plt.grid(True, which='both')

# Original triangle and lines plot
plt.plot(points[:, 0], points[:, 1], 'bo-', label='Original Points')

# Rotated triangle and lines plot
plt.plot(rotated_points[:, 0], rotated_points[:, 1], 'ro-', label='Rotated Points')

# Labels
plt.legend()
plt.title(f'Rotation by {args.rot_deg} Degrees')
plt.xlabel('X')
plt.ylabel('Y')
plt.axis('equal')
plt.show()