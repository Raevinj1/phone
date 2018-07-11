def setup():
    size (300, 700)
    background(255, 100, 0)
    noStroke()
    img = loadImage("black-sun-with-rays_2600.png")
    x = 0
    while x < 300:
         y = 0
         x = x + 150
         while y < 700:
            image(img, x, y)
            y = y + 150
            
                
    
