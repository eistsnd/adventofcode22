import re
import operator
from util import sign


def value_appender(value):
    def _(stack):
        stack.append(int(value))

    return _


def calculation_appender(left, right, op):
    def _(stack):
        stack.append(op)
        stack.append(right)
        stack.append(left)

    return _


op_table = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}


if __name__ == '__main__':
    yelling_table = {}

    with open('day21_input.txt') as file:
        for line in file:
            number = re.search(r'\d+', line)

            if number:
                key = re.search(r'[a-z]+', line).group()
                yelling_table[key] = value_appender(number.group())
            else:
                keys = re.findall(r'[a-z]+', line)
                op = re.search(r'[\/\-\+\*]', line).group()
                yelling_table[keys[0]] = calculation_appender(keys[1], keys[2], op)


    def calc(yelling_table, start):
        calc_stack = [start]

        result = None
        while calc_stack:
            item = calc_stack.pop()

            if type(item) in [int, float]:
                next_item = calc_stack.pop()
                if type(next_item) in [int, float]:
                    op = calc_stack.pop()
                    result = op_table[op](next_item, item)
                    if calc_stack:
                        calc_stack.append(result)
                    else:
                        break
                else:
                    calc_stack.append(item)
                    yelling_table[next_item](calc_stack)
            else:
                yelling_table[item](calc_stack)

        return result

    first_calc_result = calc(yelling_table, 'root')
    # 158661812617812
    print(first_calc_result)

    # part 2
    left = 'hqpw'
    right = 'nprj'
    right_calc = calc(yelling_table, right)
    left_calc = calc(yelling_table, left)

    n = 40

    def step(n):
        return 2**n

    humn = 2325

    diff_sign = sign(left_calc - right_calc)

    while right_calc != left_calc:
        humn = humn + diff_sign * step(n)
        yelling_table['humn'] = value_appender(humn)
        left_calc = calc(yelling_table, left)

        new_diff_sign = sign(left_calc - right_calc)
        if new_diff_sign != diff_sign:
            n -= 1
            diff_sign = new_diff_sign

    # 3352886133831
    print(humn)





