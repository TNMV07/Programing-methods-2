from actuator import Actuator
import pytest


def test_actuator_valid_command():
    actuator = Actuator()
    actuator.set_command(3.0)
    assert actuator.command() == 3.0


def test_actuator_boundary_min():
    actuator = Actuator()
    actuator.set_command(0.0)
    assert actuator.command() == 0.0


def test_actuator_boundary_max():
    actuator = Actuator()
    actuator.set_command(6.29)
    assert actuator.command() == 6.29


def test_actuator_command_too_high():
    actuator = Actuator()
    with pytest.raises(ValueError):
        actuator.set_command(7.0)


def test_actuator_command_negative():
    actuator = Actuator()
    with pytest.raises(ValueError):
        actuator.set_command(-0.1)
