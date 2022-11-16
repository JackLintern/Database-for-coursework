import sqlite3
con = sqlite3.connect('SnakeDB.db')
cursor = con.cursor()
currentGameNumber = 0
MoveNum = 0
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

def Datainsert(CurrentMap, RealMap):
  #CURRENT MAP SHOULD BE AFTER CONVERTED TO SRING FROM ARRAY
  #REAL MAP SHOULD BE MAP AS ARRAY
  DataValues = '''
  INSERT INTO `Data`  VALUES
  ('''+ currentGameNumber + ''', '''+GetMoveID(currentGameNumber)+''', '''+GetLength(CurrentMap)+''', '''+CurrentMap+''','''+GetSurrounding8(RealMap)+''','''+GetDistance(RealMap)+''')
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
  #CHECK THIS WORKS, MAY HAVE LOCAL VAR REF BEFORE ASSIGNMENT OR NOT UPDATING GLOBAL VAR JUST LOCAL
  
  
def GetLength(map):
  #SUBMIT MAP AFTER CONVERTED TO STRING FROM ARRAY
  count = 0
  for i in range(len(map)):
   if map[i] == 1 or map[i] == 5:
        count +=1
  return(count)
  #https://replit.com/@linternj137/Encrypttest#main.py
  
def GetMoveID(gamenum):
  MoveIDSQL = '''
      SELECT MoveID FROM Data WHERE Gamenumber = '''+gamenum+''' ORDER BY Gamenumber DESC LIMIT 1
      '''
  # Select the latest game number, add one to it for the new gamenumber
  

  cursor.execute(MoveIDSQL)
  con.commit()
  return(str(int(cursor.fetchall()[0][0])+1))

def GetSurrounding8(map):
  #MAP SHOULD BE ARRAY
  Found = False
  x = 0
  y = 0
  for i in range(len(map)):
    for k in range(len(map[i])):
      if map[i][k] == "5":
        Found = True
        x = k
        y = i
      if Found == True:
        break
  return((""+map[y-1][x-1]+""+map[y-1][x]+""+map[y-1][x+1]+""+map[y][x-1]+""+map[y][x]+""+map[y-1][x+1]+""+map[y+1][x-1]+""+map[y+1][x]+""+map[y+1][x+1]+""))
        
def GetDistance(map):
  #MAP SHOULD BE ARRAY
  Found = False
  xhead = 0
  yhead = 0
  for i in range(len(map)):
    for k in range(len(map[i])):
      if map[i][k] == "5":
        Found = True
        xhead = k
        yhead = i
      if Found == True:
        break
  Found1 = False
  xfood = 0
  yfood = 0
  for i in range(len(map)):
    for k in range(len(map[i])):
      if map[i][k] == "9":
        Found1 = True
        xfood = k
        yfood = i
      if Found1 == True:
        break
  return(str(math.sqrt(((xfood-xhead)*(xfood-xhead)+(yfood-yhead)*(yfood-yhead)))))



  
def move():
  #Datainsert()
  pass
  
#Start of run time


#TODO: Convert array map to string