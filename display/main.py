import pyzed.sl as sl
import cv2

# Create a Camera object
zed = sl.Camera()

# Create a InitParameters object and set configuration parameters
init_params = sl.InitParameters()
init_params.depth_mode = sl.DEPTH_MODE.PERFORMANCE
init_params.coordinate_units = sl.UNIT.METER
init_params.sdk_verbose = 1

# Open the camera
err = zed.open(init_params)
if err != sl.ERROR_CODE.SUCCESS:
    exit(1)

while True:
    if zed.grab() == sl.ERROR_CODE.SUCCESS:
        left_image = sl.Mat()
        zed.retrieve_image(left_image, sl.VIEW.LEFT)

        frame = left_image.get_data()

        cv2.imshow("Camera", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

zed.close()
cv2.destroyAllWindows()
