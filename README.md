# Simplexercise (backend)
## Video overview
[Video Overview](https://www.youtube.com/watch?v=9Y1FDvHgPsU)

## Part 1: Django REST Framework
- Sets up models for notes, which are used to carry information for a specific request for a workout plan.
- Configures the webserver to enable the app to send and receive data.
- Connects to a PostgreSQL database.

## Part 2: Processing
- Receives a video from the app and analyzes the average angle of the knees to assess proper squat form. Uses OpenCV and OpenPose/
- Generates a workout plan for the user based on the video data and survey answers from the app.
- Updates the Note with the generated workout plan.
