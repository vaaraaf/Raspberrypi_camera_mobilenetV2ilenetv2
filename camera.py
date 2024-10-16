import time
from datetime import datetime
from picamera2 import Picamera2, Preview


def take_picture():
    picam2 = Picamera2()

    preview_config = picam2.create_preview_configuration(main={'size': (800, 600)})
    picam2.configure(preview_config)

    # picam2.start_preview(Preview.QTGL)

    picam2.start()

    picam2.capture_file(f'/home/vaaraaf/PycharmProjects/just/images/sample.jpg')

    # print(f'time is {time.time()}')
    # print(f'time is {datetime.now().strftime("%Y-%m-%d")} @ {datetime.now().strftime("%H:%M:%S")}')
    picam2.close()
