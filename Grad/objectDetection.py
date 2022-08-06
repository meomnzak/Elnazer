import cv2
import numpy as np

#network contain weights and configration
net = cv2.dnn.readNet('yolov3.weights','yolov3-416.cfg')
#extract object names from coco file
classes = []
with open('coco.names' , 'r')as f:
    classes = f.read().splitlines()
    

    
cap = cv2.VideoCapture(0)
#img = cv2.imread('image1.jpg')
while True:

    _, img = cap.read()
    height , width , _ = img.shape
    
    blob = cv2.dnn.blobFromImage(img , 1/255 , (416,416) , (0,0,0) , swapRB = True , crop = False)
    """
    for b in blob :
        for n  , img_blob in enumerate(b):
            cv2.imshow(str(n) , img_blob)
    """
    
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
            continue
            #cv2.rectangle(img , (x,y) , (x+w , y+h) , (255,255,255) , 2)
        cv2.putText(img , label+" "+confidence, (x,y+20) , font , 2 , (255,0,0) , 2)
    
    cv2.imshow('image', img)
    key = cv2.waitKey(1)
    if key == 27:
        break


cap.release()
cv2.destroyAllWindows() 
    
    

