def health_calculator(age, apple_ate, cigars_smoked):
    anwser = (100 - age) + (apple_ate * 3.5) - (cigars_smoked * 2)
    print(anwser)

roger_data = [22, 5, 0]

health_calculator(roger_data[0], roger_data[1], roger_data[2])
health_calculator(*roger_data)