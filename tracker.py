import csv
from datetime import date
from tabulate import tabulate

def workouts_log(filepath, exercise_number):
    #open the csv and update it, then print it nicely
    data = []
    with open(filepath, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["Date", "Workouts", "Set x Reps", "Weights"])
        today = date.today()
        for _ in range(exercise_number):
            workout = input("Workout: ")
            setxreps = input("Sets x reps: ")
            weights = input("Weights: ")
            #append data to list
            data.append({"Date": today, "workouts": workout, "set x reps": setxreps, "weights": weights})
            #write to csv
            writer.writerow({"Date": today, "Workouts": workout, "Set x Reps": setxreps, "Weights": weights})
    print(tabulate(data, headers="keys", tablefmt="double_grid"))
    

def display_client(filepath):
    data = []
    target_date = input("What date would you like to view: ")
    with open(filepath) as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Date'] == target_date:
                data.append(row)
        print(tabulate(data, headers="keys", tablefmt="double_grid"))


def main():
    name = input("Which client: ")
    filepath = name.lower() + '.csv'
    option = input("Would you like to edit or view: ")
    if option.lower() == 'edit':
        exercise_number = int(input("How many exercises do you want to input: "))
        workouts_log(filepath, exercise_number)
    elif option.lower() == 'view':
        display_client(filepath)



if __name__ == '__main__':
    main()

#TODO: create an option menu for either editing or viewing. If viewing, have filters (from date-date) and maybe graph on exercises