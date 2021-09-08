# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 11:29:47 2020

@author: zmocz
"""
import psycopg2 
import collections



con = psycopg2.connect(host = "localhost",database = "gymapp",user = "postgres",password = "0521")     
cur = con.cursor()
isLoggedin = False



class Login:
    
    def createUser(self,email, password):
        cur.execute("""INSERT INTO public."LoginInfo"(email, "Password")VALUES (%s, %s);""", (email,password))        
        con.commit()
        #creates user and updates Database
        

    def verifyUser(self,email, password):
        isLoggedin = False
        cur.execute("""SELECT * FROM public."LoginInfo"ORDER BY "Password" ASC """)
        data = cur.fetchall()
        i = 0
        for x in data: #traverse usernames looking for a password and username match
            username = data[i][0]
            if username == email:
                check_Pass = data[i][1]
                if password == check_Pass:
                    isLoggedin = True
            i+=1
        
        return isLoggedin #return boolean value to determine login status
    




class DBcreateW():
    
    def __init__(self,username,wname):
        self.user = username
        self.wname = wname
        #global varaibales for defining workouts
    def excercise_List(self, muscle_group):
         cur.execute("""SELECT * FROM public."exercises"ORDER BY "enumber" ASC """)
         data = cur.fetchall()
         i = 0
         nameList = []
         excer = []
         for x in data:
        
             enum = data[i][0]
             ename = data[i][1]
             ereps = data[i][2]
             if ereps == muscle_group: #traverse excersie data looking for excerises that match the desired muscle group
                 excer.append(str(enum))
                 excer.append(str(ename))
                 if  muscle_group == 5:
                     excer.append("Chest")
                 elif muscle_group == 6:
                     excer.append("Shoulder/Back")
                 elif muscle_group == 4:
                    excer.append("Triceps/Biceps")
                 nameList.append(excer)
             excer = []
             
             i += 1
         return nameList
     
    def commit_workout(self, excer_list):
        i =0 #once excersises are chosen update the workout list
        for x in excer_list:
            cur.execute("""INSERT INTO public."Workout"(username, "wName", "excersiseId")VALUES (%s, %s, %s);""", (self.user, self.wname , str(excer_list[i][0])))
            i += 1
        con.commit()

class schedule_DB():
    
    
    def pull_Workouts(self):
         cur.execute("""SELECT * FROM public."Workout" """)
         data = cur.fetchall()
         current_W = []
         workout_table =[]
         i =0
         flag = 0
         for x in data: #traverse workouts looking for name match and excersise match
             uname = data[i][0]
             wName = data[i][1]
             current_W.append(uname)
             current_W.append(wName)
             for elem in workout_table: 
                 if collections.Counter(elem) == collections.Counter(current_W) : 
                     flag = 1
             if flag == 0:
                 workout_table.append(current_W)
             current_W = []
             i += 1
             flag = 0
         
         return workout_table #return list of workouts
     
    def commit_sched(self,username,date,time,work_name):
        cur.execute("""INSERT INTO public."Schedule"("Username", "Date", "Time", "Workout_name")VALUES (%s, %s, %s,%s);""", (username, date , time,work_name))
        con.commit() #commit schdule data to database
        
    def get_sched(self,username):
        cur.execute("""SELECT * FROM public."Schedule" """)
        data = cur.fetchall()
        i = 0
        temp = []
        schedules = []
        for x in data: #retrive date and time for specfic schdule
           if data[i][0] == username:
               date = data[i][1]
               time = data[i][2]
               W_name = data[i][3]
               temp.append(date)
               temp.append(time)
               temp.append(W_name)
               schedules.append(temp)
           i += 1
           temp = []
        return schedules #return schdule in date time format
    
    def pull_workout_excersises(self,user,W_name):
        cur.execute("""SELECT * FROM public."Workout" """)
        data = cur.fetchall()
        i =0
        excersises = []
        for x in data: #find the desired workout
            uname = data[i][1]
            wName = data[i][0]
            if str(uname) == user and str(wName) == W_name:
                
                e_id = data[i][2]
                excersises.append(e_id)
            i += 1       
        cur.execute("""SELECT * FROM public."exercises"ORDER BY "enumber" ASC """)
        data = cur.fetchall()
        i =0
        ex_list = []
        temp = []
        for x in data: #find the excerises tied to the specfic workout
            enum = data[i][0]
            if str(enum) in excersises:
                temp.append(data[i][0])
                temp.append(data[i][1])
                ex_list.append(temp)
                temp = []
            i += 1
        return ex_list #returns the list of excerises 

        