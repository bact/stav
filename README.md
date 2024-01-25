# STAV: System Trustworthiness and Accountability Vocabulary

[![Project Status: WIP – Initial development is in progress, but there has not yet been a stable, usable release suitable for the public.](https://www.repostatus.org/badges/latest/wip.svg)](https://www.repostatus.org/#wip)
[![PyPI - Version](https://img.shields.io/pypi/v/stav.svg)](https://pypi.org/project/stav)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/stav.svg)](https://pypi.org/project/stav)

-----

`This work is still under development.`

**stav**:
- Norwegian: *to spell (words)*
- Swedish: *letter (alphabet)*
- Slovak: *state (condition)*
- Czech: *stance*

<!--
**Table of Contents**

- [Installation](#installation)
- [License](#license)
-->

## STAV Taxonomy

Available at [https://w3id.org/stav](https://w3id.org/stav.)

## STAV Python module

STAV terms can also be accessible through a Python module called `stav`, available freely on the [Python Package Index](https://pypi.org/project/stav/).

STAV class names are accessible through constants in the `stav` module. These class names are in capital letters with underscores separating words, `LIKE_THIS`, as stated in [PEP 8](https://peps.python.org/pep-0008/#constants).
Values of these constants are simply a STAV class name, a string in `CamelCase`.

For example, `stav.INSTRUCTIONS_OF_USE` is a string with value of "InstructionsOfUse".
(In the future, it should be able to configure the casing to "instructions_of_use", etc.)

With this, it will make the standardization of documentation within an organization, or across organizations, easier and can facilitate the use of the terms in MLOps settings, where data scientists and data engineers can use STAV terms as keys in their model logging and registration.

### Installation

```console
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


## License

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/bact/stav">STAV: System Trustworthiness and Accountability Vocabulary</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://orcid.org/0000-0002-9698-1899">Arthit Suriyawongkul</a> is licensed under <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"></a></p>

The `stav` Python module is distributed under the terms of the [Apache License 2.0](https://spdx.org/licenses/Apache-2.0.html).

This work is conducted with the financial support of the [Science Foundation Ireland Centre for Research Training in Digitally-Enhanced Reality (d-real)](https://d-real.ie/) under Grant No. 18/CRT/6224 and with the organizational support from members of these research groups:

- [Knowledge and Data Engineering Group](https://www.tcd.ie/scss/research/research-groups/kdeg/), [Trinity College Dublin](https://www.tcd.ie/scss/)
- [Transparent Digital Governance strand](https://www.adaptcentre.ie/case-studies/transparent-digital-governance/), [ADAPT Centre](https://www.adaptcentre.ie/)


## Related works

Members of [RegTech group at ADAPT Centre](https://regtech.adaptcentre.ie/) contribute to AI and data ontology projects below, and they are may be of your interest:
- [Trustworthy AI Requirements Ontology (TAIR)](https://tair.adaptcentre.ie/)
- [AI Risk Ontology (AIRO)](https://w3id.org/airo)
- [Vocabulary of AI Risks (VAIR)](https://w3id.org/vair)
- [Data Privacy Vocabulary (DPV)](https://w3id.org/dpv) - [AI Extenstion](https://github.com/w3c/dpv/issues/126) (under development)
