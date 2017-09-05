import os

d='.'
lessons = [os.path.join(d,o) for o in os.listdir(d) if os.path.isdir(os.path.join(d,o)) and not o.startswith('.')]

for idx, lesson in enumerate(lessons):
    heading = None
    with open(os.path.join(lesson, 'README.md'), mode='r') as readme:
        for line in readme:
            line = line.strip()
            if line:
                heading = " ".join(line.split()[1:])
                break
    print(str(idx+1) + '. [' + heading + '](' + lesson + ')')