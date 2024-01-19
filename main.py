# neuralrandom.py
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import random

kivy.require('1.9.0')

class MyRoot(BoxLayout):
    def __init__(self):
        super(MyRoot, self).__init__(orientation='vertical')

        # Check if the label with text "Global Knowledge" is already present
        existing_labels = [widget for widget in self.children if isinstance(widget, Label) and widget.text == 'Global Knowledge']

        # If not present, add the label
        if not existing_labels:
            self.add_widget(Label(text='Global Knowledge', font_size=64, color=(0.92, 0.45, 0)))

        # Remove any existing "Legend" button
        existing_buttons = [widget for widget in self.children if isinstance(widget, Button) and widget.text == 'Legend']
        for button in existing_buttons:
            self.remove_widget(button)
        self.random_label = Label(text="_", font_size=32)
        self.add_widget(self.random_label)

        # Create and add a Button labeled "Legend"
        legend_button = Button(text='Legend', font_size=32, on_press=self.generate_number)
        self.add_widget(legend_button)

        # Create and add a Label for displaying random numbers


    def generate_number(self, instance):
        self.random_label.text = str(random.randint(0, 1000))

class NeuralRandom(App):
    def build(self):
        return MyRoot()

if __name__ == '__main__':
    neuralRandom = NeuralRandom()
    neuralRandom.run()
