from __future__ import absolute_import

import logging

from .monitor import Monitor
from .configuration import SRBConfig

# Initialize configuration
config = SRBConfig(logging.getLogger(__name__))

from .base import EnvironmentBase, Space, AlgorithmBase
from .measure import Measure, BestPerformance
from .bench import Bench, BenchConfig
from . import algo
from . import envs
from . import tools

# Add things to all
__all__ = ['EnvironmentBase',
           'Space',
           'AlgorithmBase',
           'Monitor',
           'SRBConfig',
           'Measure',
           'BestPerformance',
           'Bench',
           'BenchConfig',
           'envs',
           'tools',
           'algo']


# Import test after __all__ (no documentation)
# from numpy.testing import Tester
# test = Tester().test
