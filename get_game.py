from getscreennew import getpicture
from argsolver import args
from logger import logger
import matplotlib.pyplot as plt
import cv2
def get_GAME(gamename="MONSTER HUNTER STORIES 2: WINGS OF RUIN"):
    FULLRES = [args.width, args.height]
    logger.info(FULLRES)
    mode=args.mode
    if args.mode in ["window",'borderless']:
        mode=args.mode+"_PIL"
    img = getpicture(gamename, mode=mode, FULLRES=FULLRES)
    return img

if __name__=="__main__":
    img=get_GAME()
    plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
    plt.show()