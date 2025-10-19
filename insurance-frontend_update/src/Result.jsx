import React from "react";

function Result({ result, error }) {
  if (error) {
    return <p className="text-red-600 text-center mt-4">{error}</p>;
  }

  if (result) {
    return (
      <p className="text-green-600 text-center mt-4 font-semibold">
        Predicted Premium Insurance : {result}
      </p>
    );
  }

  return null;
}

export default Result;
