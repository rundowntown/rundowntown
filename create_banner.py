#!/usr/bin/env python3
"""
Create a composite banner with text overlay on cowboys.jpg
Requires: pip install pillow requests
"""

from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO

def create_banner():
    # Load the cowboys image
    img = Image.open('cowboys.jpg')
    
    # Create a drawing context
    draw = ImageDraw.Draw(img)
    
    # Get image dimensions
    width, height = img.size
    
    # Download and overlay the wave (optional - or we can draw our own)
    wave_url = "https://capsule-render.vercel.app/api?type=waving&color=0:8B4513,50:D2691E,100:DEB887&height=200&section=header"
    
    try:
        response = requests.get(wave_url)
        wave_img = Image.open(BytesIO(response.content))
        wave_img = wave_img.resize((width, 200))
        wave_img.putalpha(128)  # Make semi-transparent
        
        # Paste wave at top
        img.paste(wave_img, (0, 0), wave_img)
    except:
        print("Could not load wave, adding solid overlay instead")
        # Draw a gradient overlay manually
        overlay = Image.new('RGBA', (width, 200), (139, 69, 19, 100))
        img.paste(overlay, (0, height - 200), overlay)
    
    # Try to use a good font, fallback to default
    try:
        # Try common font locations
        font_large = ImageFont.truetype("arial.ttf", 100)
        font_small = ImageFont.truetype("arial.ttf", 32)
    except:
        try:
            font_large = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 100)
            font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 32)
        except:
            print("Using default font")
            font_large = ImageFont.load_default()
            font_small = ImageFont.load_default()
    
    # Add text with shadow
    text_main = "rundowntown"
    text_sub = "Code. Create. Conquer."
    
    # Calculate text position (center)
    bbox_main = draw.textbbox((0, 0), text_main, font=font_large)
    text_width_main = bbox_main[2] - bbox_main[0]
    text_height_main = bbox_main[3] - bbox_main[1]
    
    x_main = (width - text_width_main) // 2
    y_main = height // 3
    
    # Draw shadow
    shadow_offset = 4
    draw.text((x_main + shadow_offset, y_main + shadow_offset), text_main, 
              font=font_large, fill=(0, 0, 0, 180))
    
    # Draw main text
    draw.text((x_main, y_main), text_main, 
              font=font_large, fill=(245, 245, 220))  # Beige
    
    # Add subtitle
    bbox_sub = draw.textbbox((0, 0), text_sub, font=font_small)
    text_width_sub = bbox_sub[2] - bbox_sub[0]
    x_sub = (width - text_width_sub) // 2
    y_sub = y_main + text_height_main + 20
    
    # Draw shadow for subtitle
    draw.text((x_sub + 2, y_sub + 2), text_sub, 
              font=font_small, fill=(0, 0, 0, 180))
    
    # Draw subtitle
    draw.text((x_sub, y_sub), text_sub, 
              font=font_small, fill=(222, 184, 135))  # Burlywood
    
    # Save the result
    img.save('cowboys_banner.jpg', quality=95)
    print("Banner created! Saved as 'cowboys_banner.jpg'")
    print("Now replace './cowboys.jpg' with './cowboys_banner.jpg' in your README")

if __name__ == "__main__":
    create_banner()

