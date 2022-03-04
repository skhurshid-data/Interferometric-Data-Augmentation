# Interferometric-Data-Augmentation
**Step-1-Synthetic Data Generation on mutiple C values:** This folder contains two mat files; one of them is the code for generating synthetic data and other contains the function ("xc_fonction_xs_interpol_f_xs.m") file should be placed in the folder in which the main code file is present. Load this code in matlab and change the paths; you can generate different images under different conditions of C and noise for simulation
For this current implementation do this:
```
1. C = 1 to 10  #Select a range of values of C in each iteration.
2. Noise = 0.08*randn(length(P_simo),1);            #Select a value of Noise as in this line and modify this value of 0.08 according to your own need. SNR_db will represent the amount of noise within the signal.
3. SNR_db= 2*10 * log10(SNR)         # SNR in db will automatically changed when that 0.08 value will be modified.
4. xlim([0.88 0.98]); ylim([-1.5 1.5]); #Change the values of xlim and ylim such as there should be minimum one fringe and ideally 10 to 12 fringes in a plot.
```
6. Once all above values are selected, run the code and you will get a set of plot saved in the folder.
7. Repeat these above steps by changing values and for exact implementation, the values should be same as we mentioned in paper for training regime such as C = 1 to 10 and noise upto 13.5 dB.

**Step-2-Input Images Data labeled:** Once Images are generated, you can now annotate them; this folder contains all annotated images which we used as input, you can use them directly or if you want your own data then annotate them in PASCAL-VOC format from this github repository(https://github.com/tzutalin/labelImg).
1. Install setup of labelImg from this link.
2. Open the tool and then click on open folder located at the left side.
3. Navigate to the folder in which images are present and open them.
4. Select the PASCAL-VOC format and click on draw to draw the boudning boxes around each fringe.
    i. If it is negative fringe then label it as negative_fringe and keep the name same throughout.
    ii. If it is positive fringe then label it as positive_fringe and keep the name same throughout.
5. Save each time and it's corresponding labels will be stored in xml format.
6. Keep labeling all the images selected in training set.

**Step-3-Data Augmentation-Anisotropic Scaling:** This folder contains all the codes used for anisotropic scaling as our novel augmentation method.

Now train your custom model using yolov5 from this github repository;https://github.com/ultralytics/yolov5.

**Step-4-Experimental-Signals-to-Images-Conversion:** This folder contains all the codes of experimental signals to images conversion into a sweet spot.

**Step-5 - testing the data:** Here are some testing results from given pretrained model;
These are the weights of custom trained model: https://drive.google.com/drive/folders/1_4urUrQiUjeQMvd4FBGDmCpJfxxMYsov?usp=sharing
![Exp_signal 21+1i](https://user-images.githubusercontent.com/87930540/126940471-fa60059a-4acd-4d5a-b6da-9861f912384b.png)
![mixed_exp2](https://user-images.githubusercontent.com/87930540/126940491-8600c02a-5110-4c39-81b1-0d7857adf3ff.png)
