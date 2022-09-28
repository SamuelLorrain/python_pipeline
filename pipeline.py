from typing import Callable
from io import BytesIO, StringIO

class Pipeline:
    """
    Implement a pipeline type pattern.

    Usage :
    pipeline = Pipeline(data) | processing1 | processing2 | processing3 | ...
    # call pipeline
    pipeline()
    """
    def __init__(self, data):
        self._data = data
        self._pipeline_queue = []

    def __or__(self, other: Callable):
        self._pipeline_queue.append(other)
        return self

    def __call__(self):
        currentData = self._data
        for i in self._pipeline_queue:
            currentData = i(currentData)
        return currentData

    def call(self):
        return self.__call__()


class StreamPipeline:
    """
    Implement a stream pipeline using a stream
    return a stream that goes through the defined pipeline
    """
    def __init__(self, stream: BytesIO|StringIO):
        self._stream = stream
        self._pipeline_queue = []

    def __or__(self, other: Callable):
        self._pipeline_queue.append(other)
        return self

    def _exec_pipeline(self, buffer):
        transform = buffer
        for i in self._pipeline_queue:
            transform = i(transform)
        return transform

    def readline(self, **kwargs):
        buffer = self._stream.readline(**kwargs)
        if not buffer:
            return None
        return self._exec_pipeline(buffer)

    def read(self, **kwargs):
        buffer = self._stream.readline(**kwargs)
        if not buffer:
            return None
        return self._exec_pipeline(buffer)

    def close(self):
        self._stream.close()

if __name__ == '__main__':
    def x(s):
        return "-" + s + "-"

    def y(s):
        return "_" + s + "_"

    def z(s):
        return "~" + s + "~"

    pipeline = Pipeline("i") | x | y | x | y | z | x | y | z
    print(pipeline())

    spipeline = StreamPipeline(StringIO("test")) | x | y |z | x | y | z
    while i := spipeline.read():
        print(i)

