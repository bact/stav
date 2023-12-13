# STAV: System Trustworthiness and Accountability Vocabulary

`This work is still under development.`

**stav**:
- Norwegian: *to spell (words)*
- Swedish: *letter (alphabet)*
- Slovak: *state (condition)*
- Czech: *stance*


## STAV Python module

STAV terms can also be accessible through a Python module called `stav`, available freely on the [Python Package Index](https://pypi.org/project/stav/).

STAV class names are accessible through constants in the `stav` module. These class names are in capital letters with underscores separating words, `LIKE_THIS`, as stated in [PEP 8](https://peps.python.org/pep-0008/#constants).
Values of these constants are simply a STAV class name, a string in `CamelCase`.

For example, `stav.INSTRUCTIONS_OF_USE` is a string with value of "InstructionsOfUse".
(In the future, it should be able to configure the casing to "instructions_of_use", etc.)

With this, it will make the standardization of documentation within an organization, or across organizations, easier and can facilitate the use of the terms in MLOps settings, where data scientists and data engineers can use STAV terms as keys in their model logging and registration.

### Install

```sh
pip install stav
```

### Use with MLflow

```python
from mlflow import log_artifact, log_metric, log_param
import stav

metric_names = [
    stav.METRICS_RECALL,
    stav.METRICS_PRECISION,
    stav.METRICS_RMSE,
]

log_param(stav.ENERGY_CONSUMPTION, "3.3M GPU")

log_param(stav.AI_PROVIDER, "Acme Corporation")
log_param(stav.AI_DEPLOYER, "Sirius Cybernetics")
log_artifact("use_intructions.txt", artifact_path=stav.INSTRUCTIONS_OF_USE)
```

## Sister projects

STA*V* (a *V*ocabulary) and STA*P* (an ODRL *P*rofile) are sisters for system trustworthiness and accountability.

- **STAV** provides a vocabulary (with focus on *informational items*) extracted from regulations and policy documents, mostly AI safety-related, like EU Artificial Intelligence Act draft. Its IRI is [https://w3id.org/stav](https://w3id.org/stav). Its code repository is at [https://github.com/bact/stav/](https://github.com/bact/stav/).

- **STAP** provides a set of core accountability relationships, based on [Open Digital Rights Language](https://www.w3.org/TR/odrl-model/). They are trying not to be AI-specific. Its IRI is [https://w3id.org/stap](https://w3id.org/stap). Its code repository is at [https://github.com/bact/stap/](https://github.com/bact/stap/).


## Author
STAV is developed and maintained by Arthit Suriyawongkul ([@bact](https://github.com/bact/)) with supports from members of these research groups:

- [Knowledge and Data Engineering Group](https://www.tcd.ie/scss/research/research-groups/kdeg/), [Trinity College Dublin](https://www.tcd.ie/scss/)
- [Transparent Digital Governance strand](https://www.adaptcentre.ie/case-studies/transparent-digital-governance/), [ADAPT Centre](https://www.adaptcentre.ie/)

This work is conducted with the financial support of the [Science Foundation Ireland Centre for Research Training in Digitally-Enhanced Reality (d-real)](https://d-real.ie/) under Grant No. 18/CRT/6224.


## Related works

Members of [RegTech group at ADAPT Centre](https://regtech.adaptcentre.ie/) contribute to AI and data ontology projects below, and they are may be of your interest:
- [Trustworthy AI Requirements Ontology (TAIR)](https://tair.adaptcentre.ie/)
- [AI Risk Ontology (AIRO)](https://w3id.org/airo)
- [Vocabulary of AI Risks (VAIR)](https://w3id.org/vair)
- [Data Privacy Vocabulary (DPV)](https://w3id.org/dpv) - [AI Extenstion](https://github.com/w3c/dpv/issues/126) (under development)
