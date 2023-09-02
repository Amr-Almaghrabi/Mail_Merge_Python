names = []

with open("Input/Names/invited_names.txt", mode="r") as f:
    listed_names = f.readlines()
    for i in listed_names:
        new_i = i.strip()
        names.append(new_i)

with open("Input/Letters/starting_letter.txt", mode="r") as starting_letter:
    start = starting_letter.read()

    for i in range(len(names)):
        with open(f"Output/ReadyToSend/letter{i}", mode="w") as letter:
            new_start = start.replace("[name]", names[i])
            new_start.strip()
            letter.write(new_start)
