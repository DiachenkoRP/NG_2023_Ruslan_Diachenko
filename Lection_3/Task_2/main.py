# Print bloks
voidBlock = " "
solidBlock = "\u2588"   # u2588 - solid

# Recursion who draw romb
def drawRomb(height = 1, width = 1):
    print(voidBlock * height+ solidBlock * width + solidBlock * width+ voidBlock * height)
    if height > 1:
        drawRomb(height-1, width+1)
    print(voidBlock * height + solidBlock * width + solidBlock * width + voidBlock * height)

# Main
drawRomb(15)

# Intresting fact, drawed romb looks like a simple romb if WIDTH value = 1
#  But if edit width, It looks like zoom(if width < 1, romb distance high, if width>1 romb distance low, go to romb) :)


