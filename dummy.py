import os
import pyttsx3 as p
import sys, time 


for char in "Welcome to my chatbot": 
  print(char , end='') 
  sys.stdout.flush() 
  time.sleep(0.05) 
p.speak("Welcome to my chatbot")   

while True: 
  print("\n") 
  for char in "what can I do for you? ": 
   print(char , end='') 
   sys.stdout.flush() 
   time.sleep(0.05) 
  p.speak("what can I do for you ?  ")
  userinput = input()

  if ("run" in userinput and ("Chrome" in userinput or ("Google" in userinput))) or ("open" in userinput and ("Chrome" in userinput or ("Google" in userinput))) or  ("launch" in userinput and ("Chrome" in userinput or ("Google" in userinput))):
    p.speak("chrome gets opened soon")
    os.system("chrome")        
  elif ("run" in userinput and ("Notepad" in userinput)) or ("execute" in userinput and ("Notepad" in userinput)) or ("open" in userinput and ("Notepad" in userinput)) or ("launch" in userinput and ("Notepad" in userinput)) :
    p.speak("notepad will be launched")
    os.system("notepad")       
  elif (("run" in userinput) and ("Player" in userinput or ("Media" in userinput))) or (("execute" in userinput) and ("Player" in userinput or ("Media" in userinput))) or (("open" in userinput) and ("Player" in userinput or ("Media" in userinput))) or (("launch" in userinput) and ("Player" in userinput or ("Media" in userinput))) :        
    p.speak("media player is ready to rock")
    os.system("wmplayer")
  elif (("run" in userinput) and ("Access" in userinput or ("MSAccess" in userinput))) or (("execute" in userinput) and ("Access" in userinput or ("MSAccess" in userinput))) or (("open" in userinput) and ("Access" in userinput or ("MSAccess" in userinput))) or (("launch" in userinput) and ("Access" in userinput or ("MSAccess" in userinput))) :       
    p.speak("MS Access gets launched")
    os.system("MSACCESS")
  elif (("run" in userinput) and ("Excel" in userinput or ("MSExcel" in userinput))) or (("execute" in userinput) and ("Excel" in userinput or ("MSExcel" in userinput))) or (("open" in userinput) and ("Excel" in userinput or ("MSExcel" in userinput))) or (("launch" in userinput) and ("Excel" in userinput or ("MSExcel" in userinput))):       
    p.speak("Enjoy creating new Microsoft excel now")
    os.system("EXCEL")
  elif (("run" in userinput) and ("Sharepoint" in userinput or ("Sharepoint Workspace" in userinput))) or (("execute" in userinput) and ("Sharepoint" in userinput or ("Sharepoint Workspace" in userinput))) or (("open" in userinput) and ("Sharepoint" in userinput or ("Sharepoint Workspace" in userinput))) or (("launch" in userinput) and ("Sharepoint" in userinput or ("Sharepoint Workspace" in userinput))) :       
    p.speak("Sharepoint Workspace gets opened now")
    os.system("GROOVE")
  elif (("run" in userinput) and ("Microsoft Infopath" in userinput or ("MS Infopath" in userinput))) or (("execute" in userinput) and ("Microsoft Infopath" in userinput or ("MS Infopath" in userinput))) or (("open" in userinput) and ("Microsoft Infopath" in userinput or ("MS Infopath" in userinput))) or (("launch" in userinput) and ("Microsoft Infopath" in userinput or ("MS Infopath" in userinput))) :       
    p.speak("Microsoft infopath gets opened now")
    os.system("INFOPATH")
  elif (("run" in userinput) and ("Microsoft Publication" in userinput or ("MS Publication" in userinput))) or (("execute" in userinput) and ("Microsoft Publication" in userinput or ("MS Publication" in userinput))) or (("open" in userinput) and ("Microsoft Publication" in userinput or ("MS Publication" in userinput))) or (("launch" in userinput) and ("Microsoft Publication" in userinput or ("MS Publication" in userinput))):       
    p.speak("Create new Microsoft Publication now")
    os.system("MSPUB")
  elif (("run" in userinput) and ("Microsoft Onenote" in userinput or ("Onenote" in userinput))) or (("execute" in userinput) and ("Microsoft Onenote" in userinput or ("Onenote" in userinput))) or (("open" in userinput) and ("Microsoft Onenote" in userinput or ("Onenote" in userinput))) or (("launch" in userinput) and ("Microsoft Onenote" in userinput or ("Onenote" in userinput))):       
    p.speak("Microsoft Onenote will launch soon")
    os.system("ONENOTE")
  elif (("run" in userinput) and ("Microsoft Outlook" in userinput or ("Outlook" in userinput))) or (("execute" in userinput) and ("Microsoft Outlook" in userinput or ("Outlook" in userinput))) or (("open" in userinput) and ("Microsoft Outlook" in userinput or ("Outlook" in userinput))) or (("launch" in userinput) and ("Microsoft Outlook" in userinput or ("Outlook" in userinput))):       
    p.speak("Microsoft Outlook will launch shortly")
    os.system("OUTLOOK")
  elif (("run" in userinput) and (("MS Powerpoint" in userinput) or ("Microsoft Powerpoint" in userinput) or ("Powerpoint" in userinput))) or (("execute" in userinput) and (("MS Powerpoint" in userinput) or ("Microsoft Powerpoint" in userinput) or ("Powerpoint" in userinput))) or (("open" in userinput) and (("MS Powerpoint" in userinput) or("Microsoft Powerpoint" in userinput) or ("Powerpoint" in userinput))) or (("launch" in userinput) and (("MS Powerpoint" in userinput) or ("Microsoft Powerpoint" in userinput) or ("Powerpoint" in userinput))):       
    p.speak("New Microsoft Powerpoint is ready to create")
    os.system("POWERPNT")
  elif (("run" in userinput) and (("MS Word" in userinput) or ("Microsoft Word" in userinput) or ("Word Document" in userinput))) or (("execute" in userinput) and (("MS Word" in userinput) or ("Microsoft Word" in userinput) or ("Word Document" in userinput))) or (("open" in userinput) and (("MS Word" in userinput) or("Microsoft Word" in userinput) or ("Word Document" in userinput))) or (("launch" in userinput) and (("MS Word" in userinput) or ("Microsoft Word" in userinput) or ("Word Document" in userinput))):       
    p.speak("Enjoy creating new Microsoft Word Document")
    os.system("WINWORD")
  elif ("run" in userinput and ("Internet Explorer" in userinput)) or ("execute" in userinput and ("Internet Explorer" in userinput)) or ("open" in userinput and ("Internet Explorer" in userinput)) or ("launch" in userinput and ("Internet Explorer" in userinput)) :
    p.speak("Internet Explorer will be launched soon")
    os.system("iexplore")  
  elif ("run" in userinput and ("Unity" in userinput)) or ("execute" in userinput and ("Unity" in userinput)) or ("open" in userinput and ("Unity" in userinput)) or ("launch" in userinput and ("Unity" in userinput)) :
    p.speak("Unity gamebox will be launched soon")
    os.system("Unity")  
  elif ("run" in userinput and ("Books" in userinput)) or ("execute" in userinput and ("Books" in userinput)) or ("open" in userinput and ("Books" in userinput)) or ("launch" in userinput and ("Books" in userinput)) :
    p.speak("Get ready to download your favourite books from Google Books downloader ")
    os.system("gbooks")  
  elif ("run" in userinput and ("File Explorer" in userinput)) or ("execute" in userinput and ("File Explorer" in userinput)) or ("open" in userinput and ("File Explorer" in userinput)) or ("launch" in userinput and ("File Explorer" in userinput)) :
    p.speak("Look out your files and folders in file explorer ")
    os.system("explorer")  
  elif ("run" in userinput and ("Microsoft Edge" in userinput)) or ("execute" in userinput and ("Microsoft Edge" in userinput)) or ("open" in userinput and ("Microsoft Edge" in userinput)) or ("launch" in userinput and ("Microsoft Edge" in userinput)) :
    p.speak("Microsoft Edge will be launched soon")
    os.system("msedge") 
  elif ("run" in userinput and ("Paint" in userinput)) or ("execute" in userinput and ("Paint" in userinput)) or ("open" in userinput and ("Paint" in userinput)) or ("launch" in userinput and ("Paint" in userinput)) :
    p.speak("Paint will be opened soon")
    os.system("mspaint")  
  elif (("run" in userinput) and ("Calculator" in userinput or ("Calc" in userinput))) or (("execute" in userinput) and ("Calculator" in userinput or ("Calc" in userinput))) or (("open" in userinput) and ("Calculator" in userinput or ("Calc" in userinput))) or (("launch" in userinput) and ("Calculator" in userinput or ("Calc" in userinput))):       
    p.speak("Enjoy creating Calculations now")
    os.system("calc")
  elif ("exit" in userinput) or ("quit" in userinput):
    print("\n") 
    for char in "Thanks for opting me . Share your smiles ": 
     print(char , end='') 
     sys.stdout.flush() 
     time.sleep(0.05) 
    p.speak("Thanks for opting me . Share your smiles")
    break
  else:
    print("don't support")
 
