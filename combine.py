import Parser
from pydub import AudioSegment
import os

def merge_and_normalize_audio(file_paths, output_path, delay_ms=1000):
    audio_segments = [AudioSegment.from_file(file_path) for file_path in file_paths]

    reference_audio = audio_segments[0]
    normalized_audio_segments = []

    for audio_segment in audio_segments[1:]:
        volume_diff = reference_audio.dBFS - audio_segment.dBFS
        normalized_audio = audio_segment + volume_diff
        normalized_audio_segments.append(normalized_audio)
    
    silence_segment = AudioSegment.silent(duration=delay_ms)

    merged_audio = reference_audio
    for normalized_audio in normalized_audio_segments:
        merged_audio += silence_segment + normalized_audio

    merged_audio.export(output_path, format="mp3")

def comb(word):
	words = word.split()
	folder_path = os.getcwd()

	if len(words) < 2: return 0
	print("\033[93mTrying a combining method\033[93m")

	raw_music = []
	for element in words:
		save_path = f"{folder_path}\\{element}.mp3"

		try:
			Parser.define(element, save_path, 0, 0, 'english')
		except:
			pass

		if os.path.exists(save_path):
			raw_music.append(save_path)

	if len(raw_music) == 0: return 0

	merge_and_normalize_audio(raw_music, word + ".mp3", 200)

	return 1
