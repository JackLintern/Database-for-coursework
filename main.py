import sqlite3
import math
con = sqlite3.connect('SnakeDB.db')
cursor = con.cursor()
currentGameNumber = 0


#Array to store move numbers when food was collected

MoveNum = 0
def onetime():
  creationsql = '''
  CREATE DATABASE 'SnakeDB';
  '''
  
  cursor.execute(creationsql)
  con.commit()
def createtable():
  DataTableSQL = "CREATE TABLE 'Data'('Gamenumber','MoveID','Length','Currentmap','Surrounding8','Distance','ReferenceMap')"
  ScoreTableSQL = "CREATE TABLE 'Score'('Gamenumber','MoveID', 'Movesuntildead', 'Movesuntilfood', 'CloserToFood', 'DirectionPicked', 'Score')"
  cursor.execute(ScoreTableSQL)
  con.commit()

def Datainsert(CurrentMap, RealMap, DirectionToFood):
  #CURRENT MAP SHOULD BE AFTER CONVERTED TO SRING FROM ARRAY
  #REAL MAP SHOULD BE MAP AS ARRAY
  Surrounding8 = GetSurrounding8(RealMap)
  DataValues = '''
  INSERT INTO `Data`  VALUES
  ('''+ currentGameNumber + ''', '''+GetMoveID(currentGameNumber)+''', '''+GetLength(CurrentMap)+''', '''+CurrentMap+''','''+Surrounding8+''','''+GetDistance(RealMap)+''','''+ReferenceMap(Surrounding8, DirectionToFood)+''')
  '''
  cursor.execute(DataValues)
  con.commit()

def Scoreinsert(MoveID, TotalMoves, Map, LastMap):
  ScoreValues = '''
  INSERT INTO `Score`  VALUES
  ('''+currentGameNumber+''','''+MoveID+''','''+str(int(TotalMoves)-int(MoveID))+''', '''+MovesUntilDead(MoveID)+''', '''+CloserToFood(Map, LastMap)+''')
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
  return(str(int(cursor.fetchall()[0][0])+1))
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

def MapArrayToString(map):
  StringMap = ""
  for i in range(len(map)):
    for k in range(len(map)):
      StringMap = StringMap + map[i][k] 


def MovesUntilDead(MoveID):
  return(str(TotalMoves-MoveID))
def MovesUntilFood(MoveID):
  for i in range(len(FoodMoves)):
    if MoveID <= FoodMoves[i]:
      return(str(int(FoodMoves[i])-int(MoveID)))
def CloserToFood(map, lastmap):
  if GetDistance(map) > GetDistance(lastmap):
    return "True"
  else:
    return "False"
##################################################################
def PickAMove(Surrounding8, ):
  pass
def GetDirectionToFood(map):
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
  if math.sqrt((xhead-xfood)*(xhead-xfood)) < math.sqrt((yhead-yfood)*(yhead-yfood)):
    if yhead-yfood > 0:
      return("w")
    else:
      return("s")
  else:
    if xhead-xfood > 0:
      return("a")
    else:
      return("d")
  
def GenerateScore(MovesUntilDead, MovesUntilFood, CloserToFood):
  score = 0
  score = (int(MovesUntilDead)*int(MovesUntilDead))+MovesUntilFood
  if bool(CloserToFood) == True:
    score = score * 2
  return(score)

#################################################################
def ReferenceMap(Surrounding8, DirectionToFood):
  return(str(Surrounding8) + str(DirectionToFood))
  
def Move():
  #Datainsert()
  pass
exit = False
#temporary
#Start of run time
while exit == False:
  TotalMoves = 0
  Alive = True
  FoodMoves = []
  currentGameNumber = GetGameNumber()
  while Alive == True:
    surrounding8 = GetSurrounding8(map)
    directiontofood = GetDirectionToFood(map)
    refmap = ReferenceMap(surrounding8, directiontofood)
    arraymap = MapArrayToString(map)
    TotalMoves += 1
    PickAMove(refmap)

#TODO: DirectionPickedFunction