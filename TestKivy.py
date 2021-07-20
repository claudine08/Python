import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout,self).__init__(**kwargs)

        self.cols = 2

        self.add_widget(Label(text = 'Name: ',font_size = 30))
        self.name = TextInput(multiline = False)
        self.add_widget(self.name)

        self.add_widget(Label(text='Address: ', font_size=30))
        self.address = TextInput(multiline=True)
        self.add_widget(self.address)

        self.add_widget(Label(text='Job: ', font_size=30))
        self.job = TextInput(multiline=False)
        self.add_widget(self.job)

        self.add_widget(Label(text='Hobbies: ', font_size=30))
        self.hobbies = TextInput(multiline=True)
        self.add_widget(self.hobbies)

        self.submit = Button(text='Submit', font_size = 30)
        self.submit.bind(on_press = self.press)
        self.add_widget(self.submit)
    def press(self, instance):
        name = self.name.text
        address = self.address.text
        job = self.job.text
        hobbies = self.hobbies.text
        self.add_widget(Label(text = f'Hello {name} ! you live in {address} and work as: {job} and your hobbies are: {hobbies} ',font_size = 10))





class MyApp(App):
    def build(self):
        return MyGridLayout()
MyApp().run()
