import time
from pathlib import Path
from docutils.nodes import image

from ToolBox_Pytorch import download_model
from picamera2 import Picamera2, Preview
my_cam = Picamera2()
config = my_cam.create_preview_configuration()
my_cam.configure(config)
my_cam.start_preview(Preview.QTGL)
my_cam.start()
try:
    from ToolBox_Pytorch import download_model
except:
    import git
    git.Git('./').clone('https://github.com/vaaraaf/ToolBox_Pytorch')
    from ToolBox_Pytorch import download_model

my_model, my_transform = download_model.download_mobilenet_v2()
try:
    from laptop_webcam_movilenetV2.evaluation import evaluate_image
except:
    import git
    git.Git('./').clone('https://github.com/vaaraaf/laptop_webcam_movilenetV2')
    from laptop_webcam_movilenetV2.evaluation import evaluate_image
current_directory = Path(__file__)
parent_directory = current_directory.parent
image_directory = parent_directory / 'images'
sample_image_directory = image_directory / 'sample.jpg'
while True:
    my_cam.capture_file(sample_image_directory)
    evaluate_image(model= my_model,
                   transform= my_transform,
                   image_path = image_directory / 'sample.jpg')
    time.sleep(3)
