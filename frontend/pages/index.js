import { useState } from "react";
import axios from "axios";

export default function Home() {
  const [file, setFile] = useState(null);
  const [text, setText] = useState("");
  const [translatedText, setTranslatedText] = useState("");
  const [targetLang, setTargetLang] = useState("es");

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleExtractText = async () => {
    if (!file) return alert("Please upload a file first.");
    const formData = new FormData();
    formData.append("file", file);

    const response = await axios.post("http://localhost:8000/ocr/extract-text/", formData);
    setText(response.data.extracted_text);
  };

  const handleTranslate = async () => {
    if (!text) return alert("No text to translate.");

    const response = await axios.post("http://localhost:8000/translate/", {
      text,
      target_lang: targetLang,
    });

    setTranslatedText(response.data.translations[0].text);
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gray-100">
      <h1 className="text-2xl font-bold mb-4">PDF/Text Translator</h1>

      <input type="file" onChange={handleFileChange} className="mb-4" />
      <button onClick={handleExtractText} className="px-4 py-2 bg-blue-500 text-white rounded-md">Extract Text</button>

      <textarea value={text} onChange={(e) => setText(e.target.value)}
        className="mt-4 w-96 h-40 p-2 border rounded-md"></textarea>

      <select value={targetLang} onChange={(e) => setTargetLang(e.target.value)} className="mt-2">
        <option value="es">Spanish</option>
        <option value="fr">French</option>
        <option value="de">German</option>
      </select>

      <button onClick={handleTranslate} className="mt-2 px-4 py-2 bg-green-500 text-white rounded-md">Translate</button>

      <h2 className="mt-4 text-xl font-bold">Translated Text:</h2>
      <p className="mt-2 p-4 bg-white w-96 border rounded-md">{translatedText}</p>
    </div>
  );
}
