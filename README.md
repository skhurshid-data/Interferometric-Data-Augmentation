# Interferometric-Data-Augmentation
Step-1-Synthetic Data Generation on mutiple C values: This folder contains two mat files; one of them is the code for generating synthetic data and other contains the function(the "xc_fonction_xs_interpol_f_xs.m" file should be placed in the folder in which the main code file is present. Load this code in matlab and change the paths; you can generate different images under different conditions of c and noise for simulation.

Step-2-Input Images Data labeled: Once Images are generated then annotate them; this folder contains all annotated images which we used as input, you can use them directly or if you want your own data then annotate them in PASCAL-VOC format from this github repository(https://github.com/tzutalin/labelImg).

Step-3-Data Augmentation-Anisotropic Scaling: This folder contains all the codes used for anisotropic scaling as our novel augmentation method.

Now train your custom model using yolov5 from this github repository;https://github.com/ultralytics/yolov5.

Step-4-Experimental-Sgnals-to-Images-Conversion: This folder contains all the codes of experimental signals to images conversion into a sweet spot.
![mixed_experimental_results_v2](https://user-images.githubusercontent.com/87930540/126939869-36718797-0ebd-45b7-a67f-8b5b6af3949b.jpg)

![mixed_experimental_results](https://user-images.githubusercontent.com/87930540/126939901-3e09c498-4be6-4134-bfeb-926fb29160c8.jpg)
