from WhisperAudioSplitter import WhisperAudioSplitter
import soundfile as sf
import os

class AudioSplitter(object):
    """
    This is an interface for audio splitting. It gets an audio file and searches for a particular string
    (from the Whisper generated transcript) and responds with a sub audio file of that particular string.
    """

    def __init__(self, sampling_rate=16000) -> None:
        """
        Constructor method for AudioSplitter class.

        Args:
            sampling_rate (int): The sampling rate of the audio file. Default value is 16000.
        """
        self.sampling_rate = sampling_rate
        self.splitter = WhisperAudioSplitter(sampling_rate=self.sampling_rate)

    def split_audio(self, audio_path, whisper_transcript=None, annotator_portion='', output_path='', class_name=''):
        """
        Splits the audio file into sub audio files based on the given input.

        Args:
            audio_path (str): The path of the audio file to be split.
            whisper_transcript (dict): The transcript generated by Whisper. Default value is None.
            annotator_portion (str): The text string to search for within the audio file.
            output_path (str): The path where the split audio file will be saved. Default value is ''.
            class_name (str): The name of the class to which the audio file belongs. Default value is ''.
        """
        # Check if the audio file can be split based on the Whisper transcript
        if self.splitter.generate(audio_path=audio_path, transcript=whisper_transcript, annotator_portion=annotator_portion):
            # Search for the text segment within the Whisper response
            indexes = self.splitter.search_for_text_segment(whisper_response=self.splitter.result, annotator_text=annotator_portion)
            # If the text segment is found, split the audio file based on the segment
            if indexes is not None:
                start = indexes[0]
                end = indexes[1]
                self.audio_operation(audio_path=audio_path, start=start, end=end, class_name=class_name, output_path=output_path)

    def audio_operation(self, audio_path, start=0, end=0, output_path='', class_name=''):
        """
        Performs the audio splitting operation on the given audio file.

        Args:
            audio_path (str): The path of the audio file to be split.
            start (int): The start time (in samples) of the segment to be split. Default value is 0.
            end (int): The end time (in samples) of the segment to be split. Default value is 0.
            output_path (str): The path where the split audio file will be saved. Default value is ''.
            class_name (str): The name of the class to which the audio file belongs. Default value is ''.
        """
        try:
            file_name = os.path.basename(audio_path)
            file_name = f'{class_name}_{file_name}'
            data, samplerate = sf.read(audio_path)
            data = data[start:end]
            sf.write(file_name, data, samplerate)
            print('[+] Saved Split')
        except Exception as e:
            print(f'[-] Error {e}')


if __name__ == "__main__":
   
    audio_splitter=AudioSplitter(sampling_rate=16000)
    audio_splitter.split_audio(audio_path='/home/ali/Desktop/idrak_work/transcriptor_module-transcriptor-module/WTranscriptor/audios/backy.wav',
                annotator_portion='I might be interested',class_name='intrested')