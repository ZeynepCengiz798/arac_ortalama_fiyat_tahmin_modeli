import streamlit as st
import numpy as np
import joblib
import tensorflow as tf
import pickle

st.set_page_config(page_title="2. El Araç Fiyat Tahmini", layout="centered")
st.title("🚗 2. El Araç Fiyat Tahmin Uygulaması")

# --- 1. Eğitimde kullanılan bilgiler ---
categorical_cols = ['fuel', 'transmission', 'body', 'owner_type', 'state']
numeric_cols = ['km', 'myear', 'marka_model_yil_avg', 'relative_price']

# --- 2. Model ve objeleri yükle ---
def load_artifacts():
    scaler = joblib.load("scaler.pkl")
    label_encoders = joblib.load("label_encoders.pkl")
    loaded_model = tf.keras.models.load_model("trained_model.keras")
    with open("marka_model_yil_avg.pkl", "rb") as f:
        marka_model_yil_avg_dict = pickle.load(f)
    return scaler, label_encoders, loaded_model, marka_model_yil_avg_dict

scaler, label_encoders, loaded_model, marka_model_yil_avg_dict = load_artifacts()

# --- 3. Kullanıcı Girişi ---
st.header("Araç Bilgilerini Giriniz")

# Kilometre ve model yılı (numeric)
km = st.number_input("Kilometre", min_value=0, value=50000, step=1000)

# OEM ve model yılını seçmek için dict üzerinden seçim
valid_keys = list(marka_model_yil_avg_dict.keys())

# OEM seçimi
valid_oems = sorted(set([k[0] for k in valid_keys]))
selected_oem = st.selectbox("Marka (OEM)", valid_oems)

# Model seçimi
valid_models = sorted(set([k[1] for k in valid_keys if k[0] == selected_oem]))
selected_model = st.selectbox("Model", valid_models)

# Yıl seçimi
valid_years = sorted(set([k[2] for k in valid_keys if k[0] == selected_oem and k[1] == selected_model]), reverse=True)
selected_year = st.selectbox("Model Yılı", valid_years)

# Ortalama fiyatı bul
key = (selected_oem, selected_model, selected_year)
avg_price = marka_model_yil_avg_dict.get(key)

if avg_price is None:
    st.error("❌ Bu marka-model-yıl kombinasyonu için ortalama fiyat bulunamadı.")
    st.stop()

# Kullanıcıdan ilan fiyatını al
listed_price = st.number_input("İlan Fiyatı (₺)", min_value=10000, step=1000, value=300000)

# Göreli fiyat hesapla
relative_price = listed_price / avg_price

st.info(f"🔍 Ortalama fiyat: {avg_price:,.0f} ₺ | Göreli fiyat: {relative_price:.2f}")

# Kategorik sütunlar
selected_values = {}
cat_inputs = []

def selectbox_with_encoder(col_name):
    le = label_encoders[col_name]
    options = list(le.classes_)

    selected = st.selectbox(f"{col_name.capitalize()}", options)
    encoded = le.transform([selected])[0]
    return selected, encoded

for col in categorical_cols:
    selected, encoded = selectbox_with_encoder(col)
    selected_values[col] = selected
    cat_inputs.append(np.array([[encoded]]))
# Sayısal verileri hazırla
numeric_input = np.array([[km, selected_year, avg_price, relative_price]])
numeric_scaled = scaler.transform(numeric_input)

# --- 4. Tahmin ---
if st.button("📊 Tahmin Et"):
    model_inputs = [numeric_scaled] + cat_inputs
    prediction = loaded_model.predict(model_inputs)

    # Tahmin log(1 + fiyat) olduğu için, tersini al
    predicted_price = np.expm1(prediction[0][0])

    # Sonucu kullanıcıya göster
    st.markdown(f"### 🚘 Tahmini Araç Fiyatı: {predicted_price:,.0f} ₺")
