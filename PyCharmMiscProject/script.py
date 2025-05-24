import face_recognition
ryan = face_recognition.load_image_file("ryan.jpg")
harrison = face_recognition.load_image_file("ford.jpg")
bladerunner_old = face_recognition.load_image_file("brold.jpg")
bladerunner_new = face_recognition.load_image_file("brnew.jpg")

ryan_encoding = face_recognition.face_encodings(ryan)[0]
harrison_encoding = face_recognition.face_encodings(harrison)[0]
bladerunner_new_encoding = face_recognition.face_encodings(bladerunner_new)[0]
bladerunner_old_encoding = face_recognition.face_encodings(bladerunner_old)[0]

ryan1 = face_recognition.compare_faces([ryan_encoding], bladerunner_old_encoding)
harrison1 = face_recognition.compare_faces([harrison_encoding], bladerunner_old_encoding)
ryan2 = face_recognition.compare_faces([ryan_encoding], bladerunner_new_encoding)
harrison2 = face_recognition.compare_faces([harrison_encoding], bladerunner_new_encoding)
print(ryan1, harrison1, ryan2, harrison2)