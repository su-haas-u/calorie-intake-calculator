from model.user_data import UserData as ud
from model.model_cc import CalorieCalculatorModel as ccm

class Presenter:
    def process_user_input(self, age, weight_unit, weight, height_unit, height, sex, activity_level, deficit):
        try:
            # Debugging output
            #print(f'Processing: Age={age}, Weight={weight}, Height={height}, Sex={sex}, Activity Level={activity_level}, Deficit={deficit}')

            if not all([self, age, weight_unit, weight, height_unit, height, sex, activity_level, deficit]):
                return "All fields are required."
            age = int(age)
            weight_unit = weight_unit
            weight = float(weight)
            height_unit = height_unit
            height = float(height)
            sex = sex
            activity_level = activity_level
            deficit = int(deficit)

            # Debugging output
            #print(f'Converted: Age={age}, Weight={weight}, Height={height}, Deficit={deficit}')

            user = ud(age, weight_unit, weight, height_unit, height, sex, activity_level, deficit)
            calculator = ccm(user)
            calculator.validate_inputs()
            daily_intake = calculator.calculate_daily_calorie_intake(deficit)
            
            # Debugging output
            #print('Reached daily_intake calculation.')           
            #print(f'Daily Intake: {daily_intake}')
            return f'For a calorie deficit of {deficit} you need to consume\n{round(daily_intake)} per day.\nGood luck!'
        except ValueError as e:
            return f'Input error: {e}' 
        except Exception as e:
            return f'Unexpected error: {e}'