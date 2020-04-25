#
# Autogenerated by Thrift Compiler (0.14.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
from thrift.TRecursive import fix_spec

import sys
import logging
from .ttypes import *
from thrift.Thrift import TProcessor
from thrift.transport import TTransport
all_structs = []


class Iface(object):
    def launchVideo(self, path, layer, sceneName, sourceName, dimensions):
        """
        Parameters:
         - path
         - layer
         - sceneName
         - sourceName
         - dimensions

        """
        pass

    def removeSource(self, sceneName, sourceName):
        """
        Parameters:
         - sceneName
         - sourceName

        """
        pass

    def muteSource(self, sourceName):
        """
        Parameters:
         - sourceName

        """
        pass

    def unmuteSource(self, sourceName):
        """
        Parameters:
         - sourceName

        """
        pass

    def heartbeat(self):
        pass


class Client(Iface):
    def __init__(self, iprot, oprot=None):
        self._iprot = self._oprot = iprot
        if oprot is not None:
            self._oprot = oprot
        self._seqid = 0

    def launchVideo(self, path, layer, sceneName, sourceName, dimensions):
        """
        Parameters:
         - path
         - layer
         - sceneName
         - sourceName
         - dimensions

        """
        self.send_launchVideo(path, layer, sceneName, sourceName, dimensions)
        self.recv_launchVideo()

    def send_launchVideo(self, path, layer, sceneName, sourceName, dimensions):
        self._oprot.writeMessageBegin('launchVideo', TMessageType.CALL, self._seqid)
        args = launchVideo_args()
        args.path = path
        args.layer = layer
        args.sceneName = sceneName
        args.sourceName = sourceName
        args.dimensions = dimensions
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_launchVideo(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = launchVideo_result()
        result.read(iprot)
        iprot.readMessageEnd()
        return

    def removeSource(self, sceneName, sourceName):
        """
        Parameters:
         - sceneName
         - sourceName

        """
        self.send_removeSource(sceneName, sourceName)
        self.recv_removeSource()

    def send_removeSource(self, sceneName, sourceName):
        self._oprot.writeMessageBegin('removeSource', TMessageType.CALL, self._seqid)
        args = removeSource_args()
        args.sceneName = sceneName
        args.sourceName = sourceName
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_removeSource(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = removeSource_result()
        result.read(iprot)
        iprot.readMessageEnd()
        return

    def muteSource(self, sourceName):
        """
        Parameters:
         - sourceName

        """
        self.send_muteSource(sourceName)
        self.recv_muteSource()

    def send_muteSource(self, sourceName):
        self._oprot.writeMessageBegin('muteSource', TMessageType.CALL, self._seqid)
        args = muteSource_args()
        args.sourceName = sourceName
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_muteSource(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = muteSource_result()
        result.read(iprot)
        iprot.readMessageEnd()
        return

    def unmuteSource(self, sourceName):
        """
        Parameters:
         - sourceName

        """
        self.send_unmuteSource(sourceName)
        self.recv_unmuteSource()

    def send_unmuteSource(self, sourceName):
        self._oprot.writeMessageBegin('unmuteSource', TMessageType.CALL, self._seqid)
        args = unmuteSource_args()
        args.sourceName = sourceName
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_unmuteSource(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = unmuteSource_result()
        result.read(iprot)
        iprot.readMessageEnd()
        return

    def heartbeat(self):
        self.send_heartbeat()
        self.recv_heartbeat()

    def send_heartbeat(self):
        self._oprot.writeMessageBegin('heartbeat', TMessageType.CALL, self._seqid)
        args = heartbeat_args()
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_heartbeat(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = heartbeat_result()
        result.read(iprot)
        iprot.readMessageEnd()
        return


class Processor(Iface, TProcessor):
    def __init__(self, handler):
        self._handler = handler
        self._processMap = {}
        self._processMap["launchVideo"] = Processor.process_launchVideo
        self._processMap["removeSource"] = Processor.process_removeSource
        self._processMap["muteSource"] = Processor.process_muteSource
        self._processMap["unmuteSource"] = Processor.process_unmuteSource
        self._processMap["heartbeat"] = Processor.process_heartbeat
        self._on_message_begin = None

    def on_message_begin(self, func):
        self._on_message_begin = func

    def process(self, iprot, oprot):
        (name, type, seqid) = iprot.readMessageBegin()
        if self._on_message_begin:
            self._on_message_begin(name, type, seqid)
        if name not in self._processMap:
            iprot.skip(TType.STRUCT)
            iprot.readMessageEnd()
            x = TApplicationException(TApplicationException.UNKNOWN_METHOD, 'Unknown function %s' % (name))
            oprot.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
            x.write(oprot)
            oprot.writeMessageEnd()
            oprot.trans.flush()
            return
        else:
            self._processMap[name](self, seqid, iprot, oprot)
        return True

    def process_launchVideo(self, seqid, iprot, oprot):
        args = launchVideo_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = launchVideo_result()
        try:
            self._handler.launchVideo(args.path, args.layer, args.sceneName, args.sourceName, args.dimensions)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("launchVideo", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_removeSource(self, seqid, iprot, oprot):
        args = removeSource_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = removeSource_result()
        try:
            self._handler.removeSource(args.sceneName, args.sourceName)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("removeSource", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_muteSource(self, seqid, iprot, oprot):
        args = muteSource_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = muteSource_result()
        try:
            self._handler.muteSource(args.sourceName)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("muteSource", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_unmuteSource(self, seqid, iprot, oprot):
        args = unmuteSource_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = unmuteSource_result()
        try:
            self._handler.unmuteSource(args.sourceName)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("unmuteSource", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_heartbeat(self, seqid, iprot, oprot):
        args = heartbeat_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = heartbeat_result()
        try:
            self._handler.heartbeat()
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("heartbeat", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

# HELPER FUNCTIONS AND STRUCTURES


class launchVideo_args(object):
    """
    Attributes:
     - path
     - layer
     - sceneName
     - sourceName
     - dimensions

    """


    def __init__(self, path=None, layer=None, sceneName=None, sourceName=None, dimensions=None,):
        self.path = path
        self.layer = layer
        self.sceneName = sceneName
        self.sourceName = sourceName
        self.dimensions = dimensions

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.path = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.layer = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.sceneName = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.sourceName = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRUCT:
                    self.dimensions = SourceDimensions()
                    self.dimensions.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('launchVideo_args')
        if self.path is not None:
            oprot.writeFieldBegin('path', TType.STRING, 1)
            oprot.writeString(self.path.encode('utf-8') if sys.version_info[0] == 2 else self.path)
            oprot.writeFieldEnd()
        if self.layer is not None:
            oprot.writeFieldBegin('layer', TType.I32, 2)
            oprot.writeI32(self.layer)
            oprot.writeFieldEnd()
        if self.sceneName is not None:
            oprot.writeFieldBegin('sceneName', TType.STRING, 3)
            oprot.writeString(self.sceneName.encode('utf-8') if sys.version_info[0] == 2 else self.sceneName)
            oprot.writeFieldEnd()
        if self.sourceName is not None:
            oprot.writeFieldBegin('sourceName', TType.STRING, 4)
            oprot.writeString(self.sourceName.encode('utf-8') if sys.version_info[0] == 2 else self.sourceName)
            oprot.writeFieldEnd()
        if self.dimensions is not None:
            oprot.writeFieldBegin('dimensions', TType.STRUCT, 5)
            self.dimensions.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(launchVideo_args)
launchVideo_args.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'path', 'UTF8', None, ),  # 1
    (2, TType.I32, 'layer', None, None, ),  # 2
    (3, TType.STRING, 'sceneName', 'UTF8', None, ),  # 3
    (4, TType.STRING, 'sourceName', 'UTF8', None, ),  # 4
    (5, TType.STRUCT, 'dimensions', [SourceDimensions, None], None, ),  # 5
)


class launchVideo_result(object):


    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('launchVideo_result')
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(launchVideo_result)
launchVideo_result.thrift_spec = (
)


class removeSource_args(object):
    """
    Attributes:
     - sceneName
     - sourceName

    """


    def __init__(self, sceneName=None, sourceName=None,):
        self.sceneName = sceneName
        self.sourceName = sourceName

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.sceneName = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.sourceName = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('removeSource_args')
        if self.sceneName is not None:
            oprot.writeFieldBegin('sceneName', TType.STRING, 1)
            oprot.writeString(self.sceneName.encode('utf-8') if sys.version_info[0] == 2 else self.sceneName)
            oprot.writeFieldEnd()
        if self.sourceName is not None:
            oprot.writeFieldBegin('sourceName', TType.STRING, 2)
            oprot.writeString(self.sourceName.encode('utf-8') if sys.version_info[0] == 2 else self.sourceName)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(removeSource_args)
removeSource_args.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'sceneName', 'UTF8', None, ),  # 1
    (2, TType.STRING, 'sourceName', 'UTF8', None, ),  # 2
)


class removeSource_result(object):


    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('removeSource_result')
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(removeSource_result)
removeSource_result.thrift_spec = (
)


class muteSource_args(object):
    """
    Attributes:
     - sourceName

    """


    def __init__(self, sourceName=None,):
        self.sourceName = sourceName

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.sourceName = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('muteSource_args')
        if self.sourceName is not None:
            oprot.writeFieldBegin('sourceName', TType.STRING, 1)
            oprot.writeString(self.sourceName.encode('utf-8') if sys.version_info[0] == 2 else self.sourceName)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(muteSource_args)
muteSource_args.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'sourceName', 'UTF8', None, ),  # 1
)


class muteSource_result(object):


    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('muteSource_result')
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(muteSource_result)
muteSource_result.thrift_spec = (
)


class unmuteSource_args(object):
    """
    Attributes:
     - sourceName

    """


    def __init__(self, sourceName=None,):
        self.sourceName = sourceName

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.sourceName = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('unmuteSource_args')
        if self.sourceName is not None:
            oprot.writeFieldBegin('sourceName', TType.STRING, 1)
            oprot.writeString(self.sourceName.encode('utf-8') if sys.version_info[0] == 2 else self.sourceName)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(unmuteSource_args)
unmuteSource_args.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'sourceName', 'UTF8', None, ),  # 1
)


class unmuteSource_result(object):


    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('unmuteSource_result')
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(unmuteSource_result)
unmuteSource_result.thrift_spec = (
)


class heartbeat_args(object):


    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('heartbeat_args')
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(heartbeat_args)
heartbeat_args.thrift_spec = (
)


class heartbeat_result(object):


    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('heartbeat_result')
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(heartbeat_result)
heartbeat_result.thrift_spec = (
)
fix_spec(all_structs)
del all_structs

