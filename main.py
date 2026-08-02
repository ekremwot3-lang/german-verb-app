import json
import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

class MainApp(App):
    def build(self):
        self.load_data()
        self.current_card = None
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        self.word_label = Label(text="Yükleniyor...", font_size='24sp', size_hint_y=0.2)
        layout.add_widget(self.word_label)
        
        self.meaning_label = Label(text="", font_size='18sp', size_hint_y=0.2)
        layout.add_widget(self.meaning_label)
        
        btn_layout = BoxLayout(orientation='horizontal', size_hint_y=0.2, spacing=10)
        
        show_btn = Button(text="Anlamını Göster", on_press=self.show_meaning)
        next_btn = Button(text="Sonraki Kelime", on_press=self.next_word)
        
        btn_layout.add_widget(show_btn)
        btn_layout.add_widget(next_btn)
        layout.add_widget(btn_layout)
        
        self.next_word(None)
        return layout

    def load_data(self):
        try:
            with open('duzenli_dosyaniz.json', 'r', encoding='utf-8') as f:
                self.words = json.load(f)
        except Exception:
            try:
                with open('app_data.json', 'r', encoding='utf-8') as f:
                    self.words = json.load(f)
            except Exception:
                self.words = [{"almanca": "Lernen", "turkce": "Öğrenmek"}]

    def next_word(self, instance):
        if self.words:
            self.current_card = random.choice(self.words)
            if isinstance(self.current_card, dict):
                self.word_label.text = self.current_card.get('almanca', self.current_card.get('word', ''))
                self.meaning_label.text = ""
            else:
                self.word_label.text = str(self.current_card)
                self.meaning_label.text = ""

    def show_meaning(self, instance):
        if self.current_card and isinstance(self.current_card, dict):
            self.meaning_label.text = self.current_card.get('turkce', self.current_card.get('meaning', ''))

if __name__ == '__main__':
    MainApp().run()