import os

# Define file paths
colors_file = "colores.txt"
svg_file = "logo.svg"
output_folder = "logos"

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Read colors from the text file
with open(colors_file, "r") as f:
    colors = [color.strip() for color in f.read().split(",")]

# Read the original SVG content
with open(svg_file, "r") as f:
    svg_content = f.read()

# Replace color and save a new SVG for each color
for color in colors:
    new_svg_content = svg_content.replace("#ff0000", color)
    output_file = os.path.join(output_folder, f"{color}.svg")
    with open(output_file, "w") as f:
        f.write(new_svg_content)

print(f"Generated {len(colors)} SVG files in the '{output_folder}' folder.")
