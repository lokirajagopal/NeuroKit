"""Submodule for NeuroKit."""

from ..signal import signal_rate as eog_rate
from .eog_clean import eog_clean
from .eog_features import eog_features
from .eog_findpeaks import eog_findpeaks
from .eog_process import eog_process
from .eog_plot import eog_plot
from .eog_eventrelated import eog_eventrelated
from .eog_intervalrelated import eog_intervalrelated


__all__ = ["eog_rate", "eog_clean", "eog_features", "eog_findpeaks", "eog_process", "eog_plot",
           "eog_eventrelated", "eog_intervalrelated"]
