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
            print(count_cha_limit)
        else:
            count_cha_limit = 0
            text_translated = google_trans_new.google_translator().translate(text=text_input, lang_tgt="vi")
            print(text_translated)
            scr_output = text_translated.split("\n")
            scr_input = text_input.split("\n")
            for j in range(0, len(scr_input) - 1):
                for k in range(0, i - 1):
                    if scr_input[j] and scr_input[j].strip:
                        if scr_input[j] == paras[k].text:
                            paras[k].text = paras[k].text.replace(scr_input[j], scr_output[j])
                            k = i - 1
            text_input = str()
source.save(name_file+"_translated.docx")
end = time.time()
print(end-start)
