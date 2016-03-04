import pytest
from main import *
from board import *
from person import *

class TestDonkey():
    @pytest.fixture
    def createboard(self):

        """Creating the board instance"""
        pygame.init()
        #display_game = pygame.display.set_mode((1920,1080))
        displaysize=[1920,1080]
        function(displaysize[0], displaysize[1])
        function1(displaysize[0], displaysize[1])

        return board(displaysize[0], displaysize[1], 1,0)

    def test_fireballrange(self,createboard):

        """ Checking whether the range of fireball is correct and whether fireballs are correctly released"""

        createboard.drawgrid([0, 0])
        init=[createboard.mario.rect.x, createboard.mario.rect.y]
        createboard.donkey.wallList = createboard.wallList
        createboard.donkey.fireballsList = createboard.fireballsList

        displaysize=[1920,1080]
        getdestruction(init[0],init[1])
        for i in range(5):
            fireball=createboard.donkey.throwfireballs()
            for j in range(1000):
                assert fireball.rect.x >= 0
                fireball.update()
                assert fireball.rect.x < displaysize[0]
        #for i in range(10):
    #         createboard.donkey.update()
    #         assert createboard.donkey.maximum < displaysize[0]

    def test_fireballpositions(self,createboard):

        """ Checking whether fireball is in its correct position range"""

        createboard.drawgrid([0, 0])
        init=[createboard.mario.rect.x, createboard.mario.rect.y]
        createboard.donkey.wallList = createboard.wallList
        createboard.donkey.ladderList = createboard.ladderList
        createboard.donkey.fireballsList = createboard.fireballsList
        
        displaysize=[1920,1080]
        getdestruction(init[0],init[1])
        for i in range(10):
            fireball=createboard.donkey.throwfireballs()
            for j in range(10000):
                assert fireball.rect.x >= 0
                fireball.update()
                assert fireball.rect.x < displaysize[0]
            
