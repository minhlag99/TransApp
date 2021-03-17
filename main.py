import docx
import google_trans_new
import googletrans
import time
#source
start = time.time()
path = "input.docx"
name_file = path.split(".")[0]
source = docx.Document(path)
paras = source.paragraphs
#var count
count_cha_limit = 0
text_input = str()
for i in range(0,len(paras)):
    text = paras[i].text
    count_cha_limit = len(text_input) + len(text)
    if text and text.strip:
        if count_cha_limit < 5000:
            text_input = text_input + text + "\n"
        else:
            data_scr = text_input.split("\n")
            print(data_scr[len(data_scr)-1])
            print("Làm dấu")
            text_input = str()
end = time.time()
print(end-start)
