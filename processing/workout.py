class Workout:
    def total_time(self):
        result = 0
        for exercise in self.list_of_exercises:
            result += exercise.length
        return result   
    
    def __init__(self, list_of_exercises):
        self.list_of_exercises = []
        for e in list_of_exercises:
            self.list_of_exercises.append(e)

    def __str__(self):
        result = ""
        for exercise in self.list_of_exercises:
            result += f"{exercise}\n"
        result += f"Total time: {self.total_time()} minutes\n"
        return result

    