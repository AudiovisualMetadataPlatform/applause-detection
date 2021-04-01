import json

class SegmentationSchema:
	MINIMUM_SILENCE = 10.0
	def __init__(self, segments=[], filename = ""):
		self.segments = segments
		self.media = SegmentationMedia(filename)
		
		# populate media duration with the end timestamp of the last segment if exists
		last_segment = None
		if len(self.segments) > 0:
			last_segment = self.segments[-1]
		if last_segment is not None:
			media.duration = last_segment['end']
			

	@classmethod
	def from_json(cls, json_data: dict):
		segments = list(map(SegmentationSegment.from_json, json_data["segments"]))
		media = SegmentationMedia(json_data["media"]["duration"], json_data["media"]["filename"])
		return cls(segments, media)

class SegmentationMedia:
	filename = ""
	duration = 0
	def __init__(self, duration = 0, filename = ""):
		self.duration = duration
		self.filename = filename

	@classmethod
	def from_json(cls, json_data):
		return cls(**json_data)

class SegmentationSegment:
	label = ""
	start = 0
	end = 0
	def __init__(self, label, start=None, end=None):
		self.label = SegmentationSegment.formatLabel(label)
		self.start = start
		self.end = end

	@classmethod
	def from_json(cls, json_data: dict):
		return cls(**json_data)