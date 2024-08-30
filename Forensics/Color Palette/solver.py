from PIL import Image
import numpy as np
import base64
from sklearn.cluster import KMeans

def extract_dominant_colors(image_path, num_colors=5):
  # Open the image and convert it to RGB
  with Image.open(image_path) as img:
    img = img.convert('RGB')
    img_np = np.array(img)

  # Reshape the image to be a list of pixels
  pixels = img_np.reshape(-1, 3)

  # Perform k-means clustering to find dominant colors
  kmeans = KMeans(n_clusters=num_colors)
  kmeans.fit(pixels)
  dominant_colors = kmeans.cluster_centers_.astype(int)

  # Convert RGB values to hex
  hex_colors = ['{:02x}{:02x}{:02x}'.format(c[0], c[1], c[2]) for c in dominant_colors]

  return hex_colors

def hex_to_raw_and_base64(hex_color):
  # Convert the hex color to raw bytes
  raw_bytes = bytes.fromhex(hex_color)
  
  # Encode the raw bytes to base64
  base64_encoded = base64.b64encode(raw_bytes).decode('utf-8')
  
  return base64_encoded

def main(image_path, num_colors):
  hex_colors = extract_dominant_colors(image_path, num_colors)
  print(f"Dominant colors in {image_path}:")
  
  # Convert each dominant hex color to raw and then to base64
  for hex_color in hex_colors:
    base64_encoded = hex_to_raw_and_base64(hex_color)
    print(f"Hex: {hex_color} -> Base64: {base64_encoded}")

main('./coming_soon_colorfest.png', 5)