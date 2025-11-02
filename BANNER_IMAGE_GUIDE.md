# 🖼️ How to Add a Custom Banner Image

## Quick Start - 3 Ways to Add Your Cowboy/Western Image

### Method 1: Upload to Your Repository (Recommended)

1. **Save your cowboy/western image** to your computer (e.g., `banner.jpg` or `banner.png`)

2. **Create an `assets` folder** in your repository:
   ```
   rundowntown/
   ├── assets/
   │   └── banner.jpg
   ├── README.md
   └── ...
   ```

3. **Upload the image** to GitHub (drag & drop or use git)

4. **Replace `YOUR_IMAGE_URL_HERE`** in README.md with:
   ```
   https://raw.githubusercontent.com/rundowntown/rundowntown/main/assets/banner.jpg
   ```

### Method 2: Use an External URL (Quick & Easy)

1. **Upload your image** to any image host:
   - [Imgur](https://imgur.com) - Free, no account needed
   - [GitHub Issues](https://github.com/rundowntown/rundowntown/issues) - Drag image into a new issue, copy URL (don't submit)
   - Any CDN or image hosting service

2. **Copy the direct image URL** (must end in .jpg, .png, .gif, etc.)

3. **Replace `YOUR_IMAGE_URL_HERE`** in README.md with that URL

### Method 3: Use GitHub Issues Trick (Fastest)

1. Go to your repository's Issues tab
2. Click "New Issue"
3. Drag your cowboy image into the text box
4. GitHub will upload it and give you a URL like:
   ```
   https://user-images.githubusercontent.com/12345/filename.png
   ```
5. Copy that URL (don't submit the issue - just close it)
6. Use that URL in your README

---

## Example Western/Cowboy Image Sources

If you don't have an image yet, here are some free sources:

- **Unsplash**: https://unsplash.com/s/photos/western-cowboy
- **Pexels**: https://www.pexels.com/search/western/
- **Pixabay**: https://pixabay.com/images/search/cowboy/

Look for keywords like:
- "Western landscape"
- "Cowboy silhouette"
- "Desert sunset"
- "Wild west"
- "Old west town"

---

## Customizing the Text Overlay

In your README.md, you can adjust these settings:

### Text Size
```html
<h1 style="font-size: 80px;">  <!-- Change 80px to make bigger/smaller -->
```

### Text Color
```html
color: #F5F5DC;  <!-- Beige/cream color -->
color: #FFFFFF;  <!-- White -->
color: #DAA520;  <!-- Goldenrod -->
```

### Shadow Intensity
```html
text-shadow: 3px 3px 8px #000000;  <!-- More shadow = more readable -->
text-shadow: 5px 5px 15px #000000; <!-- Even stronger shadow -->
```

### Vertical Position
```html
<h1 style="margin-top: -150px;">  <!-- Adjust -150px to move text up/down -->
```

### Image Height
```html
<img src="..." style="max-height: 350px;">  <!-- Change 350px for taller/shorter banner -->
```

---

## Full Example with Real Image

Here's what it looks like with a real URL:

```html
<div align="center">
  <img src="https://images.unsplash.com/photo-1544526226-d4568090ffb8" alt="Header" style="width: 100%; max-height: 350px; object-fit: cover;">
  <h1 style="margin-top: -150px; font-size: 80px; color: #F5F5DC; text-shadow: 3px 3px 8px #000000;">rundowntown</h1>
  <p style="font-size: 24px; color: #DEB887; text-shadow: 2px 2px 4px #000000;">Code. Create. Conquer.</p>
</div>
```

---

## Pro Tips

1. **Image Aspect Ratio**: Wide images (16:9 or wider) work best for banners
2. **Dark Images**: Work better for light-colored text overlay
3. **Center Focus**: Make sure important parts aren't covered by text
4. **File Size**: Keep under 1MB for fast loading
5. **Resolution**: 1920x400 to 2560x600 pixels is ideal

---

## Troubleshooting

**Text not showing?**
- Some GitHub markdown renderers don't support inline styles
- Try increasing text-shadow for better visibility

**Image not loading?**
- Make sure the URL ends with .jpg, .png, or .gif
- Check that the image URL is publicly accessible
- Try pasting the URL directly in a browser to test

**Want the animated wave back?**
- Just uncomment the OPTION 2 line in your README
- Delete or comment out the HTML div section

---

Ready to go! Just find your perfect cowboy image and drop the URL in! 🤠

