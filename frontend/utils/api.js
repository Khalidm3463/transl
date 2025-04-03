import axios from "axios";

const API_BASE_URL = "http://localhost:8000";

export const extractText = async (file) => {
  const formData = new FormData();
  formData.append("file", file);
  return axios.post(`${API_BASE_URL}/ocr/extract-text/`, formData);
};

export const translateText = async (text, targetLang) => {
  return axios.post(`${API_BASE_URL}/translate/`, { text, target_lang: targetLang });
};
