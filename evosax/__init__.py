from .strategy import Strategy
from .strategies import (
    SimpleGA,
    SimpleES,
    CMA_ES,
    DE,
    PSO,
    OpenES,
    PGPE,
    PBT,
    PersistentES,
    xNES,
    ARS,
    Sep_CMA_ES,
    BIPOP_CMA_ES,
    IPOP_CMA_ES,
    Full_iAMaLGaM,
    Indep_iAMaLGaM,
    MA_ES,
    LM_MA_ES,
    RmES,
    GLD,
    SimAnneal,
)


Strategies = {
    "SimpleGA": SimpleGA,
    "SimpleES": SimpleES,
    "CMA_ES": CMA_ES,
    "DE": DE,
    "PSO": PSO,
    "OpenES": OpenES,
    "PGPE": PGPE,
    "PBT": PBT,
    "PersistentES": PersistentES,
    "xNES": xNES,
    "ARS": ARS,
    "Sep_CMA_ES": Sep_CMA_ES,
    "BIPOP_CMA_ES": BIPOP_CMA_ES,
    "IPOP_CMA_ES": IPOP_CMA_ES,
    "Full_iAMaLGaM": Full_iAMaLGaM,
    "Indep_iAMaLGaM": Indep_iAMaLGaM,
    "MA_ES": MA_ES,
    "LM_MA_ES": LM_MA_ES,
    "RmES": RmES,
    "GLD": GLD,
    "SimAnneal": SimAnneal,
}

from .utils import FitnessShaper, ParameterReshaper, ESLog
from .networks import NetworkMapper
from .problems import ProblemMapper

__all__ = [
    "Strategy",
    "SimpleGA",
    "SimpleES",
    "CMA_ES",
    "DE",
    "PSO",
    "OpenES",
    "PGPE",
    "PBT",
    "PersistentES",
    "xNES",
    "ARS",
    "Sep_CMA_ES",
    "BIPOP_CMA_ES",
    "IPOP_CMA_ES",
    "Full_iAMaLGaM",
    "Indep_iAMaLGaM",
    "MA_ES",
    "LM_MA_ES",
    "RmES",
    "GLD",
    "SimAnneal",
    "Strategies",
    "FitnessShaper",
    "ParameterReshaper",
    "ESLog",
    "NetworkMapper",
    "ProblemMapper",
]
