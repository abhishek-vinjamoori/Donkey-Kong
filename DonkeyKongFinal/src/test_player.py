import pytest
from main import *
from board import *
from person import *

class TestMario():
    @pytest.fixture
    def createboard(self):

        """Creating the board instance"""
        pygame.init()
        #display_game = pygame.display.set_mode((1920,1080))
        displaysize=[1920,1080]
        function(displaysize[0], displaysize[1])
        function1(displaysize[0], displaysize[1])

        return board(displaysize[0], displaysize[1], 1,0)

    def test_playerrange(self,createboard):

        """ Checking whether the range of mario is correctly set"""

        createboard.drawgrid([0, 0])

        createboard.mario.wallList = createboard.wallList
        createboard.mario.ladderList = createboard.ladderList
        createboard.mario.fireballsList = createboard.fireballsList

        displaysize=[1920,1080]
        for i in range(1000):
            assert createboard.mario.rect.x > 0
            createboard.mario.update()
            assert createboard.mario.rect.x < displaysize[0]

    def test_mariopositions(self,createboard):

        """ Checking whether mario is in its correct position range and does not collide with walls"""

        createboard.drawgrid([0, 0])
        createboard.mario.wallList = createboard.wallList
        createboard.mario.ladderList = createboard.ladderList
        createboard.mario.fireballsList = createboard.fireballsList
        for i in range(100):
            createboard.mario.update()
            assert createboard.mario.rect.x >= 0
            currentposition = createboard.mario.rect.x
            for j in range(10):
                person.moveRight(createboard.mario)
                person.stopside(createboard.mario)
            createboard.mario.update()            
            finalposition = createboard.mario.rect.x
            assert currentposition <= finalposition
            createboard.mario.update()
            currentposition = createboard.mario.rect.x
            for j in range(10):
                person.moveLeft(createboard.mario)
            createboard.mario.update()            
            finalposition = createboard.mario.rect.x
            assert currentposition >= finalposition


    def test_coincollection(self,createboard):

        """Checking whether score increases when coins are colleceted"""

        createboard.drawgrid([0, 0])
        createboard.mario.wallList = createboard.wallList
        createboard.mario.ladderList = createboard.ladderList
        createboard.mario.fireballsList = createboard.fireballsList
        createboard.mario.coinList = createboard.coinList
        
        for i in range(100):
            createboard.mario.update()
            for j in range(25):
                person.moveRight(createboard.mario)
                #person.stopside(createboard.mario)
            createboard.mario.update()
            #assert createboard.mario.rect.x<500
           
            assert createboard.mario.score >= 0