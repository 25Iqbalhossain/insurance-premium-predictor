import React, { useState } from "react";
import Form from "../Form";
import Result from "../Result"; // Case-sensitive: make sure file name is "Result.jsx"

function Home() {
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");

  return (
    <div className="min-h-screen bg-gray-100 flex flex-col items-center justify-center">
      <Form setResult={setResult} setError={setError} />
      <Result result={result} error={error} />
    </div>
  );
}

export default Home;
