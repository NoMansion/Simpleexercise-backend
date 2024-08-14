from exercise import Exercise
from workout import Workout

leg_exercises = []
chest_exercises = []
back_exercises = []
shoulder_exercises = []
arm_exercises = []
cardio_exercises = []

def create_exercise_pools():
    leg_exercises.append(Exercise('Barbell Squat', 15, 4, 4,))
    leg_exercises.append(Exercise('Standing Calf Raise', 15, 15, 3))
    leg_exercises.append(Exercise('Seated Leg Curl', 15, 15, 3))
    leg_exercises.append(Exercise('Leg Extension', 15, 12, 2))
    leg_exercises.append(Exercise('Lunges', 20, 20, 4))

    chest_exercises.append(Exercise('Barbell Incline Bench Press', 25, 5, 5))
    chest_exercises.append(Exercise('Chest Dips', 15, 6, 4))
    chest_exercises.append(Exercise('Flat Bench Dumbbell Press', 15, 8, 3))
    chest_exercises.append(Exercise('Cable Fly', 15, 8, 4))
    chest_exercises.append(Exercise('Dumbbell Pullover', 15, 8, 3))

    back_exercises.append(Exercise('Chin-ups', 15, 6, 4))
    back_exercises.append(Exercise('Lat Pulldown', 10, 8, 3))
    back_exercises.append(Exercise('Single Arm Dumbbell Row', 20, 7, 3))
    back_exercises.append(Exercise('Face Pull', 15, 12, 3))
    back_exercises.append(Exercise('T Bar Rows', 15, 4, 4))

    shoulder_exercises.append(Exercise('Seated Dumbbell Shoulder Press', 15, 7, 4))
    shoulder_exercises.append(Exercise('Barbell Upright Row', 15, 8, 3))
    shoulder_exercises.append(Exercise('Seated Rear Delt Fly', 15, 10, 3))
    shoulder_exercises.append(Exercise('Side Lateral Raise', 10, 10, 3))
    shoulder_exercises.append(Exercise('Overhead Bar Front Raise', 15, 10, 3))

    arm_exercises.append(Exercise('Close Grip Bench Press', 15, 6, 3))
    arm_exercises.append(Exercise('Triceps Extension', 10, 10, 2))
    arm_exercises.append(Exercise('Bicep Curls', 15, 8, 3))
    arm_exercises.append(Exercise('Low Cable Overhead Triceps Extension', 15, 15, 3))
    arm_exercises.append(Exercise('Palms-down Wrist Curl Over Bench', 20, 25, 3))

    cardio_exercises.append(Exercise('Running', 30, 1, 1))
    cardio_exercises.append(Exercise('Burpees', 15, 10, 3))
    cardio_exercises.append(Exercise('Cycling', 30, 1, 1))
    cardio_exercises.append(Exercise('Jumprope', 20, 50, 3))
    cardio_exercises.append(Exercise('Jumping Jacks', 20, 25, 3))

def check_time(exercises: list, length: int):
    total_time = 0
    for e in exercises:
        total_time += e.length
    return total_time >= length

def create_exercise_day(workout_exercises, workout_counter, c_length, length):
    
    list_of_exercises = []
    while not check_time(list_of_exercises, length):
        list_of_exercises.append(workout_exercises[workout_counter])
        workout_counter += 1
        if workout_counter > c_length:
            workout_counter = 0
    return Workout(list_of_exercises)

def create_gen_day_no_legs(chest_exercises, back_exercises, shoulder_exercises, arm_exercises, cardio_exercises, counter, c_length, length):
    list_of_exercises = []
    while counter <= c_length:
        list_of_exercises.append(chest_exercises[counter])
        if check_time(list_of_exercises, length):
            counter += 1
            break
        list_of_exercises.append(back_exercises[counter])
        if check_time(list_of_exercises, length):
            counter += 1
            break
        list_of_exercises.append(shoulder_exercises[counter])
        if check_time(list_of_exercises, length):
            counter += 1
            break
        list_of_exercises.append(arm_exercises[counter])
        if check_time(list_of_exercises, length):
            counter += 1
            break
        list_of_exercises.append(cardio_exercises[counter])
        if check_time(list_of_exercises, length):
            counter += 1
            break
        counter += 1
        if counter > c_length:
            counter = 0
    return Workout(list_of_exercises)

