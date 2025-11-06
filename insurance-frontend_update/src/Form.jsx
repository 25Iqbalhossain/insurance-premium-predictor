import React, { useState } from "react";
import { predictPremium } from "./api";

function Form({ setResult, setError }) {
  const [formData, setFormData] = useState({
    age: "",
    weight: "",
    height: "",
    income_lpa: "",
    smoker: "false",
    city: "",
    occupation: "retired",
  });

  const handleChange = (e) => {
    const { id, value } = e.target;
    setFormData({ ...formData, [id]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    // 🧩 prepare payload for backend (numbers + booleans)
    const payload = {
      age: parseInt(formData.age),
      weight: parseFloat(formData.weight),
      height: parseFloat(formData.height),
      income_lpa: parseFloat(formData.income_lpa),
      smoker: formData.smoker === "true", // boolean conversion
      city: formData.city.trim(),
      occupation: formData.occupation, // keep string
    };

    try {
      const response = await predictPremium(payload);
      setResult(response.data.predicted_insurance_premium);
      setError("");
    } catch (error) {
      setResult(null);
      const apiError = error?.response?.data;
      const message =
        (apiError && (apiError.error || apiError.detail)) || error.message || "Something went wrong!";
      setError(typeof message === "string" ? message : JSON.stringify(message));
    }
  };

  return (
    <form
      onSubmit={handleSubmit}
      className="bg-white shadow-lg rounded-2xl p-6 w-full max-w-lg mx-auto mt-10"
    >
      <h2 className="text-xl font-bold text-center text-indigo-700 mb-6">
        Insurance Premium Predictor
      </h2>

      <div className="grid grid-cols-2 gap-4">
        <div>
          <label className="block text-gray-700 font-medium mb-1">Age</label>
          <input
            id="age"
            type="number"
            value={formData.age}
            onChange={handleChange}
            required
            className="w-full border border-gray-300 p-2 rounded-lg focus:ring-2 focus:ring-indigo-400"
          />
        </div>

        <div>
          <label className="block text-gray-700 font-medium mb-1">Weight (kg)</label>
          <input
            id="weight"
            type="number"
            value={formData.weight}
            onChange={handleChange}
            required
            className="w-full border border-gray-300 p-2 rounded-lg focus:ring-2 focus:ring-indigo-400"
          />
        </div>

        <div>
          <label className="block text-gray-700 font-medium mb-1">Height (cm)</label>
          <input
            id="height"
            type="number"
            value={formData.height}
            onChange={handleChange}
            required
            className="w-full border border-gray-300 p-2 rounded-lg focus:ring-2 focus:ring-indigo-400"
          />
        </div>

        <div>
          <label className="block text-gray-700 font-medium mb-1">Income ( Yearly )</label>
          <input
            id="income_lpa"
            type="number"
            value={formData.income_lpa}
            onChange={handleChange}
            required
            className="w-full border border-gray-300 p-2 rounded-lg focus:ring-2 focus:ring-indigo-400"
          />
        </div>

        <div>
          <label className="block text-gray-700 font-medium mb-1">Smoker</label>
          <select
            id="smoker"
            value={formData.smoker}
            onChange={handleChange}
            className="w-full border border-gray-300 p-2 rounded-lg focus:ring-2 focus:ring-indigo-400"
          >
            <option value="false">No</option>
            <option value="true">Yes</option>
          </select>
        </div>

        <div>
          <label className="block text-gray-700 font-medium mb-1">City</label>
          <input
            id="city"
            type="text"
            value={formData.city}
            onChange={handleChange}
            required
            className="w-full border border-gray-300 p-2 rounded-lg focus:ring-2 focus:ring-indigo-400"
          />
        </div>

        <div className="col-span-2">
          <label className="block text-gray-700 font-medium mb-1">Occupation</label>
          <select
            id="occupation"
            value={formData.occupation}
            onChange={handleChange}
            className="w-full border border-gray-300 p-2 rounded-lg focus:ring-2 focus:ring-indigo-400"
          >
            <option value="retired">Retired</option>
            <option value="freelancer">Freelancer</option>
            <option value="student">Student</option>
            <option value="government_job">Government Job</option>
            <option value="business_owner">Business Owner</option>
            <option value="unemployed">Unemployed</option>
            <option value="private_job">Private Job</option>
          </select>
        </div>
      </div>

      <button
        type="submit"
        className="bg-indigo-600 hover:bg-indigo-700 text-white font-semibold w-full py-2 mt-5 rounded-lg transition-all duration-300"
      >
        Predict
      </button>
    </form>
  );
}

export default Form;
