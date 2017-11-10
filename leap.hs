data Weekdays = 
   Monday | Tuesday | Wednesday | Thursday | Friday | Saturday | Sunday
   deriving (Enum,Show)

data Months =
   Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec
   deriving (Enum,Read)

leap :: Int -> Bool
leap n 
   |((n `mod` 4) == 0) && ((n `mod` 100) /= 0) = True
   |((n `mod` 100) == 0) && ((n `mod` 400) == 0) = True
   |otherwise = False 

mLengths :: Int -> [Int]
mLengths n
   |leap n == True = [31,29,31,30,31,30,31,31,30,31,30,31]
   |otherwise = [31,28,31,30,31,30,31,31,30,31,30,31]

numDays :: (Int,Months,Int) -> Int
numDays (1,Jan,1752) = 0
numDays (a,b,c)
   |leap c == True = 366 + numDays(a,b,c-1)
   |otherwise = 365 + numDays(a,b,c-1)


