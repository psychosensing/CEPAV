# CEPAV
Competitive Esports: Physiological, Affective, and Video - Dataset

The CEPAV dataset contains raw and processed data, videos, materials, and code for the project Applying a Synergistic Mindsets Intervention to an Esports Context. The CEPAV dataset can be found here: https://osf.io/kgdsx/

This is the copy of the Code component and it contains Jupiter and R markdown notebooks presenting code used for data synchronization, calculating means, SNR and graphs.

    sync_merge_s1.ipynb - Jupiter notebook script used for synchronizing data ECG, ICG, Blood Pressure and Accelerometry data for Stage 1.
    sync_merge_s3.ipynb - Jupiter notebook script used for synchronizing data ECG, ICG, Blood Pressure and Accelerometry data for Stage 3.
    means_analysis_s1.ipynb - Jupiter notebook script used for calculating Signal to Noise Ratio for physiological and behavioral signals.
    means_analysis_s3.ipynb - Jupiter notebook script used for calculating means of physiological and behavioral activity for Stage 1.
    snr_script.ipynb - Jupiter notebook script used for calculating means of physiological and behavioral activity for Stage 3.
    visualize_data.ipynb - Jupiter notebook script used for generating Fig. 3.
    histograms_script_avg.py - Python script, drawing histograms for average values, to run on all files
    histograms_avg.ipynb - Jupiter notebook script used for generating Fig. 4.
    CEPAV.Rmd - R markdown script used for generating Fig. 5.
    individual_processing_debug_s1.ipynb - Jupiter notebook script used for synchronizing problematic data ECG, ICG, Blood Pressure and Accelerometry data for Stage 1.
    individual_processing_debug_s3.ipynb - Jupiter notebook script used for synchronizing problematic data ECG, ICG, Blood Pressure and Accelerometry data for Stage 3.
