from .analysis import Analysis
from .compound import Compound
from .procedure import Procedure
from .report import Report
from .step import Step

__doc__ = "This data model describes a COF preparation including information about chemical entities and the experimental procedure. Preliminary specifications according to the example PDF provided."

__all__ = [
    "Analysis",
    "Compound",
    "Procedure",
    "Report",
    "Step",
]
