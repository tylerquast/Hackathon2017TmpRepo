from PIL import Image as PIL_Image

orig_img_path = '/home/xilinx/jupyter_notebooks/common/data/webcam.jpg'
!fswebcam  --no-banner --save {orig_img_path} -d /dev/video0 2> orig_img_path

img = PIL_Image.open(orig_img_path)
img
