from story import Step, EndStep

def import_csv(filename):
    file = open(filename, 'r')
    raw = file.read()
    lines = raw.split("\n")
    cells = []
    for i in lines:
        cells.append(i.split('\t'))
    return cells

def import_steps(filename):
    cells = import_csv(filename)
    steps = []
    for i in cells:
        if i[2] == "_END_STEP":
            s = EndStep(i[1])
        else:
            s = Step(i[1], [i[2], i[3]], [])
        steps.append(s)
    for i in range(len(steps)):
        if not steps[i].is_end():
            steps[i].add_outcomes([steps[int(cells[i][4])], steps[int(cells[i][5])]])
    return steps

if __name__ == '__main__':
    i = import_steps('test.txt')
    i[0].go()