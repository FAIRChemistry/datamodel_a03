import sdRDM


from typing import Optional
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from pydantic import Field
from pydantic.types import PositiveFloat
from typing import List
from typing import Optional
from .measurement import Measurement
from .method import Method
from .molecule import Molecule
from .positivefloat import PositiveFloat
from .step import Step


class Report(sdRDM.DataModel):

    """Reports on a chemical experiment, that includes Reactants and Reactants as well as the method. The Data model will natively be exported to the AnIML data format used to track data from analytical instruments."""

    reagents: List[Molecule] = Field(
        description="List of reagents that were used in the experiment",
        default_factory=ListPlus,
    )

    reactants: List[Molecule] = Field(
        description="List of reactants that were used in the experiment",
        default_factory=ListPlus,
    )

    measurements: List[Measurement] = Field(
        description="All measurements that were conducted in an experiment",
        default_factory=ListPlus,
    )

    methods: List[Method] = Field(
        description="Methods that were used in this experiment",
        default_factory=ListPlus,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_a03.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="13944dc93cd3f3cd0ca43f90838c16476cc85df0"
    )

    def add_to_reagents(
        self,
        id: Optional[str] = None,
        inchi: Optional[str] = None,
        cas_number: Optional[str] = None,
        used_mass: Optional[PositiveFloat] = None,
    ) -> None:
        """
        Adds an instance of 'Molecule' to the attribute 'reagents'.

        Args:
            id (Optional[str]): Unique identifier for a molecule/stock. Defaults to None
            inchi (Optional[str]): InChI code that uniquely identifies the structure of a molecule. Defaults to None
            cas_number (Optional[str]): A CAS Registry Number also referred to as CAS RN or informally CAS Number, is a unique numerical identifier assigned by the Chemical Abstracts Service (CAS), US to every chemical substance described in the open scientific literature. Defaults to None
            used_mass (Optional[PositiveFloat]): Mass that was weighed in and used in the experiment. Defaults to None
        """

        self.reagents.append(
            Molecule(
                id=id,
                inchi=inchi,
                cas_number=cas_number,
                used_mass=used_mass,
            )
        )

    def add_to_reactants(
        self,
        id: Optional[str] = None,
        inchi: Optional[str] = None,
        cas_number: Optional[str] = None,
        used_mass: Optional[PositiveFloat] = None,
    ) -> None:
        """
        Adds an instance of 'Molecule' to the attribute 'reactants'.

        Args:
            id (Optional[str]): Unique identifier for a molecule/stock. Defaults to None
            inchi (Optional[str]): InChI code that uniquely identifies the structure of a molecule. Defaults to None
            cas_number (Optional[str]): A CAS Registry Number also referred to as CAS RN or informally CAS Number, is a unique numerical identifier assigned by the Chemical Abstracts Service (CAS), US to every chemical substance described in the open scientific literature. Defaults to None
            used_mass (Optional[PositiveFloat]): Mass that was weighed in and used in the experiment. Defaults to None
        """

        self.reactants.append(
            Molecule(
                id=id,
                inchi=inchi,
                cas_number=cas_number,
                used_mass=used_mass,
            )
        )

    def add_to_measurements(
        self,
        entry_id: Optional[str] = None,
        product_yield: Optional[PositiveFloat] = None,
    ) -> None:
        """
        Adds an instance of 'Measurement' to the attribute 'measurements'.

        Args:
            entry_id (Optional[str]): Unique identifier of the measurement. Defaults to None
            product_yield (Optional[PositiveFloat]): Documented yield in mg. Defaults to None
        """

        self.measurements.append(
            Measurement(
                entry_id=entry_id,
                product_yield=product_yield,
            )
        )

    def add_to_methods(
        self,
        steps: List[Step] = ListPlus(),
        name: Optional[str] = None,
        reference: Optional[str] = None,
    ) -> None:
        """
        Adds an instance of 'Method' to the attribute 'methods'.

        Args:
            steps (List[Step]): Steps that make up the procedure.
            name (Optional[str]): Name of the method (e.g. Preparation). Defaults to None
            reference (Optional[str]): Reference to the original publication from which the method was adapted from. Defaults to None
        """

        self.methods.append(
            Method(
                steps=steps,
                name=name,
                reference=reference,
            )
        )
