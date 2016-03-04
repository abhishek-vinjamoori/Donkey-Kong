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

    def test_donkeyrange(self,createboard):

        """ Checking whether the range of donkey is correctly set"""

        createboard.drawgrid([0, 0])

        createboard.donkey.wallList = createboard.wallList
        createboard.donkey.ladderList = createboard.ladderList
        createboard.donkey.fireballsList = createboard.fireballsList

        displaysize=[1920,1080]
        for i in range(100):
            assert createboard.donkey.maximum > 0
            createboard.donkey.update()
            assert createboard.donkey.maximum < displaysize[0]

    def test_donkeypositions(self,createboard):

        """ Checking whether donkey is in its correct position range"""

        createboard.drawgrid([0, 0])
        createboard.donkey.wallList = createboard.wallList
        createboard.donkey.ladderList = createboard.ladderList
        createboard.donkey.fireballsList = createboard.fireballsList
        for i in range(100):
            createboard.donkey.update()
            assert createboard.donkey.rect.x >= 0
            assert createboard.donkey.rect.x <= createboard.donkey.maximum
            currentposition = createboard.donkey.rect.y
            createboard.donkey.update()            
            finalposition = createboard.donkey.rect.y
            assert currentposition == finalposition