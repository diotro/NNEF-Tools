# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tflite_fb

import flatbuffers

class FloorModOptions(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsFloorModOptions(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = FloorModOptions()
        x.Init(buf, n + offset)
        return x

    # FloorModOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

def FloorModOptionsStart(builder): builder.StartObject(0)
def FloorModOptionsEnd(builder): return builder.EndObject()
