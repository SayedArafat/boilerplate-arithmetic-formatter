def arithmetic_arranger(problems, result=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    length = 0
    arranged_problems = ''
    list_line1 = []
    list_line2 = []
    underline_list = []
    if result:
        sum = 0
        list_line_result = []

    for problem in problems:
        problem = problem.split()
        if (problem[1] == '+') or (problem[1] == '-'):
            for element in problem:
                element = element.strip()
                # print(element)
                if len(element) > 4:
                    return 'Error: Numbers cannot be more than four digits.'
                if element != '+' and element != '-':
                    try:
                        num = int(element)
                    except ValueError:
                        return 'Error: Numbers must only contain digits.'
                if problem[1] == '+' and result == True:
                    if element == '+':
                        continue
                    sum += num

                if problem[1] == '-' and result == True:
                    if element == '-':
                        continue
                    if element == problem[2]:
                        num = -num
                    sum += num
                if length < len(element):
                    length = len(element)

            raw_text1 = '{:>%(length)s}' % {'length': length + 2}
            raw_text2 = '%(sign)s {:>%(length)s}' % {
                'sign': problem[1],
                'length': length
            }
            result_text = '{:>%(length)s}' % {'length': length + 2}
            line1 = raw_text1.format(problem[0])
            line2 = raw_text2.format(problem[2])
            if result:
                result_line = result_text.format(sum)
                list_line_result.append(result_line)
            list_line1.append(line1)
            list_line2.append(line2)
            sum = 0
            length = 0
        else:
            return "Error: Operator must be '+' or '-'."
    underline_string = ''
    for i in range(len(list_line2)):
        for j in list_line2[i]:
            underline_string += '-'
        underline_list.append(underline_string)
        underline_string = ''

    for i in list_line1:
        if i is list_line1[-1]:
            arranged_problems = arranged_problems + i + '\n'

            break
        arranged_problems = arranged_problems + i + '    '

    for i in list_line2:
        if i is list_line2[-1]:
            arranged_problems = arranged_problems + i + '\n'

            break
        arranged_problems = arranged_problems + i + '    '

    for i in underline_list:
        if i is underline_list[-1] and result:
            arranged_problems = arranged_problems + i + '\n'
            break
        elif i is underline_list[-1]:
            arranged_problems = arranged_problems + i
            break
        arranged_problems = arranged_problems + i + '    '

    if result:
        for i in list_line_result:
            if i is list_line_result[-1]:
                arranged_problems = arranged_problems + i
                break
            arranged_problems = arranged_problems + i + '    '

    return arranged_problems
