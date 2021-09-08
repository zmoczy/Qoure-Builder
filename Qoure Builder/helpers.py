# -*- coding: utf-8 -*-
screen_helper = """


# This is the initial screen that displays upon launching the app 
<LoginScreen>
    name: 'login'
    # This is a card for aesthetic purposes
    MDCard:
        size_hint: None, None
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        size_hint: (.9,.8)
        elevation: 15
        md_bg_color: [40/255, 10/255, 50/255, 1]
        padding: 60
        spacing: 30

    # Header to appear above Login
    MDLabel:
        text: 'Quore Builder'
        halign: 'center'
        theme_text_color: 'Custom'
        text_color: (150/255, 46/255, 176/255, 1)
        pos_hint: {'center_x':0.5, 'center_y':0.7}
        font_style: 'H3'

    # Setting up a submit button to call the function verify user upon release
    MDRoundFlatButton:
        text: 'Submit'
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        on_release: app.verfy_user()

    # Setting up a create user button to call the function create user upon release
    MDRoundFlatIconButton:
        text: 'Create Account'
        icon: 'newspaper'
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        on_release: app.create_user()

    # Setting up username text field 
    MDTextField:
        id: username_field
        hint_text:'Enter Username'
        icon_right: "weight-lifter"
        icon_right_color: app.theme_cls.primary_color
        pos_hint: {'center_x':0.5, 'center_y':0.55}
        size_hint_x: None
        width: 300

    # Setting up password text field that hides entered text
    MDTextField:
        id: password_field
        hint_text:'Enter Password'
        icon_right_color: app.theme_cls.primary_color
        pos_hint: {'center_x':0.5, 'center_y':0.45}
        size_hint_x: None
        width: 300
        password: True
        
        

# This will be the second screen after login where it will display the 3 functions of the application
<NavScreen>
    name: 'nav'    

    # This is a card for aesthetic purposes
    MDCard:
        size_hint: None, None
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        size_hint: (.9,.8)
        elevation: 15
        md_bg_color: [40/255, 10/255, 50/255, 1]
        padding: 60
        spacing: 30

    # This button will redirect to the Creaton page 
    MDRoundFlatButton:
        text: 'Create Workout'
        size_hint: (.5,.1)
        pos_hint: {'center_x': 0.5, 'center_y': 0.7}
        on_release: app.switch_Workoutscreen()

    # This button will redirect to the Schedule page 
    MDRoundFlatButton:
        text: 'Schedule Workout'
        size_hint: (.5,.1)
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        on_release: app.switch_schdule()

    # This button will redirect to the Begin Workout page 
    MDRoundFlatButton:
        text: 'Begin Workout'
        size_hint: (.5,.1)
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        on_release: app.switch_begin()



# This Screen will appear when there has been an error recieving a message and displaying upon catch
<ErrorScreen>
    name: 'error'

    # This label recieves a string passed when swapping screen and displays for the user
    MDLabel:
        id: error_message
        text: error_message.text
        halign: 'center'
        theme_text_color: 'Error'
        size_hint: (.5,.5)
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        font_style: 'H2'


    # This button will return the user to the login page
    MDRectangleFlatButton:
        text: 'Return to login'
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        on_release: root.manager.current= 'login'


# This screen will appear after pressing "Create Workout" on the Nav Page
<NameScreen>
    name: 'name'

    # This is a card for aesthetic purposes
    MDCard:
        size_hint: None, None
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        size_hint: (.9,.8)
        elevation: 15
        md_bg_color: [40/255, 10/255, 50/255, 1]
        padding: 60
        spacing: 30

    # Header to appear above Workout naming
    MDLabel:
        text: 'Customize Workout'
        halign: 'center'
        theme_text_color: 'Custom'
        text_color: (150/255, 46/255, 176/255, 1)
        pos_hint: {'center_x':0.5, 'center_y':0.7}
        font_style: 'H3'

    # Text field to prompt user to name their workout
    MDTextField:
        id: workout_name
        hint_text:'Name Workout'
        icon_right: "weight-lifter"
        icon_right_color: app.theme_cls.primary_color
        pos_hint: {'center_x':0.5, 'center_y':0.55}
        size_hint_x: None
        width: 300

    # This button allows user to view exercises focused on arm results on next page
    MDRoundFlatButton:
        text: 'Arm Workout'
        size_hint: (.2,.1)
        pos_hint: {'center_x': 0.3, 'center_y': 0.4}
        on_release: app.arms()
        
    # This button allows user to view exercises focused on chest results on next page
    MDRoundFlatButton:
        text: 'Chest Workout'
        size_hint: (.2,.1)
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        on_release: app.chest()

    # This button allows user to view exercises focused on back results on next page
    MDRoundFlatButton:
        text: 'Back Workout'
        size_hint: (.2,.1)
        pos_hint: {'center_x': 0.7, 'center_y': 0.4}
        on_release: app.shoulder_creation()

    # This button will return user to nav
    MDRectangleFlatIconButton:
        text: 'Return to Nav'
        icon: 'arrow-collapse-left'
        pos_hint: {'center_x': 0.2, 'center_y': 0.2}
        on_release: app.return_to_nav()


"""
