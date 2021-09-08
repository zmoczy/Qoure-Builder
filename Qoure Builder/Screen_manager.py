from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from helpers import *
from DBcom import Login
from DBcom import DBcreateW
from kivymd.uix.datatables import MDDataTable
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.metrics import dp
from kivymd.uix.button import MDRoundFlatButton, MDRoundFlatIconButton, MDRectangleFlatIconButton
from kivymd.uix.picker import MDTimePicker, MDDatePicker
from kivymd.uix.card import MDCard
from kivymd.uix.list import TwoLineListItem
from kivymd.uix.list import MDList
from DBcom import schedule_DB


# Theses are screens that are created on the python to have easier connection with Database
# If the class is empty it means the screen was created in the helpers.py file and referenced
# by using the screen manager.
class LoginScreen(Screen):
    pass


class NavScreen(Screen):
    pass


class ErrorScreen(Screen):
    pass


class NameScreen(Screen):
    pass


# The screen for this section was developed in python instead of the kivy language
class ScheduleScreen(Screen):
    def __init__(self, sc_manager, username, **kwargs):
        super(ScheduleScreen, self).__init__(**kwargs)
        # Link to the Database for the schedule table
        self.scheduler = schedule_DB()
        self.schedule_table = self.scheduler.get_sched(username)
        self.manager = sc_manager

        # This is a card for aesthetics
        self.schedule_card = MDCard(pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                    size_hint=(.9, .8),
                                    elevation=15,
                                    md_bg_color=[40 / 255, 10 / 255, 50 / 255, 1],
                                    padding=60,
                                    spacing=30)

        # This displays the header at the top of the page
        self.schedule_header = MDLabel(text='Scheduled Workouts',
                                       halign='center',
                                       theme_text_color='Custom',
                                       text_color=(170 / 255, 46 / 255, 200 / 255, 1),
                                       pos_hint={'center_x': 0.35, 'center_y': 0.8},
                                       font_style='H4')

        # Adding the widgets to the screen manager
        self.add_widget(self.schedule_card)
        self.add_widget(self.schedule_header)

        # This creates the display list ot show the scheduled workouts in the database
        self.list_view = MDList(pos_hint={'center_x': 0.4, 'center_y': 0.5}, size_hint=(0.6, 0.4))

        # Populating the schedule list from the schedule database table
        for x in self.schedule_table:
            date_time = x[0] + " " + x[1]
            self.workout_display = TwoLineListItem(text=str(x[2]),
                                                   secondary_text=str(date_time),
                                                   size_hint=(.5, .3))
            self.list_view.add_widget(self.workout_display)
        self.add_widget(self.list_view)

        # Creating the buttons and linking to functions to preform
        self.schedule_btn = MDRoundFlatIconButton(text="    Schedule",
                                                  size_hint=(.1, .1),
                                                  pos_hint={'center_x': .8, 'center_y': .5},
                                                  icon='timer',
                                                  on_release=self.press_button_selection)

        self.nav_btn = MDRectangleFlatIconButton(text="Return to Nav",
                                                 pos_hint={'center_x': .2, 'center_y': .2},
                                                 icon='arrow-collapse-left'
                                                 , on_release=self.return_to_nav)

        self.add_widget(self.schedule_btn)
        self.add_widget(self.nav_btn)

    # Functions to change the current screen being displayed
    def return_to_nav(self, instance):
        self.manager.current = 'nav'

    def press_button_selection(self, instance):
        self.manager.current = 'selection'


