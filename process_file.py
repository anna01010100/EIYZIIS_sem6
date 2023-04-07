import nltk
import spacy


class ProcessFile:
    def __init__(self, input_text):
        self.nlp = spacy.load("en_core_web_sm")
        self.input = self.nlp(input_text)
        self.my_dict = {}

    def result(self):
        for i in self.input:
            if i.text not in [',', ':', '!', '?', '.', ';', "'", "\n"]:
                self.my_dict[i.text] = f"lexeme: {i.lemma_}, pos: {i.pos_}, 'part_of_sent: {i.dep_}\n"
        print(self.my_dict)
        str1 = self.beauty_result()
        return str1

    def beauty_result(self):
        str_result = ''
        for key, i in self.my_dict.items():
            str_result = str_result + (key + "\n\t" + str(i) + '\n\n')

        return str_result

