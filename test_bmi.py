import ET0735_Lab2.bmi as bmi

def test_bmi_normal_weight():
    result = bmi.calculate_bmi(1.70, 60)    # BMI ≈ 20.8
    assert (result == 0)

def test_bmi_over_weight():
    result = bmi.calculate_bmi(1.70, 80)    # BMI ≈ 27.7
    assert (result == 1)

def test_bmi_under_weight():
    result = bmi.calculate_bmi(1.70, 50)    # BMI ≈ 17.3
    assert (result == -1)