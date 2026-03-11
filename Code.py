def get_goal():
    print("Choose your goal:")
    print("1 - Lose fat")
    print("2 - Gain muscle")
    print("3 - General fitness")
    print("4 - Strength")
    print("5 - Endurance")

    choice = input("Enter the number of your goal: ").strip()

    goals = {
        "1": "lose fat",
        "2": "gain muscle",
        "3": "general fitness",
        "4": "strength",
        "5": "endurance"
    }
    return goals.get(choice)


def get_activity_level():
    print("\nChoose your current physical activity frequency:")
    print("1 - Sedentary")
    print("2 - 1 to 2 days/week")
    print("3 - 3 to 4 days/week")
    print("4 - 5+ days/week")

    choice = input("Enter the number of your activity level: ").strip()

    levels = {
        "1": "sedentary",
        "2": "low",
        "3": "moderate",
        "4": "high"
    }
    return levels.get(choice)


def get_free_days():
    print("\nHow many free days do you have to train per week?")
    choice = input("Enter a number from 1 to 6: ").strip()

    if not choice.isdigit():
        return None

    days = int(choice)
    if 1 <= days <= 6:
        return days
    return None


def choose_session_type(goal, activity_level, free_days):
    beginner = activity_level in ["sedentary", "low"]

    if free_days == 1:
        return "full_body"

    if free_days == 2:
        if goal in ["strength", "gain muscle"] and not beginner:
            return "upper_or_lower_focus"
        return "full_body"

    if free_days >= 3:
        if goal == "gain muscle":
            return "hypertrophy_focus"
        if goal == "strength":
            return "strength_focus"
        if goal == "lose fat":
            return "fat_loss_focus"
        if goal == "endurance":
            return "endurance_focus"
        return "general_fitness_focus"

    return "full_body"


