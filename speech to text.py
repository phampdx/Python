import assemblyai as aai
aai.settings.api_key = "XXXXX"
# URL of the file to transcribe
# You can also transcribe a local file by passing in a file path
# FILE_URL = './path/to/file.mp3'
FILE_URL="C://Music//DHP_ViaDucQGiaoTong_edit.wav"
config = aai.TranscriptionConfig(language_code="vi")
transcriber = aai.Transcriber(config=config)
transcript = transcriber.transcribe(FILE_URL)
if transcript.status == aai.TranscriptStatus.error:
    print(transcript.error)
else:
    print(transcript.text)

