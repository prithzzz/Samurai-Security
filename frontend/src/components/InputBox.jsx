import React, { useState } from "react";

const InputBox = ({ onSubmit }) => {
  const [input, setInput] = useState("");

  return (
    <div className="card">
      <h2>Enter Model / Prompt</h2>

      <textarea
        className="input-box"
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Enter input here..."
      />

      <br />

      <button
        className="button"
        onClick={() => onSubmit(input)}
      >
        Analyze
      </button>
    </div>
  );
};

export default InputBox;