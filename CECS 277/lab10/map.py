""" Map for Dungeons and Monsters

Written by: Omar Juarez, Yunjae Cho
Date: Fall 2024

"""

class Map:
    """Represents a Map.
    Attributes:
        _instance (static Map) - the single Map instance
        _initialized (static bool) - if a Map instance is initialized
    """
    _instance = None
    _initialized = False

    def __new__(cls):
        """If the map hasn't been constructed, we construct it and store
        it in the instance class variable.
        Args:
            cls
        Returns:
            instance variable with map in it
        """
        if cls._instance is None:
             cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        """Create and fill the 2D map list from the file contents.
        The 2D list is filled with all False values. The map stores
        the contents of the file and the revealed list is used to
        determine whether the contents of the map are displayed or not.
        Args:
            self
        Returns:
            none
        """
        if not self._initialized:
            self._initialized = True

            # load initial map
            file = open("map.txt")
            self._map = []
            for line in file.readlines():
                row = []
                for char in line:
                    # exclude new line
                    if char != '\n':
                        row.append(char)
                    
                self._map.append(row)
            
            # initiate a 2d list with False bool value
            self._revealed = [[False for x in range(len(self._map[0]))] for y in range(len(self._map))] 
    
    def __getitem__(self, row):
        """- overloaded operator [] - returns the specified row
        from the map.
        Args:
            self (Map)
            row (int) - the row num to get items
        Returns:
            a string list of the specified row from the map
        """
        return self._map[row]
    
    def __len__(self):
        """returns the number of rows in the map list
        Args:
            self (Map)
        Returns:
            an integer for the number of rows in the map list
        """
        return len(self._map)
    
    def show_map(self, loc):
        """Shows the map represented in string format of a 5 x 5 matrix
        of characters where revealed locations are the characters from the map,
        unrevealed locations are x's and the hero's location is a *.
        Args:
            self (Map)
            loc (int []): the location of the Hero
        Returns:
            the map as a string in the format of a 5 x 5 matrix of characters"""
        for i in range(len(self._map)):
            for j in range(len(self._map[i])):
                s = self._map[i][j]
                # the Hero location
                if i == loc[0] and j == loc[1]:
                    s = '*'
                # the start location
                elif i == 0 and j == 0:
                    pass
                # if the location is not revealed, print 'x'
                elif not self._revealed[i][j]:
                    s = 'x'
                print(s, end=' ')
            print()
    
    def reveal(self, loc):
        """sets the value in the 2D revealed list at the specific location to True.
        Args:
            self (Map)
            loc (int []): the location to reveal
        Returns:
            none
        """
        self._revealed[loc[0]][loc[1]] = True
    
    def remove_at_loc(self, loc):
        """overwrites the character in the map list at the specified location with an n.
        Args:
            self (Map)
            loc (int []): the location to remove
        Returns:
            none
        """
        self._map[loc[0]][loc[1]] = 'n'