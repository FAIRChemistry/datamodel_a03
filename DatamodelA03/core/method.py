import sdRDM


from typing import Optional
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from pydantic import Field
from typing import List
from typing import Optional
from .step import Step


class Method(sdRDM.DataModel):

    """Describes a workflow that was done for a particular part of the experiment or the complete"""

    name: Optional[str] = Field(
        description="Name of the method (e.g. Preparation)",
        default=None,
    )

    steps: List[Step] = Field(
        description="Steps that make up the procedure",
        default_factory=ListPlus,
    )

    reference: Optional[str] = Field(
        description="Reference to the original publication from which the method was adapted from.",
        default=None,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_a03.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="13944dc93cd3f3cd0ca43f90838c16476cc85df0"
    )

    def add_to_steps(
        self,
        description: Optional[str] = None,
    ) -> None:
        """
        Adds an instance of 'Step' to the attribute 'steps'.

        Args:
            description (Optional[str]): Free text description of the step. Defaults to None
        """

        self.steps.append(
            Step(
                description=description,
            )
        )