# The screen for this section was developed in python instead of the kivy language
class SelectionScreen(FloatLayout):
    def __init__(self, username, sc_manager, **kwargs):
        super(SelectionScreen, self).__init__(**kwargs)
        # Initializing screen manager and link to database
        self.manager = sc_manager
        self.user = username
        self.date = ""
        self.time = ""
        self.work_data = schedule_DB()
        self.workout_table = self.work_data.pull_Workouts()

        # This is a card for aesthetics
        self.select_card = MDCard(
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            size_hint=(.9, .8),
            elevation=15,
            md_bg_color=[40 / 255, 10 / 255, 50 / 255, 1],
            padding=60,
            spacing=30)

        # This displays the header for the page
        self.select_header = MDLabel(text='Choose a Workout',
                                     halign='center',
                                     theme_text_color='Custom',
                                     text_color=(170 / 255, 46 / 255, 200 / 255, 1),
                                     pos_hint={'center_x': 0.35, 'center_y': 0.8},
                                     font_style='H4')

        # This is the creation of the data table for users to select what workout to schedule
        self.data_tables = MDDataTable(
            pos_hint={'center_x': 0.35, 'center_y': 0.55},
            size_hint=(0.5, 0.4),
            use_pagination=True,
            check=True,
            column_data=[
                ("Workout", dp(35)),
                ("user", dp(35)),
            ]
            , row_data=[
                self.workout_table[i] for i in range(len(self.workout_table))],
        )

        # Setting up buttons to bring up time/date displays and commit to Database
        self.time_bttn = MDRoundFlatButton(text="Open time picker",
                                           pos_hint={'center_x': .8, 'center_y': .7},
                                           on_release=self.time_picker)

        self.date_bttn = MDRoundFlatButton(text="Open date picker",
                                           pos_hint={'center_x': .8, 'center_y': .5},
                                           on_release=self.date_picker)

        self.submit_btn = MDRoundFlatButton(text="Submit",
                                            pos_hint={'center_x': .8, 'center_y': .3},
                                            on_release=self.commit_sched)

        self.return_bnt = MDRectangleFlatIconButton(text="   Return",
                                                    pos_hint={'center_x': .2, 'center_y': .2},
                                                    icon='arrow-collapse-left'
                                                    , on_release=self.return_to_sched)

        # Adding all the widgets to the screen for display
        self.data_tables.bind(on_check_press=self.check_press)
        self.add_widget(self.select_card)
        self.add_widget(self.select_header)
        self.add_widget(self.data_tables)
        self.add_widget(self.time_bttn)
        self.add_widget(self.date_bttn)
        self.add_widget(self.return_bnt)
        self.add_widget(self.submit_btn)

    # Function to change screen
    def return_to_sched(self, instance):
        self.manager.current = 'sched'

    # Function to commit changes to database
    def commit_sched(self, instance):
        self.work_data.commit_sched(self.user, self.date, self.time, self.work_name)
        self.manager.current = 'nav'

    # Functions to display date/time pickers and links the data to Database
    def date_picker(self, instance):
        date_pick = MDDatePicker(callback=self.got_date)
        date_pick.open()

    def got_date(self, the_date):
        self.date = str(the_date)

    def time_picker(self, instance):
        time_pick = MDTimePicker()
        time_pick.bind(time=self.got_time)
        time_pick.open()

    def got_time(self, picker_widget, the_time):
        self.time = str(the_time)

    # Function to occur when workout selected from datatable
    def check_press(self, instance_table, current_row):
        self.work_name = ""
        self.user_name = ""
        self.user_name = current_row[1]
        self.work_name = current_row[0]


