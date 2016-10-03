from PIL import Image, ImageDraw

def getDifference(src1, src2):
    img1 = Image.open(src1) # pic 1
    img2 = Image.open(src2) # pic 2
    ANS = Image.open(src1) # result
    draw = ImageDraw.Draw(ANS)
    pix1 = img1.load()
    pix2 = img2.load()
    width = min(img1.size[0], img2.size[0])
    height = min(img1.size[1], img2.size[1])
    eps = 30
    for i in range(width):
        for j in range(height):
            dx1 = pix1[i, j][0] - pix2[i, j][0]
            dx2 = pix1[i, j][1] - pix2[i, j][1]
            dx3 = pix1[i, j][2] - pix2[i, j][2]
            draw.point((i, j),
                       (abs(dx1), abs(dx2), abs(dx3)))  # drawing difference
    ANS.save("ans.jpg", "JPEG")
    del draw


getDifference('img1.jpg', 'img2.jpg')
