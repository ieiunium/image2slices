from PIL import Image, ImageDraw
import sys
import math

if __name__ == "__main__":

  if len(sys.argv) != 3:
    print """usage: python main.py format image.bla\n where format in [0,1,2,3,4]"""
    exit
  
  format = int(sys.argv[1])
  if format < 0 or format > 4:
    print """usage: python main.py format image.bla\n where format in [0,1,2,3,4]"""
    exit
  inputFileName = sys.argv[2]
  
  width = 0
  height = 0

  img = Image.open(inputFileName, 'r')
  img_w, img_h = img.size
  if img_w > img_h:
    width = img_w
    height = int(width * math.sqrt(2))
    pass;
  else:
    height = img_h
    width = int(height / math.sqrt(2))
    pass;

  background = Image.new('RGBA', (width, height), (255, 255, 255, 255))
  bg_w, bg_h = background.size
  offset = ((bg_w - img_w) / 2, (bg_h - img_h) / 2)
  background.paste(img, offset)

  format_cells = ((4,4),(2,4),(2,2),(1,2),(1,1))
  imgDrawer = ImageDraw.Draw(background)
  hlines = format_cells[format][0]
  vlines = format_cells[format][1]
  hd = int(width / hlines)
  vd = int(height / vlines)
  for i in range(hlines):
    for j in range(vlines):
      img1 = background.crop((i * hd, j * vd) + ( (i+1) * hd, (j+1) * vd))
      img1.save(inputFileName + str(i) + 'x'+ str(j) + '.png')
      pass;