class Create_Workout(FloatLayout):
    def __init__(self, muscle_group, w_name, U_id, sc_manger, **kwargs):
        super(Create_Workout, self).__init__(**kwargs)
        # Linking to Database
        self.excersiseList = []
        self.create_exList = DBcreateW(w_name, U_id)
        self.manager = sc_manger
        lister = self.create_exList.excercise_List(muscle_group)

        # Creation of the datatable where users select exercises to create a workout
        self.data_tables = MDDataTable(
            pos_hint={'center_x': 0.5, 'center_y': 0.6},
            size_hint=(0.7, 0.6),
            use_pagination=True,
            check=True,
            column_data=[

                ("ID", dp(25)),
                ("Exercise", dp(45)),
                ("Muscle Group", dp(23))
            ]
            ,
            row_data=[
                lister[i] for i in range(len(lister))],
        )

        # Adding the datatable to the screen
        self.data_tables.bind(on_check_press=self.check_press)
        self.add_widget(self.data_tables)

        # Creation of buttons and binding them to functions upon release
        create_btn = MDRoundFlatButton(text='Create Workout', pos_hint={'center_x': 0.5, 'center_y': 0.2})
        create_btn.bind(on_release=self.press_button_Create)

        return_btn = MDRoundFlatButton(text='Return to Nav', pos_hint={'center_x': 0.5, 'center_y': 0.1})
        return_btn.bind(on_release=self.press_button_Return)

        # Adding buttons to screen for display
        self.add_widget(create_btn)
        self.add_widget(return_btn)

    # Selects exercises from list on check press
    def check_press(self, instance_table, current_row):
        if current_row in self.excersiseList:
            self.excersiseList.remove(current_row)
        else:
            self.excersiseList.append(current_row)

    # Commits the workout to the database and returns user to nav screen
    def press_button_Create(self, instance):
        self.create_exList.commit_workout(self.excersiseList)
        self.manager.current = 'nav'

    # Returns the user to the nav screen
    def press_button_Return(self, instance):
        self.manager.current = 'nav'


# The screen for this section was developed in python instead of the kivy language
class begin_workout(FloatLayout):
    def __init__(self, username, sc_manager, **kwargs):
        super(begin_workout, self).__init__(**kwargs)
        # Initializing screen manager and database connection
        self.manager = sc_manager
        self.user = username
        self.date = ""
        self.time = ""
        self.work_data = schedule_DB()
        self.workout_table = self.work_data.pull_Workouts()

        # Card used for aesthetic purposes
        self.begin_card = MDCard(
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            size_hint=(.9, .8),
            elevation=15,
            md_bg_color=[40 / 255, 10 / 255, 50 / 255, 1],
            padding=60,
            spacing=30)

        # Displays the header for the screen
        self.select_header = MDLabel(text='Choose a Workout',
                                     halign='center',
                                     theme_text_color='Custom',
                                     text_color=(170 / 255, 46 / 255, 200 / 255, 1),
                                     pos_hint={'center_x': 0.5, 'center_y': 0.8},
                                     font_style='H4')

        # Creation of the datatable for user to select what workout to begin
        self.data_tables = MDDataTable(
            pos_hint={'center_x': 0.5, 'center_y': 0.55},
            size_hint=(0.5, 0.4),
            use_pagination=True,
            check=True,
            column_data=[

                ("Workout", dp(35)),
                ("user", dp(35)),
            ]
            , row_data=[
                self.workout_table[i] for i in range(len(self.workout_table))],
        )

        # Setting up return button
        self.return_bnt = MDRectangleFlatIconButton(text="   Return",
                                                    pos_hint={'center_x': .5, 'center_y': .2},
                                                    icon='arrow-collapse-left'
                                                    , on_release=self.return_to_nav)

        # Adding widgets to the screen for display
        self.data_tables.bind(on_check_press=self.check_press)
        self.add_widget(self.begin_card)
        self.add_widget(self.select_header)
        self.add_widget(self.data_tables)
        self.add_widget(self.return_bnt)

    def return_to_nav(self, instance):
        self.manager.current = 'nav'

    # Function to occur on checking a box on the datatable
    def check_press(self, instance_table, current_row):
        self.work_name = ""
        self.user_name = ""
        self.user_name = current_row[1]
        self.work_name = current_row[0]
        self.view = view_workout(self.user_name, self.work_name, self.manager)
        screen = Screen(name="view")
        screen.add_widget(self.view)
        self.manager.add_widget(screen)
        self.manager.current = 'view'