def create_gen_day_with_legs(chest_exercises, back_exercises, shoulder_exercises, arm_exercises, cardio_exercises, counter, c_length, length):
    list_of_exercises = []
    while counter <= c_length:
        list_of_exercises.append(leg_exercises[counter])
        if check_time(list_of_exercises, length):
            counter += 1
            break
        list_of_exercises.append(chest_exercises[counter])
        if check_time(list_of_exercises, length):
            counter += 1
            break
        list_of_exercises.append(back_exercises[counter])
        if check_time(list_of_exercises, length):
            counter += 1
            break
        list_of_exercises.append(shoulder_exercises[counter])
        if check_time(list_of_exercises, length):
            counter += 1
            break
        list_of_exercises.append(arm_exercises[counter])
        if check_time(list_of_exercises, length):
            counter += 1
            break
        list_of_exercises.append(cardio_exercises[counter])
        if check_time(list_of_exercises, length):
            counter += 1
            break
        counter += 1
        if counter > c_length:
            counter = 0
    return Workout(list_of_exercises)

def create_two_in_one_day(workout1_exercises, workout1_counter, workout2_exercises, workout2_counter, c_length, length):
    list_of_exercises = []
    while not check_time(list_of_exercises, length):
        list_of_exercises.append(workout1_exercises[workout1_counter])
        workout1_counter += 1
        list_of_exercises.append(workout2_exercises[workout2_counter])
        workout2_counter += 1
        if workout1_counter > c_length:
            workout1_counter = 0
        if workout2_counter > c_length:
            workout2_counter = 0
    return Workout(list_of_exercises)

