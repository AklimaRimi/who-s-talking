# who-s-talking 

[New Recording - 6_22_2023, 10_29_16 PM.webm](https://github.com/AklimaRimi/who-s-talking/assets/59701116/c4759068-4b82-4ec7-9c11-4ef7b83822ab)


# Problem Statement

This project is built to recognize voices. 

# Methodology

  ## Data Collection
  ### Libraries : Selenium, Subprocess, Youtube_dl
  As I wanted to wante to make Deep learning project which can recognize voice, so I need clear voice to train a model. For the sake of this project, I decided to take some famous motivational speakers podcast. We all know , podcasts are containing less background noise and posibility to get clear voice. 

The famous motivational speakers I choosed are: Oprah Winfrey, Eric Thomas, Les Brown, Simon Sinek, Brene Brown, Gary Vee, Mel Robbins, Eckhart Tolle, Nick Vujicic, Rabin Sharma, Jay Shetty

  I have collected all of the podcast from youtube. The steps are:
  
    1. Selected individual's youtube playlist.
    2. Scraped all the videos from playlist using selenium
    3. From video, I filtered the audio using pytube library. As I only need the audio data.
    4. I did repeat this process for all speakers.
    
  To see the work [Here](https://github.com/AklimaRimi/who-s-talking/blob/main/script/vid%20downloader.py)
  ## Data Preprocessing
  ### Libraries: Librosa, soundfile, moviepy
  As different audio data has different length and size. So, I decided to clip the audios into 5sec, so the data can be feeded by model, every data would be same size.

  [Code](https://github.com/AklimaRimi/who-s-talking/blob/main/script/audio_preprocessed.ipynb)
  
  ## Data Filtering

  After clipping the audios into 5 sec audio, there has possibility to get blank data or audio with no voice. I had to manually deleted the audios which didn't contain any voice or contained noise.  

     After all of the filtering process 5500 audio files and for each speakers there has 500 audio files. This is a Balanced dataset I had created.


## Audio to numeric conversion
  ### Libraries: liborsa

  As a training model can not be trained using audio file and  computer just know the numeric value. For this conversion, I used librosa library. To do that I have to follow several things:

    1. 
    2. 
    3. 
    4. 
    
  


# Model Architecture

# Model Size Compression

# Achievement
