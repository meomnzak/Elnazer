import cv2
import numpy as np
from scipy.spatial import distance as dist


MODEL_PATH = "yolo-coco"

MIN_CONF = 0.3
NMS_THRESH = 0.3

USE_GPU = False

MIN_DISTANCE = 250




def detect_people(frame, net, ln, personIdx=0):
	(H, W) = frame.shape[:2]
	results = []


	blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (416, 416),
		swapRB=True, crop=False)
	net.setInput(blob)
	layerOutputs = net.forward(ln)

	boxes = []
	centroids = []
	confidences = []
	for output in layerOutputs:

		for detection in output:
			
			scores = detection[5:]
			classID = np.argmax(scores)
			confidence = scores[classID]

		
			if classID == personIdx and confidence > MIN_CONF:
			
				box = detection[0:4] * np.array([W, H, W, H])
				(centerX, centerY, width, height) = box.astype("int")

				x = int(centerX - (width / 2))
				y = int(centerY - (height / 2))

			
				boxes.append([x, y, int(width), int(height)])
				centroids.append((centerX, centerY))
				confidences.append(float(confidence))


	idxs = cv2.dnn.NMSBoxes(boxes, confidences, MIN_CONF, NMS_THRESH)

	if len(idxs) > 0:

		for i in idxs.flatten():
			(x, y) = (boxes[i][0], boxes[i][1])
			(w, h) = (boxes[i][2], boxes[i][3])


			r = (confidences[i], (x, y, x + w, y + h), centroids[i])
			results.append(r)

	return results



face_cascade = cv2.CascadeClassifier(
    'cascades/haarcascade_profileface.xml')

faceCascade2 = cv2.CascadeClassifier(
    'cascades/haarcascade_frontalface_default.xml')

#network contain weights and configration
net = cv2.dnn.readNet('yolov3.weights','yolov3-416.cfg')
#extract object names from coco file
classes = []
with open('coco.names' , 'r')as f:
    classes = f.read().splitlines()
    

ln = net.getLayerNames()
ln = [ln[i - 1] for i in net.getUnconnectedOutLayers()]

LABELS = open("coco.names").read().strip().split("\n")


camera = cv2.VideoCapture(0)
while (cv2.waitKey(1) == -1):
    success, img = camera.read()
    if success:
        results = detect_people(img, net, ln,personIdx=LABELS.index("person"))
        violate = set()
        if len(results) >= 2:
            centroids = np.array([r[2] for r in results])
            D = dist.cdist(centroids, centroids, metric="euclidean")
            for i in range(0, D.shape[0]):
                for j in range(i + 1, D.shape[1]):
                    if D[i, j] < MIN_DISTANCE:
                        violate.add(i)
                        violate.add(j)
				

    
        for (i, (prob, bbox, centroid)) in enumerate(results):
            
            (startX, startY, endX, endY) = bbox
            (cX, cY) = centroid
            color = (0, 255, 0)
            
            if i in violate:
                color = (0, 0, 255)
            
        
        cv2.rectangle(img, (startX, startY), (endX, endY), color, 2)
        cv2.circle(img, (cX, cY), 5, color, 1)
        
        text = "Distance Violations: {}".format(len(violate))
        
        cv2.putText(img, text, (10, img.shape[0] - 25),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.85, (0, 0, 255), 3)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        height , width , _ = img.shape
        blob = cv2.dnn.blobFromImage(img , 1/255 , (416,416) , (0,0,0) , swapRB = True , crop = False)
       
        net.setInput(blob)
        
        outputLayesNames = net.getUnconnectedOutLayersNames()
        layerOutputs = net.forward(outputLayesNames)
        
        
        boxes = []
        confidences = []
        
        classes_ids  = []
        
        
        for output in layerOutputs:
            for detection in output:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.1 :
                    centerX = int(detection[0]*width)
                    centerY = int(detection[1]*height)
                    w = int(detection[2]*width)
                    h = int(detection[3]*height)
                    
                    x = int(centerX - w/2)
                    y = int(centerY - h/2)
                    
                    boxes.append([x , y , w ,h ])
                    confidences.append((float (confidence)))
                    classes_ids.append(class_id)
                    
        
        
        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
        
        font =cv2.FONT_HERSHEY_PLAIN
        #colors = np.random.uniform(0 , 255 , size = (len(boxes), 3))
        
        for i  in indexes.flatten():
            x , y, w ,h  = boxes[i]
            label = str(classes[classes_ids[i]])
            confidence  = str(round(confidences[i],2))
            #color = colors[i]
            if label == 'cell phone' or label == 'book':
                cv2.rectangle(img , (x,y) , (x+w , y+h) , (0,0,255) , 2)
            else:
                cv2.rectangle(img , (x,y) , (x+w , y+h) , (255,255,255) , 2)
            cv2.putText(img , label+" "+confidence, (x,y+20) , font , 2 , (255,0,0) , 2)
        
        
        
        
        
        
        
        
  
        
        
        
        
        
        
        
        
        
        
        
        
        
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faceFront = faceCascade2.detectMultiScale(
            gray, 1.3, 5, minSize=(30, 30))
        facesL = face_cascade.detectMultiScale(
            gray, 1.3, 5, minSize=(30, 30))
        # 1 code to flip horizontaly
        flipped = cv2.flip(gray , 1)
        facesR = face_cascade.detectMultiScale(flipped , 1.3  , 5 ,  minSize=(30, 30)  )
        for (x, y, w, h) in faceFront:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            roi_gray = gray[y:y+h, x:x+w]
        for (x, y, w, h) in facesL:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
            roi_gray = gray[y:y+h, x:x+w]
        for (x, y, w, h) in facesR: 
            cv2.rectangle(img, (x+80,y), ((x+w+50), y+h), (0, 0, 255), 2)
            roi_gray = gray[y:y+h, x:x+w]
        cv2.imshow('Cam', img)
        key = cv2.waitKey(1)
        if key == 27:
            break
camera.release()
cv2.destroyAllWindows() 