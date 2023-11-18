import pytest
from television import *


class Test:
    def setup_method(self):
        self.tv1 = Television()

    def teardown_method(self):
        del self.tv1

    def test_init(self):
        assert self.tv1.__str__() == 'Power = False, Channel = 0, Volume = 0'

    def test_power(self):
        self.tv1.power()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 0'
        self.tv1.power()
        assert self.tv1.__str__() == 'Power = False, Channel = 0, Volume = 0'

    def test_mute(self):
        self.tv1.power(), self.tv1.volume_up()  # TV is on, Volume Increased
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 1'
        self.tv1.mute()  # TV is on and muted
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 0'
        self.tv1.mute()  # Tv is on and not muted
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 1'
        self.tv1.power(), self.tv1.mute()  # TV is off and muted
        assert self.tv1.__str__() == 'Power = False, Channel = 0, Volume = 1'

    def test_channel_up(self):
        self.tv1.channel_up()  # TV is off and channel increased
        assert self.tv1.__str__() == 'Power = False, Channel = 0, Volume = 0'
        self.tv1.power(), self.tv1.channel_up()  # TV is on and channel is increased
        assert self.tv1.__str__() == 'Power = True, Channel = 1, Volume = 0'
        self.tv1.channel_up(), self.tv1.channel_up(), self.tv1.channel_up()
        # TV is increased to MAX_CHANNEL and increases
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 0'

    def test_channel_down(self):
        self.tv1.channel_down() # TV is off and channel decreases
        assert self.tv1.__str__() == 'Power = False, Channel = 0, Volume = 0'
        self.tv1.power(), self.tv1.channel_down()
        assert self.tv1.__str__() == 'Power = True, Channel = 3, Volume = 0'

    def test_volume_up(self):
        self.tv1.volume_up() # TV is off and volume increases
        assert self.tv1.__str__() == 'Power = False, Channel = 0, Volume = 0'
        self.tv1.power(), self.tv1.volume_up() # TV is on and volume increases
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 1'
        self.tv1.mute(), self.tv1.volume_up() # TV is on, muted, and volume increases
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 2'
        self.tv1.volume_up()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 2'

    def test_volume_down(self):
        self.tv1.volume_down() # TV is off and volume decreases
        assert self.tv1.__str__() == 'Power = False, Channel = 0, Volume = 0'
        self.tv1.power(), self.tv1.volume_up(), self.tv1.volume_up(), self.tv1.volume_down()
        # TV is on, volume is at max volume, and volume decreases
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 1'
        self.tv1.mute(), self.tv1.volume_down()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 0'
        self.tv1.volume_down() # TV is on and volume decreases at minimum volume
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 0'