def create_weekly_plan(num_days, specificity, leg_focus, length):
    workouts = [None] * 7
    counter = 0
    leg_counter = 0
    chest_counter = 0
    back_counter = 0
    shoulder_counter = 0
    arm_counter = 0
    c_length = len(cardio_exercises) - 1
    cardio_counter = 0

    if num_days == 1:
        if specificity != "Very general" and leg_focus:
            workouts[0] = create_exercise_day(leg_exercises, leg_counter, c_length, length)
        else:
            workouts[0] = create_gen_day_with_legs(chest_exercises, back_exercises, shoulder_exercises, arm_exercises, cardio_exercises, counter, c_length, length)

    if num_days == 2:
        if (specificity == 'Very specific' or specificity == 'Somewhat specific') and leg_focus:
            workouts[0] = create_exercise_day(leg_exercises, leg_counter, c_length, length)
            workouts[1] = create_exercise_day(leg_exercises, leg_counter, c_length, length)
        else:
            workouts[0] = create_gen_day_with_legs(chest_exercises, back_exercises, shoulder_exercises, arm_exercises, cardio_exercises, counter, c_length, length)
            workouts[1] = create_gen_day_with_legs(chest_exercises, back_exercises, shoulder_exercises, arm_exercises, cardio_exercises, counter, c_length, length)

    if num_days == 3:
        if specificity == 'Very specific' and leg_focus:
            workouts[0] = create_exercise_day(leg_exercises, leg_counter, c_length, length)
            workouts[1] = create_exercise_day(leg_exercises, leg_counter, c_length, length)
            workouts[2] = create_exercise_day(leg_exercises, leg_counter, c_length, length)
        elif specificity == 'Somewhat specific' and leg_focus:
            workouts[0] = create_exercise_day(leg_exercises, leg_counter, c_length, length)
            workouts[1] = create_exercise_day(leg_exercises, leg_counter, c_length, length)
            workouts[2] = create_gen_day_no_legs(chest_exercises, back_exercises, shoulder_exercises, arm_exercises, cardio_exercises, counter, c_length, length)
        else:
            workouts[0] = create_gen_day_with_legs(chest_exercises, back_exercises, shoulder_exercises, arm_exercises, cardio_exercises, counter, c_length, length)
            workouts[1] = create_gen_day_with_legs(chest_exercises, back_exercises, shoulder_exercises, arm_exercises, cardio_exercises, counter, c_length, length)
            workouts[2] = create_gen_day_with_legs(chest_exercises, back_exercises, shoulder_exercises, arm_exercises, cardio_exercises, counter, c_length, length)

    if num_days == 4:
        if specificity == 'Very specific' and leg_focus:
            workouts[0] = create_exercise_day(leg_exercises, leg_counter, c_length, length)
            workouts[1] = create_exercise_day(leg_exercises, leg_counter, c_length, length)
            workouts[2] = create_exercise_day(leg_exercises, leg_counter, c_length, length)
            workouts[3] = create_exercise_day(leg_exercises, leg_counter, c_length, length)
        elif specificity == 'Somewhat specific' and leg_focus:
            workouts[0] = create_exercise_day(leg_exercises, leg_counter, c_length, length)
            workouts[1] = create_exercise_day(leg_exercises, leg_counter, c_length, length)
            workouts[2] = create_gen_day_no_legs(chest_exercises, back_exercises, shoulder_exercises, arm_exercises, cardio_exercises, counter, c_length, length)
            workouts[3] = create_gen_day_no_legs(chest_exercises, back_exercises, shoulder_exercises, arm_exercises, cardio_exercises, counter, c_length, length)
        else:
            workouts[0] = create_gen_day_with_legs(chest_exercises, back_exercises, shoulder_exercises, arm_exercises, cardio_exercises, counter, c_length, length)
            workouts[1] = create_gen_day_with_legs(chest_exercises, back_exercises, shoulder_exercises, arm_exercises, cardio_exercises, counter, c_length, length)
            workouts[2] = create_gen_day_with_legs(chest_exercises, back_exercises, shoulder_exercises, arm_exercises, cardio_exercises, counter, c_length, length)
            workouts[3] = create_gen_day_with_legs(chest_exercises, back_exercises, shoulder_exercises, arm_exercises, cardio_exercises, counter, c_length, length)

    if num_days == 5:
        if specificity == 'Very specific' and leg_focus:
            workouts[0] = create_exercise_day(leg_exercises, leg_counter, c_length, length)
            workouts[1] = create_exercise_day(leg_exercises, leg_counter, c_length, length)
            workouts[2] = create_exercise_day(leg_exercises, leg_counter, c_length, length)
            workouts[3] = create_exercise_day(leg_exercises, leg_counter, c_length, length)
            workouts[4] = create_exercise_day(leg_exercises, leg_counter, c_length, length)
        elif specificity == 'Somewhat specific' and leg_focus:
            workouts[0] = create_exercise_day(leg_exercises, leg_counter, c_length, length)
            workouts[1] = create_exercise_day(leg_exercises, leg_counter, c_length, length)
            workouts[2] = create_gen_day_no_legs(chest_exercises, back_exercises, shoulder_exercises, arm_exercises, cardio_exercises, counter, c_length, length)
            workouts[3] = create_gen_day_no_legs(chest_exercises, back_exercises, shoulder_exercises, arm_exercises, cardio_exercises, counter, c_length, length)
            workouts[4] = create_gen_day_no_legs(chest_exercises, back_exercises, shoulder_exercises, arm_exercises, cardio_exercises, counter, c_length, length)
        else:
            workouts[0] = create_gen_day_with_legs(chest_exercises, back_exercises, shoulder_exercises, arm_exercises, cardio_exercises, counter, c_length, length)
            workouts[1] = create_gen_day_with_legs(chest_exercises, back_exercises, shoulder_exercises, arm_exercises, cardio_exercises, counter, c_length, length)
            workouts[2] = create_gen_day_with_legs(chest_exercises, back_exercises, shoulder_exercises, arm_exercises, cardio_exercises, counter, c_length, length)
            workouts[3] = create_gen_day_with_legs(chest_exercises, back_exercises, shoulder_exercises, arm_exercises, cardio_exercises, counter, c_length, length)
            workouts[4] = create_gen_day_with_legs(chest_exercises, back_exercises, shoulder_exercises, arm_exercises, cardio_exercises, counter, c_length, length)

    if num_days == 6:
        if specificity == 'Very specific' and leg_focus:
            workouts[0] = create_exercise_day(leg_exercises, leg_counter, c_length, length)
            workouts[1] = create_exercise_day(leg_exercises, leg_counter, c_length, length)
            workouts[2] = create_exercise_day(leg_exercises, leg_counter, c_length, length)
            workouts[3] = create_exercise_day(leg_exercises, leg_counter, c_length, length)
            workouts[4] = create_exercise_day(leg_exercises, leg_counter, c_length, length)
            workouts[5] = create_exercise_day(leg_exercises, leg_counter, c_length, length)
        elif specificity == 'Somewhat specific' and leg_focus:
            workouts[0] = create_exercise_day(leg_exercises, leg_counter, c_length, length)
            workouts[1] = create_exercise_day(leg_exercises, leg_counter, c_length, length)
            workouts[2] = create_gen_day_no_legs(chest_exercises, back_exercises, shoulder_exercises, arm_exercises, cardio_exercises, counter, c_length, length)
            workouts[3] = create_gen_day_no_legs(chest_exercises, back_exercises, shoulder_exercises, arm_exercises, cardio_exercises, counter, c_length, length)
            workouts[4] = create_gen_day_no_legs(chest_exercises, back_exercises, shoulder_exercises, arm_exercises, cardio_exercises, counter, c_length, length)
            workouts[5] = create_gen_day_no_legs(chest_exercises, back_exercises, shoulder_exercises, arm_exercises, cardio_exercises, counter, c_length, length)
        else:
            workouts[0] = create_gen_day_with_legs(chest_exercises, back_exercises, shoulder_exercises, arm_exercises, cardio_exercises, counter, c_length, length)
            workouts[1] = create_gen_day_with_legs(chest_exercises, back_exercises, shoulder_exercises, arm_exercises, cardio_exercises, counter, c_length, length)
            workouts[2] = create_gen_day_with_legs(chest_exercises, back_exercises, shoulder_exercises, arm_exercises, cardio_exercises, counter, c_length, length)
            workouts[3] = create_gen_day_with_legs(chest_exercises, back_exercises, shoulder_exercises, arm_exercises, cardio_exercises, counter, c_length, length)
            workouts[4] = create_gen_day_with_legs(chest_exercises, back_exercises, shoulder_exercises, arm_exercises, cardio_exercises, counter, c_length, length)
            workouts[5] = create_gen_day_with_legs(chest_exercises, back_exercises, shoulder_exercises, arm_exercises, cardio_exercises, counter, c_length, length)

    if num_days == 7:
        if specificity == 'Very specific' and leg_focus:
            workouts[0] = create_exercise_day(leg_exercises, leg_counter, c_length, length)
            workouts[1] = create_exercise_day(leg_exercises, leg_counter, c_length, length)
            workouts[2] = create_exercise_day(leg_exercises, leg_counter, c_length, length)
            workouts[3] = create_exercise_day(leg_exercises, leg_counter, c_length, length)
            workouts[4] = create_gen_day_no_legs(chest_exercises, back_exercises, shoulder_exercises, arm_exercises, cardio_exercises, counter, c_length, length)
            workouts[5] = create_gen_day_no_legs(chest_exercises, back_exercises, shoulder_exercises, arm_exercises, cardio_exercises, counter, c_length, length)
            workouts[6] = create_gen_day_no_legs(chest_exercises, back_exercises, shoulder_exercises, arm_exercises, cardio_exercises, counter, c_length, length)
        elif specificity == 'Somewhat specific' and leg_focus:
            workouts[0] = create_exercise_day(leg_exercises, leg_counter, c_length, length)
            workouts[1] = create_exercise_day(leg_exercises, leg_counter, c_length, length)
            workouts[2] = create_gen_day_no_legs(chest_exercises, back_exercises, shoulder_exercises, arm_exercises, cardio_exercises, counter, c_length, length)
            workouts[3] = create_gen_day_no_legs(chest_exercises, back_exercises, shoulder_exercises, arm_exercises, cardio_exercises, counter, c_length, length)
            workouts[4] = create_gen_day_no_legs(chest_exercises, back_exercises, shoulder_exercises, arm_exercises, cardio_exercises, counter, c_length, length)
            workouts[5] = create_gen_day_no_legs(chest_exercises, back_exercises, shoulder_exercises, arm_exercises, cardio_exercises, counter, c_length, length)
            workouts[6] = create_gen_day_no_legs(chest_exercises, back_exercises, shoulder_exercises, arm_exercises, cardio_exercises, counter, c_length, length)
        else:
            workouts[0] = create_gen_day_with_legs(chest_exercises, back_exercises, shoulder_exercises, arm_exercises, cardio_exercises, counter, c_length, length)
            workouts[1] = create_gen_day_with_legs(chest_exercises, back_exercises, shoulder_exercises, arm_exercises, cardio_exercises, counter, c_length, length)
            workouts[2] = create_gen_day_with_legs(chest_exercises, back_exercises, shoulder_exercises, arm_exercises, cardio_exercises, counter, c_length, length)
            workouts[3] = create_gen_day_with_legs(chest_exercises, back_exercises, shoulder_exercises, arm_exercises, cardio_exercises, counter, c_length, length)
            workouts[4] = create_gen_day_with_legs(chest_exercises, back_exercises, shoulder_exercises, arm_exercises, cardio_exercises, counter, c_length, length)
            workouts[5] = create_gen_day_with_legs(chest_exercises, back_exercises, shoulder_exercises, arm_exercises, cardio_exercises, counter, c_length, length)
            workouts[6] = create_gen_day_with_legs(chest_exercises, back_exercises, shoulder_exercises, arm_exercises, cardio_exercises, counter, c_length, length)

    result = ""
    days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    for i in range(0,7):
        if (workouts[i] == None):
            result += f"{days_of_week[i]}:\n Rest day\n\n"
        else:
            result += f"{days_of_week[i]}:\n {workouts[i]}\n"

    return result

