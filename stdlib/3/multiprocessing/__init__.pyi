# Stubs for multiprocessing

from typing import Any, Callable, Iterable, Mapping, Optional, Dict, List

from multiprocessing.context import BaseContext
from multiprocessing.managers import SyncManager
from multiprocessing.pool import AsyncResult
from multiprocessing.process import current_process as current_process

class Lock():
    def acquire(self, block: bool = ..., timeout: int = ...) -> None: ...
    def release(self) -> None: ...
    def __enter__(self) -> 'Lock': ...
    def __exit__(self, exc_type, exc_value, tb) -> None: ...

class Event(object):
    def __init__(self, *, ctx: BaseContext) -> None: ...
    def is_set(self) -> bool: ...
    def set(self) -> None: ...
    def clear(self) -> None: ...
    def wait(self, timeout: Optional[int] = ...) -> bool: ...

class Pool():
    def __init__(self, processes: Optional[int] = ...,
                 initializer: Optional[Callable[..., None]] = ...,
                 initargs: Iterable[Any] = ...,
                 maxtasksperchild: Optional[int] = ...,
                 context: Any = None) -> None: ...
    def apply(self,
              func: Callable[..., Any],
              args: Iterable[Any] = ...,
              kwds: Dict[str, Any]=...) -> Any: ...
    def apply_async(self,
                func: Callable[..., Any],
                args: Iterable[Any] = ...,
                kwds: Dict[str, Any] = ...,
                callback: Callable[..., None] = None,
                error_callback: Callable[[BaseException], None] = None) -> AsyncResult: ...
    def map(self,
            func: Callable[..., Any],
            iterable: Iterable[Any] = ...,
            chunksize: Optional[int] = ...) -> List[Any]: ...
    def map_async(self, func: Callable[..., Any],
                  iterable: Iterable[Any] = ...,
                  chunksize: Optional[int] = ...,
                  callback: Callable[..., None] = None,
                  error_callback: Callable[[BaseException], None] = None) -> AsyncResult: ...
    def imap(self,
             func: Callable[..., Any],
             iterable: Iterable[Any] = ...,
             chunksize: Optional[int] = None) -> Iterable[Any]: ...
    def imap_unordered(self,
                       func: Callable[..., Any],
                       iterable: Iterable[Any] = ...,
                       chunksize: Optional[int] = None) -> Iterable[Any]: ...
    def starmap(self,
                func: Callable[..., Any],
                iterable: Iterable[Iterable[Any]] = ...,
                chunksize: Optional[int] = None) -> List[Any]: ...
    def starmap_async(self,
                      func: Callable[..., Any],
                      iterable: Iterable[Iterable[Any]] = ...,
                      chunksize: Optional[int] = ...,
                      callback: Callable[..., None] = None,
                      error_callback: Callable[[BaseException], None] = None) -> AsyncResult: ...
    def close(self) -> None: ...
    def terminate(self) -> None: ...
    def join(self) -> None: ...
    def __enter__(self) -> 'Pool': ...
    def __exit__(self, exc_type, exc_val, exc_tb) -> None: ...

class Process():
    # TODO: set type of group to None
    def __init__(self,
                 group: Any = ...,
                 target: Callable = ...,
                 name: str = ...,
                 args: Iterable[Any] = ...,
                 kwargs: Mapping[Any, Any] = ...,
                 daemon: bool = ...) -> None: ...
    def start(self) -> None: ...
    def run(self) -> None: ...
    def terminate(self) -> None: ...
    def is_alive(self) -> bool: ...
    def join(self, timeout: float = ...) -> None: ...

class Queue():
    def __init__(self, maxsize: int = ...) -> None: ...
    def get(self, block: bool = ..., timeout: float = ...) -> Any: ...
    def put(self, item: Any, block: bool = ..., timeout: float = ...) -> None: ...
    def qsize(self) -> int: ...
    def empty(self) -> bool: ...
    def full(self) -> bool: ...
    def put_nowait(self, item: Any) -> None: ...
    def get_nowait(self) -> Any: ...
    def close(self) -> None: ...
    def join_thread(self) -> None: ...
    def cancel_join_thread(self) -> None: ...

class Value():
    def __init__(self, typecode_or_type: str, *args: Any, lock: bool = ...) -> None: ...

# ----- multiprocessing function stubs -----
def cpu_count() -> int: ...
def freeze_support() -> None: ...
def Manager() -> SyncManager: ...
