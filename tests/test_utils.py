import calc_parexp
import calc_model


def add_keys_to_calc_expression(calc: (calc_parexp.CalcParExp | calc_model.CalculatorModel), *content):
    for k in content:
        calc.add_key(k)
