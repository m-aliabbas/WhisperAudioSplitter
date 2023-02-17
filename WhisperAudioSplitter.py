# some_file.py
import sys
sys.path.append('/home/ali/Desktop/idrak_work/transcriptor_module-transcriptor-module/WTranscriptor')
import soundfile as sf
from whisper1 import WhisperTranscriptorAPI
from utils import *

class WhisperAudioSplitter(object):

    #-------------------- constructor ----------------------------------------
    #
    def __init__(self,sampling_rate=16000) -> None:

        self.asr=WhisperTranscriptorAPI(model_path='openai/whisper-base.en',
                                        file_processing=True)
        self.result = None
        self.transcript = None
        self.segments = None
        self.sampling_rate = sampling_rate

    #---------------------- generate transcript and timestamps ---------------
    #

    def generate(self,audio_path='',transcript=None,annotator_portion=''):
        try:
            self.result = self.asr.generate_timestamps(audio_path=audio_path)
            if transcript is None:
                self.transcript = self.result['text']
            self.segments = self.result['segments']
            return True
        except Exception as e:
            print(f'[-] {e}')
            return False
        
    
    #--------------- geting start and ending time of wanted audio ------------
    #
    def search_for_text_segment(self,whisper_response, annotator_text, sampling_rate=16000):
        """Search for a given text segment within a Whisper response.

        Args:
            whisper_response (dict): A dictionary containing the Whisper response.
            annotator_text (str): The text to search for.
            sampling_rate (int): The sampling rate of the audio.

        Returns:
            A tuple containing the start and end time (in samples) of the text segment, as well as the segment dictionary.
        """
        # Get the segments from the Whisper response
        segments = whisper_response.get('segments', [])
        start, end = 0, 0
        # Search for the text segment within the Whisper response
        for i, segment in enumerate(segments):
            #only check for starting portion of annotator text, because most of
            #time annoator response can be consist of multiple sentence
            if annotator_text[:int(len(annotator_text) / 3)] in segment['text']:
                # Compute the start and end times in samples and return them
                start, end = search_for_words(segment=segment, annotator_text=annotator_text,
                                                     segments=segments[i + 1:])
                if not start:
                    start = segment['start']
                if not end:
                    end = segment['end']
                start = int(start * sampling_rate)
                end = int(end * sampling_rate)
                return start, end

        # If the text segment wasn't found, return None
        return None
    
    
        
   
                





    
    