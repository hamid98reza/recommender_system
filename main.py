
from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.pagelayout import PageLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty,ObjectProperty
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.metrics import dp
import os
import random
import pickle
import sklearn
import numpy as np


photo_list = []   
for file,_,pictures in os.walk("photos"):   #⚠️enter the path of your image folder
    for picture in pictures:
        path = os.path.join(file,picture)
        photo_list.append(path)


class PagelayoutExample(PageLayout):
    pass

#[0.39689729, 0.75986623, 0.26056338, 0.67626398, 0.33705882,0.18207694, 0.86341314, 0.82180275]
class GridlayoutExample(GridLayout):
    input1 = StringProperty("genre")
    input2 = StringProperty("budget")
    input3 = StringProperty("desc")
    input4 = StringProperty("director")
    input5 = StringProperty("stars")
    input6 = StringProperty("industry")
    count = 0
    
    content = StringProperty("please Hit Enter after entering value in each table")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

  
    def callback(self, event):
        predicted = self.calculation_model()
        if isinstance(predicted,str):
            self.count+=1
            self.content = predicted
            print(self.count)
            print(event.text)
        else:
            self.content = str(predicted)

    def calculation_model(self):
        try:
            x_train_list = [float(self.input1),float(self.input2),float(self.input3),float(self.input4),
                                float(self.input5),float(self.input6),0.86,0.8,]
            
            x_train_list = np.array(x_train_list)
            print(x_train_list)
            x_train_list = x_train_list.reshape(1,-1)   # since it contains single
            print(x_train_list.ndim) 
            with open('model_air.pkl', 'rb') as fp:
                model = pickle.load(fp)
            # model = skops.io.load("model_air.skops")
            result = model.predict(x_train_list)
            return result
        except:
            return "Please enter correct values"

    def on_text_validation1(self,event):
        self.input1 = str(event.text)
    def on_text_validation2(self,event):
        self.input2 = str(event.text)
    def on_text_validation3(self,event):
        self.input3 = str(event.text)
    def on_text_validation4(self,event):
        self.input4 = str(event.text)
    def on_text_validation5(self,event):
        self.input5 = str(event.text)
    def on_text_validation6(self,event):
        self.input6 = str(event.text)

class BoxlayoutExample(BoxLayout):
    pass

class WidgetExample(Widget):
    pass

class ScrollviewExample(ScrollView):
    pass

class StacklayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "lr-tb"
        self.padding=(dp(20),dp(20),dp(20),dp(20),)
        self.spacing=(dp(10),dp(10))
        
        self.L = Label(text="recommendation",size_hint=(1,.1))
        self.add_widget(self.L)
        for i in range(100):
            #size = dp(100), i+10
            size = dp(100)
            self.b = Button(text=f"movie.{i}",size_hint=(None,None),font_size ="20sp" ,
                        background_color =(1, 1, 1, 1),color =(1, 0, 0, 1),background_normal= random.choice(photo_list), 
                       size=(size,size), on_press=self.callback)
            
            self.add_widget(self.b)

    def callback(self,event):
        print("hello")
        self.L.text = event.text
        print(self.L)
        
        






class TheMovieApp(App):
    pass

TheMovieApp().run()




#https://stackoverflow.com/questions/40001239/how-to-use-a-kivy-stringproperty