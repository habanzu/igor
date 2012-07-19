# Copyright

"Record parsers for IGOR's packed experiment files."


from .base import Record, UnknownRecord, UnusedRecord
from .variables import VariablesRecord
from .history import HistoryRecord
from .wave import WaveRecord
from .recreation import RecreationRecord
from .procedure import ProcedureRecord
from .gethistory import GetHistoryRecord
from .packedfile import PackedFileRecord
from .folder import FolderStartRecord, FolderEndRecord


# From PackedFile.h
RECORD_TYPE = {
    0: UnusedRecord,
    1: VariablesRecord,
    2: HistoryRecord,
    3: WaveRecord,
    4: RecreationRecord,
    5: ProcedureRecord,
    6: UnusedRecord,
    7: GetHistoryRecord,
    8: PackedFileRecord,
    9: FolderStartRecord,
    10: FolderEndRecord,
    }
