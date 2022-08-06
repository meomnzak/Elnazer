<h1 align="center">Elnazer</h1>

<div align= "center"><img src="https://github.com/meomnzak/Elnazer/blob/main/Grad/captures/logo.png" width="200" height="200"/>
  <h4>By putting a camera in the exam room and by using computer vision first we make  students attendance process by face recognition and then when the exam start the system prevent students from cheating by some rules like calculating the distance between the students and see if any student turned his head and recognizing things like phones, headphones, books and other things.</h4>
</div>

<div align= "center"><img src="https://github.com/meomnzak/Elnazer/blob/main/Grad/captures/home.PNG"/></div>

## :innocent: Motivation
Professors and teaching assistant are suffering from students monitoring activities in the exam rooms which are hard, boring and time-consuming missions. So the challenge was to make a reliable system to detect cheating.


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
      <img width="607" alt="phone" src="https://github.com/meomnzak/Elnazer/blob/main/Grad/captures/phone.gif">
      
      - Using haarcascade profile classifier we detect students face turning around to cheat from their classmates.

- ### Distance
      <img width="607" alt="distance" src="https://github.com/meomnzak/Elnazer/blob/main/Grad/captures/distance.gif">
      
      - This feature uses OpenCV and YOLO to monitor/analyze whether people are maintaining enough distance between them or not.







