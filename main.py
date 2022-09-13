from appJar import gui

app = gui()

w = 0

f = open("plaintext.csv", "a+")
c = open("ciphertext.csv", "a+")

c.truncate(0)
f.truncate(0)

def press(button):
    global w

    if button == "Process with Caesarian":
        if w == 0:
            app.infoBox("The Cryptography Machine", "Please enter your shift from 1-26 in the input box.")
            w = 1
        else:
            f.write(app.getEntry("Plaintext"))
            shift = int(app.getEntry("Input"))
            # make the program examine the word letter by letter and encrypt it that way using wordarr
            k = 0
            while k < len(app.getEntry("Plaintext")):
                holderChar = app.getEntry("Plaintext")[k]
                holderChar = ord(holderChar)
                if (holderChar + shift) >= 123:
                    holderChar = holderChar + shift - 26
                elif (holderChar + shift) >= 91 and (holderChar + shift) <= 96:
                    holderChar = holderChar + shift - 26
                else:
                    holderChar = holderChar + shift
                holderChar = chr(holderChar)
                c.write(holderChar)
                c.write(" ")
                k = k + 1
            f.close()
            c.close()
            app.stop()
    if button == "Process with Vinegere":
        if w == 0:
            app.infoBox("The Cryptography Machine", "Please enter an uppercase key in the input box.")
            w = 1
        else:
            engiShift = (app.getEntry("Input"))
            f.write(app.getEntry("Plaintext"))
            f.write("\n")
            f.write("Key: ")
            f.write(engiShift)
            vigKeyArray = []

            w = 0
            while w < len(engiShift):
                if engiShift[w] == 'A':
                    vigKeyArray.append(1)
                elif engiShift[w] == 'B':
                    vigKeyArray.append(2)
                elif engiShift[w] == 'C':
                    vigKeyArray.append(3)
                elif engiShift[w] == 'D':
                    vigKeyArray.append(4)
                elif engiShift[w] == 'E':
                    vigKeyArray.append(5)
                elif engiShift[w] == 'F':
                    vigKeyArray.append(6)
                elif engiShift[w] == 'G':
                    vigKeyArray.append(7)
                elif engiShift[w] == 'H':
                    vigKeyArray.append(8)
                elif engiShift[w] == 'I':
                    vigKeyArray.append(9)
                elif engiShift[w] == 'J':
                    vigKeyArray.append(10)
                elif engiShift[w] == 'K':
                    vigKeyArray.append(11)
                elif engiShift[w] == 'L':
                    vigKeyArray.append(12)
                elif engiShift[w] == 'M':
                    vigKeyArray.append(13)
                elif engiShift[w] == 'N':
                    vigKeyArray.append(14)
                elif engiShift[w] == 'O':
                    vigKeyArray.append(15)
                elif engiShift[w] == 'P':
                    vigKeyArray.append(16)
                elif engiShift[w] == 'Q':
                    vigKeyArray.append(17)
                elif engiShift[w] == 'R':
                    vigKeyArray.append(18)
                elif engiShift[w] == 'S':
                    vigKeyArray.append(19)
                elif engiShift[w] == 'T':
                    vigKeyArray.append(20)
                elif engiShift[w] == 'U':
                    vigKeyArray.append(21)
                elif engiShift[w] == 'V':
                    vigKeyArray.append(22)
                elif engiShift[w] == 'W':
                    vigKeyArray.append(23)
                elif engiShift[w] == 'X':
                    vigKeyArray.append(24)
                elif engiShift[w] == 'Y':
                    vigKeyArray.append(25)
                elif engiShift[w] == 'Z':
                    vigKeyArray.append(26)
                else:
                    break
                w = w + 1
            k = 0
            m = 0
            p = 0

            while m < len(app.getEntry("Plaintext")):
                holderChar = app.getEntry("Plaintext")[m]
                holderChar = ord(holderChar)
                if holderChar != 32:
                    if (holderChar + vigKeyArray[p]) >= 123:
                        holderChar = holderChar + vigKeyArray[p] - 26
                    elif 91 <= (holderChar + vigKeyArray[p]) <= 96:
                        holderChar = holderChar + vigKeyArray[p] - 26
                    else:
                        holderChar = holderChar + vigKeyArray[p]
                    holderChar = chr(holderChar)
                    c.write(holderChar)
                    p = p + 1
                    if p == len(vigKeyArray):
                        p = 0
                    m = m + 1
                else:
                    c.write(" ")
                    m = m + 1
            m = 0
            f.close()
            c.close()
            app.stop()
    if button == "Process with Enigma":
        if w == 0:
            app.infoBox("The Cryptography Machine", "Please enter an uppercase 3-letter randomized key in the input box.")
            w = 1
        else:
            engiShift = (app.getEntry("Input"))
            f.write(app.getEntry("Plaintext"))
            f.write("\n")
            f.write("Key: ")
            f.write(engiShift)
            vigKeyArray = []
            w = 0
            while w < len(engiShift):
                if engiShift[w] == 'A':
                    vigKeyArray.append(1)
                elif engiShift[w] == 'B':
                    vigKeyArray.append(2)
                elif engiShift[w] == 'C':
                    vigKeyArray.append(3)
                elif engiShift[w] == 'D':
                    vigKeyArray.append(4)
                elif engiShift[w] == 'E':
                    vigKeyArray.append(5)
                elif engiShift[w] == 'F':
                    vigKeyArray.append(6)
                elif engiShift[w] == 'G':
                    vigKeyArray.append(7)
                elif engiShift[w] == 'H':
                    vigKeyArray.append(8)
                elif engiShift[w] == 'I':
                    vigKeyArray.append(9)
                elif engiShift[w] == 'J':
                    vigKeyArray.append(10)
                elif engiShift[w] == 'K':
                    vigKeyArray.append(11)
                elif engiShift[w] == 'L':
                    vigKeyArray.append(12)
                elif engiShift[w] == 'M':
                    vigKeyArray.append(13)
                elif engiShift[w] == 'N':
                    vigKeyArray.append(14)
                elif engiShift[w] == 'O':
                    vigKeyArray.append(15)
                elif engiShift[w] == 'P':
                    vigKeyArray.append(16)
                elif engiShift[w] == 'Q':
                    vigKeyArray.append(17)
                elif engiShift[w] == 'R':
                    vigKeyArray.append(18)
                elif engiShift[w] == 'S':
                    vigKeyArray.append(19)
                elif engiShift[w] == 'T':
                    vigKeyArray.append(20)
                elif engiShift[w] == 'U':
                    vigKeyArray.append(21)
                elif engiShift[w] == 'V':
                    vigKeyArray.append(22)
                elif engiShift[w] == 'W':
                    vigKeyArray.append(23)
                elif engiShift[w] == 'X':
                    vigKeyArray.append(24)
                elif engiShift[w] == 'Y':
                    vigKeyArray.append(25)
                elif engiShift[w] == 'Z':
                    vigKeyArray.append(26)
                else:
                    break
                w = w + 1
            i = 0
            x = 0
            z = 0

            while x < len(app.getEntry("Plaintext")):
                holderChar = app.getEntry("Plaintext")[x]
                holderChar = ord(holderChar)
                if holderChar == 32:
                    c.write(" ")
                    z = z + 1
                else:
                    while z < len(vigKeyArray):
                        if (holderChar + vigKeyArray[z]) >= 123:
                            holderChar = holderChar + vigKeyArray[z] - 26
                        elif 91 <= (holderChar + vigKeyArray[z]) <= 96:
                            holderChar = holderChar + vigKeyArray[z] - 26
                        else:
                            holderChar = holderChar + vigKeyArray[z]
                        vigKeyArray[z] = vigKeyArray[z] + 1
                        if vigKeyArray[z] > 26:
                            vigKeyArray[z] = 1
                        z = z + 1

                holderChar = chr(holderChar)
                c.write(holderChar)
                z = 0
                x = x + 1
            f.close()
            c.close()
            app.stop()
    if button == "Info":
        app.infoBox("The Cryptography Machine", "The Cryptography Machine is a program created for educational purposes. This program is intended to showcase some basic ciphers and provide an easy way to facilitate learning about these ciphers. This program is not intended to help people to encrypt sensitive information, and will not function well for that purpose. To use the program, enter the plaintext that you wish to encrypt into the plaintext section, then press one of the 3 buttons. The program will then inform you of what you need to do from there."
                                                                 "                                                                                                                                          Thank you for using the Cryptography Machine!")

wordsArr = []

app.setTitle("The Cryptography Machine")
app.addLabel("title", "The Cryptography Machine")
app.setLabelBg("title", "blue")
app.addLabelEntry("Plaintext")
app.addLabelEntry("Input")
app.addButtons(["Process with Caesarian", "Process with Vinegere", "Process with Enigma"], press)
app.addButton("Info", press)
app.go()

























