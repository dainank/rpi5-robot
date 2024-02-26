# Commands

```python
from adafruit_crickit import crickit
crickit.onboard_pixel.brightness = 0.01
crickit.onboard_pixel.fill(0x0000FF)

// RGB
RGB = dict(red=0xFF0000, green=0x00FF00, blue=0x0000FF)
crickit.onboard_pixel.fill(RGB['red'])
```

