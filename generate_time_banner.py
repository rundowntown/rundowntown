#!/usr/bin/env python3
"""
Generate time-based Western-themed banner with sun/moon positioning
Requires: pip install pillow requests
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import requests
from io import BytesIO
from datetime import datetime
import pytz
import os

def get_time_period():
    """Determine current time period (dawn, noon, dusk, night)"""
    # Get current hour (use UTC or change to your timezone)
    now = datetime.now(pytz.UTC)
    hour = now.hour
    
    if 5 <= hour < 10:
        return "dawn", "☀️", (hour - 5) / 5  # 0 to 1 progression
    elif 10 <= hour < 16:
        return "noon", "☀️", 1.0
    elif 16 <= hour < 20:
        return "dusk", "🌅", 1.0 - ((hour - 16) / 4)  # 1 to 0 progression
    else:
        return "night", "🌙", 0.5

def create_gradient_overlay(width, height, colors):
    """Create a gradient overlay"""
    gradient = Image.new('RGBA', (width, height))
    draw = ImageDraw.Draw(gradient)
    
    # Create horizontal gradient
    for i in range(height):
        # Interpolate between colors
        ratio = i / height
        if ratio < 0.5:
            # First half of gradient
            r1, g1, b1 = colors[0]
            r2, g2, b2 = colors[1]
            local_ratio = ratio * 2
        else:
            # Second half of gradient
            r1, g1, b1 = colors[1]
            r2, g2, b2 = colors[2]
            local_ratio = (ratio - 0.5) * 2
        
        r = int(r1 + (r2 - r1) * local_ratio)
        g = int(g1 + (g2 - g1) * local_ratio)
        b = int(b1 + (b2 - b1) * local_ratio)
        
        draw.rectangle([(0, i), (width, i + 1)], fill=(r, g, b, 120))
    
    return gradient

def get_colors_for_period(period):
    """Return color scheme for each time period"""
    colors = {
        "dawn": [(255, 107, 53), (247, 147, 30), (253, 200, 48)],      # Orange sunrise
        "noon": [(222, 184, 135), (218, 165, 32), (255, 215, 0)],      # Bright gold
        "dusk": [(139, 69, 19), (210, 105, 30), (222, 184, 135)],      # Brown sunset
        "night": [(47, 79, 79), (105, 105, 105), (139, 69, 19)]        # Dark gray/brown
    }
    return colors.get(period, colors["dusk"])

def add_sun_moon_icon(draw, width, height, period, position):
    """Add sun or moon icon at position (0=left, 0.5=center, 1=right)"""
    icon_size = 80
    
    # Calculate position
    x = int(width * position)
    y_base = 60  # Height from top
    
    if period == "night":
        # Draw moon (crescent)
        y = y_base
        # Outer circle (white/yellow)
        draw.ellipse([(x - icon_size//2, y), (x + icon_size//2, y + icon_size)], 
                     fill=(255, 255, 200), outline=(200, 200, 150))
        # Inner circle (to create crescent)
        offset = 15
        draw.ellipse([(x - icon_size//2 + offset, y), (x + icon_size//2 + offset, y + icon_size)], 
                     fill=(0, 0, 0, 0))
    else:
        # Draw sun
        y = y_base
        # Sun circle
        sun_color = (255, 215, 0) if period == "noon" else (255, 140, 0)
        draw.ellipse([(x - icon_size//2, y), (x + icon_size//2, y + icon_size)], 
                     fill=sun_color, outline=(255, 255, 0))
        
        # Sun rays (simple lines)
        ray_length = 20
        for angle in range(0, 360, 45):
            import math
            rad = math.radians(angle)
            x1 = x + int((icon_size//2 + 5) * math.cos(rad))
            y1 = y + icon_size//2 + int((icon_size//2 + 5) * math.sin(rad))
            x2 = x + int((icon_size//2 + ray_length) * math.cos(rad))
            y2 = y + icon_size//2 + int((icon_size//2 + ray_length) * math.sin(rad))
            draw.line([(x1, y1), (x2, y2)], fill=sun_color, width=4)

def create_time_banner():
    """Create the main time-based banner"""
    
    # Get current time period
    period, emoji, position = get_time_period()
    
    # Load cowboys background
    if os.path.exists('cowboys.jpg'):
        img = Image.open('cowboys.jpg')
    else:
        # Create a default background if cowboys.jpg doesn't exist
        img = Image.new('RGB', (1200, 400), (139, 69, 19))
    
    # Resize to standard banner size
    banner_width = 1200
    banner_height = 400
    img = img.resize((banner_width, banner_height), Image.Resampling.LANCZOS)
    
    # Create gradient overlay
    colors = get_colors_for_period(period)
    gradient = create_gradient_overlay(banner_width, banner_height, colors)
    
    # Paste gradient on image
    img = img.convert('RGBA')
    img = Image.alpha_composite(img, gradient)
    
    # Convert back to RGB for drawing
    img = img.convert('RGB')
    draw = ImageDraw.Draw(img)
    
    # Add sun/moon icon
    add_sun_moon_icon(draw, banner_width, banner_height, period, position)
    
    # Try to load a nice font
    try:
        font_large = ImageFont.truetype("arial.ttf", 120)
        font_small = ImageFont.truetype("arial.ttf", 40)
    except:
        try:
            font_large = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 120)
            font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 40)
        except:
            try:
                # Windows fonts
                font_large = ImageFont.truetype("C:\\Windows\\Fonts\\arial.ttf", 120)
                font_small = ImageFont.truetype("C:\\Windows\\Fonts\\arial.ttf", 40)
            except:
                print("Using default font")
                font_large = ImageFont.load_default()
                font_small = ImageFont.load_default()
    
    # Add text
    text_main = f"{emoji} rundowntown"
    text_sub = "Code. Create. Conquer."
    
    # Calculate text position (center)
    bbox_main = draw.textbbox((0, 0), text_main, font=font_large)
    text_width_main = bbox_main[2] - bbox_main[0]
    text_height_main = bbox_main[3] - bbox_main[1]
    
    x_main = (banner_width - text_width_main) // 2
    y_main = banner_height // 2 - 50
    
    # Draw shadow
    shadow_offset = 5
    draw.text((x_main + shadow_offset, y_main + shadow_offset), text_main, 
              font=font_large, fill=(0, 0, 0))
    
    # Draw main text
    text_color = (245, 245, 220) if period != "noon" else (139, 69, 19)
    draw.text((x_main, y_main), text_main, font=font_large, fill=text_color)
    
    # Add subtitle
    bbox_sub = draw.textbbox((0, 0), text_sub, font=font_small)
    text_width_sub = bbox_sub[2] - bbox_sub[0]
    x_sub = (banner_width - text_width_sub) // 2
    y_sub = y_main + text_height_main + 20
    
    # Draw shadow for subtitle
    draw.text((x_sub + 3, y_sub + 3), text_sub, font=font_small, fill=(0, 0, 0))
    
    # Draw subtitle
    draw.text((x_sub, y_sub), text_sub, font=font_small, fill=(222, 184, 135))
    
    # Save the result
    img.save('current_banner.jpg', quality=95)
    print(f"Banner created for {period.upper()} time!")
    print(f"  Time period: {period}")
    print(f"  Sun/Moon position: {position:.2f}")
    
    return period

if __name__ == "__main__":
    create_time_banner()