def build_session(goal, activity_level, free_days):
    beginner = activity_level in ["sedentary", "low"]
    session_type = choose_session_type(goal, activity_level, free_days)

    if goal == "gain muscle":
        if beginner:
            return {
                "title": "Exact Gym Session - Muscle Gain",
                "duration": "60 to 70 minutes",
                "warmup": [
                    "5 minutes brisk treadmill walk",
                    "2 rounds: 10 bodyweight squats, 10 arm circles each side, 10 hip hinges"
                ],
                "main_session": [
                    {
                        "name": "Leg Press",
                        "sets": "4",
                        "reps": "10",
                        "rest": "90 seconds",
                        "instruction": "Use a controlled lowering phase of about 2 seconds and push strongly without locking the knees hard."
                    },
                    {
                        "name": "Machine Chest Press",
                        "sets": "4",
                        "reps": "10",
                        "rest": "75 seconds",
                        "instruction": "Lower under control, press powerfully, and stop 1 to 2 reps before failure."
                    },
                    {
                        "name": "Lat Pulldown",
                        "sets": "4",
                        "reps": "10",
                        "rest": "75 seconds",
                        "instruction": "Pull to upper chest, keep chest up, and avoid swinging backward."
                    },
                    {
                        "name": "Dumbbell Romanian Deadlift",
                        "sets": "3",
                        "reps": "10",
                        "rest": "90 seconds",
                        "instruction": "Hinge at the hips, keep back neutral, and feel the hamstrings stretch."
                    },
                    {
                        "name": "Machine Shoulder Press",
                        "sets": "3",
                        "reps": "10",
                        "rest": "75 seconds",
                        "instruction": "Press overhead with control and do not arch the lower back."
                    },
                    {
                        "name": "Biceps Curl",
                        "sets": "2",
                        "reps": "12",
                        "rest": "60 seconds",
                        "instruction": "Keep elbows still and avoid using momentum."
                    },
                    {
                        "name": "Triceps Pushdown",
                        "sets": "2",
                        "reps": "12",
                        "rest": "60 seconds",
                        "instruction": "Fully extend the elbows at the bottom without leaning your whole body into it."
                    }
                ],
                "finisher": "5 minutes easy bike cooldown",
                "coach_note": "This is a full gym session for muscle gain with basic hypertrophy movements and manageable complexity."
            }

        return {
            "title": "Exact Gym Session - Muscle Gain",
            "duration": "65 to 75 minutes",
            "warmup": [
                "5 minutes incline treadmill walk",
                "2 rounds: 10 bodyweight squats, 8 push-ups, 10 band pull-aparts"
            ],
            "main_session": [
                {
                    "name": "Back Squat",
                    "sets": "4",
                    "reps": "8",
                    "rest": "120 seconds",
                    "instruction": "Brace before each rep, descend under control, and drive up strongly."
                },
                {
                    "name": "Bench Press",
                    "sets": "4",
                    "reps": "8",
                    "rest": "90 seconds",
                    "instruction": "Lower to mid chest with control and press explosively while keeping shoulders stable."
                },
                {
                    "name": "Barbell Row",
                    "sets": "4",
                    "reps": "8",
                    "rest": "90 seconds",
                    "instruction": "Keep torso stable and pull elbows back rather than shrugging."
                },
                {
                    "name": "Romanian Deadlift",
                    "sets": "3",
                    "reps": "10",
                    "rest": "90 seconds",
                    "instruction": "Move through the hips, keep the bar close, and maintain a neutral spine."
                },
                {
                    "name": "Shoulder Press",
                    "sets": "3",
                    "reps": "10",
                    "rest": "75 seconds",
                    "instruction": "Press overhead with control and avoid flaring the ribs excessively."
                },
                {
                    "name": "Dumbbell Curl",
                    "sets": "2",
                    "reps": "12",
                    "rest": "60 seconds",
                    "instruction": "Use strict form and control the lowering phase."
                },
                {
                    "name": "Triceps Rope Pushdown",
                    "sets": "2",
                    "reps": "12",
                    "rest": "60 seconds",
                    "instruction": "Separate the rope slightly at the bottom and keep elbows tucked."
                }
            ],
            "finisher": "5 minutes easy bike cooldown",
            "coach_note": "This session is built as a true gym workout sequence for hypertrophy."
        }

    if goal == "strength":
        if beginner:
            return {
                "title": "Exact Gym Session - Strength",
                "duration": "55 to 65 minutes",
                "warmup": [
                    "5 minutes bike",
                    "2 rounds: 10 bodyweight squats, 10 glute bridges, 10 wall push-ups"
                ],
                "main_session": [
                    {
                        "name": "Leg Press",
                        "sets": "5",
                        "reps": "5",
                        "rest": "120 seconds",
                        "instruction": "Use a heavy but controlled load and stop before form breaks."
                    },
                    {
                        "name": "Machine Chest Press",
                        "sets": "5",
                        "reps": "5",
                        "rest": "120 seconds",
                        "instruction": "Press hard, but keep the shoulders down and stable."
                    },
                    {
                        "name": "Seated Row",
                        "sets": "4",
                        "reps": "6",
                        "rest": "90 seconds",
                        "instruction": "Pull firmly toward the torso and control the return."
                    },
                    {
                        "name": "Dumbbell Romanian Deadlift",
                        "sets": "4",
                        "reps": "6",
                        "rest": "90 seconds",
                        "instruction": "Hinge with control and keep the dumbbells close to the legs."
                    },
                    {
                        "name": "Farmer Carry",
                        "sets": "3",
                        "reps": "20 to 30 meters",
                        "rest": "60 seconds",
                        "instruction": "Walk tall, brace the core, and keep the shoulders packed."
                    }
                ],
                "finisher": "3 minutes easy walk",
                "coach_note": "This session uses lower reps and longer rests to emphasize strength."
            }

        return {
            "title": "Exact Gym Session - Strength",
            "duration": "60 to 75 minutes",
            "warmup": [
                "5 minutes rowing machine",
                "2 rounds: 8 bodyweight squats, 8 push-ups, 8 hip hinges"
            ],
            "main_session": [
                {
                    "name": "Back Squat",
                    "sets": "5",
                    "reps": "5",
                    "rest": "150 seconds",
                    "instruction": "Brace hard before each rep, keep chest stacked, and drive up with intent."
                },
                {
                    "name": "Bench Press",
                    "sets": "5",
                    "reps": "5",
                    "rest": "120 seconds",
                    "instruction": "Use full-body tension and keep bar path consistent."
                },
                {
                    "name": "Barbell Row",
                    "sets": "4",
                    "reps": "6",
                    "rest": "90 seconds",
                    "instruction": "Keep torso angle consistent and pull strongly into the lower chest or upper stomach."
                },
                {
                    "name": "Romanian Deadlift",
                    "sets": "4",
                    "reps": "6",
                    "rest": "120 seconds",
                    "instruction": "Keep lats engaged and hinge without rounding."
                },
                {
                    "name": "Farmer Carry",
                    "sets": "3",
                    "reps": "25 meters",
                    "rest": "60 seconds",
                    "instruction": "Walk under control and maintain trunk stiffness."
                }
            ],
            "finisher": "5 minutes easy walk",
            "coach_note": "This session is structured like a real strength day inside the gym."
        }

    if goal == "lose fat":
        return {
            "title": "Exact Gym Session - Fat Loss",
            "duration": "55 to 65 minutes",
            "warmup": [
                "5 minutes incline walk",
                "2 rounds: 10 bodyweight squats, 10 shoulder circles, 10 walking lunges total"
            ],
            "main_session": [
                {
                    "name": "Goblet Squat",
                    "sets": "3",
                    "reps": "10",
                    "rest": "60 seconds",
                    "instruction": "Move continuously but with control. Do not rush the reps."
                },
                {
                    "name": "Machine Chest Press",
                    "sets": "3",
                    "reps": "10",
                    "rest": "60 seconds",
                    "instruction": "Keep a steady pace and clean form."
                },
                {
                    "name": "Lat Pulldown",
                    "sets": "3",
                    "reps": "10",
                    "rest": "60 seconds",
                    "instruction": "Pull down to chest level and control the return."
                },
                {
                    "name": "Romanian Deadlift",
                    "sets": "3",
                    "reps": "10",
                    "rest": "75 seconds",
                    "instruction": "Use hips, not lower back, to drive the movement."
                },
                {
                    "name": "Walking Lunges",
                    "sets": "2",
                    "reps": "12 each leg",
                    "rest": "60 seconds",
                    "instruction": "Take stable steps and keep the torso tall."
                },
                {
                    "name": "Plank",
                    "sets": "3",
                    "reps": "30 to 40 seconds",
                    "rest": "45 seconds",
                    "instruction": "Brace the abs and do not let the hips sag."
                }
            ],
            "finisher": "12 minutes incline treadmill walk at a challenging but sustainable pace",
            "coach_note": "This session keeps rest shorter and uses full-body work to increase training density."
        }

    if goal == "endurance":
        return {
            "title": "Exact Gym Session - Endurance",
            "duration": "50 to 60 minutes",
            "warmup": [
                "5 minutes bike",
                "2 rounds: 10 bodyweight squats, 10 step-ups total, 10 arm circles"
            ],
            "main_session": [
                {
                    "name": "Bodyweight Squat",
                    "sets": "3",
                    "reps": "15",
                    "rest": "45 seconds",
                    "instruction": "Keep moving smoothly and maintain rhythm."
                },
                {
                    "name": "Push-Ups",
                    "sets": "3",
                    "reps": "12",
                    "rest": "45 seconds",
                    "instruction": "Use a variation you can perform with clean form."
                },
                {
                    "name": "Seated Row",
                    "sets": "3",
                    "reps": "15",
                    "rest": "45 seconds",
                    "instruction": "Pull with control and keep chest up."
                },
                {
                    "name": "Walking Lunges",
                    "sets": "3",
                    "reps": "12 each leg",
                    "rest": "45 seconds",
                    "instruction": "Stay balanced and avoid rushing."
                },
                {
                    "name": "Mountain Climbers",
                    "sets": "3",
                    "reps": "30 seconds",
                    "rest": "30 seconds",
                    "instruction": "Keep hips relatively steady and move quickly."
                },
                {
                    "name": "Plank",
                    "sets": "3",
                    "reps": "30 seconds",
                    "rest": "30 seconds",
                    "instruction": "Brace and breathe under control."
                }
            ],
            "finisher": "15 minutes bike, rower, or treadmill at steady moderate intensity",
            "coach_note": "This session is designed to keep the body working for longer with manageable resistance."
        }

    return {
        "title": "Exact Gym Session - General Fitness",
        "duration": "55 to 65 minutes",
        "warmup": [
            "5 minutes brisk treadmill walk",
            "2 rounds: 10 bodyweight squats, 10 arm circles, 10 hip hinges"
        ],
        "main_session": [
            {
                "name": "Goblet Squat",
                "sets": "3",
                "reps": "10",
                "rest": "75 seconds",
                "instruction": "Control the descent and stand up strongly."
            },
            {
                "name": "Machine Chest Press",
                "sets": "3",
                "reps": "10",
                "rest": "75 seconds",
                "instruction": "Press with control and stable shoulders."
            },
            {
                "name": "Lat Pulldown",
                "sets": "3",
                "reps": "10",
                "rest": "75 seconds",
                "instruction": "Pull to upper chest and avoid jerking."
            },
            {
                "name": "Romanian Deadlift",
                "sets": "3",
                "reps": "10",
                "rest": "75 seconds",
                "instruction": "Hinge cleanly and keep the back neutral."
            },
            {
                "name": "Walking Lunges",
                "sets": "2",
                "reps": "10 each leg",
                "rest": "60 seconds",
                "instruction": "Use controlled steps and stay upright."
            },
            {
                "name": "Plank",
                "sets": "3",
                "reps": "30 seconds",
                "rest": "45 seconds",
                "instruction": "Brace the core and keep a straight line."
            }
        ],
        "finisher": "8 minutes easy cardio cooldown",
        "coach_note": "This session works like a coach-led full-body gym workout."
    }


