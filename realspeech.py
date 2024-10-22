import librosa
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import warnings

warnings.filterwarnings("ignore", category=UserWarning, message="X does not have valid feature names")

def analyze_voice(file_path):
    try:
        y, sr = librosa.load(file_path, sr=None)

        pitches, magnitudes = librosa.piptrack(y=y, sr=sr)
        mdvp_fo = np.mean(pitches[pitches > 0])  
        mdvp_fhi = np.max(pitches) 
        mdvp_flo = np.min(pitches[pitches > 0]) 

        jitter_local = np.std(pitches[pitches > 0]) / mdvp_fo * 100 if mdvp_fo != 0 else 0

        amplitude = librosa.feature.rms(y=y)[0]
        shimmer_local = np.std(amplitude) / np.mean(amplitude) * 100 if np.mean(amplitude) != 0 else 0

        hnr = librosa.effects.hpss(y)[0] 
        nhr = 1 / np.mean(hnr) if np.mean(hnr) != 0 else 0

        return [
            mdvp_fo, mdvp_fhi, mdvp_flo, jitter_local, shimmer_local, nhr
        ]
    except Exception as e:
        print(f"Error analyzing voice: {e}")
        return None

def predict_parkinsons(voice_features):
    try:
        df = pd.read_csv('D:\\IEEE HACKATHON\\build\\parkinsons.data')

        X = df[['MDVP:Fo(Hz)', 'MDVP:Fhi(Hz)', 'MDVP:Flo(Hz)', 'MDVP:Jitter(%)',
                 'MDVP:Shimmer', 'NHR']]
        y = df['status']

        X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_val_scaled = scaler.transform(X_val)

        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train_scaled, y_train)

        y_val_pred = model.predict(X_val_scaled)
        accuracy = accuracy_score(y_val, y_val_pred)
        print(f"Validation accuracy using Random Forest Classifier: {accuracy}")

        voice_features_scaled = scaler.transform([voice_features])

        prediction = model.predict(voice_features_scaled)

        if prediction == 1:
            print("Prediction: You likely do not have Parkinson's disease.")
        else:
            print("Prediction: You may have Parkinson's disease.")
    except Exception as e:
        print(f"Error predicting Parkinson's: {e}")