# The screen for this section was developed in python instead of the kivy language
class view_workout(FloatLayout):
    def __init__(self, username, w_name, sc_manager, **kwargs):
        super(view_workout, self).__init__(**kwargs)
        # Setting up database connection and screen manager
        self.manager = sc_manager
        self.user = username
        self.w_Name = w_name
        self.work_data = schedule_DB()
        self.workout_table = self.work_data.pull_workout_excersises(self.user, self.w_Name)

        # This Card is in the background for aesthetics
        self.begin_card = MDCard(
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            size_hint=(.9, .8),
            elevation=15,
            md_bg_color=[40 / 255, 10 / 255, 50 / 255, 1],
            padding=60,
            spacing=30)

        # Displays the header for this screen
        self.select_header = MDLabel(text='View Workout',
                                     halign='center',
                                     theme_text_color='Custom',
                                     text_color=(170 / 255, 46 / 255, 200 / 255, 1),
                                     pos_hint={'center_x': 0.5, 'center_y': 0.8},
                                     font_style='H4')

        # Initialization of datatable users check off what workout they have completed
        self.data_tables = MDDataTable(
            pos_hint={'center_x': 0.5, 'center_y': 0.55},
            size_hint=(0.5, 0.4),
            use_pagination=True,
            check=True,

            # name column, width column, sorting function column(optional)
            column_data=[

                ("ID", dp(25)),
                ("excersise", dp(35)),
            ]
            , row_data=[
                self.workout_table[i] for i in range(len(self.workout_table))],
        )

        self.return_bnt = MDRectangleFlatIconButton(text="   Return",
                                                    pos_hint={'center_x': .5, 'center_y': .2},
                                                    icon='arrow-collapse-left'
                                                    , on_release=self.return_to_nav)

        # Adding widgets to screen for display
        self.data_tables.bind(on_check_press=self.check_press)
        self.add_widget(self.begin_card)
        self.add_widget(self.select_header)
        self.add_widget(self.data_tables)
        self.add_widget(self.return_bnt)

    def return_to_nav(self, instance):
        self.manager.current = 'nav'

    # Function to do nothing on check press
    def check_press(self, instance_table, current_row):
        self.work_name = ""
        self.user_name = ""
        self.user_name = current_row[1]
        self.work_name = current_row[0]


