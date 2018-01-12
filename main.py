import os
from PIL import Image
import numpy,time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

need_update = True

def get_screenimage():
    os.system("adb shell screencap -p /sdcard/123/screen.png")
    os.system('adb pull /sdcard/123/screen.png F:\python凡梦\jump-weixin\image')
    return numpy.array(Image.open('image/screen.png'))

def jump_next(point1,point2):

    x1,y1 = point1;x2,y2 = point2;
    dis = ((x2-x1)**2+(y2-y1)**2)**0.5
    os.system('adb shell input swipe 320 410 320 410 {}'.format(int(dis*2)))

def upate_image(frame):
    global need_update
    if need_update:
        time.sleep(1)
        axes_image.set_array(get_screenimage())
        need_update = False
    return axes_image,

def on_calck(event,coor=[]):
    global need_update
    coor.append((event.xdata,event.ydata))
    if len(coor)==2:
        jump_next(coor.pop(),coor.pop())
    need_update = True

if __name__ =="__main__":
    figure = plt.figure()
    axes_image = plt.imshow(get_screenimage(),animated = True)#把图片划到坐标轴上
    figure.canvas.mpl_connect('button_press_event',on_calck)
    ani = FuncAnimation(figure,upate_image,interval=50,blit=True)
    plt.show()

