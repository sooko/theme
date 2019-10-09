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
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.event import EventDispatcher
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.behaviors import ButtonBehavior, ToggleButtonBehavior
from kivy.uix.image import Image
from kivy.properties import StringProperty, NumericProperty, ListProperty
from kivy.uix.floatlayout import FloatLayout
# menu_button_image = StringProperty("asset/3btn.png")
#     menu_button_color = ListProperty([1, 1, 1, 1])
#     connect_button_image = StringProperty("asset/disconnect.png")
#     connect_button_color = ListProperty([1, 1, 1, 1])
Builder.load_string('''
<NavbarScan>:
    size_hint:1,None
    height:"30sp"
    BtnImg:
        color:root.menu_button_color
        source:root.menu_button_image
        size_hint:None,1
        width:"30sp"
        on_press:
            root.menu_button_color[3]=.1
            root.menu_press(self)
        on_release:
            root.menu_button_color[3]=1
            root.menu_release(self)
            
    Label
        text:root.text
        font_size:self.height/2.5
        halign:"right"
        valign:"middle"
        text_size:self.size
        color:root.text_color
    Label:
        size_hint:None,1
        width:"10sp"
    BtnImg:
        source:root.scan_button_image
        size_hint:None,1
        color:root.scan_button_color
        width:"20sp"
        # on_press:
        #     # root.scan_button_color[3]=.1
        # on_release:
        #     # root.scan_button_color[3]=1

<AcountScreen>:
    pos_hint:{"center_x": .5, "center_y": self.pos_anim}
    Button:
        pos_hint:{"center_x":.5,"center_y":.5}
        background_color:0,0,0,.8
        # on_press:root.pos_hint={"center_x":.5,"center_y":5}
    Button:
        size_hint:ac.size_hint
        pos_hint:ac.pos_hint
        background_color:0,0,0,0
        height:ac.height
    BoxLayout:
        spacing:10
        id:ac
        size_hint:.9,None
        pos_hint:{"center_x":.5,"y":.5}
        orientation:"vertical"
        height:self.minimum_height
        Label:
            pos_hint:{"center_x":.5,"center_y":.5}
            size_hint:.5,None
            height:"1sp"
        Label:
            size_hint:1,None
            height:"10sp"
            font_size:self.height/1.5
            color:0,1,1,1
        Label:
            size_hint:1,None
            height:"30sp"
            text:"user name :"
            font_size:self.height/1.5
            color:0,1,1,1
        TextInput
            id:ti_user_name
            text:root.user_name
            size_hint:.5,None
            height:"30sp"
            background_color:0,0,0,0
            pos_hint:{"center_x":.5,"center_y":.5}
            foreground_color:1,1,1,1
            multiline:False
            keyboard_suggestions:True
            canvas.after:
                Color:
                    rgba:1,1,1,.5
                Rectangle:
                    size:self.width,1
                    pos:self.pos
        Label:
            size_hint:1,None
            height:"30sp"
            text:"server :"
            font_size:self.height/1.5
            color:0,1,1,1
        TextInput:
            text:root.server
            id:ti_server
            size_hint:.5,None
            height:"30sp"
            background_color:0,0,0,0
            pos_hint:{"center_x":.5,"center_y":.5}
            foreground_color:1,1,1,1
            multiline:False
            keyboard_suggestions:True
            canvas.after:
                Color:
                    rgba:1,1,1,.5
                Rectangle:
                    size:self.width,1
                    pos:self.pos
        BoxLayout:
            orientation:"vertical"
            pos_hint:{"center_x":.5,"center_y":.5}
            size_hint:.9,None
            height:"60sp"
        BoxLayout:
            pos_hint:{"center_x":.5,"center_y":.5}
            size_hint:.9,None
            height:"30sp"
            spacing:10
            Button:
                warna:.1
                canvas.before:
                    Color:
                        rgba:1,1,1,self.warna
                    RoundedRectangle:
                        size:self.size
                        pos:self.pos
                text:"exit"
                background_color:0,0,0,0
                color:0,1,1,1
                on_press:
                    self.warna=1
                    self.color=0,0,0,1
                on_release:
                    self.warna=.1
                    self.color=0,1,1,1
                    root.exit(self)
            Button:
                color:0,1,1,1
                warna:.1
                canvas.before:
                    Color:
                        rgba:1,1,1,self.warna
                    RoundedRectangle:
                        size:self.size
                        pos:self.pos
                text:"set"
                background_color:0,0,0,0
                on_press:
                    self.warna=1
                    self.color=0,0,0,1
                on_release:
                    self.warna=.1
                    self.color=0,1,1,1
                    root.set([ti_user_name.text,ti_server.text])
        BoxLayout:
            orientation:"vertical"
            pos_hint:{"center_x":.5,"center_y":.5}
            size_hint:.9,None
            height:"30sp"
            
            
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
            # on_parent:
            #     root.add()
<BtnMenu>:

<Navbar>:
    line:1
    size_hint:.98,None
    height:"50sp"
    pos_hint:{"center_x":.5,"top":1}
    canvas:
        Color:
            rgba:1,1,1,root.line
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
        color:root.text_color
    BtnOption:
        color:root.option_button_color
        size_hint:None,.4
        pos_hint:{"center_x":.5,"center_y":.5}
        width:"10sp"
        source:root.option_button_image
        on_press:
            root.option_button_color[3]=.1
            root.option_press+=1
        on_release:
            root.option_button_color[3]=1
            root.option_release+=1
<NavbarConnect>:
    line:1
    size_hint:.98,None
    height:"50sp"
    pos_hint:{"center_x":.5,"top":1}
    canvas:
        Color:
            rgba:1,1,1,root.line
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
        color:root.connect_button_color
        size_hint:None,1
        width:"40sp"
        source:root.connect_button_image
        on_press:
            root.connect_button_color[3]=.1
            root.connect_press+=1
        on_release:
            root.connect_button_color[3]=1
            root.connect_release+=1
<NavbarConnectScan>:
    text_color:0,1,1,1
    line:1
    spacing:5
    size_hint:.98,None
    height:"50sp"
    pos_hint:{"center_x":.5,"top":1}
    canvas:
        Color:
            rgba:1,1,1,root.line
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
        color:root.text_color
    BtnOption:
        color:root.connect_button_color
        size_hint:None,1
        width:"40sp"
        source:root.connect_button_image
        on_press:
            root.connect_button_color[3]=.1
            root.connect_press+=1
        on_release:
            root.connect_button_color[3]=1
            root.connect_release+=1
    Label:
        size_hint:None,1
        width:"5sp"
    BtnOption:
        color:root.scan_button_color
        size_hint:None,None
        width:"25sp"
        height:"25sp"
        source:root.scan_button_image
        on_press:
            root.scan_button_color[3]=.1
            root.scan_press+=1
        on_release:
            root.scan_button_color[3]=.8
            root.scan_release+=1
        pos_hint:{"center_x":.5,"center_y":.5}
    Label:
        size_hint:None,1
        width:"5sp"
<stdTheme>:
    anim_type:"slide_above_simple"
    Menu:
    BoxLayout:
        orientation:"vertical"
        NavBar:
            # on_menu_release:root.on_menu_release()
            # on_connect_release:root.on_option_release()
        AcountScreen:
''')
class AcountScreen(FloatLayout,EventDispatcher):
    pos_anim = NumericProperty(.5)
    user_name=StringProperty("")
    server=StringProperty("")
    def __init__(self,*args,**kwargs):
        self.register_event_type('on_set')
        self.register_event_type('on_exit')
        super(AcountScreen,self).__init__(**kwargs)
    def set(self,a):
        self.dispatch('on_set', a)
    def exit(self,a):
        self.dispatch('on_exit', a)
    def on_set(self,data):
        # print(data)
        pass
    def on_exit(self,data):
        pass
