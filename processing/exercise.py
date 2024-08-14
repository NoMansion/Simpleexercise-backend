class Exercise:
    def __init__(self, name, length, reps, sets):
        self.name = name
        self.length = length
        self.reps = reps
        self.sets = sets
        

    def __str__(self):
        if (self.reps > 1 and self.sets > 1):
            return f"{self.name}: {self.sets} sets of {self.reps} reps. \n Estimated time: {self.length} minutes"
        elif (self.reps <= 1 and self.sets < 1):
            return f"{self.name}: {self.sets} sets of {self.reps} rep. \n Estimated time: {self.length} minutes"
        elif (self.reps > 1 and self.sets <= 1):
            return f"{self.name}: {self.sets} set of {self.reps} reps. \n Estimated time: {self.length} minutes"
        else:
            return f"{self.name}: {self.sets} set of {self.reps} rep. \n Estimated time: {self.length} minutes"
        
