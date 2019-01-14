Video Examples: https://www.youtube.com/watch?v=eWjIBFLX3xM
                https://www.youtube.com/watch?v=cfLKqUpWepc
                
1. I started this project because I was looking for an easy and intuitive way of morphing between wavetables with an XY pad where you could easily add, remove and find the “in-between” of the sampled wavetables.  
2. There are a large number of morphing XY wavetable synthesizers, but I hadn’t heard of one using machine learning. In my opinion machine learning techniques make it super simple for any user to add, remove and adapt the XY morphing to their intended end goal. 
3. For the implementation the method of my choice was regression (since I wanted the wavetables to morph continuously between examples). I tried using polynomial regression but ended up having better results with neural networks. I used Wekinator for one variant of the wavetable synth and used Keras/Tensorflow for the other variations. 
4. I think this project was mostly successful, the morphing between the 256 sample wavetables works how I envisioned (on both variants), alternatively the morphing between the 11025 sample wavetables isn’t very precise but I find it quite interesting to create new sounds. 
5. All the code in this project is my own work. I have used resources like the Keras documentation (https://keras.io/) and tutorials (https://machinelearningmastery.com/regression-tutorial-keras-deep-learning-library-python/), python-osc documentation (https://pypi.org/project/python-osc/) and Wekinator documentation (http://www.wekinator.org/detailed-instructions/) to learn from examples but ultimately ended up writing my own code. 
 
Running Instructions: 

smlXYwtWeki(2in-256out):  
- Start Wekinator with 2 inputs and 256 continuous outputs (using default settings). 
- Open smlXYwtWeki(2in-256out) max patch or the m4l version inside ableton. 
(if you want a quick start/test there is a Wekinator pre-trained model in the smlXYwtWeki folder called “classic waveforms”, you can just load it, then press “run” on the smlXYwtWeki GUI and morph between 5 classic waveforms with the XY pad) 
- Click “replace” on the smlXYwtWeki GUI and chose any audio sample to extract wavetables from. 
- Click on the waveform representation to the right of “replace” to choose the start of the wavetable (256 samples) you want to extract, alternatively use the slice number box under “replace” to move between the wavetable position 256 samples at a time. If you have MIDI (note, velocity) going into the synthesizer at this time you should hear the selected wavetable being output as audio. 
- Chose a wavetable with a sound you enjoy, place the XY pad (bottom left) on a chosen position and press the “+ Example” button (top right), Wekinator should now have added the example to the model. (There is a “bug” with this variant where sometimes Wekinator doesn’t register the example added, please make sure the example has been added on the Wekinator GUI before proceeding to add another example). 
- After recording all the wanted wavetable examples and their wanted XY positions on the XYpad press the train button (top right) to train the model. 
- After training (should be fast), press the “Run” toggle to start using the trained model and move the XY pad to interpolate between the waveforms. 

smlXYwtKeras(2in-256out) & (2in-11025out): 
- To run the python3 code it is required to install keras and python-osc modules. 
- After having all dependencies installed, just run the main.py python3 script inside the respective folder (run with python3). 
- Open smlXYwtKeras(2in-256out) or smlXYwtKeras(2in-11025out) (depending on which main.py script you are running) max patch or the m4l version inside ableton. 
- Click “replace” on the smlXYwtKeras GUI and chose any audio sample to extract wavetables from. 
- Click on the waveform representation to the right of “replace” to choose the start of the wavetable (256/11025 samples) you want to extract, alternatively use the slice number box under “replace” to move between the wavetable position 256/11025 samples at a time. If you have MIDI (note, velocity) going into the synthesizer at this time you should hear the selected wavetable being output as audio. 
- Chose a wavetable with a sound you enjoy, place the XY pad (bottom left) on a chosen position and press the “+ Example” button (top right), Keras should now have added the example to the model.  
- After recording all the wanted wavetable examples and their wanted XY positions on the XYpad press the train button (top right) to train the model. 
After training (may take a while, check python3 terminal for status), press the “Run” toggle to start using the trained model and move the XY pad to interpolate between the waveforms.  version inside ableton. 
- Click “replace” on the smlXYwtKeras GUI and chose any audio sample to extract wavetables from. 
- Click on the waveform representation to the right of “replace” to choose the start of the wavetable (256/11025 samples) you want to extract, alternatively use the slice number box under “replace” to move between the wavetable position 256/11025 samples at a time. If you have MIDI (note, velocity) going into the synthesizer at this time you should hear the selected wavetable being output as audio. 
- Chose a wavetable with a sound you enjoy, place the XY pad (bottom left) on a chosen position and press the “+ Example” button (top right), Keras should now have added the example to the model.  
- After recording all the wanted wavetable examples and their wanted XY positions on the XYpad press the train button (top right) to train the model. 
After training (may take a while, check python3 terminal for status), press the “Run” toggle to start using the trained model and move the XY pad to interpolate between the waveforms. 
