import os
import pandas as pd
import threading

# Caminho absoluto deste ficheiro
abs_path = os.path.abspath(__file__)

# Caminho desta pasta
dir_path = os.path.dirname(abs_path)

# Caminho desta pasta + o ficheiro que eu quero acessar
FILE = os.path.join(dir_path, "streamers_new.csv")


def threaded_job(job):
	# Função para correr o job em modo threading
	thread = threading.Thread(target=job)
	thread.start()

	# Esperar pela thread terminar
	thread.join()


def returnStreamers():
	df = pd.read_csv(FILE)

	streamers = []

	for index, streamer in df.iterrows():
		streamer_obj = {
			"name": streamer["Nome"],
			"twitch": streamer["Twitch"],
			"descr": streamer["Descr"],
			"avatar": streamer["Avatar"]
			}

		#print(streamer_obj)
		streamers.append(streamer_obj)

	streamers1 = streamers[len(streamers)//2:]
	streamers2 = streamers[:len(streamers)//2]

	return streamers1, streamers2