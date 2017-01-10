__author__ = 'philippe & Mick'from tkinter import *master = Tk()class World(object):    def __init__(self, width, axis_x, axis_y):        self.WIDTH = width        (self.AXIS_X, self.AXIS_Y) = (axis_x, axis_y)        self.WALLS = [(1, 1), (1, 2), (2, 1), (2, 2)]        self.SPECIALS = [(4, 1, "red", -1), (4, 0, "green", 1)]        self.board = Canvas(master, width=self.AXIS_X*self.WIDTH, height=self.AXIS_Y*self.WIDTH)        #self.Player = (0, y-1)        self.score = 1        self.restart = False         self.Player = (0, self.AXIS_Y-1)        self.me = self.board.create_rectangle(self.Player[0]*self.WIDTH+self.WIDTH*2/10, self.Player[1]*self.WIDTH+self.WIDTH*2/10,            self.Player[0]*self.WIDTH+self.WIDTH*8/10, self.Player[1]*self.WIDTH+self.WIDTH*8/10, fill="orange", width=1, tag="me")                self.WALK_REWARD = -0.04        self.ACTIONS = [["up", 0, -1], ["down", 0, 1], ["left", -1, 0], ["right", 1, 0]]    def render_grid(self):        #global specials, walls, Width, x, y, Player        for i in range(self.AXIS_X):            for j in range(self.AXIS_Y):                # Check if walls/specials for current coordinates                walls = [e for e in self.WALLS if i == e[0] and j == e[1]]                specials = [e for e in self.SPECIALS if i == e[0] and j == e[1]]                if (not walls) and (not specials):                    self.board.create_rectangle(i*self.WIDTH, j*self.WIDTH, (i+1)*self.WIDTH,                         (j+1)*self.WIDTH, fill="white", width=1)                elif walls and ((i, j) == walls[0]):                    self.board.create_rectangle(i*self.WIDTH, j*self.WIDTH, (i+1)*self.WIDTH,                         (j+1)*self.WIDTH, fill="black", width=1)                elif specials and ((i, j) == specials[0][0:2]):                    self.board.create_rectangle(i*self.WIDTH, j*self.WIDTH, (i+1)*self.WIDTH,                         (j+1)*self.WIDTH, fill=specials[0][2], width=1)                        def start_game(self):        master.mainloop()    ## ---- player part ----    def try_move(self, dx, dy):        if self.restart:            restart_game()        new_x = self.Player[0] + dx        new_y = self.Player[1] + dy        self.score += self.WALK_REWARD                if (new_x >= 0) and (new_x < self.AXIS_X) and (new_y >= 0) and (new_y < self.AXIS_Y) and not ((new_x, new_y) in self.WALLS):            self.board.coords(self.me, new_x*self.WIDTH+self.WIDTH*2/10, new_y*self.WIDTH+self.WIDTH*2/10,                 new_x*self.WIDTH+self.WIDTH*8/10, new_y*self.WIDTH+self.WIDTH*8/10)                        self.Player = (new_x, new_y)                for (i, j, c, w) in self.SPECIALS:            if new_x == i and new_y == j:                self.score -= self.WALK_REWARD                self.score += w                if self.score > 0:                    print("Success! score: ", self.score)                else:                    print("Fail! score: ", self.score)                self.restart = True                return    def restart_game(self):        self.Player = (0, self.AXIS_Y-1)        self.score = 1        self.restart = False        self.board.coords(self.me, self.Player[0]*self.WIDTH+self.WIDTH*2/10,             self.Player[1]*self.WIDTH+self.WIDTH*2/10, self.Player[0]*self.WIDTH+self.WIDTH*8/10,             self.Player[1]*self.WIDTH+self.WIDTH*8/10)    def has_restarted(self):        return self.restart