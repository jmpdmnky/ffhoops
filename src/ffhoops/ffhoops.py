import json
import subprocess

class ffhoops:

    def __init__(self, file_path='', data={}, raw_ffprobe={}):
        self.file_path = file_path
        self.data = raw_ffprobe
        #self._raw_ffprobe_data = raw_ffprobe

        if raw_ffprobe:
            #self._raw_ffprobe_data = raw_ffprobe
            self._handle_raw_ffprobe_data(raw_ffprobe)

    def _handle_raw_ffprobe_data(self, data):
        ## things we might care about

        self.format = data['format']['format_name']

        self.num_channels = data['streams'][0]['channels']

        try:
            self.channel_layout = data['streams'][0]['channel_layout']
        except:
            self.channel_layout = 'mono'

        self.codec = data['streams'][0]['codec_name']
        self.codec_long = data['streams'][0]['codec_long_name']
        self.sample_rate  = data['streams'][0]['sample_rate']
        self.duration = data['streams'][0]['duration']
        self.bit_rate = data['streams'][0]['bit_rate']
        self.format  = data['format']['format_name']
        self.format_long = data['format']['format_long_name']
        self.size = data['format']['size']

    
    @classmethod
    def ffprobe(cls, file_path):
        args = "ffprobe -v error -show_format -of json -show_streams".split()
        args += [file_path]
        p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        
        if err:
            raise Exception(err) # TODO: make this better

        file_data = json.loads(out)

        return cls(file_path=file_data, raw_ffprobe=file_data)


if __name__ == '__main__':
    test_file = 'C:/Users/rwhoo/Desktop/Stuff/ffmpeg_test/test/audio/stereo-test.mp3'

    audio_file = ffhoops.ffprobe(test_file)

    print(audio_file.format)

    print(audio_file.data)