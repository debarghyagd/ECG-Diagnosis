# ECG-Diagnosis
> This repo is dedicated to my Heart Health Diagnosis model, which trains on the Physionet'21 Challange's WBDF Dataset of Healthy & CVD afflicted patients(~45K Samples), as a part of the project submission by Team Health_Hacktivists at DIRECTRIX'23, FIEM


## Data Preprocessing 

### Data Extraction/Filtering
#### Original patient data is in the form of .hea & .mat files . The patient's diagnosis SNOMED Code is mapped to the apt Cardio-Vascular Disease (or Lack thereof), which has been grouped into four umbrella heart health categories.
#### The patients are then filtered on the basis of available SNOMED Codes(which diseases to take into account) and converted to Pandas Series objects to be further preprocessed. 

### Data Cleaning & Scaling
#### The NeuroKit2 Library performs data cleaning, delineation and estimating R-Peaks and Offsets in raw ECG Signal Data.
#### StandarScalar from sklearn.preprocessing is used to perform feature transformation


## Feature Engineering & Data Labelling
#### Features that take into account the periodicity, duration and amplitude of offsets and peaks are then handcrafted and stored in a Pandas DataFrame object.
#### The after being labelled with apt heart health categories in a OneHotEncoding manner is then ready to be trained


## Model Training
#### Ensemble Learning approach is used towards model training.
#### Priliminary Estimator: Random Forest Classifier [with Elastic-Net Regularization &  Crossvalidation]
#### Alternate Estimators: XGBoost, LigtGBM


## Testing, Output & Usage
#### Best Result: 84.4% (F1-Score)
#### This project is aimed to be used as heart health diagnosis support to 3rd Party Applications and therefore returns a JSON response containing the diagnosed condition(s) and a recommendation regarding necessity/urgency of contacting medical professionals.
#### Run the ~ecg.ipynb file
