# WhisperAudioSplitter
WhisperAudioSplitter uses Whisper Transcriptor to get word level timestamps of Audios. Whisper by default did not
return word level timestamp. To combat this issue Stable Whisper is used https://github.com/jianfch/stable-ts, also
this repository helps in making word level transcript accurately. 

## Usage
'''
from AudioSplitter import AudioSplitter
audio_splitter=AudioSplitter(sampling_rate=16000)
audio_splitter.split_audio(audio_path='filename.wav',
                annotator_portion='I might be interested',class_name='intrested')
'''
