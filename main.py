import sqlite3
con = sqlite3.connect('SnakeDB.db')
cursor = con.cursor()
currentGameNumber = 0

def onetime():
  creationsql = '''
  CREATE DATABASE 'SnakeDB';
  '''
  
  cursor.execute(creationsql)
  con.commit()
def createtable():
  DataTableSQL = "CREATE TABLE 'Data'('Gamenumber','MoveID','Length','Currentmap','Surrounding8','Distance')"
  ScoreTableSQL = "CREATE TABLE 'Score'('Gamenumber','MoveID', 'Movesuntildead', 'Movesuntilfood', 'CloserToFood', 'DirectionPicked')"
  cursor.execute(ScoreTableSQL)
  con.commit()

def Datainsert():
  DataValues = '''
  INSERT INTO `Data`  VALUES
  ('''+ currentGameNumber + ''', "etc.")
  '''
  cursor.execute(DataValues)
  con.commit()

def Scoreinsert():
  ScoreValues = '''
  INSERT INTO `Score`  VALUES
  ('''"value1", "etc."''')
  '''
  cursor.execute(ScoreValues)
  con.commit()
def GetGameNumber():
  GameNumberSQL = '''
      SELECT Gamenumber FROM Data ORDER BY Gamenumber DESC LIMIT 1
      '''
  # Select the latest game number, add one to it for the new gamenumber
  

  cursor.execute(GameNumberSQL)
  con.commit()
  currentGameNumber = str(int(cursor.fetchall()[0][0])+1)
def GetLength():
  pass
  #https://replit.com/@linternj137/Encrypttest#main.py
  
#Start of run time
GetGameNumber()