import sqlite3
con = sqlite3.connect('SnakeDB.db')
cursor = con.cursor()


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
  ('''"value1", "etc."''')
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
  rows = cursor.fetchall() 
  HighNum = rows[0]