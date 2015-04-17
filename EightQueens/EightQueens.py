#!/usr/bin/python
# William Thing
# Eight Queens
#
# Still in-progress
#

class EightQueensBoard:
   __max_x = 8
   __max_y = 8
   __queens = []
   
   def __init__(self):
      return
      
   #  pre:  assume resize method passes
   #  post: check to see if all queens can exist on the board
   #        remove all queens that cannot exist on resized table   
   def resize_check(self):
      for i in range(len(self.__queens)):
         print i
         print 'size', len(self.__queens)
         check = self.__queens[i]
         if (check.get_x > self.__max_x or check.get_y > self.__max_y):
            self.__queens.remove(check)
            i -= 1
            print 'this is i', i
            
   #  post: changes board size to given n by n, unless n = 0
   #        then does nothing
   def resize(self, n):
      if n == 0: return
      self.__max_x = n
      self.__max_y = n
      self.resize_check()
   
   #  post: prints how many Queens are on the board and size of board.
   #        returns the amount of Queens on the board.
   def about(self):
      print "There are %d Queens on the board." % len(self.__queens)
      print "The size of board is %d by %d" % (self.__max_x, self.__max_y)
      return len(self.__queens)
   
   #  post: add given Queen to the board   
   def add(self, queen):
      self.__queens.append(queen)
   
   #  pre:  assume there are Queens on the board
   #  post: returns True if all Queens are not at the same location and can attack,
   #        otherwise return False.  
   def can_attack(self):
      free_queens = len(self.__queens)
      for queen in range(len(self.__queens)):
         free_queens -= 1
         for other in range(free_queens):
            if self.__queens[queen].__cmp__(self.__queens[queen+other+1]) == 0:
               return False
      return True

# named Point because made more sense, but could change to Queen
# But for now interchangeable in references
class Point:
   __x = 0
   __y = 0
   
   #  pre:  takes in a given x and y coordinate
   #  post: constructs a Point object with coordinates x, y
   def __init__(self, x, y):
      self.__x = x
      self.__y = y
   
   #  post: moves this Point to another given location   
   def move(self, a, b):
      self.__x = a;
      self.__y = b;
   
   #  post: returns x-coordinate
   def get_x(self):
      return self.__x
      
   #  post: returns y-coordinate   
   def get_y(self):
      return self.__y      
      
   #  post: return printable string representation
   def __str__(self):
      return 'Point (%d, %d)' % (self.__x, self.__y)
   
   #  pre:  takes in given Point other
   #  post: return a new Point that is the addition of both this 
   #        and other Point 
   def __add__(self, other):
      return Point(self.__x + other.__x, self.__y + other.__y)
   
   #  post: return the negative if this Point is greater, positive
   #        if other Point is greater, and zero if there equal   
   def __cmp__(self, other):
      if (self.__x == other.__x and self.__y == other.__y):
         return 0
      else:
         diff = (other.__x - self.__x) + (other.__y - self.__y)
         if (diff == 0):
            return -1
         else :
            return diff
      
      
def main():
   q = EightQueensBoard()
   q.about()
   pointy = Point(10, 20)
   pointy2 = Point(20, 10)
   print pointy
   print pointy2
   pointy3 = pointy.__add__(pointy2)
   print pointy3
   pointy3.move(4, 4)
   print pointy3
   print pointy3.__cmp__(pointy)
   
   q.add(pointy)
   q.add(pointy2)
   q.add(pointy3)
   q.add(pointy3)
   print q.can_attack()
   # need to fix methods below because of errors
   #q.resize(6)	
   #q.about()
   

   
if __name__ == "__main__": main()
