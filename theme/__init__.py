from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config
Config.set('graphics', 'height', 770)
Config.set('graphics', 'width', 370)
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty,NumericProperty,ListProperty,DictProperty
from kivy.uix.behaviors import ButtonBehavior
from kivy.garden.navigationdrawer import NavigationDrawer
from kivy.uix.behaviors.touchripple import  TouchRippleButtonBehavior
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.app import App
Builder.load_string('''
<RootMenu>:
    orientation:"vertical"
    size_hint:1,None
    height:self.minimum_height
<MenuButton>:
    size_hint:1,None
    height:"50sp"
    canvas:
        Color:
            rgba:1,1,1,.2
        Rectangle:
            size:self.width,1
            pos:self.pos
<Menu>:
    orientation:"vertical"
    FloatLayout:
        canvas:
            Color:
                rgba:1,1,1,1
            Rectangle:
                size:self.width,1
                pos:self.pos
        size_hint:1,.3
        FloatLayout:
            size_hint:None,None
            pos_hint:{"center_x":.5,"center_y":.6}
            size: 0.6*min(root.size), 0.6*min(root.size)
            canvas:
                Color:
                    rgba:1,1,1,1
                Ellipse:
                    size:self.size
                    pos:self.pos
                    source:root.icon
        BoxLayout:
            size_hint:1,.2
            pos_hint:{"center_x":.5,"y":0}
            orientation:"vertical"
            Label:
                text:root.user_name
                halign:"center"
                valign:"bottom"
                text_size:self.size
                font_size:self.height
            Label:
                text:root.server
                font_size:self.height
                
    ScrollView:        
        RootMenu:
            id:rm
            on_parent:
                root.add()
<BtnMenu>:
<stdTheme>:
    anim_type:"slide_above_simple"
    Menu:
    BoxLayout:
        orientation:"vertical"
        NavBar:
            on_menu_release:root.on_menu_release()
            on_option_release:root.on_option_release()
        Label
        
<Navbar>:
    size_hint:.98,None
    height:"50sp"
    pos_hint:{"center_x":.5,"top":1}
    canvas:
        Color:
            rgba:1,1,1,1
        Rectangle:
            size:self.width-1,1
            pos:self.x,self.y
    BtnMenu:
        color:root.menu_button_color
        size_hint:None,1
        width:"36sp"
        source:root.menu_button_image
        on_press:
            root.menu_button_color[3]=.1
            root.menu_press+=1
        on_release:
            root.menu_button_color[3]=1
            root.menu_release+=1
    Label:
        text:root.text
        halign:"left"
        valign:"middle"
        text_size:self.size
        font_size:self.height/2.5
    BtnOption:
        color:root.option_button_color
        size_hint:None,1
        width:"40sp"
        source:root.option_button_image
        on_press:
            root.option_button_color[3]=.1
            root.option_press+=1
        on_release:
            root.option_button_color[3]=1
            root.option_release+=1
''')
class RootMenu(BoxLayout):
    pass
class MenuButton(TouchRippleButtonBehavior,Label):
    pass
class BtnMenu(ButtonBehavior,Image):
    pass
class BtnOption(ButtonBehavior,Image):
    pass
class NavBar(BoxLayout):
    menu_press=NumericProperty(0)
    menu_release=NumericProperty(0)
    option_press=NumericProperty(0)
    option_release=NumericProperty(0)
    text=StringProperty("myapp")
    child=StringProperty("")
    menu_button_image=StringProperty("asset/3btn.png")
    menu_button_color=ListProperty([1,1,1,1])
    option_button_image=StringProperty("asset/3dot.png")
    option_button_color=ListProperty([1,1,1,1])
    def __init__(self,*args,**kwargs):
        super(NavBar,self).__init__(**kwargs)
class Menu(BoxLayout):
    user_name=StringProperty("")
    server=StringProperty("")
    list_text=ListProperty(["home","acount","setting"])
    icon=StringProperty("asset/python.png")
    def __init__(self,*args,**kwargs):
        super(Menu,self).__init__(**kwargs)
    def add(self):
        for i in self.list_text:
            self.ids["rm"].add_widget(MenuButton(text=i,on_press=self.on_menu_choose))
    def on_menu_choose(self,instance):
        print(instance.text)
# class StdTheme(NavigationDrawer):
#     def __init__(self,*args,**kwargs):
#         super(StdTheme,self).__init__(**kwargs)
#     def on_menu_release(self):
#         self.toggle_state()
#     def on_option_release(self):
#         print("option_release")
#
# class Theme(App):
#     def build(self):
#         return StdTheme()
# if __name__=="__main__":
#     Theme().run()