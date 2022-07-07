text = "X-DSPAM-Confidence:    0.8475"

pos = text.find('0')
apos = text.find('5', pos)
host = text[pos: apos+1]

print(float(host))
