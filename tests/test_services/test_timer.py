import pytest

from TicTacToe.src.Services.Timer import Timer

@pytest.fixture()
def timer():
    yield Timer()

def test_start(timer):
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

def test_stop(timer):
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
