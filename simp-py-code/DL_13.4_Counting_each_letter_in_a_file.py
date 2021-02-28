from tkinter.filedialog import askopenfilename
def counting_letter():
    file_name = askopenfilename()
    infile = open(file_name, "r")
    file_read = infile.read()
    
    count_for_a = 0
    count_for_b = 0
    count_for_c = 0
    count_for_d = 0
    count_for_e = 0
    count_for_f = 0
    count_for_g = 0
    count_for_i = 0
    count_for_j = 0
    count_for_k = 0
    count_for_l = 0
    count_for_m = 0
    count_for_n = 0
    count_for_o = 0
    count_for_p = 0
    count_for_q = 0
    count_for_r = 0
    count_for_s = 0
    count_for_t = 0
    count_for_u = 0
    count_for_v = 0
    count_for_w = 0
    count_for_x = 0
    count_for_y = 0
    count_for_z = 0
    
    words = [x for x in file_read.split()]
    print(words)
    for word in words:
        for letter in word:
            print(letter)
            if letter.isalpha() and letter.lower() == "a":
                count_for_a += 1
            if letter.isalpha() and letter.lower() == "b":
                count_for_b += 1
            if letter.isalpha() and letter.lower() == "c":
                count_for_c += 1
            if letter.isalpha() and letter.lower() == "d":
                count_for_d += 1
            if letter.isalpha() and letter.lower() == "e":
                count_for_e += 1
            if letter.isalpha() and letter.lower() == "f":
                count_for_f += 1
            if letter.isalpha() and letter.lower() == "g":
                count_for_g += 1
            if letter.isalpha() and letter.lower() == "h":
                count_for_h += 1
            if letter.isalpha() and letter.lower() == "i":
                count_for_i += 1
            if letter.isalpha() and letter.lower() == "j":
                count_for_j += 1
            if letter.isalpha() and letter.lower() == "k":
                count_for_k += 1
            if letter.isalpha() and letter.lower() == "l":
                count_for_l += 1
            if letter.isalpha() and letter.lower() == "m":
                count_for_m += 1
            if letter.isalpha() and letter.lower() == "n":
                count_for_n += 1
            if letter.isalpha() and letter.lower() == "o":
                count_for_o += 1
            if letter.isalpha() and letter.lower() == "p":
                count_for_p += 1
            if letter.isalpha() and letter.lower() == "q":
                count_for_q += 1
            if letter.isalpha() and letter.lower() == "r":
                count_for_r += 1
            if letter.isalpha() and letter.lower() == "s":
                count_for_s += 1
            if letter.isalpha() and letter.lower() == "t":
                count_for_t += 1
            if letter.isalpha() and letter.lower() == "u":
                count_for_u += 1
            if letter.isalpha() and letter.lower() == "v":
                count_for_v += 1
            if letter.isalpha() and letter.lower() == "w":
                count_for_w += 1
            if letter.isalpha() and letter.lower() == "x":
                count_for_x += 1
            if letter.isalpha() and letter.lower() == "y":
                count_for_y += 1
            if letter.isalpha() and letter.lower() == "z":
                count_for_z += 1
            
                
        
    print(count_for_r)

counting_letter()