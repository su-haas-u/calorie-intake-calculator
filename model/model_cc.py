class CalorieCalculatorModel:

    def __init__(self, user_data):
        self.user_data = user_data

    ACTIVITY_MULTIPLIERS = {
        "Sedentary": 1.2,
        "Lightly Active": 1.375,
        "Moderately Active": 1.55,
        "Very Active": 1.725,
        "Super Active": 1.9
    }

    WEIGHT_UNITS = {
        "kilograms", 
        "pounds", 
        "stones"
    }

    HEIGHT_UNITS = {
        "centimetres",
        "inches",
        "feet + inches"
    }

    SEXES ={
        "male",
        "female"
    }

    def validate_inputs(self) -> bool:
        if not 0 < self.user_data.age < 150:
            raise ValueError("Please enter a valid age.")
        if self.user_data.weight <= 0:
            raise ValueError("Please enter a valid, 3 or 4-digit number.")
        if self.user_data.height <= 0:
            raise ValueError("Please enter a valid number for height")
        if self.user_data.sex not in self.SEXES:
            raise ValueError("'Male' or 'Female' is required.")
        if self.user_data.activity_level not in self.ACTIVITY_MULTIPLIERS:
            raise ValueError(f"Invalid activity level: {self.user_data.activity_level}")
        if self.user_data.weight_unit not in self.WEIGHT_UNITS:
            raise ValueError(f"Invalid weight unit: {self.user_data.weight_unit}")
        if self.user_data.height_unit not in self.HEIGHT_UNITS:
            raise ValueError(f"Invalid height unit: {self.user_data.height_unit}")
        
    def convert_units(self):
        if self.user_data.weight_unit == 'pounds':
            self.user_data.weight /= 2.20
        elif self.user_data.weight_unit == 'stones':
            self.user_data.weight *= 6.35 
        if self.user_data.height_unit == 'inches':
            self.user_data.height *= 2.54
        elif self.user_data.height == 'centimetres':
            self.user_data.height = self.user_data.height
        '''
        elif self.user_data.height_unit == 'feet and inches' and self.user_data.height_feet is not None and self.user_data.height_inches is not None:
            self.user_data.height = (((self.user_data.height_feet * 12) + (self.user_data.height_inches)) * 2.54)
        '''
    def calculate_bmr(self):
        self.convert_units()
        if self.user_data.sex == 'male':
            self.user_data.bmr = 10 * self.user_data.weight + 6.25 * self.user_data.height - 5 * self.user_data.age + 5
        else:
            self.user_data.bmr = 10 * self.user_data.weight + 6.25 * self.user_data.height - 5 * self.user_data.age - 161
        return self.user_data.bmr
    
    def calculate_tdee(self):
        bmr = self.calculate_bmr()
        multiplier = self.ACTIVITY_MULTIPLIERS[self.user_data.activity_level]
        tdee = bmr * multiplier
        return tdee

    def calculate_daily_calorie_intake(self, min_calorie_intake = 1200):
        tdee = self.calculate_tdee()
        calorie_intake = max(tdee - self.user_data.deficit, min_calorie_intake)
        return calorie_intake

'''
    #User's Data: Age
    def user_age():
        while True:
            try:
                age = int(input('Please enter your age: '))
                if 0 < age < 150:
                    return age
                else:
                    print ("Enter a valid number for age.")
            except ValueError:
                print('Please enter a valid number for age.')
            
    #User's Data: Weight
    def user_weight():
        while True:
            try:
                weight_format = str(input('Please enter your preferred format for weight (lb or kg): ')).lower().strip()


                if weight_format == 'lb':
                    weight_lb = float(input('Please enter your weight in pounds: '))
                    actual_weight = weight_lb/2.2046
                    return actual_weight

                if weight_format == 'kg':
                    weight_kg = float(input('Please enter your weight in kilograms: '))
                    actual_weight = weight_kg
                    break

                else:
                    print('Please enter a valid format for weight (lb or kg).')
            except ValueError:
                print('Please enter a valid value for weight.')

    #User's Data: Height
    while True:
        try:
            height_format = str(input('Please enter your preferred format for height (ft, in, or cm): ')).lower().strip()
            if height_format == 'ft':
                
                print('Please enter your height, first in feet and then inches.')
                height_feet = int(input('Height in feet: '))
                height_inches = float(input('Height in inches: '))

                total_inches = (height_feet*12) + height_inches
                actual_height = total_inches * 2.54
                break

            if height_format == 'in':
                height_inches_only = float(input('Please enter your height in only inches: '))
                actual_height = height_inches_only * 2.54
                break

            if height_format == 'cm':
                height_cm = float(input('Please enter your height in centimetres: '))
                actual_height = height_cm
                break

            else:
                print('Please enter a valid format for height ( ft and in or cm).')
        except ValueError:
            print('Please enter a valid value for height.')

    #User's Data: Sex
    def sex():
        while True:
            try: 
                sex = str(input('Please enter your sex as male(m) or female(f): ')).lower().strip()
                if sex in [ 'male', 'm', 'female', 'f']:
                    return sex
                else:
                    print('Please enter either male(m) or female(f).')
            except ValueError:
                print('Please enter your sex. Male(m) or Female(f).')
                        

    #User's Data: Activity Level
    activity_level_multiplier = 1.2  # Desk job. Sedentary lifestyle.

    def calculate_BMR():
        while True:
            try:
                user_sex = sex()
                if user_sex == 'male' or user_sex == 'm':
                    bmr = 10 * weight + 6.25 * height - 5 * age + 5
                    break

                if sex() == 'female' or sex() == 'f':
                    bmr = 10 * weight + 6.25 * height - 5 * age - 161
                    break

                else:
                    print('else: Unable to calculate BMR')
            except ValueError:
                print('ValueError: Unable to calculate BMR')
        return bmr

    #User's Data: Activity Level
    activity_level_multiplier = 1.2  # Desk job. Sedentary lifestyle.

    # Total Daily Energy Expenditure (TDEE) Formula
    bmr = calculate_BMR()
    tdee = bmr * activity_level_multiplier
 
    # Caloric deficit formula for ~0.5kg fat loss per week
    calorie_Intake = tdee - 400

    print(f"BMR: {bmr:.0f} kcal/day")
    print(f"TDEE: {tdee:.0f} kcal/day")
    print(f"Target Caloric Intake (with 400 kcal deficit): {calorie_Intake:.0f} kcal/day")
    return calorie_Intake
'''