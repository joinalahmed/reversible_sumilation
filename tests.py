# This Program takes a .tfc file as input, generates all possible gate level equations,
# generates all possible input permutations and display all gate level output matrices
import re

name = raw_input('Enter .tfc file name')
with open(name, 'r') as datafile:
    for line in datafile:
        line1 = line.strip()
        if '.v' in line1:
            aa = line1
            bb = aa
            bb = bb[3:]
            cc = re.split(',', bb)
            asd = len(cc)
            asd1 = str(asd)
            break


def strings(bc):
    bc = list(bc)
    for j in range(len(bc)):
        if bc[j] == ',':
            continue
        else:
            bc[j] = 'str(' + bc[j] + ')'


garbage = open('gen.py', 'w')
garbage.write("import itertools" + "\n")
garbage.write("\n")
garbage.write("outs=open('correct_output.txt', 'w')" + "\n")
garbage.write("a = 2 ** " + asd1 + "\n")
garbage.write("\n")
garbage.write("\n")
garbage.write("def truth_push(input_result):" + "\n")
garbage.write("    levels.append('=>')" + "\n")
garbage.write("    levels.append(input_result)" + "\n")
garbage.write("\n")
garbage.write("\n")
garbage.write("def truth_fix(input_result):" + "\n")
garbage.write("    for n, i in enumerate(input_result):" + "\n")
garbage.write("        if i == True:" + "\n")
garbage.write("            result[n] = 1" + "\n")
garbage.write("        if i == False:" + "\n")
garbage.write("            result[n] = 0" + "\n")
garbage.write("\n")
garbage.write("\n")
garbage.write("testPatterns = table = list(itertools.product([0, 1], repeat=" + asd1 + "))" + "\n")
garbage.write("for p in testPatterns:" + "\n")
garbage.write("    levels = list()" + "\n")
garbage.write('    ' + bb + ' = p' + '\n')

garbage.write("    result = [" + bb + "]\n")
garbage.write("    levels.append(result)" + "\n")
qw = open('main1.txt', 'w')
with open(name, 'r') as file_r:
    for line in file_r:
        if line.strip() == 'BEGIN':
            break
    for line in file_r:
        if line.strip() == 'END':
            break
        line1 = re.split(',', line)
        length = len(line1)
        line2 = line1[0]
        line2 = re.split('\\s', line2)
        line2 = list(line2)
        line1[0] = line2[1]
        length1 = len(line1)
        line3 = line1[length1 - 1]
        length2 = len(line3)
        line3 = re.split('\n', line3)
        line1[length1 - 1] = line3[0]
        line_final = list()
        for ii in range(len(line1)):
            line_final.append(line1[ii])
            line_final.append(',')
        del line_final[-1]
        line_final1 = ''.join(line_final)
        ff = open('main1.txt', 'a')
        ff.write(line_final1)
        ff.write('\n')
        ff.close()
with open('main1.txt', 'r+') as exp:
    for lenn in exp:
        if len(lenn) == 1:
            if lenn == '\n':
                continue
        ui = len(lenn)
        ax = lenn
        axx = re.split(',', ax)
        mn = len(axx)
        mn -= 1
        axx1 = str(axx[mn])
        axx2 = re.split('\n', axx1)
        axx[mn] = axx2[0]
        mn1 = len(axx)
        mn2 = mn1 - 1
        axx[mn2] = axx2[0]
        lenn = axx
        linen = list()
        for ii in range(len(lenn)):
            linen.append(lenn[ii])
            linen.append(',')
        del linen[-1]
        lenn = linen
        final_len = len(lenn)
        if len(lenn) == 1:
            benn = list(lenn)
            benn.append(' =')
            benn.append(' not')
            benn.append(' ')
            benn.append(benn[0])
            benn1 = ''.join(benn)
            garbage.write('    ' + benn1 + '\n')
        if len(lenn) == 3:
            tren = list(lenn)
            nn = len(tren)
            tren1 = list(tren[nn - 1])
            tren1.append(' = ')
            tren1.append(tren[0])
            tren1.append(' ')
            tren1.append('^')
            tren1.append(' ')
            tren1.append(tren[nn - 1])
            tren2 = ''.join(tren1)
            garbage.write('    ' + tren2 + '\n')
        if len(lenn) > 3:
            list1 = list(lenn)
            num = len(list1)
            insert1 = num - 1
            list2 = list1[insert1]
            list3 = list(list2)
            list3.append(' =')
            list3.append(' (')
            hg = len(list1)
            la_el = list1[hg - 1]
            list1.insert(0, la_el)
            list1.insert(1, ' =')
            list1.insert(2, ' (')
            hg1 = len(list1)
            list1[hg1 - 2] = '^ '
            list1.insert(hg1 - 2, ') ')
            z = 4
            ven = len(list1)
            for i in list1:
                list1[z] = ' and '
                z += 2
                if z == ven - 3:
                    break
            qwerty = ''.join(list1)
            garbage.write('    ' + qwerty + '\n')
        garbage.write("    result = [" + bb + "]\n")
        garbage.write("    truth_fix(result)" + "\n")
        garbage.write("    truth_push(result)" + "\n")
garbage.write("    print(str(levels))")
garbage.write("\n")
garbage.write("    outs.write(str(levels))  ")
garbage.write("\n")
garbage.write("    outs.write('\\n')")
garbage.write("\n")
garbage.close()
execfile('gen.py')
