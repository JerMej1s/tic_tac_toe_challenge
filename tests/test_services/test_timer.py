import pytest

from TicTacToe.Services.Timer import Timer

@pytest.fixture()
def timer():
    yield Timer()


class TestTimer:
    def test_start(self, timer: Timer):
        timer.start()

        assert timer.start_time is not None
        assert timer.end_time is None
        assert timer.duration is None

        timer.unit = 'ms'
        timer.start()

        assert timer.start_time is not None
        assert timer.end_time is None
        assert timer.duration is None

        timer.unit = 'ns'
        timer.start()

        assert timer.start_time is not None
        assert timer.end_time is None
        assert timer.duration is None

    def test_stop(self, timer: Timer):
        timer.start()
        duration = timer.stop()

        assert timer.end_time is not None
        assert timer.duration == duration

        timer.unit = 'ms'
        timer.start()
        duration = timer.stop()

        assert timer.end_time is not None
        assert timer.duration == duration

        timer.unit = 'ns'
        timer.start()
        duration = timer.stop()

        assert timer.end_time is not None
        assert timer.duration == duration
