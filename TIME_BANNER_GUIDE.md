# 🌅 Time-Based Banner System - How It Works

## What You Just Got! 🎉

Your GitHub profile now has an **auto-updating banner** that changes based on the time of day with **sun/moon positioning**!

## Features ✨

### 🌞 Time Periods
Your banner automatically switches between 4 periods:

1. **DAWN (5am-10am)**
   - ☀️ Emoji
   - Sun rises from left to center
   - Orange/pink sunrise colors
   
2. **NOON (10am-4pm)**
   - ☀️ Emoji  
   - Sun at top center
   - Bright desert gold colors
   
3. **DUSK (4pm-8pm)**
   - 🌅 Emoji
   - Sun sets from center to right
   - Deep orange/brown sunset colors
   
4. **NIGHT (8pm-5am)**
   - 🌙 Emoji
   - Moon on the right
   - Dark gray/brown nighttime colors

### 🎨 Features
- **Sun/Moon icon** actually positioned based on time progression
- **Custom Western color gradients** for each time period
- **Your cowboys.jpg as background** (blended with time-of-day overlay)
- **Emoji in text** (☀️/🌙 rundowntown)
- **Auto-updates every 3 hours** via GitHub Actions

## How to Activate 🚀

### Step 1: Push Everything to GitHub
```bash
git add .
git commit -m "Add time-based auto-updating banner system"
git push
```

### Step 2: Enable GitHub Actions
1. Go to your repo: `https://github.com/rundowntown/rundowntown`
2. Click **"Actions"** tab
3. If prompted, click **"I understand my workflows, go ahead and enable them"**
4. You should see "Update Time-Based Banner" workflow

### Step 3: Run It Manually (First Time)
1. In Actions tab, click **"Update Time-Based Banner"**
2. Click **"Run workflow"** → **"Run workflow"** button
3. Wait ~30 seconds
4. Check your profile - banner should update!

### Step 4: Enjoy! 
From now on, it updates automatically every 3 hours! 🎉

## Files Created 📁

### `generate_time_banner.py`
The Python script that:
- Detects current time
- Loads cowboys.jpg background
- Adds time-appropriate gradient overlay
- Draws sun/moon icon at correct position
- Adds "rundowntown" text with emoji
- Saves as `current_banner.jpg`

### `.github/workflows/update-banner.yml`
GitHub Action that:
- Runs every 3 hours (cron: `0 */3 * * *`)
- Executes the Python script
- Commits new banner
- Pushes to GitHub

### `current_banner.jpg`
The generated banner (auto-created and updated)

## Customization 🎨

### Change Update Frequency
Edit `.github/workflows/update-banner.yml` line 5:
```yaml
- cron: '0 */3 * * *'  # Every 3 hours
- cron: '0 */6 * * *'  # Every 6 hours
- cron: '0 */1 * * *'  # Every hour
```

### Change Colors
Edit `generate_time_banner.py` function `get_colors_for_period()`:
```python
colors = {
    "dawn": [(255, 107, 53), (247, 147, 30), (253, 200, 48)],  # Change these RGB values
    "noon": [(222, 184, 135), (218, 165, 32), (255, 215, 0)],
    "dusk": [(139, 69, 19), (210, 105, 30), (222, 184, 135)],
    "night": [(47, 79, 79), (105, 105, 105), (139, 69, 19)]
}
```

### Change Time Periods
Edit `get_time_period()` function:
```python
if 5 <= hour < 10:    # Change these hour ranges
    return "dawn", "☀️", (hour - 5) / 5
elif 10 <= hour < 16:
    return "noon", "☀️", 1.0
# etc...
```

### Change Timezone
Edit line 21:
```python
now = datetime.now(pytz.UTC)  # Change UTC to your timezone
# Examples:
# now = datetime.now(pytz.timezone('America/New_York'))
# now = datetime.now(pytz.timezone('America/Los_Angeles'))
# now = datetime.now(pytz.timezone('Europe/London'))
```

## Troubleshooting 🔧

### Banner not updating?
1. Check Actions tab for errors
2. Make sure Actions are enabled
3. Manually trigger the workflow

### Wrong time period showing?
- Check timezone setting in script (line 21)
- GitHub Actions run on UTC time by default

### Want to test different times?
Run manually:
```bash
python generate_time_banner.py
```
Then check `current_banner.jpg`

## How It Looks 👀

- **Dawn**: Sun rising on left, warm orange glow
- **Noon**: Bright sun at top, golden desert vibes
- **Dusk**: Sun setting on right, brown/orange sunset
- **Night**: Crescent moon on right, dark mysterious vibe

All with your cowboys.jpg background blended underneath! 🤠

## Pro Tips 💡

1. **First push**: The banner shows current time when you commit it
2. **Auto-updates**: Happens in background every 3 hours
3. **Manual trigger**: Use Actions tab to force update anytime
4. **Test locally**: Run the Python script to preview
5. **Customize**: Change colors, times, emojis - it's all yours!

---

Enjoy your dynamic Western-themed profile! 🌅🤠🌙

