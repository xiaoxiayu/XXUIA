# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities

import imageprocess_pb2 as imageprocess__pb2


class ImageStub(object):
  """The greeting service definition.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Info = channel.unary_unary(
        '/imageprocess.Image/Info',
        request_serializer=imageprocess__pb2.StringReq.SerializeToString,
        response_deserializer=imageprocess__pb2.StringReply.FromString,
        )
    self.Draw = channel.unary_unary(
        '/imageprocess.Image/Draw',
        request_serializer=imageprocess__pb2.ImgRequest.SerializeToString,
        response_deserializer=imageprocess__pb2.ImgReply.FromString,
        )
    self.DetectElements = channel.unary_stream(
        '/imageprocess.Image/DetectElements',
        request_serializer=imageprocess__pb2.DetectImg.SerializeToString,
        response_deserializer=imageprocess__pb2.ElementRect.FromString,
        )
    self.DetectSimilarity = channel.unary_stream(
        '/imageprocess.Image/DetectSimilarity',
        request_serializer=imageprocess__pb2.CmpImgRequest.SerializeToString,
        response_deserializer=imageprocess__pb2.DMatchPos.FromString,
        )
    self.DrawSimilarity = channel.unary_unary(
        '/imageprocess.Image/DrawSimilarity',
        request_serializer=imageprocess__pb2.CmpImgRequest.SerializeToString,
        response_deserializer=imageprocess__pb2.CmpImgReply.FromString,
        )
    self.OCR = channel.unary_unary(
        '/imageprocess.Image/OCR',
        request_serializer=imageprocess__pb2.OcrRequest.SerializeToString,
        response_deserializer=imageprocess__pb2.TxtReply.FromString,
        )
    self.FindImage = channel.unary_unary(
        '/imageprocess.Image/FindImage',
        request_serializer=imageprocess__pb2.FindImgRequest.SerializeToString,
        response_deserializer=imageprocess__pb2.ElementPos.FromString,
        )
    self.GetBrightnessHistArray = channel.unary_stream(
        '/imageprocess.Image/GetBrightnessHistArray',
        request_serializer=imageprocess__pb2.ImgRequest.SerializeToString,
        response_deserializer=imageprocess__pb2.HistBarData.FromString,
        )
    self.GetDiffRect = channel.unary_unary(
        '/imageprocess.Image/GetDiffRect',
        request_serializer=imageprocess__pb2.CmpImgRequest.SerializeToString,
        response_deserializer=imageprocess__pb2.ElementRect.FromString,
        )
    self.CompareColorHist = channel.unary_unary(
        '/imageprocess.Image/CompareColorHist',
        request_serializer=imageprocess__pb2.CmpImgRequest.SerializeToString,
        response_deserializer=imageprocess__pb2.FloatReply.FromString,
        )
    self.Filter2D = channel.unary_unary(
        '/imageprocess.Image/Filter2D',
        request_serializer=imageprocess__pb2.FilterRequest.SerializeToString,
        response_deserializer=imageprocess__pb2.ImgReply.FromString,
        )
    self.SSIM = channel.unary_unary(
        '/imageprocess.Image/SSIM',
        request_serializer=imageprocess__pb2.ImgCmpRequest.SerializeToString,
        response_deserializer=imageprocess__pb2.FloatReply.FromString,
        )
    self.CosineSim = channel.unary_unary(
        '/imageprocess.Image/CosineSim',
        request_serializer=imageprocess__pb2.TxtCmpRequest.SerializeToString,
        response_deserializer=imageprocess__pb2.FloatReply.FromString,
        )
    self.reflow_compare_text = channel.unary_unary(
        '/imageprocess.Image/reflow_compare_text',
        request_serializer=imageprocess__pb2.ImgCmpRequest.SerializeToString,
        response_deserializer=imageprocess__pb2.ReflowTextReply.FromString,
        )
    self.reflow_compare_image = channel.unary_unary(
        '/imageprocess.Image/reflow_compare_image',
        request_serializer=imageprocess__pb2.ImgCmpRequest.SerializeToString,
        response_deserializer=imageprocess__pb2.FloatReply.FromString,
        )
    self.magic_wand_fill = channel.unary_unary(
        '/imageprocess.Image/magic_wand_fill',
        request_serializer=imageprocess__pb2.MagicWandRequest.SerializeToString,
        response_deserializer=imageprocess__pb2.ImgReply.FromString,
        )


class ImageServicer(object):
  """The greeting service definition.
  """

  def Info(self, request, context):
    """Sends a greeting
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Draw(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DetectElements(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DetectSimilarity(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DrawSimilarity(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def OCR(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FindImage(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetBrightnessHistArray(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetDiffRect(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CompareColorHist(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Filter2D(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SSIM(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CosineSim(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def reflow_compare_text(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def reflow_compare_image(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def magic_wand_fill(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ImageServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Info': grpc.unary_unary_rpc_method_handler(
          servicer.Info,
          request_deserializer=imageprocess__pb2.StringReq.FromString,
          response_serializer=imageprocess__pb2.StringReply.SerializeToString,
      ),
      'Draw': grpc.unary_unary_rpc_method_handler(
          servicer.Draw,
          request_deserializer=imageprocess__pb2.ImgRequest.FromString,
          response_serializer=imageprocess__pb2.ImgReply.SerializeToString,
      ),
      'DetectElements': grpc.unary_stream_rpc_method_handler(
          servicer.DetectElements,
          request_deserializer=imageprocess__pb2.DetectImg.FromString,
          response_serializer=imageprocess__pb2.ElementRect.SerializeToString,
      ),
      'DetectSimilarity': grpc.unary_stream_rpc_method_handler(
          servicer.DetectSimilarity,
          request_deserializer=imageprocess__pb2.CmpImgRequest.FromString,
          response_serializer=imageprocess__pb2.DMatchPos.SerializeToString,
      ),
      'DrawSimilarity': grpc.unary_unary_rpc_method_handler(
          servicer.DrawSimilarity,
          request_deserializer=imageprocess__pb2.CmpImgRequest.FromString,
          response_serializer=imageprocess__pb2.CmpImgReply.SerializeToString,
      ),
      'OCR': grpc.unary_unary_rpc_method_handler(
          servicer.OCR,
          request_deserializer=imageprocess__pb2.OcrRequest.FromString,
          response_serializer=imageprocess__pb2.TxtReply.SerializeToString,
      ),
      'FindImage': grpc.unary_unary_rpc_method_handler(
          servicer.FindImage,
          request_deserializer=imageprocess__pb2.FindImgRequest.FromString,
          response_serializer=imageprocess__pb2.ElementPos.SerializeToString,
      ),
      'GetBrightnessHistArray': grpc.unary_stream_rpc_method_handler(
          servicer.GetBrightnessHistArray,
          request_deserializer=imageprocess__pb2.ImgRequest.FromString,
          response_serializer=imageprocess__pb2.HistBarData.SerializeToString,
      ),
      'GetDiffRect': grpc.unary_unary_rpc_method_handler(
          servicer.GetDiffRect,
          request_deserializer=imageprocess__pb2.CmpImgRequest.FromString,
          response_serializer=imageprocess__pb2.ElementRect.SerializeToString,
      ),
      'CompareColorHist': grpc.unary_unary_rpc_method_handler(
          servicer.CompareColorHist,
          request_deserializer=imageprocess__pb2.CmpImgRequest.FromString,
          response_serializer=imageprocess__pb2.FloatReply.SerializeToString,
      ),
      'Filter2D': grpc.unary_unary_rpc_method_handler(
          servicer.Filter2D,
          request_deserializer=imageprocess__pb2.FilterRequest.FromString,
          response_serializer=imageprocess__pb2.ImgReply.SerializeToString,
      ),
      'SSIM': grpc.unary_unary_rpc_method_handler(
          servicer.SSIM,
          request_deserializer=imageprocess__pb2.ImgCmpRequest.FromString,
          response_serializer=imageprocess__pb2.FloatReply.SerializeToString,
      ),
      'CosineSim': grpc.unary_unary_rpc_method_handler(
          servicer.CosineSim,
          request_deserializer=imageprocess__pb2.TxtCmpRequest.FromString,
          response_serializer=imageprocess__pb2.FloatReply.SerializeToString,
      ),
      'reflow_compare_text': grpc.unary_unary_rpc_method_handler(
          servicer.reflow_compare_text,
          request_deserializer=imageprocess__pb2.ImgCmpRequest.FromString,
          response_serializer=imageprocess__pb2.ReflowTextReply.SerializeToString,
      ),
      'reflow_compare_image': grpc.unary_unary_rpc_method_handler(
          servicer.reflow_compare_image,
          request_deserializer=imageprocess__pb2.ImgCmpRequest.FromString,
          response_serializer=imageprocess__pb2.FloatReply.SerializeToString,
      ),
      'magic_wand_fill': grpc.unary_unary_rpc_method_handler(
          servicer.magic_wand_fill,
          request_deserializer=imageprocess__pb2.MagicWandRequest.FromString,
          response_serializer=imageprocess__pb2.ImgReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'imageprocess.Image', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