class RootMenu(BoxLayout):
    pass
class MenuButton(TouchRippleButtonBehavior,Label):
    data=StringProperty("")
    def __init__(self,*args,**kwargs):
        super(MenuButton,self).__init__(**kwargs)


class Btn(TouchRippleButtonBehavior,Label):
    pass
class BtnImg(TouchRippleButtonBehavior,Image):
    pass

class BtnMenu(ButtonBehavior,Image):
    pass
class BtnOption(ButtonBehavior,Image):
    pass
class NavBar(BoxLayout):
    text_color=ListProperty([0,1,1,1])
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
class NavBarConnect(BoxLayout):
    menu_press = NumericProperty(0)
    menu_release = NumericProperty(0)
    connect_press = NumericProperty(0)
    connect_release = NumericProperty(0)
    text = StringProperty("myapp")
    child = StringProperty("")
    menu_button_image = StringProperty("asset/3btn.png")
    menu_button_color = ListProperty([1, 1, 1, 1])
    connect_button_image = StringProperty("asset/disconnect.png")
    connect_button_color = ListProperty([1, 1, 1, 1])
    def __init__(self, *args, **kwargs):
        super(NavBarConnect, self).__init__(**kwargs)
class NavBarConnectScan(BoxLayout):
    scan_press=NumericProperty(0)
    scan_release=NumericProperty(0)
    menu_press = NumericProperty(0)
    menu_release = NumericProperty(0)
    connect_press = NumericProperty(0)
    connect_release = NumericProperty(0)
    text = StringProperty("myapp")
    child = StringProperty("")
    menu_button_image = StringProperty("asset/3btn.png")
    menu_button_color = ListProperty([1, 1, 1, 1])
    connect_button_image = StringProperty("asset/disconnect.png")
    connect_button_color = ListProperty([1, 1, 1, 1])
    scan_button_image = StringProperty("asset/qr.png")
    scan_button_color = ListProperty([1, 1, 1, .8])
    def __init__(self, *args, **kwargs):
        super(NavBarConnectScan, self).__init__(**kwargs)

