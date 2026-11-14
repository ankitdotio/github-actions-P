from PIL import Image

ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def image_to_ascii(image_path, new_width=80):
    img = Image.open(image_path)
    
    # Adjust height by 0.55 to account for terminal character aspect ratios
    width, height = img.size
    aspect_ratio = height / width
    new_height = int(new_width * aspect_ratio * 0.55)
    img = img.resize((new_width, new_height))
    
    # Convert to grayscale and map pixel brightness (0-255) to characters
    img = img.convert("L")
    pixels = img.getdata()
    characters = "".join(ASCII_CHARS[pixel // 25] for pixel in pixels)
    
    # Format into lines matching the new width
    ascii_image = "\n".join(
        characters[i:(i + new_width)] for i in range(0, len(characters), new_width)
    )
    return ascii_image

print(image_to_ascii("sample.jpg"))
