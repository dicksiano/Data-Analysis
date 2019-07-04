old_file = open('dataKickDecision_Main.txt')
new_file = open('dataKickDecision_Main_NoDups.txt', 'w')

lines = old_file.readlines()

old = ""
for line in lines:
    if line != old:
        new_file.write(line)
    old = line

old_file.close()
new_file.close()
