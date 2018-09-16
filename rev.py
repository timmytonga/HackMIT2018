import requests
import json
import time
import pyaudio
import wave

API_KEY = "Bearer 01A0mTVL32qozZKVOwK8yOkKiwnRuEP2Q034eCl8-OFeVmCtJ_gwlklxiAfz6mtWTQpdl3okZTyP3CrqpfPewraPAOYF0"
HEADERS = {'Authorization': API_KEY}
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
WAVE_OUTPUT_FILENAME = "output.wav"
RECORDING = False

def record_audio():
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("* recording")
    frames = []
    
    while RECORDING:
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording")
    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    

def submit_job_url(media_url):
    url = "https://api.rev.ai/revspeech/v1beta/jobs"
    payload = {'media_url': media_url,
               'metadata': "Test"}
    request = requests.post(url, headers=HEADERS, json=payload)

    if request.status_code != 200:
        raise

    response_body = request.json()
    return response_body['id']

def submit_job_file(file):
    url = "https://api.rev.ai/revspeech/v1beta/jobs"
    files = { 'media': (file, open(file, 'rb'), 'audio/wav') }
    request = requests.post(url, headers=HEADERS, files=files)
    if request.status_code != 200:
        raise

    response_body = request.json()
    return response_body['id']

def view_job(id=59594172):
    url = 'https://api.rev.ai/revspeech/v1beta/jobs/{id}'
    request = requests.get(url, headers=HEADERS)

    if request.status_code != 200:
        raise

    response_body = request.json()
    return response_body

def get_transcript(id='59594172'):
    url = 'https://api.rev.ai/revspeech/v1beta/jobs/{id}/transcript'
    headers = HEADERS.copy()
    headers['Accept'] = 'application/vnd.rev.transcript.v1.0+json'
    request = requests.get(url, headers=headers)

    if request.status_code != 200:
        raise

    response_body = request.json()
    return response_body

def test_workflow_with_url(url):
    print ("Submitting job with URL")
    id = submit_job_url(url)
    print ("Job created")
    view_job(id)

    while True:
        job = view_job(id)
        status = job["status"]
        print ('Checking job transcription status: { status }')
        if status == "transcribed":
            break
        if status == "failed":
            raise

        print ("Trying in another 30 seconds")
        time.sleep(30)

    return get_transcript(id)

def test_workflow_with_file(file):
    print ("Submitting job with file")
    id = submit_job_file(file)
    print ("Job created")
    view_job(id)

    while True:
        job = view_job(id)
        status = job["status"]
        print ('Checking job transcription status: { status }')
        if status == "transcribed":
            break
        if status == "failed":
            raise

        print ("Trying in another 30 seconds")
        time.sleep(30)

    return get_transcript(id)

def get_transcript():
    #Testing with file upload
    file = "output.wav"
    transcript = ''
    data = test_workflow_with_file(file)['monologues']
    for i in range(len(data)):
        elements = data[i]['elements']
        for element in elements:
            transcript += element['value']
    print(transcript)

def display_time_section(t_start, t_end):
    #Displays the text spoken in a particular time frame
    transcript = ''
    media_url = "https://support.rev.com/hc/en-us/article_attachments/200043975/FTC_Sample_1_-_Single.mp3"
    data = test_workflow_with_url(media_url)['monologues']
    for i in range(len(data)):
        elements = data[i]['elements']
        for element in elements:
            if element['type'] == 'text':
                if element['end_ts'] > t_start:
                    if element['end_ts'] < t_end:
                        transcript += element['value']
                    else:
                        break
            else:
                transcript += element['value']
    return transcript
        
if __name__ == "__main__":
    #print(display_time_section(.5,1.0))
    #main()
    record_audio()
