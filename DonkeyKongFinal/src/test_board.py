import pytest
from main import *
from board import *

class TestBoard():
    @pytest.fixture
    def createboard(self):

        """Creating the board instance"""
        #display_game = pygame.display.set_mode((1920,1080))
        displaysize=[1920,1080]
        function(displaysize[0], displaysize[1])
        function1(displaysize[0], displaysize[1])
        return board(displaysize[0], displaysize[1], 1,0)

    def test_coincount(self,createboard):

        """ Checking whether correct number of coins are created"""

        assert  createboard.drawgrid(960) >= 25
