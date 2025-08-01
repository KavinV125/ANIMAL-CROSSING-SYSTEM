import cv2

# ===== File paths (use raw strings to avoid escape sequence issues) =====
classFile = r'D:\Object_Detection_Files\coco1.names'
configPath = r'D:\Object_Detection_Files\yolov4-obj.cfg'
weightsPath = r'D:\Object_Detection_Files\yolov4-obj_1000.weights'

# ===== Load class names =====
classNames = []
with open(classFile, 'r') as f:
    classNames = f.read().rstrip('\n').split('\n')

# ===== Load YOLOv4 Model =====
net = cv2.dnn_DetectionModel(weightsPath, configPath)
net.setInputSize(320, 320)
net.setInputScale(1.0 / 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

# ===== Object Detection Function =====
def getObjects(img, thres, nms, draw=True, objects=[]):
    classIds, confs, bbox = net.detect(img, confThreshold=thres, nmsThreshold=nms)
    objectInfo = []

    if len(objects) == 0:
        objects = classNames

    if len(classIds) != 0:
        for classId, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):
            className = classNames[classId - 1]
            if className in objects:
                objectInfo.append([box, className])
                if draw:
                    cv2.rectangle(img, box, color=(0, 255, 0), thickness=2)
                    cv2.putText(img, className.upper(), (box[0] + 10, box[1] + 30),
                                cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                    cv2.putText(img, f'{round(confidence * 100, 2)}%', (box[0] + 200, box[1] + 30),
                                cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

    return img, objectInfo

# ===== Main Loop to Run Webcam Detection =====
if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)

    while True:
        success, img = cap.read()
        if not success:
            print("Failed to capture frame from webcam.")
            break

        result, objectInfo = getObjects(img, 0.45, 0.2)
        cv2.imshow("Output", result)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
