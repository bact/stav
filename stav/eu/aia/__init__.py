"""
Vocabulary for accountability artifacts from EU AI Act (draft)
"""

__stav_namespace__ = "eu.aia"


class TechnicalDocumentation(object):
    NAME = "technical_documentation"

    class Description(object):
        NAME = "description"
        INTENDED_PURPOSE = "intended_purpose"
        DEVELOPER = "developer"
        SYS_DATE = "sys_date"
        SYS_VERSION = "sys_version"
        REQ_SOFTWARE = "req_software"
        REQ_HARDWARD = "req_software"
        INSTRUCTIONS_USAGE = "instructions_usage"
        INSTRUCTIONS_INSTALLATION = "instructions_installation"


class LogRecord(object):
    NAME = "log_record"


__all__ = [
    "TechnicalDocumentation",
    "LogRecord",
]

"""
eu.aia.TechnicalDocumentation
eu.aia.LogRecord
eu.aia.Intention

eu.aia.Description
eu.aia.Description.IntendedPurpose
eu.aia.Description.Developer
eu.aia.Description.SystemDate
eu.aia.Description.SystemVersion
eu.aia.Description.ExternalInteractionInfo
eu.aia.Description.Requirements.Software
eu.aia.Description.Requirements.Firmware
eu.aia.Description.SystemFormsOnMarket
eu.aia.Description.IntendedHardware
eu.aia.Description.SystemLayout
eu.aia.Description.Instructions.Usage
eu.aia.Description.Instructions.Installation
"""
