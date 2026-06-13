/**
 * COMPONENT: GenericCalculatorTemplate
 * USE: Decoupled frontend for any SIS-compliant math/finance model.
 * NOTATION: Accepts `schema` prop for field definitions and `onCalculate` for processing.
 */
import React, { useState } from 'react';

const GenericCalculatorTemplate = ({ title, schema, onCalculate }) => {
  const [inputs, setInputs] = useState({});
  const [result, setResult] = useState(null);

  const handleChange = (e) => {
    setInputs({ ...inputs, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const calculation = onCalculate(inputs);
    setResult(calculation);
  };

  return (
    <div className="p-6 max-w-lg mx-auto bg-slate-900 text-white rounded-lg border border-slate-700">
      <h2 className="text-xl font-bold mb-4">{title}</h2>
      <form onSubmit={handleSubmit} className="space-y-4">
        {schema.map((field) => (
          <div key={field.id}>
            <label className="block text-sm mb-1">{field.label}</label>
            <input
              type="number"
              name={field.id}
              placeholder={field.placeholder}
              onChange={handleChange}
              className="w-full p-2 bg-slate-800 border border-slate-600 rounded"
              required
            />
          </div>
        ))}
        <button type="submit" className="w-full bg-blue-600 py-2 rounded font-bold hover:bg-blue-500">
          Execute Calculation
        </button>
      </form>
      {result !== null && (
        <div className="mt-6 p-4 bg-slate-800 rounded border border-green-600">
          <strong>Result:</strong> {result}
        </div>
      )}
    </div>
  );
};

export default GenericCalculatorTemplate;

