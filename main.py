from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
import os
from striprtf.striprtf import rtf_to_text
from process_file import ProcessFile


class MyWidget(BoxLayout):
    input_widget = ObjectProperty(None)
    output_widget = ObjectProperty(None)

    def open_window(self):
        _popup = DownloadInfo(self.input_widget)
        _popup.open()

    def save_window(self):
        _popup = SaveInfo(self.output_widget)
        _popup.open()

    def process_file(self):
        PrF = ProcessFile(self.input_widget.text)
        dict1 = PrF.result()
        self.output_widget.text = dict1

    def about(self):
        _AboutPage = Info()
        _AboutPage.open()


class DownloadInfo(Popup):
    def __init__(self, *args, **kwargs):
        super(DownloadInfo, self).__init__(**kwargs)
        self.input_widget = args[0]

    def close_window(self):
        self.dismiss()

    def select_file(self, path):
        path = ''.join(path)
        filename, ext = os.path.splitext(path)
        if ext == ".txt":
            with open(path, encoding='utf-8') as stream:
                self.input_widget.text = stream.read()
        elif ext == ".rtf":
            with open(path, encoding='utf-8') as stream:
                rtf = stream.read()
                self.input_widget.text = rtf_to_text(rtf)
        self.close_window()


class SaveInfo(Popup):
    file_name = ObjectProperty('Input1')
    path = "D:\\Projects\\3course\\eyaziis\\lab1_\\lan1_ann\\EIYZIIS_sem6-main\\output"

    def __init__(self, *args, **kwargs):
        super(SaveInfo, self).__init__(**kwargs)
        self.output_widget = args[0]

    def close_window(self):
        self.dismiss()

    def save_file(self):
        full_dir = os.path.join(self.path, self.file_name.text)
        with open(full_dir, "w",  encoding='utf-8') as stream:
            stream.write(self.output_widget.text)
        self.output_widget.text = ""
        self.close_window()


class Info(Popup):
    pass


class MyApp(App):
    def build(self):
        return MyWidget()


if __name__ == '__main__':
    MyApp().run()