def print_session(goal, activity_level, free_days, session_type, session):
    print("\n" + "=" * 70)
    print(session["title"])
    print("=" * 70)
    print(f"Goal: {goal.title()}")
    print(f"Current activity level: {activity_level.title()}")
    print(f"Free training days per week: {free_days}")
    print(f"Chosen session style: {session_type.replace('_', ' ').title()}")
    print(f"Estimated duration: {session['duration']}")

    print("\nWARM-UP")
    for i, item in enumerate(session["warmup"], start=1):
        print(f"{i}. {item}")

    print("\nMAIN WORKOUT")
    for i, exercise in enumerate(session["main_session"], start=1):
        print(f"\nExercise {i}: {exercise['name']}")
        print(f"Sets: {exercise['sets']}")
        print(f"Reps: {exercise['reps']}")
        print(f"Rest: {exercise['rest']}")
        print(f"How to do it: {exercise['instruction']}")

    print("\nFINISHER / COOLDOWN")
    print(session["finisher"])

    print("\nCOACH NOTE")
    print(session["coach_note"])

    print("\nSESSION RULE")
    print("Choose loads that feel challenging but still let you keep good form on all prescribed sets.")


def main():
    print("Welcome to the Gym Training Planner\n")

    goal = get_goal()
    if not goal:
        print("Invalid goal selection.")
        return

    activity_level = get_activity_level()
    if not activity_level:
        print("Invalid activity level selection.")
        return

    free_days = get_free_days()
    if free_days is None:
        print("Invalid number of free days.")
        return

    session_type = choose_session_type(goal, activity_level, free_days)
    session = build_session(goal, activity_level, free_days)
    print_session(goal, activity_level, free_days, session_type, session)


if __name__ == "__main__":
    main()
