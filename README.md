<h1 align="center">Elnazer</h1>

<div align= "center"><img src="https://github.com/meomnzak/Elnazer/blob/main/Grad/captures/logo.png" width="200" height="200"/>
  <h4>By putting a camera in the exam room and by using computer vision first we make  students attendance process by face recognition and then when the exam start the system prevent students from cheating by some rules like calculating the distance between the students and see if any student turned his head and recognizing things like phones, headphones, books and other things.</h4>
</div>

<div align= "center"><img src="https://github.com/meomnzak/Elnazer/blob/main/Grad/captures/home.PNG"/></div>

## :innocent: Motivation
Professors and teaching assistant are suffering from students monitoring activities in the exam rooms which are hard, boring and time-consuming missions. So the challenge was to make a reliable system to detect cheating.

## :warning: TechStack/framework used
- [Python](https://www.python.org/)
- [OpenCV](https://opencv.org/)
- [YOLO](https://pjreddie.com/darknet/yolo/)
- [Keras](https://keras.io/)
- [TensorFlow](https://www.tensorflow.org/)
- [MobileNetV2](https://arxiv.org/abs/1801.04381)

## :star: Features
 - ### Attendance
      <img width="607" alt="attendace" src="https://github.com/meomnzak/Elnazer/blob/main/Grad/captures/attendance.gif">
      
      - Take pictures for every student and encode all the images to recognize the faces of students and mark them as attended. We use an Algorithm called haarcascade classifier that used to identify and detect faces in images or real time videos.

      
 - ### Mask detection
      <img width="607" alt="mask" src="https://github.com/meomnzak/Elnazer/blob/main/Grad/captures/mask.gif">
      
      - As a requirment for exams on these days all the students must wear masks so we built a Face Mask Detection System with OpenCV, Keras, and TensorFlow using Deep Learning and Computer Vision concepts in order to detect masks on real-time video streams.
 
 - ### Detect books and cell phones
      <img width="607" alt="book" src="https://github.com/meomnzak/Elnazer/blob/main/Grad/captures/book.gif">
      <img width="607" alt="phone" src="https://github.com/meomnzak/Elnazer/blob/main/Grad/captures/phone.gif">
      
      - Using a pre trained model called Yolo3 and a dataset called coco we detect the books and cell phones with students in exam halls and mark them as cheaters.

 - ### Turning around
      <img width="607" alt="turning" src="https://github.com/meomnzak/Elnazer/blob/main/Grad/captures/turning.gif">
      
     - Using haarcascade profile classifier we detect students face turning around to cheat from their classmates.

 - ### Distance
      <img width="607" alt="distance" src="https://github.com/meomnzak/Elnazer/blob/main/Grad/captures/distance.gif">
      
     - This feature uses OpenCV and YOLO to monitor/analyze whether students are maintaining enough distance between them or not. 


## 🚀&nbsp; Installation
1. Clone the repo
```
$ git clone https://github.com/meomnzak/Elnazer.git
```

2. Change your directory to the cloned repo 
```
$ cd Face-Mask-Detection/Grad
```

3. Then download the YOLOv3 weights from this <a href="https://pjreddie.com/media/files/yolov3.weights">link</a> and store it as <b>yolov3.weights</b>

4. Download the required python packages
```bash
pip install -r requirements.txt
```

5. Run the main.py file
```bash
python main.py
```

## Contributors
<table>
  <tr>
    <td align="center"><img src="https://github.com/meomnzak/Elnazer/blob/main/Grad/captures/MoamenProfile.jpg" width="100px;" height="100px;" alt=""/><br/><sub><b>Moamen Zakaria</b></sub></a><br/><p align="center">
      <p align="center">
        <a href="www.linkedin.com/in/moamen-zakaria-465543177" alt="Linkedin">
          <img src="http://www.iconninja.com/files/863/607/751/network-linkedin-social-connection-circular-circle-media-icon.svg" width = "30">
        </a>
        <a href="https://github.com/meomnzak" alt="Github">
          <img src="http://www.iconninja.com/files/241/825/211/round-collaboration-social-github-code-circle-network-icon.svg" width = "30">
        </a>
      </p>
    </td>
    <td align="center"><img src="https://github.com/meomnzak/Elnazer/blob/main/Grad/captures/nour.jpg" width="100px;" height="100px;" alt=""/><br/><sub><b>Nour El-Din Atalla</b></sub></a><br/><p align="center">
      <p align="center">
        <a href="https://www.linkedin.com/in/nour-el-din-atalla-6a9939247" alt="Linkedin">
          <img src="http://www.iconninja.com/files/863/607/751/network-linkedin-social-connection-circular-circle-media-icon.svg" width = "30">
        </a>
        <a href=https://github.com/nouratalla" alt="Github">
          <img src="http://www.iconninja.com/files/241/825/211/round-collaboration-social-github-code-circle-network-icon.svg" width = "30">
        </a>
      </p>
    </td>
  </tr>
</table>



