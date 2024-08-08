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
    original_vector = np.array([x, y])
    rotated_vector = np.dot(rotation_matrix, original_vector)
    return rotated_vector

def calculate_centroid(points):
    """
    Calculate the centroid of a polygon given by points.
    """
    x_coords = points[:, 0]
    y_coords = points[:, 1]
    centroid = [np.mean(x_coords), np.mean(y_coords)]
    return centroid

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

# Calculate the centroid of the rotated triangle
centroid = calculate_centroid(rotated_points)

# Original and rotated points plot
plt.figure(figsize=(8, 8))
plt.axhline(0, color='grey', linewidth=0.5)
plt.axvline(0, color='grey', linewidth=0.5)
plt.grid(True, which='both')

# Original triangle and lines plot
plt.plot(points[:, 0], points[:, 1], 'bo-', label='Body original position')

# Rotated triangle and lines plot
plt.plot(rotated_points[:, 0], rotated_points[:, 1], 'ro-', label='Body rotated position')

# Add reference frames to the original triangle (placed at -1.5, 0)
plt.quiver(-1.5, 0, 1, 0, color='black', scale=1, scale_units='inches', label='World frame {W}')
plt.quiver(-1.5, 0, 0, 1, color='black', scale=1, scale_units='inches')

# Add reference frames to the rotated triangle (centered at the centroid)
rot_x_axis = rotate(1, 0, rot_rad)
rot_y_axis = rotate(0, 1, rot_rad)
plt.quiver(centroid[0], centroid[1], rot_x_axis[0], rot_x_axis[1], color='red', scale=1, scale_units='inches', label='Body Frame {B}')
plt.quiver(centroid[0], centroid[1], rot_y_axis[0], rot_y_axis[1], color='red', scale=1, scale_units='inches')

# Labels
plt.legend()
plt.title(f'Rotation by {args.rot_deg} Degrees')
plt.xlabel('X')
plt.ylabel('Y')
plt.axis('equal')
plt.show()