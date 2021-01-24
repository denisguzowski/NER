import pandas as pd

dframe = pd.read_csv("./data/ner_dataset.csv", encoding = "ISO-8859-1", error_bad_lines=True)

for i in range(len(dframe.index)):
    if (pd.notna(dframe['Sentence #'][i])):
        sentence_n = int(dframe['Sentence #'][i][10:]) 
    dframe.at[i, 'Sentence #'] = sentence_n

dframe = dframe.rename(columns={"Sentence #": "SentenceN"})

dframe.to_csv(r'./data/my_dataset.csv', index = False)