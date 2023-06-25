# who-s-talking 

[New Recording - 6_22_2023, 10_29_16 PM.webm](https://github.com/AklimaRimi/who-s-talking/assets/59701116/c4759068-4b82-4ec7-9c11-4ef7b83822ab)


# Problem Statement

This project is built to recognize voices. 

# Methodology

  ## Data Collection
  ### Libraries: Selenium, Subprocess, Youtube_dl
  As I wanted to do a Deep learning project that could recognize the voice, so I need a clear voice to train a model. For the sake of this project, I decided to listen to some famous motivational speakers' podcasts. We all know, podcasts are containing less background noise and the possibility to get a clear voice. 

The famous motivational speakers I chose are: Oprah Winfrey, Eric Thomas, Les Brown, Simon Sinek, Brene Brown, Gary Vee, Mel Robbins, Eckhart Tolle, Nick Vujicic, Rabin Sharma, Jay Shetty

  I have collected all of the podcasts from youtube. The steps are:
  
    1. Selected individual's youtube playlist.
    2. Scraped all the videos from the playlist using Selenium
    3. From the video, I filtered the audio using the Pytube library. As I only need the audio data.
    4. I did repeat this process for all speakers.
    
  To see the work [Here](https://github.com/AklimaRimi/who-s-talking/blob/main/script/vid%20downloader.py)
  ## Data Preprocessing
  ### Libraries: Librosa, sound file, moviepy
  As different audio data have different lengths and sizes. So, I decided to clip the audio into 5sec so that the data can be fed by the model, every data would be the same size.

  [Code](https://github.com/AklimaRimi/who-s-talking/blob/main/script/audio_preprocessed.ipynb)
  
  ## Data Filtering

  After clipping the audio into 5-sec audio, there has a possibility to get blank data or audio with no voice. I had to manually delete the audios which didn't contain any voice or contained noise.  

     After all of the filtering process 5500 audio files and for each speaker there have 500 audio files. This is a Balanced dataset I created.


## Audio to numeric conversion
  ### Libraries: liborsa

  A training model can not be trained using an audio file and  computers understand the numeric value. For this conversion, I used the librosa library. To do that, I have to follow several things:


mel_spec = librosa.feature.melspectrogram(y=audio, sr=sr, n_fft=fft_length, hop_length=hop_length, n_mels=num_mel_bins)
    
  1. I set the Sample_rate = 8000 because my audio sizes are 5 seconds.
  2. I used MelSpecttogram and amplitude_db to calculate pitch and decibel as numeric values of speech.
     
    
    The spectrogram is a Short-time Fourier Transform used for non-periodic data. We know speech, and music can change over time.
      We as human beings, can not differentiate 20000Hz and 22000Hz frequencies, frequencies sound. What Mel scale does, convert audio like listener listens to a speaker from a specific distance, and makes a range for frequencies.

      So a Mel Spectrogram is a spectrogram where the frequencies are converted to the male scale.


    
  


# Model Architecture

# Model Size Compression

# Achievement
