import React, { useState } from "react";
import Form from "./Form.jsx";
import Result from "./Result.jsx";

function App() {
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");

  return (
    <div className="flex items-center justify-center min-h-screen bg-gradient-to-b from-indigo-100 to-blue-100">
      <div className="bg-white p-8 rounded-2xl shadow-2xl w-full max-w-lg">
        <h1 className="text-3xl font-extrabold text-center text-indigo-700 mb-6">
          Insurance Premium Predictor
        </h1>
        <Form setResult={setResult} setError={setError} />
        <Result result={result} error={error} />
      </div>
    </div>
  );
}

export default App;
