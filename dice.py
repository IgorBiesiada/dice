from random import randint
import re
def roll_dice(dice_code):

    dice_type_list = {
        'D3': 3,
        'D4': 4,
        'D6': 6,
        'D8': 8,
        'D10': 10,
        'D12': 12,
        'D20': 20,
        'D100': 100
    }

    pattern = r'^(\d*)D(\d+)([+-]\d+)?$'
    match = re.match(pattern, dice_code)

    if not match:
        return 'Invalid dice code'


    roll = int(match.group(1)) if match.group(1) else 1
    dice_type = f'D{match.group(2)}'
    mod = int(match.group(3)) if match.group(3) else 0

    if dice_type not in dice_type_list:
        return 'Invalid dice type'

    dice_max = dice_type_list[dice_type]
    result = [randint(1, dice_max) for _ in range(roll)]
    total = sum(result) + mod

    return {
        'result': result,
        'modifier': mod,
        'total': total
    }

print(roll_dice('D6'))













