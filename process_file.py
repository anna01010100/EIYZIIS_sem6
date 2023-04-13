import nltk
import spacy


class ProcessFile:
    def __init__(self, input_text):
        self.nlp = spacy.load("en_core_web_sm")
        self.input = self.nlp(input_text)
        self.my_dict = {}

    def result(self):
        for i in self.input:
            if i.text not in [',', ':', '!', '?', '.', ';', "'", "\n", "–"]:
                self.my_dict[i.text] = f"lexeme: {i.lemma_}, pos: {i.pos_}, morphological_features: {i.morph}, " \
                                       f"possible_role: {str(self.role_of_word_in_sentence(i))}\n"
        print(self.my_dict)
        str1 = self.beauty_result()
        return str1

    def beauty_result(self):
        str_result = ''
        for key, i in self.my_dict.items():
            str_result = str_result + (key + "\n\t" + str(i) + '\n\n')

        return str_result

    def role_of_word_in_sentence(self, token) -> list:
        role_of_word = []
        if token.pos_ in ("NOUN", "PROPN", "PRON", "NUM"):
            role_of_word.append("Subject")
        if token.pos_ in ("AUX", "VERB"):
            role_of_word.append("Predicate")
        if token.pos_ in ("VERB", "PROPN", "PRON", "NOUN", "ADJ", "NUM"):
            role_of_word.append("Object")
        if token.pos_ in ("ADJ"):
            role_of_word.append("Attribute")
        if token.pos_ in ("ADV"):
            role_of_word.append("Adverbial Modifier")
        if not role_of_word:
            role_of_word.append("Not detected")
        return role_of_word
