# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tflite_fb

import flatbuffers

class StridedSliceOptions(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsStridedSliceOptions(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = StridedSliceOptions()
        x.Init(buf, n + offset)
        return x

    # StridedSliceOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # StridedSliceOptions
    def BeginMask(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # StridedSliceOptions
    def EndMask(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # StridedSliceOptions
    def EllipsisMask(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # StridedSliceOptions
    def NewAxisMask(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # StridedSliceOptions
    def ShrinkAxisMask(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

def StridedSliceOptionsStart(builder): builder.StartObject(5)
def StridedSliceOptionsAddBeginMask(builder, beginMask): builder.PrependInt32Slot(0, beginMask, 0)
def StridedSliceOptionsAddEndMask(builder, endMask): builder.PrependInt32Slot(1, endMask, 0)
def StridedSliceOptionsAddEllipsisMask(builder, ellipsisMask): builder.PrependInt32Slot(2, ellipsisMask, 0)
def StridedSliceOptionsAddNewAxisMask(builder, newAxisMask): builder.PrependInt32Slot(3, newAxisMask, 0)
def StridedSliceOptionsAddShrinkAxisMask(builder, shrinkAxisMask): builder.PrependInt32Slot(4, shrinkAxisMask, 0)
def StridedSliceOptionsEnd(builder): return builder.EndObject()
