const percentDiffSchema = [
  { id: 'v1', label: 'Initial Value (V1)', placeholder: 'e.g., 100' },
  { id: 'v2', label: 'Final Value (V2)', placeholder: 'e.g., 120' }
];

const percentDiffLogic = (inputs) => {
  const { v1, v2 } = inputs;
  return ((Math.abs(v1 - v2) / ((Number(v1) + Number(v2)) / 2)) * 100).toFixed(2) + '%';
};

// Usage: 
// <GenericCalculatorTemplate title="Percent Difference" schema={percentDiffSchema} onCalculate={percentDiffLogic} />