class Menu(BoxLayout):
    user_name=StringProperty("")
    server=StringProperty("")
    list_text=ListProperty(["home","acount","setting"])
    list_data=ListProperty(["a","b","c"])
    icon=StringProperty("asset/python.png")
    clock=Clock
    def __init__(self,*args,**kwargs):
        super(Menu,self).__init__(**kwargs)
        self.clock.schedule_once(self.delay,1)
    def delay(self,dt):
        for i in range(len(self.list_text)):
            self.ids["rm"].add_widget(MenuButton(data=self.list_data[i],text=self.list_text[i],on_press=self.on_menu_choose))

    def on_menu_choose(self,instance):
        self.choose(instance.text)
        self.choose_data(instance.data)
    def choose(self,data):
        pass
    def choose_data(self,data):
        pass


#
# class BtnImg(ButtonBehavior, Image):
#     pass

class NavBarScan(BoxLayout,EventDispatcher):
    text_color=ListProperty([1,1,1,1])
    text = StringProperty("My Aplication")
    btn_menu_color = ListProperty([1, 1, 1, 1])
    menu_button_image = StringProperty("asset/3btn.png")
    menu_button_color = ListProperty([1, 1, 1, 1])
    scan_button_color = ListProperty([1, 1, 1, 1])
    scan_button_image = StringProperty("asset/3dot.png")
    def __init__(self, *args, **kwargs):
        self.register_event_type("on_menu_press")
        self.register_event_type("on_menu_release")
        super(NavBarScan, self).__init__(*args, **kwargs)
    def menu_press(self,a):
        self.dispatch("on_menu_press",a)
    def menu_release(self,a):
        self.dispatch("on_menu_release",a)
    def on_menu_press(self,data):
        print("menu_pressed")
    def on_menu_release(self,data):
        print("menu_releaseed")
# class Theme(App):
#     def build(self):
#         return Menu()
# if __name__=="__main__":
#     Theme().run()

