# 🎨 Capsule Render Customization Options

All the cool things you can do with your animated banner!

## 🌊 Banner Types

### 1. Waving (Current)
```
type=waving
```
Classic wave shape at top/bottom

### 2. Cylinder
```
type=cylinder
```
3D cylinder effect - looks like a rolling barrel

### 3. Shark
```
type=shark
```
Angular, aggressive looking

### 4. Slice
```
type=slice
```
Diagonal slice cut

### 5. Rect
```
type=rect
```
Simple rectangle

### 6. Soft
```
type=soft
```
Gentle curved edges

### 7. Rounded
```
type=rounded
```
Rounded top corners

### 8. Transparent
```
type=transparent
```
No background shape

### 9. Venom
```
type=venom
```
Spiky, edgy look

---

## ✨ Animation Options

### 1. Twinkling (Subtle shimmer)
```
animation=twinkling
```

### 2. Fade In
```
animation=fadeIn
```

### 3. Scale In (Grows)
```
animation=scaleIn
```

### 4. Blink
```
animation=blinking
```

### 5. No Animation
```
Don't include animation parameter
```

---

## 🎨 Color Customization

### Gradient (Current)
```
color=0:8B4513,50:D2691E,100:DEB887
```
Format: `position:HexColor`

### Single Color
```
color=8B4513
```

### Preset Gradients
```
color=gradient
```
Rainbow gradient

### Time-Based Gradient
```
color=timeGradient
```
Changes based on time of day!

### Random Gradient
```
color=random
```
Random gradient each time

---

## 🔤 Text Customization

### Font Color
```
fontColor=F5F5DC
```

### Font Size
```
fontSize=90  (default 70)
```

### Font Alignment (Vertical)
```
fontAlignY=45  (0-100, percentage from top)
```

### Font Alignment (Horizontal)
```
fontAlign=50  (0-100, center is 50)
```

### Description/Subtitle
```
desc=Code.%20Create.%20Conquer.
descSize=28
descAlignY=65
descAlign=50
```

### Font Options
```
fontType=impact
```
Options: `impact`, `serif`, `palatino`, `comic`, `times`, `georgia`, `trebuchet`, `verdana`, `monaco`, `courier`

---

## 🎯 Advanced Effects

### Stroke (Text Outline)
```
stroke=000000
strokeWidth=2
```

### Rotate Text
```
rotate=15  (degrees, -360 to 360)
```

### Reversal (Flip Shape)
```
reversal=true
```
Flips the wave upside down

### Height
```
height=250  (pixels)
```

### Custom Color List
```
customColorList=0,2,5,8,12,15
```
Pick specific colors from palette (0-29)

---

## 🌟 Cool Combinations for Western Theme

### 1. Desert Sunset Cylinder
```
type=cylinder&color=0:8B4513,50:D2691E,100:F4A460&height=200&text=rundowntown&fontSize=80&fontColor=FFF&animation=scaleIn
```

### 2. Sharp Sheriff Star
```
type=shark&color=0:2F4F4F,50:8B4513,100:CD853F&height=250&text=rundowntown&fontSize=90&fontColor=FFD700&stroke=000000&strokeWidth=2&animation=fadeIn
```

### 3. Rustic Venom Style
```
type=venom&color=gradient&customColorList=24,25,26,27&height=300&text=rundowntown&fontSize=100&fontColor=F5DEB3&animation=twinkling
```

### 4. Time-Based (Changes Throughout Day)
```
type=waving&color=timeGradient&height=250&text=rundowntown&fontSize=90&fontColor=FFF&animation=fadeIn
```

### 5. Soft Leather Look
```
type=soft&color=0:654321,50:8B4513,100:A0522D&height=220&text=rundowntown&fontSize=85&fontColor=FAEBD7&fontType=impact
```

---

## 🚀 How to Use

Just replace the URL in your README.md line 8:

```markdown
![Wave Overlay](https://capsule-render.vercel.app/api?PARAMETERS_HERE)
```

Mix and match parameters with `&` between them!

Example:
```
https://capsule-render.vercel.app/api?type=cylinder&color=0:8B4513,100:DEB887&height=250&text=rundowntown&fontSize=90&fontColor=F5F5DC&animation=scaleIn&stroke=000000&strokeWidth=1
```

---

## 💡 Pro Tips

1. **For Western Theme**: Use browns, oranges, golds, dark grays
2. **Text Contrast**: Dark background = light text, light background = dark text
3. **Stroke**: Add black stroke for better text readability
4. **Height**: 200-300px works best for banners
5. **Animation**: `fadeIn` or `scaleIn` are most noticeable

---

Play around and find your perfect look! 🤠