# This is where the application is ran from
class QuoreApp(MDApp):

    def build(self):
        # Sets the theme for the application
        self.theme_cls.primary_palette = 'Purple'
        self.theme_cls.primary_hue = '200'
        self.theme_cls.theme_style = 'Dark'

        self.screen_str = Builder.load_string(screen_helper)
        self.screen_Manager = ScreenManager()

        self.screen_Manager.add_widget(LoginScreen(name='login'))
        self.screen_Manager.add_widget(NavScreen(name='nav'))
        self.screen_Manager.add_widget(ErrorScreen(name='error'))
        self.screen_Manager.add_widget(NameScreen(name='name'))

        # Initalizes the screen from the screen_helper string in the helper.py file
        return self.screen_Manager

    # This is the function used to verify user credentials, if invalid will direct to an error screen
    def verfy_user(self):
        self.LoginTable = Login()
        username = self.screen_Manager.get_screen('login').ids.username_field.text
        password = self.screen_Manager.get_screen('login').ids.password_field.text

        self.login_successful = self.LoginTable.verifyUser(username, password)
        if self.login_successful == True:
            U_Id = username

            # Sets up screen managers to be used on the python screens
            self.selection = SelectionScreen(username, self.screen_Manager)
            screen = Screen(name="selection")
            screen.add_widget(self.selection)
            self.screen_Manager.add_widget(screen)
            self.screen_Manager.current = 'nav'

            self.sched = ScheduleScreen(self.screen_Manager, username)
            screen = Screen(name="sched")
            screen.add_widget(self.sched)
            self.screen_Manager.add_widget(screen)

            self.begin = begin_workout(username, self.screen_Manager)
            screen = Screen(name="begin")
            screen.add_widget(self.begin)
            self.screen_Manager.add_widget(screen)

        else:
            self.screen_Manager.get_screen('login').ids.username_field.text = ''
            self.screen_Manager.get_screen('login').ids.password_field.text = ''
            self.screen_Manager.get_screen('error').ids.error_message.text = 'Login Failed'
            self.screen_Manager.current = 'error'

    # This function is used for creating user credentials and storing them into the database
    def create_user(self):
        self.LoginTable = Login()

        # Adds new users to the database for future login
        username = self.screen_Manager.get_screen('login').ids.username_field.text
        password = self.screen_Manager.get_screen('login').ids.password_field.text
        self.LoginTable.createUser(username, password)

        # Sets up screen managers to be used on the python screens
        self.selection = SelectionScreen(username, self.screen_Manager)
        screen = Screen(name="selection")
        screen.add_widget(self.selection)
        self.screen_Manager.add_widget(screen)
        self.screen_Manager.current = 'nav'

        self.begin = begin_workout(username, self.screen_Manager)
        screen = Screen(name="begin")
        screen.add_widget(self.begin)
        self.screen_Manager.add_widget(screen)

        self.sched = ScheduleScreen(self.screen_Manager, username)
        screen = Screen(name="sched")
        screen.add_widget(self.sched)
        self.screen_Manager.add_widget(screen)

    # Swaps screen to name screen
    def switch_Workoutscreen(self):
        self.screen_Manager.current = 'name'

    # Swaps screen to schedule screen
    def switch_schdule(self):
        self.screen_Manager.current = 'sched'

    # Swaps screen to begin screen for Begin Workout
    def switch_begin(self):
        self.screen_Manager.current = 'begin'

    # Swaps screen to navagation screen
    def return_to_nav(self):
        self.screen_Manager.current = 'nav'

    # The following 3 functions are used to communicate with database during workout creation
    # for easier query functionality.
    def shoulder_creation(self):
        w_name = self.screen_Manager.get_screen('name').ids.workout_name.text
        muscle_group = 6
        U_Id = self.screen_Manager.get_screen('login').ids.username_field.text
        if w_name == "":
            self.screen_Manager.get_screen('error').ids.error_message.text = 'Empty Workout Name'
            self.screen_Manager.current = 'error'
        else:
            self.create = Create_Workout(muscle_group, w_name, U_Id, self.screen_Manager)
            screen = Screen(name="create")
            screen.add_widget(self.create)
            self.screen_Manager.add_widget(screen)
            self.screen_Manager.current = 'create'

    def arms(self):
        w_name = self.screen_Manager.get_screen('name').ids.workout_name.text
        muscle_group = 4
        U_Id = self.screen_Manager.get_screen('login').ids.username_field.text
        if w_name == "":
            self.screen_Manager.get_screen('error').ids.error_message.text = 'Empty Workout Name'
            self.screen_Manager.current = 'error'
        else:
            self.create = Create_Workout(muscle_group, w_name, U_Id, self.screen_Manager)
            screen = Screen(name="create")
            screen.add_widget(self.create)
            self.screen_Manager.add_widget(screen)
            self.screen_Manager.current = 'create'

    def chest(self):
        w_name = self.screen_Manager.get_screen('name').ids.workout_name.text
        muscle_group = 5
        U_Id = self.screen_Manager.get_screen('login').ids.username_field.text
        if w_name == "":
            self.screen_Manager.get_screen('error').ids.error_message.text = 'Empty Workout Name'
            self.screen_Manager.current = 'error'
        else:
            self.create = Create_Workout(muscle_group, w_name, U_Id, self.screen_Manager)
            screen = Screen(name="create")
            screen.add_widget(self.create)
            self.screen_Manager.add_widget(screen)
            self.screen_Manager.current = 'create'


QuoreApp().run()
